#!/usr/bin/env bash
# u07-lab1 objective self-check (R7.AC5): the "overdue never flags" bug (legacy D1) is fixed at its
# root AND the CLI still works. Passes only if, driving the learner's WORKING-TREE taskflow.py:
#   - a past-due, not-done task is flagged overdue everywhere it's reported — `list --overdue`,
#     `stats` (overdue count), and the `list` / `show` display;
#   - a future-due, a no-due, and a *done* past-due task are NOT flagged;
#   - basic add / list / stats behaviour is intact (no regression).
#
# The bug is copy-pasted in three places, so the display checks fail a one-site "fix" — confirming
# the root cause means fixing all of it. The legacy CLI has no test suite, so this verifier drives
# the program itself over a throwaway DB; it FAILS on the unfixed starting state (that's the repro,
# automated) and PASSES on the reference solution.
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cli="${root}/codebases/legacy/taskflow-cli"

echo "u07-lab1: driving taskflow-cli to check the overdue fix…"
python - "$cli" <<'PY'
import os
import re
import subprocess
import sys
import tempfile
from datetime import date, timedelta

cli_dir = sys.argv[1]
db = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
db.close()
os.unlink(db.name)  # let the CLI create it; just reserve a unique path
env = {**os.environ, "TASKFLOW_DB": db.name}


def run(*args):
    r = subprocess.run(
        [sys.executable, "taskflow.py", *args],
        cwd=cli_dir, env=env, capture_output=True, text=True,
    )
    assert r.returncode == 0, f"`taskflow.py {' '.join(args)}` exited {r.returncode}: {r.stderr}"
    return r.stdout


def _id(out):
    m = re.search(r"added #(\d+)", out)
    assert m, f"could not parse new id from add output: {out!r}"
    return m.group(1)


past = (date.today() - timedelta(days=400)).isoformat()
future = (date.today() + timedelta(days=400)).isoformat()

past_id = _id(run("add", "PASTDUE", "--due", past))
future_id = _id(run("add", "FUTURE", "--due", future))
_id(run("add", "NODUE"))
done_id = _id(run("add", "OLDDONE", "--due", past))
run("done", done_id)  # past-due but done -> never overdue

# 1. stats: exactly one overdue (PASTDUE); total reflects all four (regression smoke).
stats = run("stats")
m = re.search(r"overdue:\s*(\d+)", stats)
assert m, f"`stats` did not report an overdue count:\n{stats}"
assert m.group(1) == "1", (
    f"`stats` overdue count should be 1 (only PASTDUE) — got {m.group(1)}.\n"
    "On the unfixed code this is 0: overdue is never flagged. Did you fix the date comparison?"
)
mt = re.search(r"total tasks:\s*(\d+)", stats)
assert mt and mt.group(1) == "4", f"expected 4 total tasks (regression check) — got:\n{stats}"

# 2. list --overdue: only PASTDUE.
ov = run("list", "--overdue")
assert "PASTDUE" in ov, f"`list --overdue` should include the past-due task — got:\n{ov}"
assert "FUTURE" not in ov and "NODUE" not in ov, (
    f"`list --overdue` should exclude future / no-due tasks — got:\n{ov}"
)

# 3. Root cause everywhere: the `list` display marks PASTDUE overdue, not FUTURE; `show` agrees.
listing = run("list")  # default hides done -> PASTDUE, FUTURE, NODUE
past_line = next((ln for ln in listing.splitlines() if "PASTDUE" in ln), "")
future_line = next((ln for ln in listing.splitlines() if "FUTURE" in ln), "")
assert past_line and "OVERDUE" in past_line.upper(), (
    f"the `list` display should mark the past-due task OVERDUE — got line: {past_line!r}\n"
    "(this is the SECOND copy of the bug — fixing only `is_overdue` leaves the display broken)"
)
assert future_line and "OVERDUE" not in future_line.upper(), (
    f"the `list` display must NOT mark a future task overdue — got line: {future_line!r}"
)
assert "OLDDONE" not in listing, f"default `list` should hide the done task — got:\n{listing}"

show_past = run("show", past_id)
assert "overdue" in show_past.lower(), (
    f"`show {past_id}` should flag the past-due task overdue — got:\n{show_past}\n"
    "(this is the THIRD copy of the bug — in print_task_full)"
)
show_future = run("show", future_id)
assert "overdue" not in show_future.lower(), (
    f"`show {future_id}` must NOT flag a future task overdue — got:\n{show_future}"
)

print("u07-lab1: overdue is flagged at every surface; future/no-due/done excluded; CLI intact.")
PY
