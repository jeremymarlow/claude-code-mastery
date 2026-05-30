#!/usr/bin/env bash
# u01-lab1 objective self-check (R7.AC5): the first-win one-line change landed AND nothing
# regressed. Passes only if (1) the pytest suite is still green and (2) GET /health now returns
# "service": "taskflow-api" alongside the existing "status": "ok".
#
# Runs against the learner's working tree under codebases/primary/taskflow-api (not a branch),
# so it verifies the change they actually made. Requires the codebase deps installed
# (`uv pip install -e ".[dev]"`); doctor confirms the toolchain.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
api="${root}/codebases/primary/taskflow-api"
cd "$api"

# 1. No regression: the suite must still pass.
echo "u01-lab1: running pytest (no-regression gate)…"
python -m pytest -q

# 2. The win: /health reports the service name (the one-line change).
echo "u01-lab1: checking /health behavior…"
python - <<'PY'
from fastapi.testclient import TestClient

from app.main import app

resp = TestClient(app).get("/health")
assert resp.status_code == 200, f"/health returned HTTP {resp.status_code}"
body = resp.json()
assert body.get("status") == "ok", f'/health must still return "status": "ok" — got {body}'
assert body.get("service") == "taskflow-api", (
    'the first-win change is not applied: /health should return '
    f'"service": "taskflow-api" — got {body}'
)
print("u01-lab1: /health reports service=taskflow-api and status=ok; suite green.")
PY
