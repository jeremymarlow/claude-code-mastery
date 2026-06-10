# Version record

The CLI version the course content was **last verified against**, and how. Bumped on every
refresh (R12.AC5/AC7). The drift check (`tools/check-version-drift`) compares the installed
`claude --version` to the top row here and prompts a refresh when they differ.

The course is **latest-targeting but verified-anchored** (R12.AC1): it tracks the current CLI
and is not hard-pinned, but every version-specific value in `meta/version-data.yaml` carries its
own `verified_version` + `verified_date` + `provenance`.

| Verified CLI version | Date | Method | By |
|---|---|---|---|
| 2.1.170 | 2026-06-09 | **version refresh** 2.1.159→2.1.170 (11 releases): top-level command list unchanged (`check-version-drift`); deep surface changed in four places — new `--safe-mode`, `claude agents --all`, `--fallback-model` list form, `--model` aliases incl. `fable` (Claude Fable 5). `cli-reference.{json,md}` regenerated from the installed CLI; cumulative digest added to `version-changelog.md` (official CHANGELOG; **2.1.164/165 absent upstream — marked, not fabricated**). Every `{{vd:key}}` value re-checked against the reference diff — none contradicted; per-key `verified_version`/dates left at their genuine individual verification. `_verified_version` bumped → unit callouts re-rendered via `make render`. `managed-settings` remains `unverified` (L1) | version refresh |
| 2.1.159 | 2026-06-03 | **L1 `ci` close**: the Claude-Code-in-CI **GitHub Action wrapper** verified — official docs (`code.claude.com/docs/en/github-actions`) + a **live run in this repo** (`anthropics/claude-code-action@v1` `@claude` responder, GitHub Actions run `26868750876`). `ci` flipped `unverified: false`; dogfooded as `.github/workflows/claude.yml` (U16). Also regenerated `version-data.json`, fixing pre-existing twin drift (stale `custom-commands`). Only `managed-settings` now remains `unverified` | L1 verification |
| 2.1.159 | 2026-05-31 | version refresh (L9 close): installed CLI advanced 2.1.158→2.1.159 — **internal infrastructure, no user-facing change** per the official CHANGELOG (see `version-changelog.md`). `cli-reference.json` re-introspected byte-stable + command list unchanged (`render-cli-reference --check`, `check-version-drift`), so every `{{vd:key}}` value stands; `_verified_version` bumped. Per-key `verified_version`/dates left at their genuine individual-verification — 2.1.159 added nothing to re-confirm. `ci` + `managed-settings` **remain `unverified`** (still no GitHub Actions / enterprise access) | version refresh |
| 2.1.158 | 2026-05-30 | in-REPL `/help` + docs pass (L1 close): 5 of 7 `unverified` keys confirmed — `search-refs`, `context-cmds`, `checkpoint-rewind` (rewind = `/rewind`), `test-run`, `output-styles`; `ci` + `managed-settings` stay `unverified` (no GitHub Actions / enterprise account to verify against); also confirmed `review-cmds` slash names (`/code-review`, `/security-review`) in-REPL | L1 verification |
| 2.1.158 | 2026-05-29 | `claude --version` + `claude --help` (P2 version-data seeding); 19/26 keys confirmed from CLI help, 7 marked `unverified` pending in-REPL `/help` / docs | spec build (P2) |

## How to refresh (R12.AC7)

1. Run `tools/check-version-drift` (or just `claude --version`) and compare to the top row above.
2. For each changed area, re-verify the affected `{{vd:key}}` values against the installed CLI
   (`claude --help`, subcommand `--help`, in-REPL `/help`, official docs). **Never** copy a value
   from memory (R12.AC3).
3. Update **only** `meta/version-data.yaml` (then run `tools/render-vd-json`, or `make render`, to
   regenerate the `meta/version-data.json` twin — `make check` gates that they match, L14) plus any
   genuinely affected location. Because version-specifics are quarantined, prose rarely changes
   (R12.AC8).
4. **Regenerate the CLI reference (R16.AC5):** `tools/render-cli-reference --all` — re-introspects the
   installed CLI into `meta/cli-reference.json` and re-renders `course/reference/cli-reference.md`.
   Newly-added commands/flags are auto-flagged `added_in` against the prior committed reference.
5. **Record the change synopsis (R17):** add one cumulative entry at the top of
   `meta/version-changelog.md` covering every version strictly after the last recorded through the new
   one — with the official changelog/release-notes URL + retrieval date, flagging content-affecting
   changes (new/removed/renamed commands or flags, changed defaults, deprecations). This is also
   surfaced learner-facing as the page's "What's new" section.
6. Add a new row at the top of the table above with the new version, date, and method.
7. Re-run the enforcement suite (`tools/check-version-refs`, `tools/check-version-drift`,
   `tools/render-cli-reference --check`, `tools/check-version-changelog`, …).

## Outstanding to verify on next refresh

> Canonical open-loop is **L1** in `specs/claude-code-mastery/decisions.md` → "Open loops &
> deferrals 🔓". This list is the local detail for that loop.

As of the 2026-05-30 L1 pass, 5 of the original 7 were verified; **`ci` was then verified live on
2026-06-03** (top row — real `anthropics/claude-code-action@v1` run in this repo). That leaves **one**
key `unverified: true` in `meta/version-data.yaml`, blocked by access this environment lacks:

- `managed-settings` — the enterprise/managed-settings **file path + precedence** needs an enterprise
  account or official enterprise docs (not available to the maintainer).
