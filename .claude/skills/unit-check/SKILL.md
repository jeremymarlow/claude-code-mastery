---
name: unit-check
description: Run the course enforcement suite (make check) and report per-unit pass/fail status. Use after authoring or editing a unit to confirm front matter, coverage, links, version-refs, and traceability are green before committing.
---

# Unit check

Run the course's enforcement suite and report unit health. The suite is the source of truth for
whether a unit is well-formed (R13) — trust it over a manual read.

1. Run `make check` from the repo root.
2. **Green:** report "all checks passed" plus the one-line summary; you're clear to commit.
3. **Red:** name which check failed and which unit(s) it points at, then state the specific fix —
   do not auto-fix unless asked. The five checks and what each guards:
   - `frontmatter` — YAML validates against `meta/unit-frontmatter.schema.json` (R6.AC3).
   - `coverage` — every can-do / coverage area is practised by a lab at its tier (R4).
   - `links` — internal references resolve (the dogfooded `tools/check-links`).
   - `version-refs` — version-specific values appear only as `{{vd:key}}`, never hardcoded (R12).
   - `traceability` — units ↔ requirements ↔ capabilities map both ways (R13.AC5).

Each check is also runnable on its own: `tools/check-frontmatter`, `tools/check-coverage`,
`tools/check-links`, `tools/check-version-refs`, `tools/check-traceability`. The release gate is the
stricter `make check-strict`, which fails on not-yet-authored (PENDING) coverage.
