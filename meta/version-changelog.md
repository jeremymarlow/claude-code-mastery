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

## 2.1.158 → 2.1.159  (drift-ahead of the recorded 2.1.158; retrieved 2026-05-31 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

The installed CLI moved to **2.1.159** while the course stays verified against **2.1.158** (decision
P8-no-bump — no user-facing change warranted a bump). Recorded here ahead of a formal refresh:

- **2.1.159** — Internal infrastructure improvements (no user-facing changes). _Course impact:_ none — the command/flag surface is unchanged (`check-version-drift`: command list unchanged), so `cli-reference.json` and every version-data value stand.

## 2.1.158  (baseline — first tracked version; retrieved 2026-05-31 from https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)

The first CLI version this course was verified against; there is no prior tracked version to diff
against, so this is a baseline, not a synopsis of changes.

- For reference, **2.1.158** itself: "Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8. Opt in by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`." _Course impact:_ none (auto mode is covered at awareness tier; no `{{vd:key}}` value changed).
