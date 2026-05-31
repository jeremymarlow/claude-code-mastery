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
Each unit: tier-appropriate template (R6) + valid front matter (R6.AC3) + lab/reference-solution/reset
(R7) + "common pitfalls" (R6.AC6) + "going deeper". Per-unit **rationale** lives in `decisions.md`
(`P5-UN-*`); per-unit build status in the 🔓 ledger's **L7**. `make check` green after every unit.
Each bullet below: **gist** · _Lab/refs_ · _Traceability & version keys_.

- [x] **U1** `01-onboarding-first-win` (C1, C2 · First Wins) — onboarding: `doctor` + first success + **establish** baseline config (R11; establish-not-teach).
  - _Lab_ `u01-lab1`: first-win one-line `"service"` field on `/health` (write-path). Refs `start/`+`solution/` + `verify.sh` (suite + live behavior); verified end-to-end. Baseline `CLAUDE.md` + `.claude/settings.json` shipped to `primary`.
  - _Trace:_ C1/C2 lab-traced.
- [x] **U2** `02-explore-a-codebase` (C3 · W8-light · First Wins) — explain architecture + locate a change site; validate Claude's summary vs the code.
  - _Lab_ `u02-lab1`: **read-only**, prose file+symbol answer key — no tag/branch/verifier (R7.AC3).
  - _Trace:_ C3 lab-traced. `search-refs` vd key left unverified (headless; L1).
- [x] **U3** `03-operate-safely` (C4, CV · First Wins) — **dedicated security unit** (R10.AC1): permission modes + bypass hazards (R10.AC2), secrets + prompt injection (R10.AC3), blast-radius/checkpoints (R10.AC4), define-your-own verification (R10.AC6).
  - _Lab_ `u03-lab1`: safety-fenced prompt-injection triage (R10.AC3/AC8) — untrusted fixture + plan-mode fence + objective `verify.sh` (zero side effects). Read-only (no `start/`/`solution/`, like U2).
  - _Trace:_ areas 3,4,5,6,29 (lab/intro/mention). Consumes unverified `checkpoint-rewind`/`managed-settings` (L1).
- [x] **U4** `04-memory-and-context` (C5 · First Wins) — **home** of memory/context/config teaching (R11.AC4): project `CLAUDE.md` (7), context as a managed resource (8), `settings.json`/sources (26), output-styles awareness (28).
  - _Lab_ `u04-lab1`: A/B — edit one `CLAUDE.md` line → behavior changes, confirmed via context inspector (CV); read-mostly (reverts with `git restore`, no refs/verifier). Dogfoods this repo's `CLAUDE.md` (R14.AC1).
  - _Trace:_ C5; areas 7,8,26,28. Consumes unverified `context-cmds`/`output-styles` (L1).
- [x] **U5** `05-ship-a-feature` (C6 · W1 · Daily Driver) — flagship **explore→plan→code→commit**; plan mode as a review gate (9) + extended-thinking awareness (10); two CV gates (plan, then diff).
  - _Lab_ `u05-lab1` (write-path): ship `GET /projects/{id}/stats` (per-status counts, zero-filled, ownership-404). Refs `start/`+`solution/` (schema + service via `get_project` + thin route + 3 tests) + `verify.sh` (contract + ownership + suite-green); verified end-to-end.
  - _Trace:_ C6; areas 9,10. Verified `plan-mode`/`thinking`. Foreign-project-404 = woven CV (R10.AC7).
- [x] **U6** `06-tdd` (C7 · W2 · Daily Driver) — red→green test-first: write the test, **confirm red for the right reason**, green, then **read the impl** (a test can be satisfied the wrong way) = CV gate.
  - _Lab_ `u06-lab1` (write-path): `overdue` filter on `GET /tasks` (overdue iff `due_date` < today **and** `status != done`; done/due-today/no-due excluded). Refs `start/`+`solution/` + `verify.sh` (contract + no-regression); verified end-to-end.
  - _Trace:_ C7; area 11. Consumes `test-run` (unverified, L1). Edge-case assertions = woven CV.
- [x] **U7** `07-debug-a-failure` (C8 · W3 · Daily Driver) — scientific-method debugging: reproduce → capture → **confirm root cause** (resist the symptom-patch) → fix → no-regress.
  - _Lab_ `u07-lab1` on **legacy** `taskflow-cli`: fix baked-in **D1** (overdue never flags — ISO vs `MM-DD-YYYY` string compare, in 3 sites) at its root. Refs `start/` (bug present) + `solution/` + subprocess `verify.sh` (legacy has no pytest); verified end-to-end (fails on start = the repro).
  - _Trace:_ C8; area 12. No version keys (no L1 debt). D2/D3 left for U9.
- [x] **U8** `08-git-and-pr` (C9 · W4 · Daily Driver) — turn work into a reviewable PR: atomic commits, why-messages, a description matching `git diff main...HEAD`, self-review as the reviewer.
  - _Lab_ `u08-lab1`: **prose-self-check** (no refs/verifier, like U2/U4) — make a real `archived`-flag change review-ready, graded by a reviewer's checklist (R7.AC3); optional BYO `gh pr create` stretch (R7.AC8). Dogfoods this repo's own clean-commit/PR history.
  - _Trace:_ C9 + area 13 (front matter + `## Lab`). Verified `git-pr` (no L1 debt). Not in SEEDED §2.
- [x] **U9** `09-onboard-refactor-legacy` (C10 · W5 + W8-deep · Force Mult.) — deep-onboard + *validate* the map, **build a characterization safety net first** (legacy has no tests), refactor the ~700-line god-module in increments keeping behavior identical, and **keep the U7 bug-fix OUT** (scope-creep guardrail = CV).
  - _Lab_ `u09-lab1` on **legacy**: split the monolith + de-dup (two lookups, id helpers, three overdue copies → one each), preserving D1/D2/D3. Refs `start/` (monolith) + `solution/` (`taskflow_app/` package + characterization tests) + **behavior-equivalence** `verify.sh` (35-command battery vs the original; fails on ANY behavior change incl. a D1 "fix"; + a "monolith was split" gate). Verified end-to-end. Dogfoods the `tools/_common.py` extraction.
  - _Trace:_ C10; area 14. No version keys (no L1 debt). SEEDED §2 row = legacy entry (no new primary defect).
- [x] **U10** `10-spec-driven-dev` (C11 · W7 · Force Mult.) — build a feature spec-first: requirements → design → tasks with a **real gate between phases** + **two-way traceability**, for high-cost-of-wrong work.
  - _Lab_ (prose-self-check, no refs/verifier — like U2/U4/U8): run a mini spec for a deliberately-ambiguous `taskflow-api` feature (**task dependencies** — cycles/cross-project/blocked-completion/blocker-deletion are the decisions a spec forces), then build against it; graded by a rubric (R7.AC3). **Worked example = THIS repo's own `specs/` tree** (R3.AC2).
  - _Trace:_ C11 + area 15. No version keys (no L1 debt). Not in SEEDED §2.
- [x] **U11** `11-code-and-security-review` (C12, CV · W6 · Force Mult.) — review for correctness + security, then **triage**: `/code-review` + `/security-review` as a first pass, then confirm real findings with a repro/test and **dismiss false positives with a reason**; **consolidates CV**.
  - _Lab_ `u11-lab1` (primary): a "project archiving" branch with **2 real defects + 1 false positive** — IDOR (`archive_project` skips the `owner_id` check), wrong default (`include_archived` defaults `True`), and a correct-SQLAlchemy `== False` E712 lint to **dismiss**. Refs `start/` (defective, tests green) + `solution/` (findings fixed, FP kept, + triage tests) + `verify.sh` (cross-user archive→404, default excludes archived, suite green); verified end-to-end. Dogfoods `make check` as a first-pass reviewer.
  - _Trace:_ C12 + CV + area 16. Verified `review-cmds` (no L1 debt). SEEDED §2 row filled.
- [x] **U12** `12-commands-and-skills` (C13 · Autonomy) — first Autonomy unit: package a repeated routine two ways — a **custom slash command** (saved, argument-taking prompt, `/name`) and a **skill** (named `SKILL.md` with a when-to-use description Claude can act on); when to reach for each (trigger + structure); project-vs-personal `.claude/` scope (ties to U4).
  - _Dogfood (R14.AC1):_ built two **real**, genuinely-used artifacts — `.claude/commands/close-unit.md` (`/close-unit <NN>` runs the post-authoring state-sync chore: IMPLEMENTATION §3 + tasks box/bullet + decisions/ledger + version-currency + `make check`) and `.claude/skills/prime-context/SKILL.md` (loads full project context at session start — read order + §3 status + open loops + git state). They bookend the authoring loop; worked example walks both. (Earlier `new-unit`/`unit-check` candidates were swapped out as props — no real consumer — see decisions `P5-U12-artifacts`.)
  - _Lab_ `u12-lab1` (prose-self-check, no refs — like U8/U10): learner builds one command (`/scaffold-route <name>`) + one skill (`api-test-triage`) in `taskflow-api`'s `.claude/`, graded by an objective checklist vs. the repo artifacts. A learner-consumable skill was **rejected as overboard** (area 18 covered by *building* one).
  - _Trace:_ C13 + areas 17,18. Verified `custom-commands`/`skills` (no L1 debt — already verified @ 2.1.158). Not in SEEDED §2 (no mutating branch).
- [x] **U13** `13-subagents` (C14 · Autonomy) — delegate a self-contained task to a **subagent** (a separate Claude with its own context window + optionally fenced toolset) and use the result it returns. The three reasons to delegate (context isolation / parallelism / fencing); subagent-vs-skill (separate context + returned result vs. reuse a prompt in your own context — ties to U12); scoping a self-contained brief; **delegation is trust delegation → verify the result** (ties to U3, sets up U15's MCP vetting).
  - _Lab_ `u13-lab1` (prose-self-check, no refs — like U8/U10/U12): learner defines a **read-only `explorer`** subagent in `taskflow-api`'s `.claude/agents/`, delegates a context-heavy mapping task (e.g. "where is ownership enforced? file:line + note"), uses the returned result, then **verifies ≥2 cited sites against the code** (the woven-CV step, R10.AC7). Objective checklist vs. the worked-example `explorer`; optional parallelism stretch (two independent briefs at once).
  - _Trace:_ C14 + area 19. Verified `subagents` key (`--agent`/`--agents <json>`/`agents` subcommand, `--help`-verified @ 2.1.158; added a `notes` flagging the on-disk `.claude/agents/` path as a filesystem convention) — **no L1 debt**. Not in SEEDED §2 (no mutating branch).
- [x] **U14** `14-hooks` (C15 · Autonomy) — wire a **hook**: a command the *harness* runs automatically on a lifecycle event (configured in `settings.json`), not something you/Claude invoke. The two moves — **block** (`PreToolUse` denies an action) and **react** (`PostToolUse` formats/tests/checks + feeds failures back); hook-vs-command/skill/subagent (enforced-not-invoked → the determinism is the safety property, ties to U3); event/matcher/command structure + stdin payload + JSON output.
  - _Dogfood (R14.AC2):_ wired this repo's **real** in-session hook — `.claude/settings.json` `PostToolUse`/`Write|Edit` → **`tools/check-on-edit`** (thin wrapper: gates on `course/`|`meta/` paths, runs `make check`, returns `decision:"block"` with the failing output). Same suite now runs **3 layers** — in-session hook + `.githooks/pre-commit` + GitHub Actions CI (defense in depth). **Closes open-loop L2.** Pipe-tested all paths (green→silent, unrelated→no-op, broken→block) + `jq -e` validated.
  - _Lab_ `u14-lab1` (no `start/`/`solution/` refs — artifact is a hook in the learner's `settings.json`; but objectively checkable): wire a hook in `taskflow-api` (react: `PostToolUse`→`pytest` on `app/` edits; or block: `PreToolUse`→deny `git push`), then **prove it fires** by driving it with synthetic event payloads (matching→acts, non-matching→silent) + `jq -e`. Self-check is that objective pipe-test, not prose.
  - _Trace:_ C15 + area 20. Verified `hooks` key — event-name enum + `{matcher, hooks:[{type,command}]}` structure confirmed against the **settings.json schema** (via update-config skill) @ 2.1.158; value/provenance/date updated. **No L1 debt.** Not in SEEDED §2 (no mutating branch).
- [ ] Per unit: verify version-specific details vs installed CLI; record provenance (R12.AC3–AC4)
- [ ] Per unit: reference authentic dogfooding artifacts where they exist (R14.AC2)

### P6 — Capstone, case study & finalization  → [`tasks/P6-finalize.md`](./tasks/P6-finalize.md)
- [ ] Capstone brief menu + worked exemplar (R8.AC2) · self-applicable rubric covering all can-do
      statements (R8.AC3) · structured verification-reflection prompts (R8.AC6) · optional AI-self-grade (R8.AC5)
- [ ] Optional mid-course checkpoint (R8.AC7)
- [ ] "How this was built/maintained" case study (R14.AC4) · AI-authorship transparency note (R14.AC5)
- [ ] Learner-facing `README.md` · maintainer guide w/ "author a unit with Claude Code" recipe (R13.AC3)
- [ ] Run full enforcement + traceability suite green (local + CI); meet Definition of Done (`IMPLEMENTATION.md` §6)
