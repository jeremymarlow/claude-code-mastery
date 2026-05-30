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
| `.claude/` | Dogfooding: commands, skills, hooks, `settings.json`. |
| `.github/workflows/` | CI backstop running the check suite. |

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

## Version-specific values

Never type a version-specific value (command, flag, path, settings key, feature
availability) directly into prose. Put it in `meta/version-data.yaml` under a kebab-case
key and reference it as `{{vd:key}}`. The `check-version-refs` tool fails the build on any
`{{vd:key}}` with no matching key. **[R12.AC2, R13.AC4]**

## Machine-readable artifacts

YAML is authoritative for human-edited artifacts; a generated `.json` twin is produced for
tooling where noted (`capability-map`, `version-data`). Never hand-edit a generated `.json`;
regenerate it from its `.yaml`. **[R13.AC2]**

## Accessibility & portability

- Author core meaning in **CommonMark**; GitHub callouts / Mermaid only as graceful-degrading
  enhancement. **[R15.AC1/AC2]**
- No meaning conveyed by **color or emoji alone**; diagrams/images carry text equivalents;
  headings/lists used semantically. **[R15.AC6]**
- Labs are **portable-by-default** (macOS/Linux; **WSL** is the v1 Windows story). Isolate any
  platform-specific step into a clearly-marked section. **[R15.AC3/AC4]**
