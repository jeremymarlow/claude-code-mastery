# CLI version-change digest (R17)

A running, maintainer-facing synopsis of what changed in the Claude Code CLI across refreshes —
the *narrative* companion to the bare verified-version table in [`version-record.md`](./version-record.md)
and the *exhaustive* current-surface reference in [`cli-reference.json`](./cli-reference.json).

**Provenance discipline (R12.AC3), like every `meta/` artifact:** no change is summarized from model
memory. Each entry cites the **official changelog/release-notes URL + retrieval date**; an unreachable
source is **marked, not fabricated** (R17.AC3).

**On each refresh (R12.AC7):** add one **cumulative** entry at the top spanning every version strictly
after the last recorded verified version through the new one (R17.AC2). Flag content-affecting changes —
new/removed/renamed commands or flags, changed defaults, deprecations — with a `_Course impact:_` line
cross-referencing the affected `{{vd:key}}` values and the regenerated reference (R17.AC4). The newest
entry is surfaced learner-facing as the **"What's new"** section atop `course/reference/cli-reference.md`
(decision P8-r17-surface). Enforced by `tools/check-version-changelog` (R17.AC5): the **recorded**
verified version in `version-record.md` must have a matching entry below.

Entry shape (newest first):

```markdown
## 2.1.158 → 2.3.10  (retrieved 2026-09-01 from <changelog URL>)
- **2.2.0** — <synopsis>. _Course impact:_ none.
- **2.3.0** — new `claude foo` command; `--bar` default changed. _Course impact:_ {{vd:permission-modes}}, cli-reference regen.
```

---

## 2.1.159 → 2.1.170  (retrieved 2026-06-09 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

The course is now verified against **2.1.170** (refresh 2026-06-09). Eleven releases since the last
anchor. The **top-level command list is unchanged** (`check-version-drift`); the deep surface moved in
four places, all picked up by the regenerated reference: a new **`--safe-mode`** flag, **`claude
agents --all`**, **`--fallback-model`** now accepting a comma-separated list, and the **`--model`**
aliases now including `fable` (Claude Fable 5). Every version-data (`vd`) value was re-checked against the
reference diff — **none is contradicted**; per-key `verified_version`/dates stand.

- **2.1.170** — Introduced **Claude Fable 5**; `--model` aliases now `fable`/`opus`/`sonnet` and
  `--fallback-model` accepts a comma-separated list (retries the primary each turn); fixed transcript
  saving from IDE-spawned terminals. _Course impact:_ help-text/flag changes carried by the
  regenerated `cli-reference.{json,md}`; no version-data value affected (model selection isn't a
  quarantined course fact).
- **2.1.169** — New **`--safe-mode`** flag (start with all customizations — CLAUDE.md, skills,
  plugins, hooks, MCP, custom commands/agents — disabled, for troubleshooting; sets
  `CLAUDE_CODE_SAFE_MODE=1`); `post-session` lifecycle hook for self-hosted runners; `/cd` command;
  `disableBundledSkills` setting. _Course impact:_ new top-level flag → reference regenerated
  (auto-flagged `added_in`); a useful complement to U4's recovery ladder but additive — no
  `version-data` value changed.
- **2.1.168 / 2.1.167** — Bug fixes and reliability improvements. _Course impact:_ none.
- **2.1.166** — `fallbackModel` setting (up to three fallbacks); glob patterns in deny-rule tool
  names; `MAX_THINKING_TOKENS=0` disables thinking; assorted fixes. _Course impact:_ none to
  version-data values (deny-rule globs are additive to the settings surface; {{vd:settings:inline}} names the
  loading mechanism, not rule syntax).
- **2.1.165 / 2.1.164** — **Absent from the official changelog** at retrieval time — marked, not
  fabricated (R17.AC3).
- **2.1.163** — `requiredMinimumVersion`/`requiredMaximumVersion` managed settings; `/plugin list`;
  Stop/SubagentStop hooks can return `additionalContext`; skills gain a `\$` escape for a literal `$`
  before a digit; fixed `claude -p` hanging after its final result. _Course impact:_ all additive —
  {{vd:hooks:inline}} (common-events teaching unchanged), {{vd:plugins:inline}}, {{vd:custom-commands:inline}} (0-based
  positional args unchanged; escape syntax is new detail deferred to docs), {{vd:managed-settings}}
  (still `unverified`, L1) — no value contradicted.
- **2.1.162** — `claude agents --json` gains `waitingFor`; `--tools` with explicit Grep/Glob provides
  the dedicated search tools; large agents-view/permissions fix wave; quieter startup. _Course
  impact:_ {{vd:subagents:inline}} re-checked — the `agents` subcommand description stands (the `--all` flag
  later joins it); none otherwise.
- **2.1.161** — agents-view polish; parallel Bash failure no longer cancels sibling calls; fixed
  `claude mcp` list/get/add printing secrets to the terminal; OTEL fixes. _Course impact:_ none ({{vd:mcp:inline}}
  surface unchanged; the secrets-printing fix aligns with U3/U15 hygiene teaching).
- **2.1.160** — Prompts before writing shell-startup files and `~/.config/git/`; `acceptEdits` now
  prompts before writing build-tool config files that grant code execution; Edit no longer requires a
  separate Read after `grep`; dynamic-workflow keyword renamed `workflow`→`ultracode`; a large
  Windows/terminal/agents fix wave. _Course impact:_ {{vd:permission-modes}} re-checked — mode
  *names* unchanged (the `acceptEdits` tightening is consistent with, and slightly strengthens, U3's
  posture framing); none otherwise.

## 2.1.158 → 2.1.159  (retrieved 2026-05-31 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

The course is now verified against **2.1.159** (refresh 2026-05-31, closing the L9 drift-ahead — the
reference was generated at 2.1.159 during P8 while the recorded anchor was held at 2.1.158 to keep the
upgrade trigger armed until the feature shipped).

- **2.1.159** — Internal infrastructure improvements (no user-facing changes). _Course impact:_ none — the command/flag surface is unchanged (`check-version-drift`: command list unchanged; `render-cli-reference --check` byte-stable), so `cli-reference.json` and every version-data value stand.

## 2.1.158  (baseline — first tracked version; retrieved 2026-05-31 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

The first CLI version this course was verified against; there is no prior tracked version to diff
against, so this is a baseline, not a synopsis of changes.

- For reference, **2.1.158** itself: "Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8. Opt in by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`." _Course impact:_ none (auto mode is covered at awareness tier; no version-data value changed).
