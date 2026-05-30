# Version record

The CLI version the course content was **last verified against**, and how. Bumped on every
refresh (R12.AC5/AC7). The drift check (`tools/check-version-drift`) compares the installed
`claude --version` to the top row here and prompts a refresh when they differ.

The course is **latest-targeting but verified-anchored** (R12.AC1): it tracks the current CLI
and is not hard-pinned, but every version-specific value in `meta/version-data.yaml` carries its
own `verified_version` + `verified_date` + `provenance`.

| Verified CLI version | Date | Method | By |
|---|---|---|---|
| 2.1.158 | 2026-05-29 | `claude --version` + `claude --help` (P2 version-data seeding); 19/26 keys confirmed from CLI help, 7 marked `unverified` pending in-REPL `/help` / docs | spec build (P2) |

## How to refresh (R12.AC7)

1. Run `tools/check-version-drift` (or just `claude --version`) and compare to the top row above.
2. For each changed area, re-verify the affected `{{vd:key}}` values against the installed CLI
   (`claude --help`, subcommand `--help`, in-REPL `/help`, official docs). **Never** copy a value
   from memory (R12.AC3).
3. Update **only** `meta/version-data.yaml` (then regenerate `meta/version-data.json`) plus any
   genuinely affected location. Because version-specifics are quarantined, prose rarely changes
   (R12.AC8).
4. Add a new row at the top of the table above with the new version, date, and method.
5. Re-run the enforcement suite (`tools/check-version-refs`, `tools/check-version-drift`, …).

## Outstanding to verify on next refresh

> Canonical open-loop is **L1** in `specs/claude-code-mastery/decisions.md` → "Open loops &
> deferrals 🔓". This list is the local detail for that loop.

These keys are currently `unverified: true` in `meta/version-data.yaml` and should be confirmed
when an interactive session or official docs are available:

- `search-refs`, `context-cmds`, `checkpoint-rewind` — in-REPL behaviors (`@`-refs, `/context`/
  `/compact`/`/clear`, checkpoint/rewind) confirmable via `/help`.
- `review-cmds` — `ultrareview` is CLI-verified; confirm the `/code-review` and `/security-review`
  slash-command names in-REPL.
- `test-run` — conceptual (tests run via the Bash tool); consumed by U6 (home unit, area 11), kept
  `unverified` under the L1 hold (project runner is `pytest`, confirmed for `taskflow-api`).
- `ci`, `managed-settings`, `output-styles` — external integration / enterprise / settings detail to
  confirm against official docs before any value is hardcoded.
