# Version record

The CLI version the course content was **last verified against**, and how. Bumped on every
refresh (R12.AC5/AC7). The drift check (`tools/check-version-drift`) compares the installed
`claude --version` to the top row here and prompts a refresh when they differ.

The course is **latest-targeting but verified-anchored** (R12.AC1): it tracks the current CLI
and is not hard-pinned, but every version-specific value in `meta/version-data.yaml` carries its
own `verified_version` + `verified_date` + `provenance`.

| Verified CLI version | Date | Method | By |
|---|---|---|---|
| 2.1.158 | 2026-05-30 | in-REPL `/help` + docs pass (L1 close): 5 of 7 `unverified` keys confirmed — `search-refs`, `context-cmds`, `checkpoint-rewind` (rewind = `/rewind`), `test-run`, `output-styles`; `ci` + `managed-settings` stay `unverified` (no GitHub Actions / enterprise account to verify against); also confirmed `review-cmds` slash names (`/code-review`, `/security-review`) in-REPL | L1 verification |
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

As of the 2026-05-30 L1 pass, 5 of the original 7 are verified and flipped to `unverified: false`
(`search-refs`, `context-cmds`, `checkpoint-rewind`, `test-run`, `output-styles`). Two remain
`unverified: true` in `meta/version-data.yaml`, each blocked by access this environment lacks:

- `ci` — the CLI flags (`-p`, `--output-format`, `--max-budget-usd`) are verified; the **GitHub Action
  wrapper** is not (the maintainer's env uses Gitea, with no GitHub Actions to verify against). Confirm
  the Action name/setup against official docs in an environment with GitHub Actions.
- `managed-settings` — the enterprise/managed-settings **file path + precedence** needs an enterprise
  account or official enterprise docs (not available to the maintainer).
