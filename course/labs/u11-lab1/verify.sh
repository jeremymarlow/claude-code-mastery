#!/usr/bin/env bash
# u11-lab1 objective self-check (R7.AC5): the two REAL review findings in the project-archiving
# feature are fixed, and nothing regressed. Drives the learner's WORKING TREE taskflow-api and
# asserts:
#   - SECURITY (IDOR fixed): user B archiving user A's project gets 404 and leaves it un-archived;
#   - the owner CAN archive their own project (the feature still works);
#   - CORRECTNESS (default fixed): the project list EXCLUDES archived projects by default, and
#     includes them only with ?include_archived=true;
#   - the full pytest suite is green (no regression; includes any tests the learner added).
#
# It FAILS on the starting state (cross-user archive returns 200; default list shows archived) — so a
# pass means the holes are actually closed. It does NOT grade the false-positive dismissal (the
# `== False` SQLAlchemy lint) — that's the unit's triage judgment, not a mechanical check.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
api="${root}/codebases/primary/taskflow-api"
cd "$api"

echo "u11-lab1: running pytest (no-regression gate)…"
python -m pytest -q

echo "u11-lab1: checking the archive feature's correctness + authorization…"
python - <<'PY'
from collections.abc import Iterator

from fastapi.testclient import TestClient
from sqlalchemy.pool import StaticPool
from sqlmodel import Session, SQLModel, create_engine

import app.models  # noqa: F401 — register tables on SQLModel.metadata
from app.db.session import get_session
from app.main import create_app

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


alice = _login("u11-alice@taskflow.test")
bob = _login("u11-bob@taskflow.test")


def _archive(headers, pid):
    # The feature under review is POST /projects/{id}/archive.
    return client.post(f"/projects/{pid}/archive", headers=headers)


# --- SECURITY: user B must not be able to archive user A's project (IDOR) --------------------------
victim = client.post("/projects", json={"name": "Alice secret"}, headers=alice).json()["id"]
resp = _archive(bob, victim)
assert resp.status_code == 404, (
    f"SECURITY: Bob archiving Alice's project must 404 (hide existence) — got {resp.status_code}. "
    "On the unfixed code this is 200: archive_project skips the ownership check. Route it through "
    "get_project."
)
# …and the victim project must remain un-archived (Bob's call must have no effect).
state = client.get(f"/projects/{victim}", headers=alice).json()
assert state.get("archived") is False, (
    f"SECURITY: Alice's project was archived by Bob — it must be untouched. Got archived={state.get('archived')!r}"
)

# --- the feature still works for the owner ---------------------------------------------------------
owned = client.post("/projects", json={"name": "Alice todo"}, headers=alice).json()["id"]
resp = _archive(alice, owned)
assert resp.status_code == 200, (
    f"the owner must be able to archive their own project — got {resp.status_code}: {resp.text}"
)
after = client.get(f"/projects/{owned}", headers=alice).json()
assert after.get("archived") is True, f"owner-archived project should report archived=true — got {after}"

# --- CORRECTNESS: archived projects are excluded from the list by default --------------------------
default_ids = {p["id"] for p in client.get("/projects", params={"limit": 100}, headers=alice).json()["items"]}
assert owned not in default_ids, (
    "CORRECTNESS: the archived project must be EXCLUDED from the default project list — it appeared. "
    "On the unfixed code include_archived defaults to true. Default to excluding archived."
)
assert victim in default_ids, "the un-archived project should still appear in the default list."

incl_ids = {
    p["id"]
    for p in client.get(
        "/projects", params={"include_archived": "true", "limit": 100}, headers=alice
    ).json()["items"]
}
assert owned in incl_ids, (
    "?include_archived=true must INCLUDE archived projects — the archived one was missing."
)

print("u11-lab1: IDOR closed (cross-user archive 404, no effect); owner archive works; "
      "list excludes archived by default and includes them on request; suite green.")
PY
