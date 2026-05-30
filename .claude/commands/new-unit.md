---
description: Scaffold a new course unit directory from the core template
argument-hint: <NN> <slug>
---

Scaffold a new course unit from the single source of truth. Arguments: `NN=$1` (zero-padded
two-digit number, e.g. `13`), `slug=$2` (kebab-case, e.g. `13-subagents`).

Do this:

1. Stop if `course/units/$1-$2/unit.md` already exists — never clobber an authored unit.
2. Pick the template by tier: `meta/templates/unit-core.md` for a core unit,
   `meta/templates/unit-awareness.md` for an awareness unit (default: core — all v1 units are core).
   Copy it to `course/units/$1-$2/unit.md`.
3. Fill the YAML front matter **from the meta files — do not invent values**:
   - `id`, `use_case`, `stage`, `depth_tier`, `can_do`, `workflows` → the `U$1` entry in
     `meta/use-case-catalog.yaml`.
   - `coverage_areas` → every area in `meta/coverage-matrix.yaml` whose `covered_by` names `U$1`.
   - `prerequisites` → the `U$1` row of the dependency graph in `design.md` §"Unit map".
   - `reading_time_min` / `lab_time_min` → leave a sensible estimate for the author to confirm.
4. Delete the template's HTML guidance comments as you fill each section. Leave the prose sections
   (Concept, Worked example, Lab, etc.) as template stubs for the author to write — this command
   scaffolds, it does not author content.
5. Reference any version-specific value only as `{{vd:key}}` (R12.AC2) — never hardcode a command,
   flag, path, or settings key from memory.
6. Run `make check` and report the result.
