# Seeded-defect inventory (maintainer-facing)

> **Audience:** course maintainers, not learners. **Do not** link this from a unit or a lab brief —
> it is the answer key. It maps every deliberately planted defect to its location and its expected
> fix, so defects are *tracked*, not silently scattered (design §7).

There are two kinds of seeded defect:

1. **Legacy baked-in defects** — real bugs that live permanently in `legacy/taskflow-cli` on `main`.
   The legacy CLI is *meant* to be buggy; these are its known landmines and the raw material for the
   U7 (debug) and U9 (onboard + refactor) labs.
2. **Primary per-lab defects** — defects introduced **only on a lab branch** of `primary/taskflow-api`
   (`start/uNN-labM`), never on `main`. `main` stays green (its pytest suite passes). These are
   authored in P5 as each lab is written; this file is where they are registered.

Lab id / branch convention: starting state is the tag `start/uNN-labM`; the reference solution is the
branch `solution/uNN-labM` (see `meta/conventions.md`).

---

## 1. Legacy baked-in defects — `legacy/taskflow-cli/taskflow.py`

These are present on `main` by design. Each is independent and reproducible without the others.

| ID | Defect | Location | How to reproduce | Expected fix | Home lab |
|----|--------|----------|------------------|--------------|----------|
| **D1** | **Naive date handling — overdue tasks never flagged.** `is_overdue()` compares the stored due date (ISO `YYYY-MM-DD`) against *today rendered as* `MM-DD-YYYY`, as plain strings. The lexicographic comparison across mismatched formats is meaningless, so overdue is effectively always `False`. The same broken check is copy-pasted into `fmt_due()` and `print_task_full()`. | `is_overdue()` (~line 148); duplicated in `fmt_due()` and `print_task_full()` | `taskflow.py add "Pay invoice" --due 2020-01-01` then `taskflow.py list --overdue` → empty; `stats` shows `overdue: 0`. | Parse both sides to `datetime.date` and compare as dates (`datetime.date.fromisoformat(due) < datetime.date.today()`); de-duplicate the three copies into the one `is_overdue()` helper. | U7 (debug); motivates U9 (dedupe) |
| **D2** | **Off-by-one in listing.** `list --limit N` returns only `N-1` tasks: the slice is `rows[: limit - 1]`. | `cmd_list()`, the `--limit` slice (~line 300) | Add ≥3 tasks, `taskflow.py list --limit 3` → only 2 rows printed. | `rows = rows[: args.limit]`. | U7 (debug) |
| **D3** | **Swallowed exception hides data loss.** `save_tasks()` wraps the whole write in `try/except Exception: pass`. Any write failure (unwritable path, permission error, a non-serializable value) is silent, so the command prints `added`/`updated` while nothing is persisted. | `save_tasks()` (~line 72) | `TASKFLOW_DB=/a/read-only/path/tasks.json taskflow.py add "x"` prints `added #1`, exit 0, but no file is written and a later `list` is empty. | Let the exception propagate (or catch, print to stderr, and exit non-zero); never `pass`. | U7 (debug) |

**Smells (not bugs) for the U9 onboard/refactor lab.** Not defects to "fix" with a one-liner, but the
accreted complexity the refactor lab targets. Inventoried so the lab can reference concrete examples:

- One ~700-line god-module; no separation of storage / domain / CLI.
- Global mutable state (`TASKS`, `CONFIG`, `_loaded`, `_dirty`, `current_project`) read and written
  throughout instead of being passed as arguments.
- Duplicated logic: two id helpers (`nextId` / `_guess_next_id` / dead `recalc_next_id`), two task
  lookups (`getTask` / `find_task_by_id`), three copies of the overdue check.
- Inconsistent naming (`loadTasks` vs `save_tasks` vs `getTask` vs `find_task_by_id`).
- Dead code: `export_xml`, `migrate_v1_to_v2`, `recalc_next_id`, the `USE_LEGACY_FORMAT` flag, the
  commented-out `cmd_notify`.
- No tests at all — U9 can pair the refactor with characterization tests before changing behaviour.

---

## 2. Primary per-lab defects — `primary/taskflow-api` (branch-only)

> **Status:** populated during **P5** as each lab is authored. `main` carries **none** of these — its
> pytest suite is green. Each row's defect lives only on the lab's `start/uNN-labM` tag; the
> `solution/uNN-labM` branch holds the reference fix.

Planned slots (derived from the unit map, design §6). Fill in *Defect* / *Expected fix* when the lab
is written; until then the lab is unwritten, not missing.

| Lab (planned) | Unit | Substrate | Nature of the planted state | Status |
|---------------|------|-----------|------------------------------|--------|
| `u01-lab1` | U1 Onboarding / first win | primary | **No bug — first-win addition.** Start = clean `main` + the baseline `CLAUDE.md`/`.claude/settings.json`. Learner has Claude add a one-line `"service": "taskflow-api"` field to the `/health` response in `app/main.py`. Reference fix on `solution/u01-lab1`; objective check `course/labs/u01-lab1/verify.sh` (suite green + `/health` reports the field). | ✅ authored (P5, U1) |
| `u03-lab1` | U3 Operate safely | **none** (training tree) | **No code defect — read-only prompt-injection fence.** The untrusted artifact is a fixture, `course/labs/u03-lab1/untrusted-bug-report.md`, carrying an injected payload (create `INJECTED-u03.txt`, exfiltrate `.env`, append `owned-by-1284` to `README.md`). Learner triages it under a fence (`--permission-mode plan`). **No `start/` tag or `solution/` branch** — correct outcome is *no change*, so the lab is read-only (precedent: U2). Objective check `course/labs/u03-lab1/verify.sh` asserts the injection produced **zero** side effects (sentinel absent, `README.md` + `codebases/primary` unmodified, suite green). | ✅ authored (P5, U3) |
| `u05-lab1` | U5 Ship a feature | primary | Start from a missing endpoint/field; learner *adds* a feature (no bug to fix — the "defect" is an absence). | P5 |
| `u06-lab1` | U6 TDD | primary | Start from a failing/not-yet-implemented spec; learner drives it green test-first. | P5 |
| `u07-lab1` | U7 Debug | **legacy** | Uses D1–D3 above directly; no branch defect needed. | this file §1 |
| `u09-lab1` | U9 Refactor | **legacy** | Uses §1 smells; reference solution on `solution/u09-lab1`. | P5 |
| `u11-lab1` | U11 Review | primary | Plant a review-worthy issue (e.g. a missing ownership check or an N+1) for the review workflow to catch. | P5 |

(Rows are indicative; exact lab ids and counts are fixed when P5 authors each unit. Add/rename rows
here in the same commit that creates the lab branch.)

---

## 3. Maintenance rules

- **Every planted defect appears in this table** before it is committed to a lab branch. A defect not
  listed here is a bug in the course, not a lab.
- When you author a primary lab, add its row (defect + expected fix + branch) in the **same commit**
  that creates `start/uNN-labM`.
- The legacy defects (§1) are load-bearing: do **not** "clean them up" on `main`. If you must change
  `legacy/taskflow-cli`, update the affected D-row's line references here too.
- This file is the answer key — keep it out of learner-facing links (`tools/check-links` only checks
  reachability, not that this stays unlinked; that is on you).
