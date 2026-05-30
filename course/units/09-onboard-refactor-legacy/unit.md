---
id: U9
title: "Onboard a legacy codebase and refactor it without changing behavior"
stage: force-multiplier
depth_tier: core
use_case: "Map an unfamiliar legacy codebase and refactor it safely"
can_do: [C10]
workflows: [W5, W8]
coverage_areas: [14]
prerequisites: [U2, U7]
reading_time_min: 11
lab_time_min: 40
---

# Onboard a legacy codebase and refactor it without changing behavior

## Learning objectives

By the end of this unit you can:

- **Onboard deeply to an unfamiliar, messy codebase** — drive Claude to map its architecture, data
  flow, and duplication, then *validate that map against the source* before trusting it — advances `C10`.
- **Establish a green baseline before you refactor** — and when the code has no tests, build a
  **characterization safety net** (tests that pin *current* behavior, bugs included) so "behavior
  preserved" becomes objective rather than hopeful.
- **Run a multi-file, behavior-preserving refactor in reviewable increments** — split a god-module,
  de-duplicate, keep the suite green at every step.
- **Guard the refactor against scope creep** — refuse to mix a behavior change (even a tempting
  bug-fix) into a "pure" refactor, and diff-review specifically for behavior that snuck in (`CV`).

## Fast path (TL;DR)

> This unit combines two workflows: **deep onboarding** ([W8](../../../meta/workflows.md#w8--onboarding-to-an-unfamiliarlarge-codebase),
> the heavy version of U2's light explore) and **multi-file refactoring**
> ([W5](../../../meta/workflows.md#w5--multi-file-refactoring)). The discipline: **map the code and
> validate the map → establish a green baseline → refactor in increments → keep the suite green before
> *and* after → diff-review for scope creep.** The twist with legacy code is that there's often **no
> suite to stay green** — so your first move is to **write characterization tests** that pin today's
> behavior (including its bugs) before you touch structure. The lab hands you the ~700-line
> single-file `taskflow-cli` god-module and asks you to split and de-duplicate it **without changing
> one byte of observable behavior** — including the overdue bug from U7, which you must *not* fix here
> (that's a separate change). `tools/verify-lab u09-lab1` proves behavior is identical before and after.

## Skip-check

**Skip this unit if you can already:** take an unfamiliar, untested, messy codebase, build and
*validate* a mental model of it with Claude, **establish a behavior baseline** (writing
characterization tests first when none exist), and then carry out a **multi-file, behavior-preserving
refactor** — de-duplicating and restructuring in reviewable increments, keeping the baseline green
throughout, and keeping a tempting drive-by bug-fix *out* of the refactor — rather than rewriting in
one big swing and *hoping* nothing changed.

## Concept

Most real engineering value isn't greenfield — it's **rescuing code someone else wrote, under
deadline, years ago.** That work has two halves, and this unit is both: first you have to *understand*
code you've never seen (deep onboarding), then you have to *change its shape without changing what it
does* (refactoring). An AI is a force multiplier on both — and a liability on both if you let it move
faster than you can verify.

**Part 1 — deep onboarding (W8, deep).** You met the light version in [U2](../02-explore-a-codebase/unit.md):
enough of a map to *locate* a change. Refactoring needs the deep version: enough to change structure
*safely*. The generalized pattern lives in
[`meta/workflows.md`](../../../meta/workflows.md#w8--onboarding-to-an-unfamiliarlarge-codebase) — build
a map, then **validate it against the source.** With Claude: have it summarize the architecture, the
data flow, the entry points, *and the duplication and smells* — then spot-check those claims against
the actual code. An onboarding summary is a **hypothesis until checked**, and a confident wrong map is
worse than no map because it makes you refactor boldly in the wrong direction.

**Part 2 — multi-file refactoring (W5).** A refactor is a **behavior-preserving** change: the code's
shape improves, its observable behavior does not move *at all*. The generalized pattern is in
[`meta/workflows.md`](../../../meta/workflows.md#w5--multi-file-refactoring): **green baseline → change
in reviewable increments → suite green before and after → watch for scope creep.** The rest of this
section is what's specific to doing it with Claude on legacy code.

**1 — Establish a green baseline *first*. If there's no suite, build one.** You cannot prove you
preserved behavior if you can't *measure* behavior. On a tested codebase this is "run the suite, it's
green, go." Legacy code often has **no tests** (the lab's `taskflow-cli` has never had one). That
doesn't excuse skipping the baseline — it means your *first* task is a **characterization test**: a
test that pins what the program does *right now*, correct or not. Have Claude generate a battery that
exercises the surfaces you're about to move (every command, every flag), capture the *current* output
as the expected output, and commit it. This net is what turns "I think it still works" into "the suite
is green." (It's the U7 capture reflex — pin behavior so a change is measurable — pointed at a whole
program instead of one bug.)

**2 — Refactor in reviewable increments, not one big rewrite.** The failure mode of AI-assisted
refactoring is the confident 800-line rewrite that "cleans everything up" and silently changes three
behaviors. Work in steps each small enough to diff and re-verify: extract one module, run the baseline,
green; collapse one pair of duplicated functions, run the baseline, green. Each increment is a
reviewable diff and a green checkpoint, so when something *does* move, you know which step moved it.
Plan mode (U5) is the right gate here — get the decomposition plan and approve it *before* Claude
starts moving code.

**3 — Keep the suite green before *and* after — that's the verification (CV).** The whole safety
argument of a refactor is "same behavior, better shape," and the only proof is the baseline staying
green across the change. Run it before you start (establish green), and after every increment. A
refactor that ends on a red suite isn't a refactor — it's an undiagnosed behavior change.

**4 — Guard against scope creep: a bug-fix is *not* part of a refactor.** This is the discipline the
unit turns on. While restructuring `taskflow-cli` you will walk straight past the overdue bug from
[U7](../07-debug-a-failure/unit.md) — the date comparison that's broken in three copies. The instinct
("I'm right here, I'll just fix it") is exactly the scope creep W5 warns about. **Don't.** A refactor
that also fixes a bug changes behavior, which means your baseline *should* go red — and now you can't
tell a bug-fix from an accident. De-duplicate the three copies into one (that's the refactor); leave
the one surviving copy **just as buggy as it was** (preserve behavior). Fix the bug afterward, as its
own change, against the now-single source. Diff-review every increment asking one question: *did any
observable behavior move?* If yes and you didn't mean it to, that's the bug the refactor introduced.

> **Preserve behavior, bugs and all.** The single most common way an AI refactor goes wrong is
> "helpfully" fixing things along the way. A refactor's correctness criterion is *identical behavior* —
> if your characterization tests change color, you changed behavior, even if you "improved" it. Land
> structure and behavior changes in separate diffs so each is reviewable on its own terms.

**Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — it's the
onboarding and refactoring *methods* plus tool-use you already have (reading code, running the program
and its tests via the Bash tool, plan mode from U5). See
[`meta/version-record.md`](../../../meta/version-record.md) if your CLI differs.

## Worked example

This repo's own check suite is a small, authentic version of the refactor the lab asks for. The six
`tools/check-*` scripts each need the same primitives — find the repo root, parse a unit's front
matter, resolve version-data (`vd:`) references, print PASS/FAIL consistently. Those could have been (and in an
early draft were) copy-pasted into each script. They were instead **extracted once** into
[`tools/_common.py`](../../../tools/_common.py), which all six import — the same "cross-cutting facts
live once, referenced not duplicated" rule this repo's `CLAUDE.md` states for `meta/`. That extraction
*is* a multi-file refactor: behavior-preserving (every check still reports exactly what it did before),
done so a change to "how we parse front matter" happens in one place instead of six. Read `_common.py`
and any one `check-*` that imports it and you'll see the shape the lab produces — duplication pulled up
into a shared module, callers thinned to the part that's actually unique to them.

## Lab

> **What's automated vs. what's judgment.** The verifier proves the hard, objective half — that your
> refactor **preserved behavior exactly** (the W5 "green before and after," and it fails if you let a
> behavior change, *including a bug-fix*, sneak in). The *quality* of the decomposition (are the
> modules sensible? is the duplication actually gone?) is a judgment call you apply with the checklist
> below — that's the half no script can grade.

**Goal:** deep-onboard the legacy `taskflow-cli` and perform a **multi-file, behavior-preserving
refactor** — split the ~700-line god-module into sensible modules and collapse its duplicated logic —
while keeping every observable behavior **byte-for-byte identical**, the bugs included.

**Starting state:** `start/u09-lab1` (run `tools/reset-lab u09-lab1` to restore it) — the messy
single-file `codebases/legacy/taskflow-cli/taskflow.py`: one god-module, global mutable state, two
copies of the id helper, two copies of the task lookup, **three** copies of the overdue check, dead
code, and no tests.

**Steps:**

1. `tools/reset-lab u09-lab1`, then start a session in the legacy codebase:
   `cd codebases/legacy/taskflow-cli && claude`. Use a throwaway DB so you never touch real data:
   `export TASKFLOW_DB=$(mktemp -u)`.
2. **Onboard deeply (W8).** Ask Claude to map the file: the layers (storage / domain / formatting /
   commands / CLI), the global state, and *every* piece of duplicated or dead code. Then **validate the
   map** — open the lines it cites and confirm the duplication is really there (it is: `getTask` vs
   `find_task_by_id`, `nextId` vs `_guess_next_id`, the three overdue checks, the dead `export_xml` /
   `migrate_v1_to_v2` / `recalc_next_id`). Don't refactor against an unverified summary.
3. **Build the baseline safety net.** There are no tests. Write a **characterization test** (have
   Claude help) that drives `taskflow.py` over a throwaway DB across many commands and flags and pins
   the *current* output as expected — **including** the buggy behaviors (`list --overdue` finds
   nothing; `list --limit 3` prints two rows). Run it: green. This is your "behavior preserved" meter.
4. **Plan the decomposition, then refactor in increments (W5).** In plan mode, get a module split you
   approve *before* code moves. Then execute it one increment at a time — extract a module / collapse a
   duplicate pair, **run the characterization tests, confirm green**, repeat. Keep `python taskflow.py`
   working as the entry point throughout (that's part of the behavior you're preserving).
5. **Hold the line on scope (CV).** When you reach the three overdue copies, **collapse them to one —
   but keep that one as buggy as it was.** Do **not** fix the overdue bug here. Diff-review each
   increment for any behavior that moved. Commit the refactor as its own clean history (U8).

**Self-check (objective — R7.AC3):** run `tools/verify-lab u09-lab1`. It passes only if, driving your
working-tree `taskflow.py`, the **observable behavior is identical to the starting state across a broad
command battery** (add/list with every filter and sort/show/stats/projects/tags/search/export/edit/
config/rm, the `--limit` edge, and the overdue surfaces) — **and** the god-module was actually broken
up (logic now lives across multiple modules, with `taskflow.py` no longer the monolith). Because it
compares against the *original* behavior, it **fails if you changed anything — including if you "fixed"
the overdue or `--limit` bug.** That failure is the lesson: a refactor preserves behavior.

In addition, confirm by hand (the part no script grades):

- [ ] The duplication named in step 2 is **gone**: one task lookup, one id allocator, **one** overdue
      check (still buggy — behavior preserved), no dead code left behind.
- [ ] The modules have **sensible responsibilities** (storage vs. domain vs. formatting vs. commands
      vs. CLI), not an arbitrary chop.
- [ ] Your **characterization tests** exist and are green — they're the artifact that made the refactor
      safe.
- [ ] The history is a series of **reviewable increments**, each behavior-preserving, not one giant
      "refactor everything" commit.

**Reference solution:** branch `solution/u09-lab1` — onboard and refactor unaided first, then diff
against it. (It splits `taskflow.py` into a thin entry plus a `taskflow_app/` package — storage,
dates/domain, formatting, lookups, commands, CLI — collapses the two lookups, the id helpers, and the
three overdue checks into one each, and drops the dead code, **all while preserving behavior**: the
overdue and `--limit` bugs survive intact, because fixing them would be a different change. Yours will
differ in module shape and still pass — the verifier checks behavior-equivalence and that the split
happened, not your specific layout.)

**Verify (CV):** the characterization suite is the gate. The refactor is done when that suite — and
`tools/verify-lab u09-lab1` — is green **and** the diff contains no behavior change you didn't intend.
"It looks cleaner" is not the bar; "provably identical behavior, better shape" is.

## Common pitfalls

- **Refactoring against an unvalidated map.** Claude's architecture summary is a hypothesis. Refactor
  boldly on a wrong map and you'll "simplify" away behavior you didn't know was load-bearing. Spot-check
  the map against the source first.
- **No baseline, then "it still works."** Without a green baseline you have no way to prove behavior was
  preserved — you're just hoping. On untested code, *write the characterization tests first*; that's the
  whole safety argument.
- **The confident big-bang rewrite.** One 800-line "cleanup" diff is unreviewable and hides the behavior
  change it introduced. Increment, re-verify, commit — small steps with green checkpoints.
- **Fixing the bug mid-refactor (scope creep).** The overdue bug is right there and tempting. Fixing it
  *changes behavior* — your baseline should stay green through a refactor, so a fix that turns it red
  means you can no longer tell intended from accidental change. De-dupe now; fix later, separately.
- **Letting "improve it" leak in.** "While I'm here" renames of public behavior, changed output
  formatting, a tightened validation — each is a behavior change masquerading as cleanup. If the
  characterization tests change color, you changed behavior.
- **Breaking the public interface.** Moving code into modules but breaking `python taskflow.py` (or a
  command's output) is a behavior change. The entry point and every command's I/O are part of what you
  preserve.

## Going deeper

- **Next:** U10 (spec-driven development) is the other force-multiplier discipline — building the *right*
  thing up front rather than rescuing the wrong thing later; U11 (code & security review) is how you'd
  review a refactor like this one before it merges.
- [`meta/workflows.md`](../../../meta/workflows.md#w5--multi-file-refactoring) — generalized W5, and
  [W8](../../../meta/workflows.md#w8--onboarding-to-an-unfamiliarlarge-codebase) deep onboarding (the
  heavy version of [U2](../02-explore-a-codebase/unit.md)'s light explore).
- The characterization-test reflex is [U7](../07-debug-a-failure/unit.md)'s "capture it so 'fixed' is
  objective" / [U6](../06-tdd/unit.md)'s red-green, scaled from one bug to a whole program — and U7
  literally foreshadowed this lab: the overdue bug hid in three copies *because* of the duplication you
  untangle here.
- Plan-mode-as-a-gate and diff review come straight from [U5](../05-ship-a-feature/unit.md); clean
  incremental history is [U8](../08-git-and-pr/unit.md).
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
