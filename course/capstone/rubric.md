[Claude Code Mastery](../../README.md) › [Capstone](README.md) › Capstone rubric

# Capstone rubric

<!-- Traceability (R8 — the capstone is the sole graded assessment): brief menu R8.AC2;
     this self-applicable, work-product rubric R8.AC3/AC4; verification reflection R8.AC6;
     optional AI self-grade R8.AC5; optional mid-course checkpoint R8.AC7. Kept as a comment,
     not learner-facing prose, per the P7 de-coding sweep — but R8 must resolve to a built-course
     artifact for check-traceability (R13.AC5). See decisions.md → "R8 traceability". -->

This is how you grade your **capstone work product** — not yourself. It is **self-applicable**:
a solo learner can score their own capstone against it with no external evaluator. The
dimensions below collectively cover **every can-do** in the capability map (including the cross-cutting
verification habit, CV), which is also what
[`progress-checklist.md`](../progress-checklist.md) tracks.

## How to score

For each dimension, mark the **evidence in your deliverable** at one of three levels — never a label on
you:

- **Demonstrated** — the work product clearly shows this, with evidence you can point to (a commit, a
  diff, a test, a file, a passage in your write-up).
- **Partially demonstrated** — some of it is there, but it is incomplete, unverified, or only implied.
- **Not yet demonstrated** — the capstone does not show this.

**Honest "not yet" is the point.** No single brief exercises all eighteen dimensions equally — that is
expected. The rubric is the full capability map so gaps surface; a "not yet" is not a failure, it is a
pointer back to the unit that teaches it. Aim to have **every dimension at least "demonstrated" across
your capstone *and* the labs you completed**, with the cross-cutting CV dimension demonstrated *within
the capstone itself*.

## Dimensions

### First Wins
- **[C1] Working setup, repeatably checked** — demonstrated when your environment is established and you
  can re-confirm it (e.g. `tools/doctor` or an equivalent check) rather than assuming it.
- **[C2] A single, verified change to a real codebase** — demonstrated when at least one change is made
  *and* its effect is confirmed by observation/test, not assumed from the fact that Claude produced it.
- **[C3] Explore and locate** — demonstrated when your write-up shows you used Claude to understand
  unfamiliar code and pinpoint where the work had to happen (file/symbol level), rather than guessing.
- **[C4] Operate safely** — demonstrated when you chose appropriate permission posture, protected any
  secrets, and kept blast radius bounded (and can say how) for the work you did.
- **[C5] Steer with memory and context** — demonstrated when you used `CLAUDE.md` and deliberate context
  selection to shape Claude's behavior, and can point to where it changed an outcome.

### Daily Driver
- **[C6] Feature end-to-end (explore → plan → code → commit)** — demonstrated when a non-trivial change
  went through the full loop and you verified the result yourself.
- **[C7] Test-first** — demonstrated when at least one behavior was driven from a failing test confirmed
  red *for the right reason*, then implemented to green.
- **[C8] Diagnose to root cause** — demonstrated when a failure was fixed after confirming the cause
  (a reproduction or a located root), not by guessing.
- **[C9] Clean commits and a reviewable PR** — demonstrated when the work is staged into coherent
  commits with an accurate description that matches the diff.

### Force Multiplier
- **[C10] Large multi-file refactor, kept green** — demonstrated when a behavior-preserving change spans
  multiple files and a safety net (tests / behavior-equivalence) shows behavior was preserved.
- **[C11] Spec-driven workflow** — demonstrated when you ran requirements → design → tasks with a real
  gate held between phases and two-way traceability, not all-at-once.
- **[C12] Review for correctness and security** — demonstrated when you reviewed a change (yours or
  Claude's) and triaged findings, confirming real issues and dismissing false positives with a reason.

### Autonomy & Scale
- **[C13] Package repeatable work as commands & skills** — demonstrated when you built at least one
  custom command or skill that replaces a routine you actually repeat.
- **[C14] Delegate to subagents** — demonstrated when a focused (or parallel) sub-task was delegated to a
  scoped subagent and its result was used *and verified*.
- **[C15] Automate guardrails with hooks** — demonstrated when a hook enforces a standard/guardrail and
  you proved it fires (and is a no-op when it should be).
- **[C16] Connect via MCP and vet extensions** — demonstrated when you connected an external tool/data
  source via MCP (verifying the connection and a result) and vetted a third-party extension before
  trusting it.
- **[C17] Headless / CI / parallel agents** — demonstrated when you ran Claude headlessly (`-p`) or in
  CI, or coordinated parallel agents via git worktrees, reading the result rather than assuming success.

### Cross-cutting — the through-line
- **[CV] Verify, don't trust** — demonstrated when, *within the capstone*, you read the diff, checked the
  approach, and spot-checked edges rather than relying on green tests alone — and your required
  verification reflection (see the capstone overview) records one catch, one justified accept, and one
  override. This dimension should be **demonstrated**, not partial: it is the thesis the whole course
  defends.

## Optional AI-assisted self-grade (then critique it)

You may ask Claude to score your capstone against this rubric. If you do, you **must critique the grade
rather than accept it**: find at least one dimension where Claude was too generous or too harsh, and say
why, with evidence from your deliverable. Accepting an AI grade unexamined is the exact failure mode
CV exists to prevent — so grading the grader *is* part of the assessment.
