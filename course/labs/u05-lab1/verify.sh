#!/usr/bin/env bash
# u05-lab1 objective self-check (R7.AC5): the project-stats feature is implemented to spec AND
# nothing regressed. Passes only if (1) the full pytest suite is still green and (2) the new
# endpoint GET /projects/{id}/stats meets the contract the unit specifies:
#   - 200 with body {"project_id": <id>, "total": <int>, "by_status": {<status>: <count>, ...}};
#   - by_status is zero-filled for every TaskStatus (todo / in_progress / done);
#   - counts are correct and scoped to that project;
#   - a foreign/unknown project returns 404 (ownership enforced).
#
# Like u01-lab1 this checks the learner's WORKING TREE under codebases/primary/taskflow-api (not a
# branch), so it verifies the feature they actually built — any layering/shape that satisfies the
# contract passes. Requires the codebase deps installed (`uv pip install -e ".[dev]"`); doctor
# confirms the toolchain.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
api="${root}/codebases/primary/taskflow-api"
cd "$api"

# 1. No regression: the suite must still pass (includes any tests the learner added).
echo "u05-lab1: running pytest (no-regression gate)…"
python -m pytest -q

# 2. The feature: project stats behaves to the contract above.
echo "u05-lab1: checking /projects/{id}/stats behavior…"
python - <<'PY'
from collections.abc import Iterator

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


owner = _login("u05-owner@taskflow.test")
pid = client.post("/projects", json={"name": "Stats"}, headers=owner).json()["id"]


def _seed(status: str, n: int) -> None:
    for _ in range(n):
        r = client.post(
            f"/projects/{pid}/tasks", json={"title": "t", "status": status}, headers=owner
        )
        assert r.status_code == 201, f"could not seed task: {r.text}"


_seed("todo", 2)
_seed("in_progress", 1)
_seed("done", 2)

resp = client.get(f"/projects/{pid}/stats", headers=owner)
assert resp.status_code == 200, (
    f"GET /projects/{{id}}/stats not implemented or erroring: HTTP {resp.status_code} {resp.text}"
)
body = resp.json()

assert body.get("project_id") == pid, f'stats must echo "project_id": {pid} — got {body}'
assert body.get("total") == 5, f'stats "total" should be 5 — got {body}'
assert body.get("by_status") == {"todo": 2, "in_progress": 1, "done": 2}, (
    f'"by_status" must count tasks per status — got {body.get("by_status")}'
)

# Zero-fill: a project with no tasks still reports every status as 0.
empty_pid = client.post("/projects", json={"name": "Empty"}, headers=owner).json()["id"]
empty = client.get(f"/projects/{empty_pid}/stats", headers=owner).json()
assert empty.get("total") == 0, f'empty project "total" should be 0 — got {empty}'
assert empty.get("by_status") == {"todo": 0, "in_progress": 0, "done": 0}, (
    f'"by_status" must zero-fill every TaskStatus — got {empty.get("by_status")}'
)

# Ownership: a different user must not see this project's stats (404, not an empty/forged count).
nosy = _login("u05-nosy@taskflow.test")
foreign = client.get(f"/projects/{pid}/stats", headers=nosy)
assert foreign.status_code == 404, (
    f"stats on a project you don't own must be 404 — got HTTP {foreign.status_code}"
)

print("u05-lab1: stats endpoint meets the contract; ownership enforced; suite green.")
PY
