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

> **Update obligation:** this dashboard is the **first thing a fresh session reads** — keep it
> **terse** and refresh it at every phase/unit boundary (and the matching `tasks.md` status header).
> Per-unit and per-decision detail is **not** duplicated here; it lives in `tasks.md` (§P5) and the
> `decisions.md` ledger. A stale §3 silently misleads the next session.

| Phase | Status |
|---|---|
| 1. Requirements (`requirements.md`) | ✅ **APPROVED** (2026-05-29) — turn-by-turn review; gap-free IDs |
| 2. Design (`design.md`) | ✅ **APPROVED & merged to `main`** (2026-05-29) — §0–§11; design gate passed |
| 3. Tasks (`tasks.md`) | ✅ v1 **COMPLETE** (2026-05-30) — P1–P6 executed; `make check-strict` green. ✅ **P7 (Quality pass) COMPLETE** (2026-05-31) |
| Rationale (`decisions.md`) | ✅ Per-phase decisions + the canonical 🔓 open-loops ledger |

**Phase 3 (Tasks) breakdown:** P1 ✅ · P2 ✅ · P3 ✅ · P4 ✅ (both lab codebases built; `SEEDED.md`
inventory + offline mock) · **P5 ✅ — all 16 units (U1–U16) authored; every can-do C1–C17+CV practiced
by ≥1 lab** · **P6 ✅ — capstone (briefs/exemplar/rubric), build case study + transparency note,
maintainer guide, README finalized, `tools/render-checklist` added; `make check-strict` green = the
v1 Definition-of-Done mechanical gate (L3) passes.** Current branch: **`main`** (P6 committed).

**P7 — Quality pass (post-v1, ✅ COMPLETE 2026-05-31).** A systematic 8-lens quality pass found the
product mechanically/functionally clean; remediation was confined to learner-facing prose + a closed
version-token rendering gap (new `tools/render-units` committed-rendered pattern + `tools/render-index`
navigation). **No new requirements** (traces to R5/R6/R9/R12/R15). **All 16 units** migrated to
`unit.src.md` + de-coded; capstone files + `stuck.md` swept; convention docs updated for the split; L2
reading-time bumps (U12/U13/U14) applied; per-unit render-and-eyeball fixed the `{{vd:*}}` garbles.
Built in slices on branch **`spec/quality-pass-phase`**, now **merged & pushed to `main`**. **L8 struck**; its
lone optional follow-up **T2** (unit-dir rename) is now **closed as won't-do** (2026-05-31, P7-T2-close) —
**P7 has no outstanding items.** See `decisions.md` → "P7 — Quality pass" and `tasks/P7-quality-pass.md`.

**Closeout amendment (2026-05-31):** added a session-transcript capture workflow
(`tools/render-transcript`, `tools/scan-secrets`, the `capture-session` skill) and back-filled the 14
historical build sessions into `log/transcripts/{raw,rendered}/` behind a human-reviewed secret-scan
gate, and removed the lossy `/export` `.txt` logs they replace. See `decisions.md` → **P7-amendment**.

**P8 — Version-resilience enhancements: CLI reference + changelog digest (post-v1, ✅ COMPLETE 2026-05-31).**
Two new requirements **APPROVED**, **design §12 APPROVED & committed**, and **all 9 task slices (8.1–8.9)
built** spec-first on `feat/cli-reference`; `make check` green. **Merged to `main`** (2026-05-31).
- **R16** — exhaustive, generated, version-resilient CLI reference: one tool (`tools/render-cli-reference`,
  modes `--generate`/`--render`/`--all`/`--check`) recursively introspects `claude --help` →
  `meta/cli-reference.json` (byte-stable machine truth) ∪ a provenance-tracked
  `meta/cli-reference-supplement.yaml`; renders learner-facing `course/reference/cli-reference.md` from the
  machine source alone. Expensive introspection runs only in `--generate`/`--all`; `--check` is offline.
- **R17** — CLI version-change synopsis (changelog digest) captured on every refresh, cumulative across
  the version gap, official-changelog provenance, with an automated check that the recorded version has a
  matching digest entry. Proposed artifact `meta/version-changelog.md`.

Both regenerate on version drift (R12.AC6/AC7) and gate in `make check`. Dogfooded by **U10** (built
spec-driven) + **U4** (single-source version data, points at `cli-reference.json`). Delivered: the
`tools/render-cli-reference` tool (4 modes), `meta/cli-reference.{json,schema.json}` +
`cli-reference-supplement.yaml`, `course/reference/cli-reference.md`, `meta/version-changelog.md` +
`tools/check-version-changelog`; `check-traceability` now **discovers requirements dynamically** from
`requirements.md` (no hardcoded `R#` range, R13.AC5); maintainer-guide gained the "Adding a post-v1
enhancement" playbook. **Note:** the P8 drift-ahead (`cli-reference.json` @ **2.1.159**, `version-record.md`
@ 2.1.158) was closed by the **version refresh of 2026-05-31** — `version-record.md` now records **2.1.159**
(internal-infra bump, surface byte-stable; ledger **L9** struck). Built on **`feat/cli-reference`**, now
**merged & on `main`**. See `decisions.md` → "P8 — …" / L9 and `tasks/P8-cli-reference.md`.

**v1 build is complete.** Remaining is **not release-blocking**: **L1** is now mostly closed — the
interactive `/help`+docs pass (2026-05-30) verified 5 of the 7 keys; only `ci` (GitHub Action wrapper)
and `managed-settings` (enterprise) stay `unverified`, each blocked by access this environment lacks
(Gitea instead of GitHub Actions; no enterprise account). See the 🔓 ledger in `decisions.md`.

**P9 — Collaboration retrospective (R18) + breadcrumb nav (R19) (post-v1, 🟢 BUILDING — 2026-06-01).**
Two new requirements via the post-v1 playbook, on branch **`feat/collaboration-retrospective`**. **R18** —
a multi-agent, self-evaluating retrospective of this build: 11 subjective reviewers (10 fenced read-only
personas + 1 no-persona control) read the session transcripts into a **session × reviewer matrix** corpus
(`log/evaluations/`) + a learner case study (`course/case-studies/`). Requirements + design (§13) + tasks
plan (`tasks/P9`) **approved & committed**. **Build: 9.1–9.4 ✅ DONE** (panel authored under
`.claude/agents/`; corpus conventions + `tools/check-evaluations` gate; `/evaluate-session` command;
pilot **PASS** over the foundational session). **9.5 🟢 IN PROGRESS** — full-corpus leaf pass; leaf and
synthesis stages run as separate passes. **Workflow update (2026-06-01, `P9-leaf-workflow`):** the
"one evaluated-session per *fresh* session" ritual is **retired** — now that `/evaluate-session` reviewers
write their own leaves and return only receipts (`P9-leaf-write`), the master-context cost is small, so
remaining passes run as **ordinary work** under standard context management. Leaf cells:
**143/253 — 13 of 23 sessions** have a full 11-reviewer pass (foundational, catalog-approval, design-approval,
p4-sample-codebases, u1-onboarding, u3-operate-safely, u5-unit-authoring, u6-open-loops-audit, u10-unit-authoring, u12-commands-skills, u13-subagents, p6-capstone-finalization, l1-version-key-verification); 10 sessions remain. Per-session syntheses: **1/23**
(foundational only). Then 9.6 globals/corner → 9.7 case study → 9.8 dogfood wiring → 9.9
close-out. R18 **already passes `check-traceability`** (referenced from the 9.2 corpus artifacts —
`meta/conventions.md`, `tools/check-evaluations`, the `/evaluate-session` command); its binding gate is
**corpus completeness** via `check-evaluations` (`PEND` in `check`, hard-fail in `check-strict` until the
matrix is whole), not the traceability mention. `make check-strict` currently fails on **R19** (unreferenced
— design deferred, L12) **+ the incomplete corpus** — both expected (see `tasks/P9` §note 2). **R19** (breadcrumb nav for learner docs) is an approved requirement with **design
deferred** until R18 ships. See `decisions.md` → "P9 …" / ledger **L11**–**L13** and
`tasks/P9-collaboration-retrospective.md`.

**Where the detail lives** (don't restate it here):
- Per-unit build notes (what each unit/lab is, its refs, its traceability) → [`tasks.md`](./tasks.md) §P5.
- Design decisions, rationale, and the 🔓 open-loops ledger → [`decisions.md`](./decisions.md).
- Version keys still to verify against the CLI → `meta/version-record.md` (and open loop **L1**).

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
