# Start Here — Implementation Guide

**Spec:** `claude-code-mastery`
**Audience:** a Claude Code session (and its human) picking up this spec to build or maintain
the course. **You likely have no memory of how this spec was written** — this document and
[`decisions.md`](./decisions.md) are how that context is restored.

---

## 1. What this project is (in one paragraph)

A self-paced, solo, hands-on **course** that takes a seasoned developer who is new to
AI-assisted coding to elite Claude Code practitioner. It is **outcome-driven** (organized around
real use cases, not a feature tour), **tiered** for fast-learning senior engineers, and
**version-resilient** (targets the latest CLI; built to be refreshed as the tool changes — using
this spec). Assessment is a single capstone. See [`requirements.md`](./requirements.md) §1.

## 2. Read order (do this first, every fresh session)

1. **This file** — orientation + how to work within context limits.
2. [`decisions.md`](./decisions.md) — *why* the spec is the way it is; the rejected alternatives.
   Read before "improving" any requirement.
3. [`requirements.md`](./requirements.md) — the authoritative WHAT (R1–R15, EARS). Stable IDs.
4. [`design.md`](./design.md) — the HOW (architecture, schemas, artifact inventory, traceability).
5. [`tasks.md`](./tasks.md) — the ordered, chunked build plan.

The persistent project memory (auto-loaded each session) also points here. Trust the **files**
over memory for specifics; memory is a pointer, the spec is the source of truth.

## 3. Current state

> **Update obligation:** this table is the **first thing a fresh session reads** — refresh it at
> every phase boundary (and the matching `tasks.md` status header). A stale §3 silently misleads
> the next session. Open loops live in the canonical ledger: `decisions.md` → "Open loops & deferrals 🔓".

| Phase | File | Status |
|---|---|---|
| 1. Requirements | `requirements.md` | ✅ **APPROVED** (2026-05-29) — reviewed turn-by-turn, internally consistent, gap-free IDs |
| 2. Design | `design.md` | ✅ **APPROVED & merged to `main`** (2026-05-29; merge commit) — §0–§11 complete; design gate passed |
| 3. Tasks | `tasks.md` | 🟦 **IN PROGRESS** (2026-05-30) — per-phase files `tasks/P1–P6*.md` authored & traced. **P1 ✅ P2 ✅ P3 ✅ P4 ✅** (P4: both lab codebases built — `taskflow-api` 36 pytest green on `main`; `taskflow-cli` messy + 3 seeded bugs; `SEEDED.md` + offline `fixtures/mock_api.py`); **P5 in progress — U1 ✅, U2 ✅, U3 ✅, U4 ✅, U5 ✅, U6 ✅** (U1 onboarding/first-win: `unit.md` + lab `u01-lab1` + baseline config + refs `start/u01-lab1`/`solution/u01-lab1`, C1/C2 lab-traced. U2 explore-a-codebase: `unit.md`, C3, W8-light, **read-only** lab w/ answer key — no tag/branch/verifier. U3 operate-safely: dedicated security unit (R10.AC1), `unit.md` covers permissions/secrets/injection/blast-radius/verification + managed-settings awareness; **safety-fenced read-only prompt-injection lab** `u03-lab1` w/ fixture + plan-mode fence + objective `verify.sh` (R10.AC3/AC8), no start/solution refs like U2; C4/CV + areas 3,4,5,6,29 traced. `search-refs` still unverified; U3 now also consumes unverified `checkpoint-rewind`/`managed-settings` (L1). U4 memory-and-context: home of config/memory teaching (R11.AC4) — `CLAUDE.md`/`/context`/`settings.json` + output-styles awareness; **A/B memory lab** `u04-lab1` (read-mostly, CV via context inspector, reverts with `git restore`); dogfoods this repo's own `CLAUDE.md` (R14.AC1); C5 + areas 7,8,26,28 traced; consumes unverified `context-cmds`/`output-styles`. U5 ship-a-feature: flagship **explore→plan→code→commit** (W1) — references generalized W1 in `meta/workflows.md` (R5.AC5), teaches plan mode as a review gate (area 9) + extended-thinking awareness (area 10), two CV gates (plan, then diff); **build-a-feature lab** `u05-lab1` ships `GET /projects/{id}/stats` (write-path like U1) with `start/u05-lab1` tag + `solution/u05-lab1` branch + objective `verify.sh` (contract + ownership-404 + suite-green against the learner's working tree); C6 lab-traced; areas 9,10 traced; consumes **verified** `plan-mode`/`thinking` keys; foreign-project-404 edge satisfies woven-CV R10.AC7 for this workflow lab.) U6 tdd: red→green test-first (W2, area 11) — write the failing test, **confirm red for the right reason**, implement to green, read the impl (a test can be satisfied the wrong way); **test-first lab** `u06-lab1` adds an `overdue` filter to `GET /tasks` (overdue iff `due_date` strictly before today **and** `status != done`; done/due-today/no-due-date excluded) with `start/u06-lab1` tag + `solution/u06-lab1` branch + objective `verify.sh` (contract + no-regression suite-green vs working tree); C7 lab-traced; consumes `test-run` (kept `unverified` under L1); edge-case assertions are the woven CV. `make check` green; U7–U16 remaining; **P6 remaining** (capstone). On branch `spec/tasks-phase`. |
| — | `decisions.md` | ✅ Rationale + per-phase decisions captured; hosts the open-loops ledger |

## 4. Q1/Q2 — ✅ RESOLVED with the user (2026-05-29)

Both blocking inputs are now decided (full record in `decisions.md` → "Design session"):

- **Q1 ✅** — domain = **task/project tracker**; primary `taskflow-api` (FastAPI + SQLModel + pytest),
  legacy `taskflow-cli` (messy, untested). Concrete layout/seeded-bug inventory → design §7 / P4.
- **Q2 ✅** — capability map (C1–C17 + CV) and 16-unit use-case catalog **approved** (design §1/§2/§4).
  Unit count is **content-driven** (the "~12" was relaxed); security pulled forward to U3.

**Remaining open** (don't guess; see `decisions.md` → Open decisions): repo structure (§9),
per-feature awareness/core edge cases, capstone brief menu (R8). Next Design work: §3 (workflows),
§5 (version architecture), §6 (unit model/schema/templates), §7 (labs/codebases), §8–§10.

## 5. Context-management protocol (important — this is a large build)

The full course will exceed any single context window. Work in **bounded slices**:

- **Don't load everything.** For a given task, load: `requirements.md` (or just the relevant Rs),
  the relevant `design.md` section, and the one `tasks/<section>.md` you're executing. Skip the rest.
- **One unit at a time.** Authoring is per-unit. Each unit is self-contained (R6.AC5), so you can
  build unit N loading only its task file, its front-matter schema, and the cross-cutting artifacts
  it references — not the other units.
- **Cross-cutting facts live in single files** (`meta/…`), referenced by key, never duplicated
  (R13.AC2, R12.AC2). Read the one you need; don't inline its contents elsewhere.
- **Update state as you go.** Check off tasks in `tasks.md`/`tasks/*`, bump `meta/version-record.md`,
  and append to `decisions.md` when you make a non-obvious call. The next session reads these, not your memory.
- **Verify version-specific details against the installed CLI** (`--help`, `/help`, docs) — never from
  model memory (R12.AC3, hard rule). Record provenance (R12.AC4).

## 6. Definition of Done for the build (v1)

Implementation is complete when **all** hold:

1. Every requirement R1–R15 is satisfied and referenced by ≥1 artifact (traceability check passes, R13.AC5).
2. Every can-do statement traces to ≥1 lab **and** ≥1 capstone-rubric dimension (R1.AC5, R13.AC5).
3. Every capability area in the coverage matrix is covered at its assigned tier (R4.AC2; high-leverage ⇒ lab).
4. Every unit conforms to the tier-appropriate template with valid machine-readable front matter (R6, R13.AC4).
5. Every lab has objective self-check criteria, an inspectable reference solution, and a reset path (R7).
6. The capstone, its brief menu, exemplar, and self-applicable rubric exist (R8).
7. The two sample codebases exist and pass their own test suites (R7.AC1–AC2).
8. The required enforcement suite + traceability checks run green locally and in CI (R13.AC4–AC6).
9. The version-data file, version-record, and drift-detection check exist and pass (R12).
10. Dogfooding artifacts exist and are accurately referenced; the build case study + transparency note exist (R14).
11. The "when you're stuck" recovery resources and the learner progress checklist exist (R9.AC4–AC5).

**Mechanical gate (added P3):** `make check-strict` green is the single automated signal that the
front-matter, coverage, version-reference, and traceability obligations (items 1–4 above) are *all*
met — it turns the build-time `PENDING` markers (not-yet-authored labs / rubric / requirement refs)
into hard failures. `make check` (non-strict) is the day-to-day authoring guard and stays green
throughout the build; **`make check-strict` is expected to fail until P6 completes** and must pass
for v1 done. (Items 5–7, 10 — codebases, capstone artifacts, case study — are verified by their own
P4/P6 checks and review, not by the static suite.)

## 7. Maintenance (when the CLI changes later)

Follow the R12.AC7 refresh process: run the drift-detection check → re-verify the flagged
version-specific details against the installed CLI → update **only** `meta/version-data.*` and any
truly affected locations → bump `meta/version-record.md` → re-run the enforcement suite. Because
version-specifics are quarantined (R12.AC2/AC8), a version bump should touch a bounded set of files,
not the prose.
