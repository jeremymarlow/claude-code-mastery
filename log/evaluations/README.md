# Collaboration-retrospective evaluation corpus

This directory is the **internal evaluation corpus** for the R18 collaboration retrospective — a
candid, multi-perspective assessment of how this course was actually built, as a collaboration between
a **human author** and **Claude**. It is one of two R18 deliverables; the other is the learner-facing
case study `course/case-studies/collaboration-retrospective.md` (built later, in P9 9.7 — referenced as
plain text here until it exists), which is the teaching render of this corpus's bottom line.

**Authoritative design:** `specs/claude-code-mastery/design.md` §13. **Build plan:** `tasks/P9`.
**Layout/naming convention:** `meta/conventions.md` → "Collaboration-retrospective evaluations."

## The matrix

The corpus is a **session × reviewer matrix**, summarized along both margins and then to a bottom line.
Every artifact is derived from — and traceable to — the ones beneath it:

```
LEAF (cell)            <session>/<reviewer>.md     one reviewer × one session   — cached, immutable
MARGIN · per-session   <session>/_synthesis.md     all reviewers × one session
MARGIN · per-reviewer  _global/<reviewer>.md       one reviewer × all sessions  (built from its own leaves)
CORNER                 _global/_overall.md          blends the per-reviewer globals → bottom line
                         └─►  course/case-studies/collaboration-retrospective.md  (learner render)
```

- `<session>` = the transcript filename **stem** (e.g. `2026-05-30_0816-p4-sample-codebases`).
- `<reviewer>` = an agent `name` from `.claude/agents/` (e.g. `process-architect`, `control`).
- **Cached = immutable:** a leaf is written once and committed as evidence; re-running a reviewer is a
  new, dated file — never an overwrite.

## The panel

Eleven reviewers (`.claude/agents/`): **ten subjective persona reviewers** that each judge **both
parties** across **both axes** through a distinct lens, plus **one no-persona `control`** (the
deliberate baseline — same output contract, but no persona lens and no candor mandate — used to measure
what the persona scaffolding adds). Balanced 5 process / 3 communication / 2 cross-cutting:

- **process:** `process-architect`, `context-engineer`, `verification-hawk`, `tooling-economist`, `safety-steward`
- **communication:** `intent-alignment`, `dialogue-clarity`, `collaboration-partner`
- **cross-cutting:** `outcome-auditor`, `devils-advocate`
- **control:** `control`

## Grade vocabulary

Each evaluation carries a scannable grade block — **a summary of the prose, never a replacement for
it.** Three levels, per party (`human`, `claude`) × axis (`process`, `communication`), plus one
`overall`:

- **`did-well`** — a genuine strength worth repeating.
- **`did-okay`** — adequate; neither notable nor a problem.
- **`could-improve`** — a real weakness worth naming.

## Leaf front-matter schema

Every leaf (`<session>/<reviewer>.md`) is YAML front matter over a verbose prose body:

```
---
session: <slug>
reviewer: <reviewer-id>
model_evaluated: <model that produced Claude's side that session>
grades:                        # did-well | did-okay | could-improve
  human:   { process: <grade>, communication: <grade> }
  claude:  { process: <grade>, communication: <grade> }
  overall: <grade>
---
## Insights (ordered by significance)
1. **<headline>** — <verbose reasoning>. _Evidence:_ <session locator or short quote>. [human|claude] [process|comms]
2. ...

## What worked / what didn't (both parties)
## Bottom line
```

## The candor mandate (persona reviewers)

The ten persona reviewers are bound to be **subjective and candid** — render a real opinion through the
lens; do not flatter, soften to please, or discourage; accuracy and thoroughness over diplomacy. Every
insight is **evidence-grounded**: it cites the transcript (session + locator), never asserts from
memory. Reviews cover **both parties** and **both strengths and weaknesses**. The `control` deliberately
omits this mandate (and the lens) so the panel can measure its effect.

## Model attribution (verified, R18.AC7)

Read from each transcript's raw `.jsonl` `.message.model` field — **never assumed.** Each reviewer is
told which model produced Claude's side of the session it evaluates, so no finding misattributes
behavior to a model that did not produce it.

> **Note (verified 2026-05-31):** an earlier belief that the foundational requirements/design session
> ran on `claude-sonnet-4-6` was an *assumption, and it was wrong*. The record shows **all 23 sessions
> ran on `claude-opus-4-8`** — the foundational session is the lone **mixed** case (its first 2
> assistant turns were `claude-sonnet-4-6`, then it switched to opus for the remaining 222). This
> correction is itself the verify-don't-trust thesis catching the project's own record.

| Session | Model (Claude's side) |
|---|---|
| `2026-05-29_1845-requirements-and-design-spec-creation` | `claude-opus-4-8` (mixed: `claude-sonnet-4-6` for turns 1–2, then opus) |
| `2026-05-29_2146-catalog-approval-and-scaffolding` | `claude-opus-4-8` |
| `2026-05-30_0725-design-approval-and-tasks-kickoff` | `claude-opus-4-8` |
| `2026-05-30_0816-p4-sample-codebases` | `claude-opus-4-8` |
| `2026-05-30_0848-u1-onboarding-labs-and-git-remote` | `claude-opus-4-8` |
| `2026-05-30_0942-u3-operate-safely-authoring` | `claude-opus-4-8` |
| `2026-05-30_1249-unit-authoring-and-lab-ref-pushes` | `claude-opus-4-8` |
| `2026-05-30_1316-open-loops-audit-and-u6` | `claude-opus-4-8` |
| `2026-05-30_1415-unit-authoring-through-u10` | `claude-opus-4-8` |
| `2026-05-30_1557-u12-commands-and-skills-dogfooding` | `claude-opus-4-8` |
| `2026-05-30_1703-u13-subagents-authoring` | `claude-opus-4-8` |
| `2026-05-30_1930-p6-capstone-finalization` | `claude-opus-4-8` |
| `2026-05-30_2224-l1-version-key-verification` | `claude-opus-4-8` |
| `2026-05-30_2322-quality-pass-8-lens-review-and-p7-start` | `claude-opus-4-8` |
| `2026-05-31_0832-p7-rollout-closeout-and-session-transcript-tooling` | `claude-opus-4-8` |
| `2026-05-31_1235-p8-cli-reference-spec` | `claude-opus-4-8` |
| `2026-05-31_1353-p8-cli-reference-build-through-8.5` | `claude-opus-4-8` |
| `2026-05-31_1538-p8-cli-reference-build-86-through-89` | `claude-opus-4-8` |
| `2026-05-31_1629-venv-standardization-and-doctor-bootstrap` | `claude-opus-4-8` |
| `2026-05-31_1730-memory-uniformity-and-auto-memory-disable` | `claude-opus-4-8` |
| `2026-05-31_1813-version-refresh-l9-and-r8-strict-gate` | `claude-opus-4-8` |
| `2026-05-31_1846-close-l10-drift-fold-and-t2` | `claude-opus-4-8` |
| `2026-05-31_1908-r18-retrospective-requirements-design-tasks` | `claude-opus-4-8` |

Corpus **frozen at these 23 sessions** (those present at P9 start). P9's own build sessions, captured
later, are deliberately out of the evaluated set. Regenerate this map from the raw transcripts with:

```
for f in log/transcripts/raw/*.jsonl; do
  echo "$(basename "$f" .jsonl): $(jq -rc 'select(.message.model)|.message.model' "$f" | grep -v '<synthetic>' | sort -u | paste -sd+ -)"
done
```

## Run protocol

- **One session at a time.** The maintainer drives `/evaluate-session <slug>`, which dispatches all 11
  reviewers (in parallel) over that session and writes the 11 leaf files, then writes `_synthesis.md`.
  The corpus accretes per session and stays reviewable.
- **Rendered-primary, raw-on-demand.** Reviewers read `log/transcripts/rendered/<slug>.md` as the
  primary source and dip into the raw `.jsonl` only for a specific turn the render collapses.
- **Globals last.** Once all sessions' leaves exist, `/evaluate-global` builds each `_global/<reviewer>.md`
  (each reviewer over its own leaves), then the `_global/_overall.md` corner.
- **Secret scan before every commit.** Run `tools/scan-secrets log/evaluations/<session>/**` and
  human-review any flag before committing (R18.AC10).
- **Completeness gate.** `tools/check-evaluations` reports progress (`PEND`) in `make check` and
  hard-fails in `make check-strict` until the matrix is whole — discovery-based, no hardcoded lists.
