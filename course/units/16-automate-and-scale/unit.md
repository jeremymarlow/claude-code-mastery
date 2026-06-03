<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U16
title: "Run Claude unattended — headless, in CI, and in parallel"
stage: autonomy-scale
depth_tier: core
use_case: "Run Claude unattended and in parallel"
can_do: [C17]
workflows: [W9]
coverage_areas: [6, 23, 24, 25]
prerequisites: [U8, U14]
reading_time_min: 9
lab_time_min: 25
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md)

# Run Claude unattended — headless, in CI, and in parallel

## Learning objectives

By the end of this unit you can:

- **Run Claude headlessly** with `-p`/`--print` and a structured `--output-format`, so it executes a
  task non-interactively — scriptable, pipeable, and runnable in automation.
- **Run Claude in CI** — wire a headless invocation (or your enforcement suite) into a pipeline that
  runs on every push, the way this repo's own checks do.
- **Coordinate parallel agents with git worktrees** — give each independent task its own worktree
  so agents don't collide, run them concurrently, and review each diff separately before integrating.
 
- **Keep unattended runs safe** — apply the guardrails that matter when *no one is at the keyboard to
  approve*: deterministic hooks ([Hooks](../14-hooks/unit.md)), bounded blast radius and checkpoints
  ([Operate safely](../03-operate-safely/unit.md)), and per-diff review.

## Fast path (TL;DR)

> Three moves to run Claude without babysitting it. **Headless:** `claude -p "<task>"
> --output-format json` runs non-interactively and prints structured output you can pipe or parse;
> cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
> every push; this repo's [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) is
> the worked example. **Parallel:** give each independent task its own **git
> worktree** (`claude --worktree`, or `git worktree add`), run agents concurrently, and **review each
> diff separately** before merging. The catch: unattended means **no interactive
> approval**, so the safety net is the hooks of [Hooks](../14-hooks/unit.md), the blast-radius discipline
> of [Operate safely](../03-operate-safely/unit.md), and reviewing every diff.

## Skip-check

**Skip this unit if you can already:** run Claude headlessly (`-p` with a structured `--output-format`,
bounded by `--max-budget-usd`) and consume its output in a script; wire a headless run or a check suite
into CI so it runs on every push; use git worktrees to run two or more agents on independent tasks in
parallel and review each diff before integrating; and explain what keeps an unattended run safe when no
one is there to approve each step.

## Concept

The Autonomy stage has built up to this: you packaged routines ([Commands & skills](../12-commands-and-skills/unit.md)),
delegated to subagents ([Subagents](../13-subagents/unit.md)), enforced standards with hooks
([Hooks](../14-hooks/unit.md)), and connected external tools ([MCP & vetting](../15-mcp-and-vetting/unit.md)). This
unit takes the human out of the loop entirely: **Claude running unattended — headless, in CI, and
several agents at once.**

**1 — Headless.** `claude -p "<task>"` (a.k.a. `--print`) runs **non-interactively**: it does the task
and exits, printing the result instead of dropping you into a REPL. Add `--output-format json` (or
`stream-json`) to get **structured** output a script can parse, and `--max-budget-usd` to cap spend on
an unattended run. This is the primitive everything else here is built from — Claude as a *command*,
not a *session*. `-p`/`--print` runs headlessly; `--output-format text|json|stream-json` shapes the output.

**2 — CI.** Once Claude (or a check suite) runs headlessly, it runs in a pipeline. The pattern: a CI
job invokes `claude -p … --output-format json` on every push/PR — to triage an issue, draft a fix,
review a diff — or, as in *this* repo, runs the enforcement suite as a backstop. The official GitHub
Action wraps the headless invocation; the version-/integration-specific details: CI runs use headless `-p` with `--output-format json` (and optionally `--max-budget-usd`); the official GitHub Action `anthropics/claude-code-action@v1` wraps this (installed via the Claude GitHub App + an API key or a Pro/Max OAuth token). The key
shift is that CI is **unattended**: there's no one to answer a permission prompt, so what runs must be
safe to run without one (see §5).

**3 — Parallel agents via worktrees.** When several **independent** tasks can proceed at once,
running them in one working tree means they trample each other's edits. A **git worktree** gives each
agent its own checked-out tree (and branch) on the same repo, so they don't collide. Claude can create
one with `--worktree`, or use plain `git worktree add`. `-w`/`--worktree [name]` creates a git worktree for the session; `--tmux` opens it in a tmux session. The
[parallel-worktrees pattern](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is: isolate each task
in a worktree → run them concurrently → **review and integrate each agent's diff independently**. The
independence test is the same as for subagents ([Subagents](../13-subagents/unit.md)): if task B needs task
A's output, they aren't parallel.

**4 — These compose.** Headless is the unit; CI is headless on a trigger; parallel worktrees are
several runs at once. Together they're how a senior engineer scales Claude past one interactive session
— a fleet of bounded, scriptable runs — rather than typing to it one task at a time.

**5 — Unattended changes the safety model (and that's why this unit exists last).** Interactively, *you*
are the backstop — you read each diff, you answer each permission prompt, you hit undo. Headless and in
CI, **none of that is there.** So the guardrails have to be built in *beforehand*:

- **Deterministic hooks** ([Hooks](../14-hooks/unit.md)) are the enforcement that doesn't need a human —
  a `PreToolUse` block or a `PostToolUse` check fires whether or not anyone's watching.
- **Bounded blast radius** ([Operate safely](../03-operate-safely/unit.md)) — restricted permissions/tools, a
  spend cap (`--max-budget-usd`), and checkpoints/sandboxing matter *most* when there's no interactive
  approval and no one to notice a runaway. In-REPL `/rewind` checkpoints/restores recent changes to undo them; `--no-session-persistence` disables saving sessions.
- **Per-diff review** — parallel agents each produce a diff you review **separately** before merging;
  "all the agents finished" is not "all the work is correct" — the [Subagents](../13-subagents/unit.md)
  verify-the-result rule, multiplied.

Automation amplifies whatever you point it at, including mistakes. The skill isn't typing `-p` — it's
having the guardrails so unattended runs stay safe.

**Version currency.** Verified against Claude Code 2.1.159. `-p`/`--print`,
`--output-format`, `--max-budget-usd`, and `--worktree` are `--help`-verified; the GitHub Action
integration and in-REPL rewind are external/in-REPL surfaces — confirm them against the docs / `--help`
before relying on a detail, rather than authoring from memory. CI runs use headless `-p` with `--output-format json` (and optionally `--max-budget-usd`); the official GitHub Action `anthropics/claude-code-action@v1` wraps this (installed via the Claude GitHub App + an API key or a Pro/Max OAuth token). In-REPL `/rewind` checkpoints/restores recent changes to undo them; `--no-session-persistence` disables saving sessions.
Tracked in [`meta/version-record.md`](../../../meta/version-record.md).

## Worked example

**This repo runs its own standards in CI — that workflow is the example.** Open
[`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml): on every push and PR, a job
checks out the repo, installs the tooling, and runs `make check` — the same enforcement suite you met
as a [Hooks](../14-hooks/unit.md) hook and a [`.githooks/pre-commit`](../../../.githooks/pre-commit) gate.
That's the **third and outermost layer** of the defense-in-depth from **Hooks**: the hook gives in-session
feedback, the pre-commit gate stops a bad local commit, and **CI is the backstop that runs even if
someone bypassed both** — unattended, on a fresh machine, with no local config to trust.

Two things to read from it:

- **It's headless automation.** No one approves anything; the job either passes or fails the build.
  That's the whole point of CI — and exactly why the *content* it guards had to be made safe to run
  without a human (the checks are deterministic and read-only).
- **It also schedules a drift check** (`cron`) — a weekly trigger to re-verify version-specific facts
  against the CLI. Automation isn't only for tests; here it's wired to prompt the very
  version-currency discipline this course runs on.

For the **headless** and **parallel** halves, the moves are small and composable:

```bash
# Headless: run a task non-interactively, structured output, capped spend.
claude -p "summarize what GET /tasks supports" --output-format json --max-budget-usd 0.50

# Parallel via worktrees: two independent tasks, isolated trees, reviewed separately.
git worktree add ../tf-feature-a -b feature-a
git worktree add ../tf-feature-b -b feature-b
#   run an agent in each tree; then review each diff on its own before merging
```

## Lab

> **No `start/`/`solution/` refs** — what you produce is a headless run, two worktrees, and a CI
> observation in *your* environment, not a single codebase diff (precedent: [Hooks](../14-hooks/unit.md)/[MCP & vetting](../15-mcp-and-vetting/unit.md)).
> The self-check is objective on what you can observe: the run's exit/output, `git worktree list`, and
> the two diffs you reviewed. (`claude -p` is Claude Code itself — the course prerequisite — so this
> path needs no extra service.)

**Goal:** run Claude **headless**, run **two agents in parallel via worktrees** on independent tasks in
`taskflow-api`, and read this repo's **CI** workflow — exercising all three with the unattended-safety
discipline front of mind.

**Steps:**

1. **Headless.** From `taskflow-api`, run a one-shot task with `claude -p "<task>" --output-format json`
   (e.g. *"list the query parameters `GET /tasks` accepts"*). Confirm it runs non-interactively and
   emits **structured** output you could parse in a script. Note where `--max-budget-usd` would bound an
   unattended run.
2. **Parallel via worktrees.** Pick **two genuinely independent** changes (e.g. add a `GET
   /health` detail in one; tighten a docstring in another). Create a worktree per task
   (`git worktree add …`, or `claude --worktree`), and run an agent in each. Confirm `git worktree list`
   shows ≥2 trees.
3. **Review each diff separately (the required verification step).** Before integrating, review **each**
   worktree's diff on its own — the [parallel agents via worktrees](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees)
   discipline. "Both agents finished" is not "both diffs are correct." Integrate only what passes review;
   tear the worktrees down (`git worktree remove`).
4. **CI.** Read [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml). Identify the
   trigger, what runs unattended, and how it relates to the in-session hook + pre-commit gate (defense in
   depth). **Optional stretch:** sketch a job step that runs `claude -p … --output-format json` against
   a PR.
5. **Name the safety net.** State, for *your* runs, what keeps them safe with no human in the loop:
   which hook ([Hooks](../14-hooks/unit.md)) enforces a standard, what bounds blast radius
   ([Operate safely](../03-operate-safely/unit.md) — permissions, `--max-budget-usd`, checkpoints), and the per-diff
   review.

**Self-check (objective — observed, not assumed):** you're done when **all** hold:

- [ ] A **headless** `claude -p … --output-format json` run completed non-interactively and produced
      **structured output** (not an interactive session).
- [ ] `git worktree list` showed **≥2 worktrees**, each holding an **independent** change worked by an
      agent (neither depended on the other's output).
- [ ] You **reviewed each diff separately** before integrating, and integrated only what passed — the
      parallel-worktrees verification step.
- [ ] You can describe the repo's **CI** trigger and what it runs unattended, and how it layers with the
      in-session hook + pre-commit gate.
- [ ] You can name the **unattended safety net** for your own runs (a hook + bounded blast radius +
      per-diff review) — not "Claude will be careful."
- [ ] No flag or integration detail was **authored from memory** — confirmed against `claude --help` / the docs.

**Reference:** there's no `solution/` branch — the runs and worktrees are *yours*. This repo's
[`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) is the reference CI pattern; the
[parallel-agents workflow](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is the reference for
the parallel-worktrees discipline. Compare your run + worktrees + review against them and the checklist.

## Common pitfalls

- **Parallelizing dependent tasks.** Worktrees isolate the *tree*, not the *logic* — if task B needs
  task A's change, running them at once just produces a B that has to be redone. Split only genuinely
  independent work ([Subagents](../13-subagents/unit.md)).
- **Trusting an unattended run because it finished.** No exit code proves the *diff* is right. Review
  each agent's output; in CI, make the gate fail closed (a real check), not a rubber stamp.
- **Running headless with interactive-era permissions.** With no one to approve, broad permissions or
  no spend cap turn a small mistake into a large, unwatched one. Bound it: restricted tools, a hook
  ([Hooks](../14-hooks/unit.md)), `--max-budget-usd`, checkpoints ([Operate safely](../03-operate-safely/unit.md)).
- **Leaving worktrees lying around.** Orphaned worktrees and branches accumulate and confuse later
  runs. `git worktree remove` when done; integrate or discard each branch deliberately.
- **Parsing prose output in a script.** If something downstream consumes the result, use
  `--output-format json`/`stream-json` — scraping the human-readable text is brittle.
- **Authoring flags/Action config from memory.** Headless flags, the worktree flag, and the CI Action
  are version-/integration-specific — confirm against `--help` and the docs.

## Going deeper

- **This closes the Autonomy & Scale stage** — and the unit ladder. From here the work is the
  **capstone**: an end-to-end project that puts the whole course together (context engineering + at
  least one custom extension + the verification discipline). See the progress checklist for where you
  stand against every can-do.
- **The three CI/enforcement layers** — in-session hook ([Hooks](../14-hooks/unit.md)),
  [`.githooks/pre-commit`](../../../.githooks/pre-commit), and
  [CI](../../../.github/workflows/checks.yml) — are the same suite at widening blast radius.
- The parallel-agents pattern: [`meta/workflows.md`](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees).
  Integrating each diff is the [Git & PR](../08-git-and-pr/unit.md) git/PR discipline, per worktree.
- Headless / CI / worktree surfaces: `-p`/`--print` runs headlessly; `--output-format text|json|stream-json` shapes the output. CI runs use headless `-p` with `--output-format json` (and optionally `--max-budget-usd`); the official GitHub Action `anthropics/claude-code-action@v1` wraps this (installed via the Claude GitHub App + an API key or a Pro/Max OAuth token). `-w`/`--worktree [name]` creates a git worktree for the session; `--tmux` opens it in a tmux session.
  Version-specifics in [`meta/version-record.md`](../../../meta/version-record.md). Confirm with
  `claude --help`.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
