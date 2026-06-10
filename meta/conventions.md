# Conventions

Naming, structure, and authoring conventions for the Claude Code Mastery course.
This file is the single source of truth for "how things are named"; tools and units
reference it rather than restating the rules. **[R13.AC1]**

## Directory layout

See `design.md` §9 for the canonical tree. Top level:

| Path | Holds |
|---|---|
| `specs/claude-code-mastery/` | The spec (requirements, design, tasks, decisions, this project's `IMPLEMENTATION.md`). |
| `course/units/NN-slug/unit.md` | One curriculum unit per directory. |
| `course/capstone/` | Capstone briefs, exemplar (build case study), rubric. |
| `course/` (files) | `progress-checklist.md`, `stuck.md`, `maintainer-guide.md`. |
| `codebases/primary/` | `taskflow-api` lab substrate. |
| `codebases/legacy/` | `taskflow-cli` lab substrate. |
| `codebases/SEEDED.md` | Maintainer-facing seeded-defect inventory. |
| `codebases/fixtures/` | Offline mocks/fixtures so labs needing an "external" service run standalone (R7.AC7). |
| `meta/` | Single-source machine-readable artifacts (this file lives here). |
| `meta/templates/` | Unit templates (`unit-core.md`, `unit-awareness.md`). |
| `tools/` | `doctor`, checks, drift detection, `verify-lab`/`reset-lab`. |
| `.claude/` | Dogfooding: commands, skills, hooks, `settings.json`, `agents/` (the R18 reviewer panel). |
| `.github/workflows/` | CI backstop running the check suite. |
| `log/transcripts/{raw,rendered}/` | Captured build-session transcripts: raw `.jsonl` + rendered `.md`. |
| `log/evaluations/` | R18 collaboration-retrospective corpus — the session × reviewer evaluation matrix. |

## Naming rules

| Thing | Convention | Example |
|---|---|---|
| Unit directory | `course/units/NN-slug/` — zero-padded two-digit `NN` (01–16), kebab-case slug | `course/units/05-ship-a-feature/` |
| Unit file | always `unit.md` inside its directory | `course/units/03-operate-safely/unit.md` |
| Unit ID (in front matter / refs) | `U` + integer, matching catalog | `U5` |
| Capability ID | `C` + integer, or `CV` (cross-cutting verification) | `C6`, `CV` |
| Use-case ID | `U` + integer (1:1 with its unit) | `U5` |
| Workflow ID | `W` + integer | `W1` |
| Coverage-matrix area ID | integer | `9` |
| Stage slug (front matter) | `first-wins`, `daily-driver`, `force-multiplier`, `autonomy-scale` | `daily-driver` |
| Depth tier | `core` or `awareness` | `core` |
| `meta/` files | kebab-case | `coverage-matrix.yaml` |
| Tools | kebab-case, no extension on entry points where practical | `check-coverage`, `verify-lab` |
| Lab starting state | git **tag** `start/uNN-labM` | `start/u05-lab1` |
| Lab reference solution | git **branch** `solution/uNN-labM` | `solution/u05-lab1` |
| Version-data key | kebab-case, referenced in prose as `{{vd:key}}` | `{{vd:permission-modes}}` |
| Reviewer (subagent) ID | kebab-case agent `name`, file `.claude/agents/<id>.md` | `process-architect`, `control` |
| Evaluation session ID | the transcript filename **stem** (no extension) | `2026-05-30_0816-p4-sample-codebases` |
| Leaf evaluation | `log/evaluations/<session>/<reviewer>.md` | `…/2026-05-30_0816-p4-sample-codebases/safety-steward.md` |

## Lab substrate

How labs attach to the two codebases (`design.md` §7; full rationale in `decisions.md`). The naming
rows for `start/uNN-labM` (tag) and `solution/uNN-labM` (branch) are above; this is how they're used.

- **Starting state = a tag, solution = a branch.** A lab begins at the clean, tagged commit
  `start/uNN-labM`; the worked answer lives on the branch `solution/uNN-labM`, kept separate so the
  learner attempts it unaided first. **[R7.AC4]**
- **`main` stays green.** Per-lab defects on `primary/taskflow-api` are introduced **only** on the
  lab's `start/...` tag, never on `main` — `main`'s pytest suite passes. **[R7.AC1/AC2]**
- **Legacy is the exception.** `legacy/taskflow-cli` carries real bugs on `main` by design (it is the
  debug/refactor substrate). Every such bug is registered in `codebases/SEEDED.md`.
- **Every planted defect is inventoried** in `codebases/SEEDED.md` (maintainer-facing answer key;
  never linked from a learner-facing page).
- **Verification & reset:** `tools/verify-lab <id>` runs the lab's objective self-check
  (`course/labs/<id>/verify.sh`, when automatable); `tools/reset-lab <id>` restores the working tree
  under `codebases/` to `start/<id>`. **[R7.AC5/AC6]**
- **Offline by default:** a lab that would otherwise need an external service or credential ships a
  local mock under `codebases/fixtures/` (or its own lab dir) and points at it — no network, no real
  secrets, ever. **[R7.AC7]**
- **BYO variants** (a lab run against the learner's own repo) are marked **non-verifiable** and are
  never the required path. **[R7.AC8]**

## Collaboration-retrospective evaluations (`log/evaluations/`)

The R18 corpus is a **session × reviewer matrix** (`design.md` §13; build plan `tasks/P9`). Layout —
discoverable, no hardcoded lists (the gate `tools/check-evaluations` derives the expected set from
`log/transcripts/rendered/*.md` × `.claude/agents/*.md`):

| Path | Tier | Holds |
|---|---|---|
| `log/evaluations/<session>/<reviewer>.md` | **leaf** (cell) | one reviewer's evaluation of one session — cached, immutable once written |
| `log/evaluations/<session>/_synthesis.md` | **per-session** (reviewer-axis margin) | all reviewers consolidated for that one session |
| `log/evaluations/_global/<reviewer>.md` | **per-reviewer global** (session-axis margin) | one reviewer across all its leaves |
| `log/evaluations/_global/_overall.md` | **corner** | the per-reviewer globals blended → bottom line |
| `log/evaluations/README.md` | — | corpus orientation, grade vocabulary, leaf schema, verified model-attribution map, run protocol |

- `<session>` = the transcript filename **stem**; `<reviewer>` = an agent `name` from `.claude/agents/`.
- **Grade vocabulary:** `did-well` / `did-okay` / `could-improve`, per party (`human`, `claude`) × axis
  (`process`, `communication`) plus one `overall` — a scannable summary that never replaces the prose.
- **Leaf front matter** is single-sourced as `meta/evaluation-leaf.schema.json` (the grade enum lives
  there). Two tools validate every leaf the *same* way against it: `tools/lint-evaluations <session>`
  (the interactive step-4 check in `/evaluate-session`; also prints each leaf's `overall`) and
  `tools/check-evaluations` (the corpus gate, which now hard-fails a malformed *present* leaf in both
  `make check` and `--strict`, separate from the completeness `PEND`). Validation is **structural**;
  whether the prose is insightful, evidence-cited, and even-handed stays the human reviewer's eyeball.
- **Cached = immutable:** a leaf is written once and committed as evidence; re-running a reviewer is a
  new dated file, not an overwrite.
- **Provenance & safety:** every insight cites the transcript (session + locator); model attribution is
  read from the raw `.jsonl` `.message.model` field, never assumed (R18.AC7); run `tools/scan-secrets`
  over new files before committing (R18.AC10).

## Version-specific values

Never type a version-specific value (command, flag, path, settings key, feature
availability) directly into prose. Put it in `meta/version-data.yaml` under a kebab-case
key and reference it as `{{vd:key}}`. The `check-version-refs` tool fails the build on any
`{{vd:key}}` with no matching key. **[R12.AC2, R13.AC4]**

## Machine-readable artifacts

YAML is authoritative for human-edited artifacts; a generated `.json` twin is produced for
tooling where noted (`capability-map`, `version-data`). Never hand-edit a generated `.json`;
regenerate it from its `.yaml`. **[R13.AC2]**

## Demonstration artifacts (unit content)

Every **core-tier** unit demonstrates its skill with at least one concrete artifact (design §15.1),
in one of two forms, each opened by a bold label at the start of a line — the exact strings
`tools/check-content` greps for:

- `**Captured** — <what it is>, <the exact command/source that produced it> (<date if relevant>):`
  followed by a fenced block of **real** output. Captures are regenerable: prefer artifacts a
  maintainer can re-produce on a refresh (diffs from `solution/*` refs, pytest/CLI output, excerpts
  of committed files). Provenance is part of the label. **[R20.AC1/AC4, R12.AC4]**
- `**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.`
  followed by a blockquote dialogue (`**You:**` / `**Claude:**` turns) or a marked example. Used for
  conversational exchanges, which are non-deterministic. No version-specific surface may be asserted
  inside one from memory — version facts stay `{{vd:key}}` tokens. **[R20.AC4, R12.AC3]**

Presence is enforced by `tools/check-content` (`PEND` while authoring, hard fail in
`make check-strict`); the same tool hard-fails on AI tool-call residue in any learner-facing
markdown. **[R20.AC5, R13.AC4]**

## Stage checkpoints & transfer blocks

The **last unit of each stage** (U4, U8, U11, U16) closes with a `## Stage checkpoint — <Stage>`
section: 4–6 retrieval prompts answered from memory, each naming the unit that carries the answer,
explicitly ungraded (capstone-only assessment stands). **[R21.AC4]** The Daily Driver workflow units
(U5–U8) each carry an **"On your own repo"** transfer block after the lab's verify step, marked
bring-your-own and non-verifiable. **[R21.AC5, R7.AC8]**

## Breadcrumb navigation

Every learner-facing document under `course/` carries a breadcrumb trail as its **first content
line** (after any generated-file comment and/or front matter), followed by a blank line, above the
H1 — see `design.md` §14. **[R19]**

- **Format:** linked ancestor segments joined by ` › `, ending with the document's own H1 as
  **plain text** (the current location is identified, not linked) — ancestor links are relative
  to the document itself. Live example: the first line of `course/capstone/briefs.md`
  (home › Capstone › Capstone briefs). Plain CommonMark; the trail reads correctly as text with
  no meaning by formatting alone. **[R19.AC2/AC4, R15]**
- **Hierarchy is derived from the filesystem, never declared:** a document's ancestor chain is
  every `README.md` found walking up its directory tree; the repo-root `README.md` is the course
  home and the terminus. Segment labels are each ancestor's H1. Place a new doc correctly and its
  trail follows; nothing to register. **[R19.AC3]**
- **Generated docs get their trail from their generator** (`render-units`, `render-index`,
  `render-cli-reference`, `render-checklist`), all via the single `breadcrumb()` helper in
  `tools/_common.py`; hand-authored docs follow this convention directly. **[R19.AC5]**
- **Enforcement:** `tools/check-breadcrumbs` (in `make check` and `check-strict`, hard fail)
  recomputes every expected trail from disk and fails on missing/stale/mismatched ones;
  `check-links` separately verifies the ancestor links resolve. **[R19.AC5, R13.AC4]**
- **Deliberately trail-less:** `course/maintainer-guide.md` (maintainer-facing),
  `course/units/*/unit.src.md` (source files — the trail is emitted into the generated `unit.md`),
  `course/labs/u03-lab1/untrusted-bug-report.md` (fenced untrusted-input fixture), and the course
  home `README.md` (the trail terminus carries no self-trail). **[R19.AC1]**

## Accessibility & portability

- Author core meaning in **CommonMark**; GitHub callouts / Mermaid only as graceful-degrading
  enhancement. **[R15.AC1/AC2]**
- No meaning conveyed by **color or emoji alone**; diagrams/images carry text equivalents;
  headings/lists used semantically. **[R15.AC6]**
- Labs are **portable-by-default** (macOS/Linux; **WSL** is the v1 Windows story). Isolate any
  platform-specific step into a clearly-marked section. **[R15.AC3/AC4]**
