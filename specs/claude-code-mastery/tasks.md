# Tasks — Claude Code Mastery Course

**Spec:** `claude-code-mastery`
**Phase:** Tasks / Implementation (Phase 3 of 3)
**Status:** 🟦 **IN PROGRESS** (2026-05-30) — Design authored & approved; the detailed per-phase
task files (`tasks/P1–P6*.md`) are written and trace design → requirement. P1 (Design) ✅,
P2 (Scaffolding) ✅, P3 (Tooling) ✅, and P4 (Codebases) ✅ complete; **P5→P6 remaining**. Open
loops & deferrals are tracked in `decisions.md` → "Open loops & deferrals 🔓" (the canonical ledger).

> **Chunking for context management.** The full build exceeds one context window. This file is an
> **index**; detailed tasks live in per-section files under `tasks/` so a session loads only the slice
> it's executing. Author one phase (and, in P4, one unit) at a time. Check items off here as files complete.

---

## How to execute
1. Resolve Q1/Q2 with the user (see `IMPLEMENTATION.md` §4); record in `decisions.md`.
2. Author `design.md` top-to-bottom (P1 below).
3. Generate the detailed `tasks/*.md` from the completed design, then execute P2→P6.
4. Keep state current: check boxes here, update `meta/version-record.md`, append to `decisions.md`.
5. Stop at the Definition of Done in `IMPLEMENTATION.md` §6; run the enforcement + traceability checks.

## Phase index

### P0 — Preconditions
- [x] Q1 (codebase stack/domain) resolved with user → `decisions.md` (task/project-tracker; `taskflow-api` + `taskflow-cli`)
- [x] Q2 (use-case catalog, capability map, course size) resolved with user → `decisions.md` (16 units, C1–C17+CV)
- [x] Repo structure (design §9) — adopted (user-delegated; adjustable)

### P1 — Design  → [`tasks/P1-design.md`](./tasks/P1-design.md)  ✅ COMPLETE  [filled design.md §1–§11]
- [x] Capability map (§1) · Use-case catalog (§2) · Workflows (§3) · Coverage matrix (§4)
- [x] Version-resilience architecture (§5) · Unit model + schema + unit map (§6) · Capstone (§6.5)
- [x] Lab/solution architecture (§7) · Tooling plan (§8) · Repo structure (§9) · Dogfooding (§10)
- [x] Traceability table populated (§11) — every R1–R15 ✅

### P2 — Scaffolding & cross-cutting artifacts  → [`tasks/P2-scaffold.md`](./tasks/P2-scaffold.md)  ✅ COMPLETE (2026-05-30)
- [x] Repo skeleton + naming conventions (R13.AC1) · `CLAUDE.md` (R14.AC1)
- [x] `meta/` artifacts seeded: capability-map, use-case-catalog, coverage-matrix, version-data,
      version-record, glossary, conventions, front-matter schema (R13.AC2, machine-readable)
- [x] `course/progress-checklist.md` generated from capability-map (R9.AC5) · `course/stuck.md` (R9.AC4)

### P3 — Tooling & enforcement (build early so it guards the content)  → [`tasks/P3-tooling.md`](./tasks/P3-tooling.md)  ✅ COMPLETE (2026-05-30)
- [x] `doctor` preflight + manual fallback (R11.AC2)
- [x] Required checks: front-matter validation, coverage/map cross-validation, link check,
      version-data reference integrity (R13.AC4)
- [x] Traceability checks (R13.AC5) · Drift detection (R12.AC6) · git pre-commit + CI wiring (R13.AC6)
      _(Claude Code in-session hook deferred to U14 — see `tasks/P3-tooling.md` §3.7)_

### P4 — Sample codebases  → [`tasks/P4-codebases.md`](./tasks/P4-codebases.md)  ✅ COMPLETE (2026-05-30)
- [x] Primary codebase: build, tests (36 pytest green on `main`), substrate for branch-introduced defects (R7.AC1–AC2)
- [x] Legacy codebase: deliberately messy 709-line god-module + 3 seeded bugs, for onboarding/refactor/debug (R7.AC1)
      _SEEDED.md inventory + offline `fixtures/mock_api.py` (R7.AC7) done; per-lab primary defects populate in P5._

### P5 — Units (one slice per unit — author independently)  → [`tasks/P5-units.md`](./tasks/P5-units.md)  (per-unit working files: `tasks/P5-units/NN-slug.md`)
- [x] **U1** Onboarding unit (First Wins; doctor + first-success + baseline config; R11) — `unit.md` authored; lab `u01-lab1` (first-win `/health` change) + `verify.sh`; baseline `CLAUDE.md`/`.claude/settings.json` shipped to `primary`; `make check` green (C1/C2 now lab-traced). Git refs `start/u01-lab1` (tag) + `solution/u01-lab1` (branch) created; `reset-lab`/`verify-lab` verified end-to-end.
- [x] **U3** `03-operate-safely` (C4, CV) — **dedicated security unit (R10.AC1)**: `unit.md` covers permission modes + bypass hazards (R10.AC2), secrets + prompt injection (R10.AC3), blast-radius/checkpoints (R10.AC4), define-your-own verification (R10.AC6), managed-settings awareness (area 29). Hands-on **safety-fenced prompt-injection lab** `u03-lab1` (R10.AC3/AC8): untrusted fixture + plan-mode fence + objective `verify.sh` (zero side effects). Read-only (no `start/`/`solution/` refs, like U2). Areas 3,4,5,6,29 lab/intro/mention-traced; `make check` green. Woven safety in later workflow labs (R10.AC7) is enforced as those units (U5+) are authored.
- [ ] One unit per use case (from design §6), each: tier-appropriate template (R6), valid front
      matter (R6.AC3), labs + reference solutions + reset (R7), pitfalls (R6.AC6), going-deeper
      - [x] **U2** `02-explore-a-codebase` (C3, W8-light) — `unit.md`; **read-only** exploration lab w/ file+symbol answer key (no tag/branch/verifier — R7.AC3 prose self-check); C3 lab-traced. `search-refs` vd key left unverified (headless; L1).
      - [x] **U4** `04-memory-and-context` (C5) — home of memory/context/config teaching (R11.AC4). `unit.md` covers project `CLAUDE.md` (area 7), context as a managed resource (area 8), `settings.json`/sources (area 26), output-styles awareness (area 28). **A/B memory lab** `u04-lab1`: edit one `CLAUDE.md` line → behavior changes, confirmed via context inspector (CV); read-mostly (reverts with `git restore`, no tag/branch/verifier — R7.AC3). Dogfoods this repo's own `CLAUDE.md` (R14.AC1). C5 lab-traced; areas 7,8,26,28 traced; `make check` green. Consumes unverified `context-cmds`/`output-styles` (L1).
      - [x] **U5** `05-ship-a-feature` (C6, W1) — flagship Daily-Driver loop **explore→plan→code→commit**. `unit.md` references the generalized W1 in `meta/workflows.md` (not re-explained, R5.AC5); teaches plan mode as a review gate (area 9) + extended-thinking awareness (area 10, mention+pointer); two CV gates (the plan, then the diff). **Build-a-feature lab** `u05-lab1` (write-path, like U1): ship `GET /projects/{id}/stats` (per-status counts, zero-filled, ownership-404). Git refs `start/u05-lab1` (tag) + `solution/u05-lab1` (branch: `ProjectStats` schema + `project_task_stats` service via `get_project` + thin route + 3 tests); objective `verify.sh` checks contract + ownership + suite-green against the learner's working tree; `reset-lab`/`verify-lab` verified end-to-end. C6 lab-traced; areas 9,10 traced; `make check` green. Consumes verified `plan-mode`/`thinking` vd keys. Woven CV/security edge (foreign-project 404) satisfies R10.AC7 for this workflow lab.
      - [x] **U6** `06-tdd` (C7, W2) — Daily-Driver **red→green** test-first loop. `unit.md` references generalized W2 in `meta/workflows.md`; teaches writing the test first, **confirming red for the right reason** (assertion, not import/typo), implementing to green, and **reading the impl** (a test can be satisfied the wrong way) — the CV gate for test-driven work. **Test-first lab** `u06-lab1` (write-path): add an `overdue` filter to `GET /tasks` (overdue iff `due_date` strictly before today **and** `status != done`; done/due-today/no-due-date excluded; absent param unchanged). Git refs `start/u06-lab1` (tag) + `solution/u06-lab1` (branch: `TaskFilters.overdue` + predicate in `list_tasks` vs `date.today()` + one route query param + edge-case tests); objective `verify.sh` checks contract + no-regression suite-green against the learner's working tree; `verify-lab` verified end-to-end (fails clean = all 6 returned, the right-reason red; passes on solution). C7 lab-traced; area 11 traced; `make check` green. Consumes `test-run` vd key (kept `unverified` under L1). Edge-case assertions are the woven CV (R10.AC7).
      - [x] **U7** `07-debug-a-failure` (C8, W3) — Daily-Driver **scientific-method debugging**: reproduce → capture a re-runnable repro → **confirm root cause** (resist the AI's plausible symptom-patch) → fix → no-regress. `unit.md` references generalized W3 in `meta/workflows.md`. **Debug lab** `u07-lab1` on the **legacy** `taskflow-cli`: fix baked-in bug **D1** (overdue never flags — ISO date compared against `MM-DD-YYYY` string, copy-pasted in 3 sites) at its root. Git refs `start/u07-lab1` (tag = legacy with bug present) + `solution/u07-lab1` (branch: correct `is_overdue` via `date.fromisoformat`, `fmt_due`/`print_task_full` routed through it). Objective `verify.sh` drives the CLI via subprocess over a throwaway DB (legacy has no pytest): past-due flagged across `list --overdue`/`stats`/`list`+`show` display, future/no-due/done excluded, basic CLI intact; verified end-to-end (fails on start = the automated repro, passes on solution). C8 lab-traced; area 12 traced; `make check` green. No version-specific keys (no L1 debt). D2/D3 left for extra practice + U9.
      - [x] **U8** `08-git-and-pr` (C9, W4) — Daily-Driver **turn work into a reviewable PR**: stage deliberately into atomic commits, messages that explain *why*, a PR description that matches `git diff main...HEAD`, self-review as the reviewer. `unit.md` references generalized W4 in `meta/workflows.md`; dogfooding worked example = this repo's own clean-commit/PR history. **Prose-self-check lab** `u08-lab1` (NO `start/`/`solution/` refs, NO `verify.sh` — like U2/U4): make a real `archived`-flag change in `taskflow-api` review-ready, graded by an objective reviewer's checklist (R7.AC3); optional BYO `gh pr create` stretch (R7.AC8, non-verifiable; `gh` not required per R7.AC7). C9 + area 13 lab-traced via front matter + `## Lab`; consumes **verified** `git-pr` key (no L1 debt). `make check` green. Not in `SEEDED.md` §2 (no defect/branch).
      - [x] **U9** `09-onboard-refactor-legacy` (C10, W5 + W8-deep) — Force-Multiplier **onboard + behavior-preserving refactor** on the **legacy** `taskflow-cli`: deep-onboard and *validate* the map (W8 deep, the heavy version of U2's light explore), **establish a characterization safety net first** (legacy has no tests), refactor the ~700-line god-module in reviewable increments, keep behavior identical before/after (W5), and **keep the U7 overdue bug-fix OUT** of the refactor (scope-creep guardrail = the woven CV). `unit.md` references generalized W5+W8 in `meta/workflows.md`; dogfooding worked example = the `tools/_common.py` extraction shared by the six `check-*`. **Refactor lab** `u09-lab1`: split the monolith + de-duplicate (two lookups→one, id helpers, **three** overdue copies→one), preserving the seeded D1/D2/D3 bugs. Git refs `start/u09-lab1` (tag = messy monolith as-is) + `solution/u09-lab1` (branch: `taskflow_app/` package — constants/storage/domain/lookups/formatting/commands/cli behind a 16-line `taskflow.py` entry; dead code dropped; bugs intact; + stdlib characterization tests). Objective `verify.sh` is a **behavior-equivalence** check: runs a 35-command battery against both the original (materialized from the tag) and the learner's tree, asserts identical transcripts (timestamps redacted) — so it **fails on ANY behavior change, including "fixing" D1/D2** (verified: a D1 fix makes it fail) — plus a structural gate that the monolith was actually split. Verified end-to-end (fails on untouched monolith = "not split"; passes on solution). C10 + area 14 lab-traced; `make check` green. No version-specific keys (no L1 debt). Legacy lab ⇒ not in `SEEDED.md` §2 (the refactor targets are SEEDED §1 smells).
      - [x] **U10** `10-spec-driven-dev` (C11, W7) — Force-Multiplier **build a feature spec-first**: requirements → design → tasks with a **real approval gate between phases** and **two-way traceability** (every design/task names the requirement it serves; every requirement has a design + task), for features whose cost-of-wrong is high. `unit.md` references generalized W7 in `meta/workflows.md`; **worked example = THIS repo's own `specs/claude-code-mastery/` tree** (R3.AC2) — EARS requirements with stable IDs, design sections tagged `[R…]`, phased tasks, `decisions.md`, read-`IMPLEMENTATION.md`-first. **Prose-self-check lab** (NO `start/`/`solution/` refs, NO `verify.sh` — like U2/U4/U8): run a mini spec for a deliberately-ambiguous `taskflow-api` feature (**task dependencies** — the spec must *decide* cycle handling, cross-project deps, the blocked-completion error, blocker-deletion behavior), then build against it; graded by an objective **rubric** (R7.AC3 — spec quality + whether a gate was genuinely held are judgment calls no script can grade). C11 + area 15 lab-traced via front matter + `## Lab`; consumes **no** version-specific keys (no L1 debt). `make check` green. Not in `SEEDED.md` §2 (no defect/branch).
      - [x] **U11** `11-code-and-security-review` (C12, CV, W6) — Force-Multiplier **review for correctness + security, then triage**: run `/code-review` + `/security-review` as a **first pass**, then confirm real findings with a repro/test and **dismiss false positives with a reason** ("the review is a lead, not a verdict"); **consolidates CV** (green tests necessary, not sufficient). `unit.md` references generalized W6 in `meta/workflows.md`; dogfooding worked example = `make check` as an automated first-pass reviewer (incl. its U6 false-positive triage). **Verifier-backed review lab** `u11-lab1` (primary): a "project archiving" feature branch with **two real planted defects + one false positive** — **IDOR** (`archive_project` uses a bare `session.get` and skips the `owner_id` check, unlike every other mutation), **wrong default** (`include_archived` defaults `True`, showing archived by default; contract = exclude), and a `Project.archived == False` E712 lint that's correct SQLAlchemy (**dismiss**). Git refs `start/u11-lab1` (tag = defective, happy-path tests green) + `solution/u11-lab1` (branch: ownership routed through `get_project`, default flipped to `False`, FP kept, + cross-user-404 & default-exclusion tests). Objective `verify.sh` drives the API via TestClient: cross-user archive→404 + no effect, owner archive works, default list excludes archived / `include_archived=true` includes, suite green; verified end-to-end (fails on start = cross-user 200 + default shows archived, passes on solution). C12 + CV + area 16 lab-traced; consumes **verified** `review-cmds` key (no L1 debt); `SEEDED.md` §2 row filled. `make check` green.
- [ ] Per unit: verify version-specific details vs installed CLI; record provenance (R12.AC3–AC4)
- [ ] Per unit: reference authentic dogfooding artifacts where they exist (R14.AC2)

### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
- [ ] Capstone brief menu + worked exemplar (R8.AC2) · self-applicable rubric covering all can-do
      statements (R8.AC3) · structured verification-reflection prompts (R8.AC6) · optional AI-self-grade (R8.AC5)
- [ ] Optional mid-course checkpoint (R8.AC7)
- [ ] "How this was built/maintained" case study (R14.AC4) · AI-authorship transparency note (R14.AC5)
- [ ] Learner-facing `README.md` · maintainer guide w/ "author a unit with Claude Code" recipe (R13.AC3)
- [ ] Run full enforcement + traceability suite green (local + CI); meet Definition of Done (`IMPLEMENTATION.md` §6)
