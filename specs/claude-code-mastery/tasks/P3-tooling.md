# P3 — Tooling & enforcement

**Goal:** build the enforcement suite **before** the content (P4/P5) so it guards authoring from day
one and so the checks exist as the authentic worked examples the hooks/CI units (U14/U16) reference.

**Inputs:** `design.md` §5, §8 · Targets the artifacts seeded in P2.

## Tasks

### 3.1 Package skeleton
- [x] `tools/` as a small Python package (matches codebase stack); `Makefile` with `make check`
      (runs the full suite) and per-check targets. [R13]
- [x] `{{vd:key}}` resolver/build step: reads `meta/version-data.*`, renders callouts in prose;
      unresolved key ⇒ hard error (feeds 3.5). [R12.AC2]

### 3.2 Preflight
- [x] `tools/doctor` — checks install, version-floor, authentication, a first command (pass/fail),
      **+ manual checklist fallback**. Written to double as a "scripting Claude Code" worked example. [R11.AC2, R14.AC2]

### 3.3 Required check suite (R13.AC4)
- [x] `check-frontmatter` — validate each unit's front matter against `unit-frontmatter.schema.json`. [R13.AC4a]
- [x] `check-coverage` — every can-do (C1–C17+CV) **and** every coverage-matrix area covered by ≥1 unit/lab. [R13.AC4b]
- [x] `check-links` — internal + external link checking. [R13.AC4c]
- [x] `check-version-refs` — every `{{vd:key}}` in prose resolves to a key in `version-data`. [R13.AC4d]

### 3.4 Traceability checks (R13.AC5)
- [x] `check-traceability` — every requirement ID referenced by ≥1 unit/artifact; every can-do traces
      to ≥1 lab **and** ≥1 capstone-rubric dimension. [R13.AC5]

### 3.5 Drift detection (R12.AC6)
- [x] `check-version-drift` — installed `claude --version` vs `version-record`; where feasible diff the
      `claude --help` command list vs a recorded snapshot to surface new/removed/renamed commands. [R12.AC6]

### 3.6 Lab tooling (design §7)
- [x] `tools/verify-lab.sh <id>` — run a lab's automated check. [R7.AC5]
- [x] `tools/reset-lab.sh <id>` — restore the `start/<id>` tag for a clean next lab. [R7.AC6]

### 3.7 Wiring (R13.AC6)
- [x] Local: git `pre-commit` running the suite (active via `core.hooksPath .githooks`). [R13.AC6]
      _Note: the **Claude Code in-session hook** is deferred to **U14** (the hooks unit), where it is
      authored hands-on and verified against the CLI — that hook IS the course's enforcement hook
      (R14.AC2), so building it under R12.AC3 discipline belongs there, not here. pre-commit + CI
      provide enforcement now._
- [x] CI: `.github/workflows/checks.yml` (GitHub Actions) runs the suite as the backstop gate. [R13.AC6]
- [x] Schedule/trigger `check-version-drift` to prompt refresh on CLI releases. [R12.AC7]

## Definition of Done (P3)
- [x] `make check` runs the full suite **green** against the P2-seeded artifacts, locally and in CI. [R13.AC4/AC6]
- [x] `doctor` passes on a correctly set-up machine and fails loudly otherwise. [R11.AC2]
- [x] Checks are clean enough to be shown verbatim as the U14/U16 worked examples. [R14.AC2/AC3]
