# Maintainer guide

How to add or update a unit — and refresh the course when the CLI changes — **without breaking the
catalog, coverage matrix, or capability map** (R13.AC3). The automated checks are your backstop, but
they tell you *that* something broke, not *how to avoid* breaking it; this guide is the "how."

If you are picking up this repo cold, start by reading
[`../specs/claude-code-mastery/IMPLEMENTATION.md`](../specs/claude-code-mastery/IMPLEMENTATION.md) and
running the [`prime-context` skill](../.claude/skills/prime-context/SKILL.md) — see the recipe below.

## The invariants you must not break

Everything cross-cutting lives **once** and is referenced by key (R13.AC2); duplication rots. The
[checks](../tools/) enforce these — run `make check` and keep it green:

- **Front matter** — every `course/units/NN-slug/unit.md` validates against
  [`unit-frontmatter.schema.json`](../meta/unit-frontmatter.schema.json) (`check-frontmatter`).
- **Coverage** — every can-do (C1–C17 + CV) is advanced by ≥1 unit, every coverage-matrix area is
  covered, and every `advances`/`covered_by` id is real (`check-coverage`).
- **Links** — every internal relative link resolves (`check-links`). A link to a not-yet-created file
  fails the build, so reference forward targets as plain text until they exist.
- **Version references** — every version-data token (the `vd:` references) in `course/**` resolves to
  a key in [`version-data.yaml`](../meta/version-data.yaml) (`check-version-refs`).
- **Traceability** — every requirement R1–R15 is referenced by a course artifact, and every can-do
  traces to ≥1 lab **and** ≥1 capstone-rubric dimension (`check-traceability`).

`make check` is the day-to-day guard; `make check-strict` is the release gate (it turns
not-yet-authored placeholders into hard failures).

## Adding a unit

Work in this order — **meta artifacts first, prose second** — so the single sources of truth lead and
the checks pass as you go:

1. **Decide what it teaches.** If it introduces a genuinely new capability, add the can-do to
   [`capability-map.yaml`](../meta/capability-map.yaml) (and regenerate its `.json` twin — never
   hand-edit the JSON). Otherwise map the unit to existing can-dos.
2. **Register it in the catalog.** Add the unit to
   [`use-case-catalog.yaml`](../meta/use-case-catalog.yaml) (`advances:` the can-dos it teaches) and
   ensure the [`coverage-matrix.yaml`](../meta/coverage-matrix.yaml) areas it covers point back at it
   (`covered_by:`).
3. **Create the unit from a template.** Copy [`unit-core.md`](../meta/templates/unit-core.md) (or
   [`unit-awareness.md`](../meta/templates/unit-awareness.md) for an awareness-tier unit) to
   `course/units/NN-slug/unit.md`, using a zero-padded `NN` and kebab-case slug
   (see [`../meta/conventions.md`](../meta/conventions.md)). Fill the front matter — its `can_do` list
   is what the traceability check reads.
4. **Author the lab.** Either a **mutating** lab — a `start/uNN-labM` tag (clean state), a
   `solution/uNN-labM` branch, a row in [`../codebases/SEEDED.md`](../codebases/SEEDED.md), and an
   objective `course/labs/<id>/verify.sh` (run it with [`verify-lab`](../tools/verify-lab)) — or a
   **non-mutating** lab (read-only / prose-self-check / objective pipe-test) with no refs, documented
   as such. The lab must trace a can-do: a `## Lab` heading plus the front-matter `can_do`.
5. **Quarantine version-specifics.** Never type a command, flag, path, or settings key from memory —
   put it in [`version-data.yaml`](../meta/version-data.yaml), verified against the installed CLI, and
   reference it by its version-data key (the token convention is in
   [`../meta/conventions.md`](../meta/conventions.md)) (R12.AC3).
6. **Cover it in the rubric if it adds a can-do.** A new can-do needs a `[Cn]`-tagged dimension in
   [`capstone/rubric.md`](./capstone/rubric.md), or `check-traceability --strict` fails.
7. **Sync state and check.** Run the [`close-unit` command](../.claude/commands/close-unit.md) to
   update `IMPLEMENTATION.md` §3, check the `tasks.md` box, log the decision, and run `make check`.

## Updating a unit

Edit the prose, then keep its references honest: if you rename or move anything it links to, fix the
link (`check-links`); if you change what it teaches, update the catalog/coverage entries and the
rubric to match (`check-coverage`, `check-traceability`). Re-run `make check`. The in-session hook on
edits under `course/`/`meta/` runs the suite for you and blocks on failure.

## Authoring a unit *with* Claude Code (the recipe)

This is the loop the course was built with, using its own dogfooded extensions (R14.AC2):

1. **Prime context.** Run the [`prime-context` skill](../.claude/skills/prime-context/SKILL.md) — it
   reads the spec in canonical order, surfaces the live status and open loops, and reports git state,
   so the session starts grounded in the files rather than guessing.
2. **Work one unit, in a bounded slice.** Load only the relevant requirements, the one `design.md`
   section, the front-matter schema, and the cross-cutting `meta/` artifacts the unit references — not
   the whole spec. Draft the meta entries, then the unit and lab, against the invariants above.
3. **Verify as you go.** Let the edit hook / `make check` catch breakages early; verify any
   version-specific claim against the installed CLI, never from memory.
4. **Close the unit.** Run [`close-unit`](../.claude/commands/close-unit.md) to sync every state file
   and run the checks in one step — the same chore, done the same way each time.

## Refreshing when the CLI changes

When Claude Code updates, refresh rather than rewrite (R12.AC7). The full process is in the
[build case study](./capstone/case-study.md) §5: run
[`check-version-drift`](../tools/check-version-drift), re-verify each flagged detail against the
installed CLI, update only [`version-data.yaml`](../meta/version-data.yaml), bump
[`version-record.md`](../meta/version-record.md), and re-run the suite. Because version-specifics are
quarantined, a bump touches a bounded set of files, not the prose.
