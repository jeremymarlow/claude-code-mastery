#!/usr/bin/env bash
# u06-lab1 objective self-check (R7.AC5): the `overdue` task filter is implemented to spec AND
# nothing regressed. Passes only if (1) the full pytest suite is still green and (2) the task list
# honours `GET /tasks?overdue=true` per the contract the unit specifies:
#   - a task is overdue iff it has a due_date STRICTLY BEFORE today AND status != done;
#   - overdue=true returns exactly the overdue tasks (done / due-today / no-due-date excluded);
#   - the unfiltered list (no overdue param, or overdue=false) is unchanged.
#
# Like u05-lab1 this checks the learner's WORKING TREE under codebases/primary/taskflow-api (not a
# branch), so it verifies the behavior they actually built — any layering/shape that satisfies the
# contract passes. Requires the codebase deps installed (`uv pip install -e ".[dev]"`); doctor
# confirms the toolchain.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
api="${root}/codebases/primary/taskflow-api"
cd "$api"

# 1. No regression: the suite must still pass (includes any tests the learner added).
echo "u06-lab1: running pytest (no-regression gate)…"
python -m pytest -q

# 2. The behavior: GET /tasks?overdue=true filters to the right set.
echo "u06-lab1: checking the overdue filter behavior…"
python - <<'PY'
from collections.abc import Iterator
from datetime import date, timedelta

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

import app.models  # noqa: F401 — register tables on SQLModel.metadata
from app.db.session import get_session
from app.main import create_app

# Isolated in-memory DB + session override, mirroring tests/conftest.py — never touches the dev DB.
engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
SQLModel.metadata.create_all(engine)

app = create_app()


def _override() -> Iterator[Session]:
    with Session(engine) as session:
        yield session


app.dependency_overrides[get_session] = _override
client = TestClient(app)


def _login(email: str) -> dict[str, str]:
    client.post("/auth/register", json={"email": email, "password": "password123"})
    resp = client.post("/auth/login", data={"username": email, "password": "password123"})
    assert resp.status_code == 200, f"login failed: {resp.text}"
    return {"Authorization": f"Bearer {resp.json()['access_token']}"}


owner = _login("u06-owner@taskflow.test")
pid = client.post("/projects", json={"name": "Overdue"}, headers=owner).json()["id"]

today = date.today()
yesterday = (today - timedelta(days=1)).isoformat()
tomorrow = (today + timedelta(days=1)).isoformat()
today_s = today.isoformat()


def _task(title: str, status: str, due_date: str | None) -> int:
    body: dict = {"title": title, "status": status}
    if due_date is not None:
        body["due_date"] = due_date
    r = client.post(f"/projects/{pid}/tasks", json=body, headers=owner)
    assert r.status_code == 201, f"could not seed task {title!r}: {r.text}"
    return r.json()["id"]


# Two genuinely overdue (past due, not done) and four that must be EXCLUDED.
overdue_ids = {
    _task("past-todo", "todo", yesterday),
    _task("past-inprog", "in_progress", yesterday),
}
_task("past-done", "done", yesterday)        # done is never overdue, however old
_task("due-today", "todo", today_s)          # strictly-before: today is not overdue
_task("future", "todo", tomorrow)            # future is not overdue
_task("no-due-date", "todo", None)           # no due date is never overdue

# overdue=true must return exactly the two overdue tasks.
resp = client.get("/tasks", params={"overdue": "true", "limit": 100}, headers=owner)
assert resp.status_code == 200, (
    f"GET /tasks?overdue=true not working: HTTP {resp.status_code} {resp.text}"
)
items = resp.json()["items"]
got = {t["id"] for t in items}
assert got == overdue_ids, (
    "overdue=true must return ONLY tasks past-due and not done — "
    f"expected ids {overdue_ids}, got {got} "
    "(check: due-today excluded? done excluded? no-due-date excluded?)"
)
for t in items:
    assert t["status"] != "done", f'a "done" task is never overdue — got {t}'
    assert t["due_date"] is not None and t["due_date"] < today_s, (
        f"overdue tasks must be due strictly before today — got {t}"
    )

# Regression: with no overdue param (and with overdue=false) the list is unchanged — all 6 tasks.
allt = client.get("/tasks", params={"limit": 100}, headers=owner).json()["total"]
assert allt == 6, f"unfiltered list must be unchanged (6 tasks) — got total {allt}"
false_total = client.get(
    "/tasks", params={"overdue": "false", "limit": 100}, headers=owner
).json()["total"]
assert false_total == 6, f"overdue=false must not filter — expected 6, got {false_total}"

print("u06-lab1: overdue filter meets the contract; unfiltered list unchanged; suite green.")
PY
