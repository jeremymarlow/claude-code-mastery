---
description: Sync every project state file after a unit's prose is authored, then run the checks
argument-hint: <NN>
---

Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.src.md`
is authored (the committed `unit.md` is generated from it by `make render`), then verify. Pull
specifics from the files, not memory; follow `meta/conventions.md`.

Do each step, in order:

1. **`specs/claude-code-mastery/IMPLEMENTATION.md` §3** — update the P5 progress marker so U$1 is in the
   done list (and the matching `tasks.md` status header if it tracks a count). Keep §3 terse.
2. **`specs/claude-code-mastery/tasks.md`** — add or confirm the unit's detail bullet (gist ·
   _Lab/refs_ · _Trace & version keys_). **Only check the `[ ] **U$1**` box if the unit is *fully*
   done** — prose authored **and** its lab complete: either the mutating lab's `start/`/`solution/`
   refs + `verify.sh` exist and pass end-to-end, or it is a no-refs unit (read-only / prose-self-check,
   like U2/U8/U12) that needs none. If lab artifacts are still pending, **leave the box unchecked**,
   record the prose as authored, and ensure step 3 keeps that lab open in **L7**. A checked box must
   never coexist with pending L7 lab refs for the same unit.
3. **`specs/claude-code-mastery/decisions.md`** — add the `P5-U$1-*` rationale entries (lab choice, any
   built artifacts, vd/L1 status), each with a **Why:** line, and refresh the 🔓 open-loops ledger —
   **L7** (per-lab `start/`/`solution/` refs + verifier status) and **L1** (version debt) for this unit.
4. **Verify version currency** — any `{{vd:*}}` key the unit introduced must be `unverified: false` in
   `meta/version-data.yaml`, verified against the installed CLI (R12.AC3–AC4). Flag any that isn't as
   open **L1** debt rather than claiming it's done.
5. **Run `make check-strict`** and report the result — it must be green before the unit counts as closed.
   Use **strict**, not plain `make check`: strict turns not-yet-referenced requirements and pending lab/
   rubric refs into hard failures, so "closed" means the Definition-of-Done gate actually passes. (A plain
   `make check` reports those as non-failing `PEND` — that gap let a P7 prose sweep silently drop the only
   `R8` reference without turning the suite red.) If you edited `unit.src.md`, run `make render` first so
   the generated `unit.md` (and the unit index) are current; otherwise the render drift gate will fail.

Then report a short summary of what each file received and the check result. Do not invent status: if a
verifier, a `SEEDED.md` §2 row, or a vd key isn't actually done, say so and leave it open in the ledger.
