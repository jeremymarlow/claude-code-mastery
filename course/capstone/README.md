[Claude Code Mastery](../../README.md) › Capstone

# Capstone

The capstone is the course's **single graded assessment** — the one place you prove, end to
end, that you can do real work with Claude Code and **verify** it. Units are instructional and labs are
ungraded practice; this is the only thing you "grade," and you grade the **work product**, not yourself.

## What it asks of you

Pick one brief from the [brief menu](./briefs.md) and take it from nothing to a verified, finished
result. Whichever you choose, the deliverable must show all four:

- **Context engineering** — deliberate `CLAUDE.md` / context steering.
- **At least one custom extension** — a command, subagent, skill, hook, or MCP connection you build
  and use.
- **A non-trivial workflow** — a real multi-step workflow, not a one-shot prompt.
- **Explicit verification** — you check Claude's output, not merely the test bar.

You do **not** face a blank page: the [build case study](./case-study.md) — how this course itself was
built with Claude Code — is your worked **exemplar**.

## The deliverable

1. **The work itself** — committed to a branch (or your own repo), with a short README pointing at
   what you built and how to run/verify it.
2. **A brief write-up** — which brief, the workflow you followed, the custom extension you built and
   why, and how you engineered context.
3. **The required verification reflection** — structured by these prompts, each with concrete
   evidence from your work:
   - **One catch** — a place you caught Claude producing something wrong or suboptimal, and what you
     did about it.
   - **One justified accept** — a place you accepted Claude's output, and the evidence that justified
     trusting it (not "the tests passed" alone).
   - **One override** — a place you overrode or redirected Claude, and why your judgment won.

This reflection is not optional polish — it is the core of the cross-cutting verification (CV) dimension and the
thesis the whole course defends: verify, don't trust.

## Grading your own capstone

Score the work product against the [rubric](./rubric.md). It is **self-applicable**: for each
can-do dimension you mark *demonstrated / partially demonstrated / not yet demonstrated*, with evidence
you can point to. An honest "not yet" is a pointer back to the unit, not a verdict on you.

**Optional AI-assisted self-grade.** You may have Claude score your capstone against the
rubric — but you must then **critique that grade** rather than accept it (find where it was too
generous or too harsh, with evidence). Grading the grader is itself part of the assessment.

## Optional mid-course checkpoint (ungraded)

After the **Daily Driver** stage (through **Git & PR**), you may take an optional, **ungraded** self-check to
surface gaps before the capstone. It does not change the capstone's status as the sole graded
assessment.

**The checkpoint:** ship one small feature to
[`taskflow-api`](../../codebases/primary/taskflow-api) end-to-end on your own — explore, plan, a
failing test, implement to green, a clean commit with an accurate message — then self-score against
can-dos **C5–C9 and CV** using the [rubric](./rubric.md). If any land at "not yet," revisit that
unit before attempting the capstone. Nothing here is recorded or graded; it is a mirror, not a hurdle.

## If you get stuck

The capstone is a solo job by design, but you are not without support — see
[`../stuck.md`](../stuck.md), and track your overall coverage with
[`../progress-checklist.md`](../progress-checklist.md).
