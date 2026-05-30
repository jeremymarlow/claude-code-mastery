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
- [ ] Per unit: verify version-specific details vs installed CLI; record provenance (R12.AC3–AC4)
- [ ] Per unit: reference authentic dogfooding artifacts where they exist (R14.AC2)

### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
- [ ] Capstone brief menu + worked exemplar (R8.AC2) · self-applicable rubric covering all can-do
      statements (R8.AC3) · structured verification-reflection prompts (R8.AC6) · optional AI-self-grade (R8.AC5)
- [ ] Optional mid-course checkpoint (R8.AC7)
- [ ] "How this was built/maintained" case study (R14.AC4) · AI-authorship transparency note (R14.AC5)
- [ ] Learner-facing `README.md` · maintainer guide w/ "author a unit with Claude Code" recipe (R13.AC3)
- [ ] Run full enforcement + traceability suite green (local + CI); meet Definition of Done (`IMPLEMENTATION.md` §6)
