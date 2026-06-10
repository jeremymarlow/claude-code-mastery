[Claude Code Mastery](../README.md) › When you're stuck

# When you're stuck

You're working through this course **solo** — so getting unstuck without an instructor is a skill
in itself. This page is your recovery mechanism. Work top to bottom; stop as soon as you're
moving again.

## 1. Re-read the lab's self-check

Every lab states an **objective self-check** and (where feasible) a `tools/verify-lab` command. If
you're not sure whether you're stuck, run the check — "done" is defined, not a feeling.

## 2. Use a hint before the solution

Hints are deliberately separated from solutions so you can get a nudge without spoiling the exercise:

- **Hint:** read the unit's **Common pitfalls** section — most stuck points are a known pitfall for
  *that* task.
- **Still stuck:** skim the relevant pattern in [`../meta/workflows.md`](../meta/workflows.md) (the
  unit names the workflow it uses).
- **Last resort:** inspect the reference solution branch `solution/uNN-labM` (`git diff
  start/uNN-labM solution/uNN-labM`). Read it to understand *why*, then redo the lab yourself from a
  clean `tools/reset-lab uNN-labM`.

## 3. Use Claude Code itself to get unstuck

This is the meta-skill the course is teaching — Claude is also your debugger and tutor:

- **Explain the failure:** paste the error and ask Claude to explain it *and* point at the file/line.
  Then **verify** its explanation against the code — don't just accept it.
- **Ask for the approach, not the answer:** "What are the likely causes of this, in order?" keeps you
  in the driver's seat.
- **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the debugging
  workflow) so "fixed" becomes objective.
- **Session gone sideways?** Don't keep typing corrections into a bad trajectory. Climb the recovery
  ladder from [Memory & context](./units/04-memory-and-context/unit.md): **interrupt** the current
  action, give **one precise redirect**, **roll back** what reached disk, or **restart** with the
  correction baked into the brief or `CLAUDE.md`. The tell that it's restart time: the same
  misunderstanding survived two corrections.
- **Reset and retry:** for lab work, `tools/reset-lab uNN-labM` restores the clean starting state —
  a fresh context plus a clean tree often beats untangling a confused session.

## 4. Environment problems

- Run [`../tools/doctor`](../tools/doctor) — it checks install, version, auth, and a first command.
- If `claude --version` differs from `meta/version-record.md`, some version-specific details may have
  moved; see that file and the `{{vd:*}}` callouts.

## FAQ

- **"A command/flag in a unit doesn't exist on my CLI."** Your version differs from the verified one
  (`meta/version-record.md`). Check the version-detail callout near it; report drift via
  `tools/check-version-drift`.
- **"My lab won't reset cleanly."** Commit or stash your work first, then `tools/reset-lab uNN-labM`.
- **"Do I have to do the labs in order?"** No — follow the prerequisites listed at the top of each
  unit, just under its title (the authoritative ordering); the numeric path is just the default.
- **"I'm not sure I've actually learned it."** Track yourself against
  [`progress-checklist.md`](./progress-checklist.md); the capstone rubric is the final proof.
