# Claude Code Mastery

A self-paced, hands-on course that takes a **seasoned developer who is new to AI-assisted coding**
to a fluent, elite Claude Code practitioner — someone who picks the right workflow and feature for
each real job, and who **verifies** Claude's output rather than trusting it.

The course is **outcome-driven** (organized around real use cases, not a feature tour), **tiered**
for experienced engineers (it won't teach you Git or the terminal), and **version-resilient** (it
targets the latest CLI and is built to be refreshed as the tool changes). It is built **with** Claude
Code — so the repo is itself a worked example of what it teaches.

## Who this is for

**You:** 5+ years building software; fluent with the terminal, Git, and at least one language; a
quick study who resents hand-holding; skeptical of AI output and want to learn to *verify*, not merely
*trust*. (Full persona: `specs/claude-code-mastery/requirements.md` §1.4.)

## What you'll be able to do (capabilities delivered)

Progress here is tracked as **can-do statements** — what you can *do*, never a label on you. The full
set is in [`course/progress-checklist.md`](./course/progress-checklist.md). By the end you can:

- **First Wins** — install and verify Claude Code; make a verified change; explore an unfamiliar
  codebase; operate safely (permissions, secrets, prompt injection, blast radius); steer with project
  memory and deliberate context.
- **Daily Driver** — ship a feature via explore→plan→code→commit; drive change test-first; debug an
  unfamiliar failure to root cause; turn work into a clean, reviewable PR.
- **Force Multiplier** — onboard to and refactor a legacy codebase; run a spec-driven workflow;
  review a change for correctness **and** security.
- **Autonomy & Scale** — package work as custom commands & skills; delegate to subagents; automate
  guardrails with hooks; connect tools/data via MCP (and vet third-party extensions); run Claude
  headlessly / in CI and coordinate parallel agents via git worktrees.

Throughout, one cross-cutting discipline: **verify rigorously** — read the diff, check the approach,
spot-check edges.

## What you need first (assumed)

- A recent **Claude Code CLI**, installed and authenticated (the course verifies this, it doesn't
  provision it). Run [`tools/doctor`](./tools/doctor) to confirm. This is the one assumed paid
  prerequisite; no required lab depends on a second paid service.
- A working terminal, **Git**, and a code editor. macOS/Linux, or **WSL** on Windows.
- **Python** (the sample codebases and tooling are Python). A virtualenv lives at `.venv`.

## How it's structured

| Path | What's there |
|---|---|
| [**`course/units/`**](./course/units/README.md) | **Start here** — the [16-unit index](./course/units/README.md) (table of contents) links each lesson directly. |
| [`course/capstone/`](./course/capstone/) | The single graded capstone: brief menu, worked exemplar, self-applicable rubric. |
| [`course/progress-checklist.md`](./course/progress-checklist.md) | Track which can-do statements you've achieved. |
| [`course/reference/cli-reference.md`](./course/reference/cli-reference.md) | Exhaustive, generated CLI reference (every command, flag, and in-REPL slash command). |
| [`course/stuck.md`](./course/stuck.md) | When you're stuck: hints, FAQ, using Claude to get unstuck. |
| [`codebases/`](./codebases/) | `primary/` (`taskflow-api`) and `legacy/` (`taskflow-cli`) lab substrates. |
| [`meta/`](./meta/) | The course's machine-readable backbone (capability map, catalog, coverage, version data). |
| `specs/claude-code-mastery/` | The course's own spec — and the worked example for the spec-driven unit. |

## How to start

1. Run [`tools/doctor`](./tools/doctor) and fix anything it flags (or use its manual checklist).
2. Open the [**unit index**](./course/units/README.md) and begin with **Unit 1 — Set up Claude Code
   and make your first verified change**, following the default numeric path; you may deviate per
   each unit's declared prerequisites.
3. Each unit has a **fast path** and a **skip-check** — skim and skip deliberately if you already
   know the material. Do the labs; they're where the learning is.
4. Track yourself against the progress checklist; finish with the capstone.

## A note on how this was made

Parts of this course were authored with Claude Code, using the spec-driven workflow it teaches (see
`specs/claude-code-mastery/`). That's intentional dogfooding — the full story, with an honest
AI-authorship transparency note, is the [build case study](./course/capstone/case-study.md), which
also serves as the worked exemplar for your capstone.

**Maintaining or extending the course?** See
[`course/maintainer-guide.md`](./course/maintainer-guide.md) — how to add or update a unit without
breaking the catalog, coverage matrix, or capability map, and how to refresh when the CLI changes.
