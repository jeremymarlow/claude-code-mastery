# P2 — Scaffolding & cross-cutting artifacts

**Goal:** materialize the repo skeleton and the single-source machine-readable `meta/*` artifacts
**from** the approved design, so P3 tooling has something to validate and P5 units have something to
reference. Nothing here is invented — each file is generated from the cited design section.

**Inputs:** `design.md` §1, §2, §3, §4, §5, §6, §9 · **Verify version facts against CLI 2.1.158** (R12.AC3).

## Tasks

### 2.1 Repo skeleton (design §9)
- [ ] Create the directory layout from design §9 (`course/`, `codebases/{primary,legacy}/`, `meta/`,
      `meta/templates/`, `tools/`, `.claude/`, `.github/workflows/`). [R13.AC1]
- [ ] `meta/conventions.md` — naming/style conventions (units `NN-slug`, `start/uNN-labM` +
      `solution/uNN-labM`, kebab-case meta/tools, `{{vd:key}}`). [R13.AC1]
- [ ] `meta/glossary.md` — terms from requirements §2, centralized & referenced (not duplicated). [R13.AC2]

### 2.2 Capability map (design §1)
- [ ] `meta/capability-map.yaml` — C1–C17 + CV, each `{id, statement, stage, home_unit}`. [R1]
- [ ] Generate `meta/capability-map.json` (tooling reads this). [R13.AC2]

### 2.3 Use-case catalog (design §2)
- [ ] `meta/use-case-catalog.yaml` — U1–U16, each `{unit, stage, job, success, workflows, features,
      grounding, advances, depth_tier: core}` + recorded prioritization rationale. [R2.AC2/AC4]

### 2.4 Workflows (design §3)
- [ ] `meta/workflows.md` — W1–W9 table (decision criterion, verification, stage, units) **plus** the
      generalized pattern write-up per workflow; units reference this, don't re-explain. [R3, R5.AC5]

### 2.5 Coverage matrix (design §4)
- [ ] `meta/coverage-matrix.yaml` — 29 areas, each `{id, area, tier, covered_by, version_data_key}`;
      intentional-exclusion/awareness notes recorded. [R4.AC1/AC4/AC5]

### 2.6 Version layer (design §5)
- [ ] `meta/version-data.yaml` — seed one entry per `vd:*` key referenced in the coverage matrix;
      **verify each value against the installed CLI** (`--help`/`/help`/docs) and record `provenance`,
      `verified_version: 2.1.158`, `verified_date`; mark anything unverifiable `unverified: true`. [R12.AC2/AC3/AC4]
- [ ] Generate `meta/version-data.json`.
- [ ] `meta/version-record.md` — table seeded at **2.1.158 / 2026-05-29 / method**. [R12.AC5]

### 2.7 Unit model (design §6)
- [ ] `meta/unit-frontmatter.schema.json` — JSON Schema for unit front matter (all keys from §6). [R6.AC3]
- [ ] `meta/templates/unit-core.md` + `meta/templates/unit-awareness.md` — the two ordered templates. [R6.AC1/AC2]

### 2.8 Dogfooding + learner-facing scaffolds
- [ ] `CLAUDE.md` (repo root) — project memory; **authentic** (used to build the course). [R14.AC1]
- [ ] `course/progress-checklist.md` — **generated from** `capability-map` (do not hand-maintain). [R9.AC5]
- [ ] `course/stuck.md` — "when you're stuck": hints-vs-solutions, FAQ, using Claude Code to get unstuck. [R9.AC4]
- [ ] Top-level `README.md` (learner-facing) — entry capabilities assumed + full can-do set delivered. [R1.AC6]

## Definition of Done (P2)
- [ ] Every `meta/*` artifact is machine-readable and consistent with its design section. [R13.AC2]
- [ ] `capability-map` ↔ `use-case-catalog` ↔ `coverage-matrix` cross-reference cleanly (every C-id has
      a home unit; every area has a covering unit) — will be enforced by P3 `check-coverage`.
- [ ] No version-specific value authored from memory; all carry provenance or `unverified`. [R12.AC3]
