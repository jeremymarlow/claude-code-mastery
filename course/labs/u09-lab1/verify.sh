#!/usr/bin/env bash
# u09-lab1 objective self-check (R7.AC5): a multi-file, BEHAVIOR-PRESERVING refactor of the legacy
# taskflow-cli god-module. This is a W5 "green before and after" check, automated: it drives a broad
# command battery against BOTH the original single-file program (materialised from the `start/u09-lab1`
# tag) AND the learner's working tree, then asserts the two transcripts are identical (timestamps
# redacted). It therefore PASSES on the untouched start state and on a faithful refactor, and FAILS if
# any observable behaviour moved — INCLUDING a "helpful" fix of the overdue (D1) or `--limit` (D2) bug,
# which is the scope-creep lesson the unit turns on.
#
# It also requires the refactor to have actually happened: the god-module must be split so program
# logic lives across multiple modules and `taskflow.py` is no longer the monolith. It does NOT grade
# the module layout — that's the unit's prose checklist (R7.AC3).
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
learner_dir="${root}/codebases/legacy/taskflow-cli"
ref_blob="start/u09-lab1:codebases/legacy/taskflow-cli/taskflow.py"

if ! git -C "$root" rev-parse -q --verify "refs/tags/start/u09-lab1" >/dev/null; then
  echo "u09-lab1: missing tag start/u09-lab1 — cannot establish the behaviour baseline." >&2
  exit 2
fi

echo "u09-lab1: comparing learner behaviour against the original (start/u09-lab1)…"
python - "$root" "$learner_dir" "$ref_blob" <<'PY'
import os
import re
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path

root, learner_dir, ref_blob = sys.argv[1], sys.argv[2], sys.argv[3]

# --- materialise the original single-file program from the start tag -----------------------------
ref_dir = tempfile.mkdtemp(prefix="u09-ref-")
ref_src = subprocess.run(["git", "-C", root, "show", ref_blob],
                         capture_output=True, text=True, check=True).stdout
Path(ref_dir, "taskflow.py").write_text(ref_src)
baseline_lines = len(ref_src.splitlines())

# --- the command battery (identical inputs both sides; dates are fixed relative to today) --------
PAST = (date.today() - timedelta(days=400)).isoformat()
FUT = (date.today() + timedelta(days=400)).isoformat()
BATTERY = [
    ["add", "Alpha", "--priority", "high", "--project", "work", "--due", PAST, "--tag", "a", "--tag", "b"],
    ["add", "Beta", "--due", FUT, "--assignee", "bob"],
    ["add", "Gamma", "--project", "home"],
    ["add", "Delta", "--priority", "urgent", "--due", "today"],
    ["list"],
    ["list", "--all"],
    ["list", "--overdue"],          # D1: stays empty after a faithful refactor
    ["list", "--project", "work"],
    ["list", "--status", "todo"],
    ["list", "--priority", "urgent"],
    ["list", "--sort", "priority"],
    ["list", "--sort", "due"],
    ["list", "--limit", "3"],        # D2: still prints two rows after a faithful refactor
    ["start", "2"],
    ["done", "3"],
    ["list", "--all"],
    ["show", "1"],
    ["show", "3"],
    ["stats"],
    ["projects"],
    ["tags"],
    ["search", "alpha"],
    ["assign", "4", "alice"],
    ["edit", "1", "--notes", "hello", "--priority", "normal"],
    ["show", "1"],
    ["export", "csv"],
    ["export", "json"],
    ["config", "get"],
    ["config", "set-default-project", "home"],
    ["config", "get"],
    ["rm", "2"],
    ["list", "--all"],
    ["stats"],
    ["--version"],
    ["bogus-cmd"],                   # error paths are behaviour too
]

# ISO datetimes (created/updated) are wall-clock and differ between two runs — redact them.
TS = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def transcript(workdir):
    db = tempfile.mktemp(suffix=".json")
    env = {**os.environ, "TASKFLOW_DB": db}
    out = []
    for args in BATTERY:
        r = subprocess.run([sys.executable, "taskflow.py", *args],
                           cwd=workdir, env=env, capture_output=True, text=True)
        block = f"$ taskflow {' '.join(args)}\n[exit {r.returncode}]\n{r.stdout}{r.stderr}"
        out.append(TS.sub("<TS>", block))
    return out


ref = transcript(ref_dir)
got = transcript(learner_dir)

for args, a, b in zip(BATTERY, ref, got):
    if a != b:
        print("u09-lab1: BEHAVIOUR CHANGED — your refactor is not behaviour-preserving.", file=sys.stderr)
        print(f"\nFirst divergence on: taskflow {' '.join(args)}\n", file=sys.stderr)
        print("--- original (start/u09-lab1) ---", file=sys.stderr)
        print(a, file=sys.stderr)
        print("--- your working tree ---", file=sys.stderr)
        print(b, file=sys.stderr)
        if args in (["list", "--overdue"], ["stats"], ["list", "--limit", "3"]):
            print("\nNote: a refactor PRESERVES behaviour — including the overdue / --limit bugs. "
                  "If you 'fixed' one here, that's scope creep; revert it and fix it as a separate "
                  "change.", file=sys.stderr)
        sys.exit(1)

# --- structural: the god-module was actually broken up -------------------------------------------
def is_test(p: Path) -> bool:
    n = p.name
    return n.startswith("test_") or n.endswith("_test.py") or n == "conftest.py"


def def_count(p: Path) -> int:
    return len(re.findall(r"^\s*def ", p.read_text(), re.M))

modules = [p for p in Path(learner_dir).rglob("*.py")
           if "__pycache__" not in p.parts and not is_test(p) and def_count(p) >= 1]
substantive = [p for p in modules if def_count(p) >= 2]

if len(substantive) < 2:
    print("u09-lab1: behaviour matches, but the god-module was not split — program logic still lives "
          f"in a single module ({[p.name for p in modules]}). The refactor's point is to break "
          "taskflow.py into sensible modules.", file=sys.stderr)
    sys.exit(1)

entry = Path(learner_dir, "taskflow.py")
if not entry.exists():
    print("u09-lab1: taskflow.py is gone — `python taskflow.py` is the public entry point and must "
          "keep working. Preserve it (a thin entry that imports your modules is fine).", file=sys.stderr)
    sys.exit(1)

entry_lines = len(entry.read_text().splitlines())
if entry_lines >= 0.7 * baseline_lines:
    print(f"u09-lab1: behaviour matches, but taskflow.py is still {entry_lines} lines "
          f"(baseline {baseline_lines}); the logic hasn't really moved out of the monolith. "
          "Split it across modules.", file=sys.stderr)
    sys.exit(1)

print(f"u09-lab1: behaviour identical to the original across {len(BATTERY)} commands, "
      f"and the monolith is split across {len(substantive)} modules "
      f"(taskflow.py {baseline_lines} → {entry_lines} lines). Refactor preserved behaviour. PASSED.")
PY
