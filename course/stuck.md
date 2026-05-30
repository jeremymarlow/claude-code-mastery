# When you're stuck

You're working through this course **solo** — so getting unstuck without an instructor is a skill
in itself. This page is your recovery mechanism (R9.AC4). Work top to bottom; stop as soon as you're
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
  Then **verify** its explanation against the code (CV) — don't just accept it.
- **Ask for the approach, not the answer:** "What are the likely causes of this, in order?" keeps you
  in the driver's seat.
- **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the W3 debugging
  pattern) so "fixed" becomes objective.
- **Reset and retry:** if a session has gone sideways, `tools/reset-lab uNN-labM` and start the lab
  clean — a fresh context often beats untangling a confused one.

## 4. Environment problems

- Run [`../tools/doctor`](../tools/doctor) — it checks install, version, auth, and a first command.
- If `claude --version` differs from `meta/version-record.md`, some version-specific details may have
  moved; see that file and the `{{vd:*}}` callouts.

## FAQ

- **"A command/flag in a unit doesn't exist on my CLI."** Your version differs from the verified one
  (`meta/version-record.md`). Check the `{{vd:key}}` callout near it; report drift via
  `tools/check-version-drift`.
- **"My lab won't reset cleanly."** Commit or stash your work first, then `tools/reset-lab uNN-labM`.
- **"Do I have to do the labs in order?"** No — follow the prerequisites in each unit's front matter
  (the authoritative ordering); the numeric path is just the default (R9.AC2).
- **"I'm not sure I've actually learned it."** Track yourself against
  [`progress-checklist.md`](./progress-checklist.md); the capstone rubric is the final proof.
