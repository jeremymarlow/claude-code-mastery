<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U7
title: "Debug an unfamiliar failure by confirming the root cause"
stage: daily-driver
depth_tier: core
use_case: "A test/endpoint is broken — find and fix it"
can_do: [C8]
workflows: [W3]
coverage_areas: [12]
prerequisites: [U5]
reading_time_min: 9
lab_time_min: 30
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Debug an unfamiliar failure by confirming the root cause

# Debug an unfamiliar failure by confirming the root cause

## Learning objectives

By the end of this unit you can:

- **Debug an unfamiliar failure as a scientist, not a guesser** — reproduce it deterministically,
  confirm the *root cause* before changing anything, fix it, and prove the fix.
- **Capture the failure as a repro you can re-run** so "fixed" is objective, not a vibe.
- **Confirm the root cause rather than pattern-matching the symptom** — and resist the AI's pull
  toward a plausible-looking change that treats a symptom and leaves the cause (and its copies) intact.
- **Verify the fix *and* that nothing regressed** — the bug is gone, the repro passes, and the rest
  of the program still works (cross-cutting verification, CV).

## Fast path (TL;DR)

> Debugging with Claude is [the debugging workflow](../../../meta/workflows.md#w3--debugging-an-unfamiliar-failure):
> **reproduce → capture → confirm root cause → fix → no-regress.** Get a deterministic repro first;
> have Claude (and you) **find the real cause** before touching code — the #1 failure mode is letting
> a confident AI patch a symptom. Then fix at the cause, re-run the repro to confirm it's gone, and
> check nothing else broke. The lab hands you a real bug in the messy `taskflow-cli`: **overdue tasks
> are never flagged.** You'll chase it to its root — and discover the cause is copy-pasted in three
> places, so a one-site "fix" leaves the bug alive. `tools/verify-lab u07-lab1` proves you got it.

## Skip-check

**Skip this unit if you can already:** take a bug you've never seen, **reproduce it deterministically**,
drive Claude to **confirm the actual root cause** (with evidence, not a guess) before any edit, fix it
at the cause, and verify both that the repro now passes **and** that nothing else regressed — rather
than accepting the first plausible-looking patch Claude proposes for the symptom.

## Concept

In **Ship a feature** and **TDD** you *added* behavior; debugging is the inverse skill — something already works wrong and
you don't yet know why. The discipline that separates fixing from flailing is the **scientific
method**, and it matters *more* with an AI in the loop, not less. Claude is extremely good at producing
a confident, plausible change in response to a symptom — and a plausible change that treats the symptom
without addressing the cause is the most expensive kind of wrong, because it *looks* fixed. Your job is
to keep the loop honest: reproduce, find the cause, *then* change code.

**The workflow.** The generalized pattern lives once in
[`meta/workflows.md`](../../../meta/workflows.md#w3--debugging-an-unfamiliar-failure); read it there.
The short version: **reproduce deterministically → capture it as a failing repro → confirm the root
cause → fix → confirm the repro passes and nothing regressed.** The rest of this section is what's
specific to *applying* it with Claude.

**1 — Reproduce deterministically, first.** A bug you can't reproduce on demand, you can't prove fixed.
Pin down the exact command, input, and expected-vs-actual *before* you theorize. For the lab: a task
with a due date in the past should be flagged overdue — `list --overdue` should show it, `stats` should
count it — and it isn't. That's your repro: concrete, repeatable, observable.

**2 — Capture the failure so "fixed" is objective.** Turn the repro into something you can re-run on
command — a failing test, or at minimum a scripted command sequence with a known expected output. This
is the red→green reflex from **TDD** pointed at a bug: the captured failure is what flips from red to green to *prove*
the fix, and it guards the bug from silently coming back. (The legacy CLI has no test suite at all —
which means the repro you capture here is its *first* characterization test, a thread **Refactor legacy** picks up.)

**3 — Confirm the root cause before changing anything.** This is the step the whole unit turns on.
Have Claude investigate and **explain the cause with evidence** — the specific line and *why* it
produces the wrong result — and make it convince *you* before it edits. In the lab the symptom
("overdue never flags") has a non-obvious cause: the code compares the stored date (ISO `YYYY-MM-DD`)
against today rendered as `MM-DD-YYYY`, as plain strings — a comparison that's meaningless across two
formats. A guesser sees "overdue is wrong" and tweaks something nearby; a debugger finds *that line*.
And here's the trap the lab is built around: **that broken comparison is copy-pasted in three places.**
Fixing the one Claude happens to open first makes the symptom partly disappear and leaves the bug alive
elsewhere. Confirming the root cause means finding *all* of it.

**4 — Fix at the cause, then verify the fix and the absence of regressions (CV).** Once the cause is
confirmed, fix it *there* — compare the dates as dates, at every site (the clean move is to fix the one
real check and route the others through it). Then: re-run your repro (the overdue task is now flagged),
**and** confirm nothing else broke — adding, listing, and counting tasks still behave. A debugging
change that fixes the bug and quietly breaks a neighbor is not done. Green repro **plus** a working
program — verified, not assumed — is the bar.

> **Reproduce before you trust a "fix."** The single most common way AI-assisted debugging goes wrong:
> the symptom changes, everyone declares victory, and the cause is still there (or moved). Your repro
> from step 2 is the antidote — it's not fixed until that goes green and stays green.

**Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — it's
the debugging *method* plus tool-use you already have (running the program / its tests via the Bash
tool). See [`meta/version-record.md`](../../../meta/version-record.md) if your CLI differs.

## Worked example

This course's own build debugged exactly this way. When `check-version-refs` first went in, a unit
referenced a `vd:` key that didn't resolve — but the *symptom* showed up far away, as a confusing
"unresolved key: key" failure. The fix wasn't to silence the message; it was to **reproduce** it on the
offending file, **confirm the root cause** (a unit had written a doubled-brace `vd:` token *literally*,
as a prose illustration, which the checker can't tell from a real reference), and fix it at the cause —
reword the illustration —
rather than weakening the check. The tell was the same one this unit teaches: the first plausible
explanation ("the checker is too strict") treated the symptom; the real cause was the content, and
confirming it before editing is what kept the check honest. (That exact failure happened while authoring the **TDD** unit.)

## Lab

**Goal:** find and fix a real bug in the legacy `taskflow-cli` by confirming its root cause — reproduce
it, capture it, fix it at the cause (everywhere it lives), and verify the fix without regressing the
rest of the CLI.

**The bug (your repro):** in `codebases/legacy/taskflow-cli`, **overdue tasks are never flagged.** A
task whose due date is in the past and isn't done should be reported as overdue — but:

- `python taskflow.py list --overdue` returns nothing, and
- `python taskflow.py stats` reports `overdue: 0`,

even with an obviously past-due task in the database. Expected: that task is flagged overdue, while a
task due in the future, a task with no due date, and a *done* task are not.

**Starting state:** `start/u07-lab1` (run `tools/reset-lab u07-lab1` to restore it) — the legacy CLI
with the bug present (it's a real, baked-in landmine; the CLI has no test suite).

**Steps:**

1. `tools/reset-lab u07-lab1`, then start a session in the legacy codebase:
   `cd codebases/legacy/taskflow-cli && claude`. Use a throwaway DB so you don't touch real data:
   `export TASKFLOW_DB=$(mktemp)`.
2. **Reproduce.** Add a past-due task (`python taskflow.py add "Pay invoice" --due 2020-01-01`), then
   `list --overdue` and `stats`. Confirm the symptom: nothing flagged, `overdue: 0`. That's your repro.
3. **Capture.** Write it down as a re-runnable check (a failing test, or a scripted sequence with the
   expected output) so "fixed" will be objective and the bug can't sneak back.
4. **Confirm the root cause — before any edit.** Have Claude locate *why* overdue never fires and
   explain it with the specific line and reason. Push for the real cause (how the dates are compared),
   not a nearby guess. **Then ask: where else does this same logic live?** Confirm you've found every
   copy before fixing — a partial fix is the trap.
5. **Fix and verify (CV).** Fix the cause at every site, re-run your repro (the past-due task is now
   flagged in `list --overdue`, `stats` shows `overdue: 1`, and the listing/`show` display mark it),
   and confirm a future-due, no-due, and done task are *not* flagged — and that add/list/stats still
   work. Commit with a message that names the root cause.

**Self-check (objective):** run `tools/verify-lab u07-lab1`. It passes only if a past-due, not-done task
is flagged overdue across the surfaces that report it (`list --overdue`, `stats`, and the `list`/`show`
display), future/no-due/done tasks are correctly excluded, and the CLI's basic add/list/stats behavior
still works. (It fails on the unfixed starting state — that's the repro, automated.)

**Reference solution:** branch `solution/u07-lab1` — diagnose unaided first, then diff against it. (It
fixes the date comparison to compare dates as dates and routes the duplicated checks through the single
`is_overdue` helper, so the cause is fixed at every site rather than one. Yours may differ in shape and
still pass — the verifier checks behavior, not structure.)

**Verify (CV):** the repro from step 3 is the gate. The bug is fixed when that repro goes green **and**
stays green while the rest of the CLI keeps working — not when the first symptom disappears. The
verifier deliberately checks the *display* surfaces too, so a fix applied to only one of the three
copies fails: confirming the root cause means fixing all of it.

## Common pitfalls

- **Fixing before reproducing.** If you can't reproduce it on command, you can't prove you fixed it.
  Get the deterministic repro first — always.
- **Accepting the first plausible patch.** Claude will happily propose a confident change for the
  symptom. A change that makes the symptom go away is not the same as a confirmed root cause — make it
  show you *why* the bug happens before it edits.
- **Fixing one copy of a duplicated bug.** The lab's bug lives in three places. Fix the one you found
  and the symptom only half-disappears (e.g. the count works but the display still doesn't). "Confirm
  the root cause" includes "find every instance of it."
- **Treating green-here as done.** A fix that resolves the bug but breaks a neighbor is a regression you
  introduced. Re-run the repro *and* exercise the surrounding behavior before you call it fixed.
- **Skipping the captured repro.** Eyeballing "looks fixed now" lets the bug return silently. The
  re-runnable repro is what makes the fix durable.

## Going deeper

- **Next:** **Git & PR** turns the verified fix into reviewable history; **Refactor legacy** returns
  to this same messy `taskflow-cli` and untangles the duplication that *let* this bug hide in three
  places — debugging and refactoring are two views of the same code smell.
- [`meta/workflows.md`](../../../meta/workflows.md#w3--debugging-an-unfamiliar-failure) — the generalized
  debugging pattern, and how it reuses the failing-test reflex from [TDD](../06-tdd/unit.md).
- The capture-as-a-test habit is [TDD](../06-tdd/unit.md)'s red→green pointed at a bug; the diff-reading
  and verification reflexes are [Ship a feature](../05-ship-a-feature/unit.md)'s.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
