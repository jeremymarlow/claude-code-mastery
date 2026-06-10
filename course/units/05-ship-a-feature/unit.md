<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Ship a feature end-to-end with explore → plan → code → commit

# Ship a feature end-to-end with explore → plan → code → commit

*Reading: ~14 min · Lab: ~30 min · Prerequisites: [Explore and explain an unfamiliar codebase](../02-explore-a-codebase/unit.md), [Steer Claude with project memory and deliberate context](../04-memory-and-context/unit.md)*

## Learning objectives

By the end of this unit you can:

- **Drive a non-trivial feature through the explore → plan → code → commit loop** — orient Claude in
  the code, get an explicit plan, implement against it, and land a verified change.
- **Write a brief that gives Claude what it needs** — scope, constraints, and a defined deliverable —
  and revise the brief (not just the output) when the result shows it was underspecified.
- **Use plan mode as a review gate** — make Claude design *before* it writes, and reject or redirect a
  bad plan while it's still free to change.
- **Verify at the two points that matter** — review the *plan* before code exists, then read the diff
  and run the tests before you commit — the cross-cutting verification (CV) reflex applied to a real feature.
- **Recognize when to reach for extended thinking** (awareness) — and know it's a dial, not a default.

## Fast path (TL;DR)

> This is Anthropic's flagship coding loop ([explore → plan → code → commit](../../../meta/workflows.md#w1--explore--plan--code--commit)),
> and it's the default for any change bigger than a one-liner. **Explore** (have Claude read the code and
> restate the task), **plan** (in plan mode, so nothing is written until you approve), **code** (implement
> the approved plan in small steps), **commit** (read the diff, run `pytest`, then commit). The lab has you
> ship a real endpoint — `GET /projects/{id}/stats` — this way, and `tools/verify-lab u05-lab1` proves it.
> The two verification gates are the *plan* and the *diff*.

## Skip-check

**Skip this unit if you can already:** take a non-trivial feature from a cold start to a committed,
verified change by driving Claude through explore → plan → code → commit — getting an explicit plan you
review *before* any code is written (plan mode), then reading the diff and running the suite *before*
you commit — rather than letting Claude jump straight to edits and trusting the result.

## Concept

You can now land a change, read unfamiliar code, operate safely, and steer Claude with
memory and context. This unit is where those combine into the **daily-driver loop** — the one you'll
run dozens of times a day. The mistake it cures is the most common one in AI-assisted coding: *typing a
feature request and accepting whatever edits come back.* That works for one-liners and fails for
everything else, because you've skipped the two moments where a wrong turn is cheap to catch.

**The workflow.** The generalized pattern lives once in
[`meta/workflows.md`](../../../meta/workflows.md#w1--explore--plan--code--commit); read it there. The
short version: **explore → plan → code → commit**, with a review gate at the plan and again at the diff.
The rest of this section is what's specific to *applying* it.

**The brief comes first.** Every run of the loop starts with something you type, and its quality sets a
ceiling on everything downstream. A working brief carries four things: **scope** (which part of the
system), **constraints** (the conventions and requirements the change must respect), a **deliverable**
(what "done" looks like, concretely), and **context** (what you already know that Claude can't guess).
Compare:

**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.

> **Weak:** "Add a stats endpoint for projects."
>
> **Strong:** "Add `GET /projects/{id}/stats` returning per-status task counts, zero-filled for every
> status. Ownership like the rest of the API: a project I don't own → 404. Follow this repo's
> convention — logic in a service, thin route. Start by reading the task/project routers and services
> and restating where the pieces go; don't write code yet."

The weak brief isn't wrong — it's underspecified, and Claude will fill the gaps with plausible guesses
you then have to review out. When a plan or a result disappoints, the highest-leverage fix is usually
one step upstream: revise the *brief* and re-run, rather than patching outputs one correction at a
time.

**1 — Explore before planning.** A plan built on a misread of the code is a confident plan that's wrong.
Start every feature by having Claude **read the relevant code and restate the task and constraints back
to you** — the habit from **Explore a codebase**, now load-bearing. For the lab's stats endpoint that means: where do routes
live, where does domain logic go, how is ownership enforced, what's the existing response shape? You're
checking that Claude's mental model matches the codebase *before* it proposes anything.

**2 — Plan mode is the cheapest place to be wrong.** Plan mode (`--permission-mode plan`): Claude plans without writing changes until you approve. In plan mode Claude investigates
and proposes a plan **without writing any files** — so a bad approach costs you a read, not a revert.
This is the unit's central tool. Make Claude show you: which files it will touch, what the new
behavior is, and how it'll be tested. **Then actually review it.** A plan that puts domain logic in the
router instead of the service layer contradicts this repo's one load-bearing convention (the baseline
[`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md), from **Memory & context**) — catch that in the plan and
one sentence fixes it; catch it after the code is written and you're refactoring. **Approving a plan is a
decision, not a formality** — if it's vague, wrong, or over-scoped, redirect before you let it write.

**3 — Code in small steps against the approved plan.** Once you accept the plan, implementation should
follow it. Keep the steps small enough that each diff is reviewable — a feature that lands as one
500-line dump is one you can't actually verify. If reality diverges from the plan (it sometimes should —
the code teaches you something), notice the divergence and re-plan rather than letting Claude improvise
silently.

**4 — Commit is a verification gate, not a save button (CV).** Before you commit: **read the diff** (does
it match the plan? does it touch only what it should? did the existing behavior survive?) and **run the
tests** (`pytest`). A green suite only says that nothing already-tested broke; *you* confirm the change
is the one you wanted. Only then commit, with a message that says *why*. This is the diff-reading habit
from your first unit, now on a change big enough for it to earn its keep.

> **Awareness — extended thinking.** For a genuinely hard plan — a thorny design trade-off, a subtle
> algorithm — you can have Claude think harder before answering: Effort levels low, medium, high, xhigh, max (`--effort <level>`). It's a dial you reach
> for when a problem is hard enough to warrant it, not a default for routine work (it costs latency and
> tokens). Know it exists; the lab's feature doesn't need it.

**Version currency.** This unit was verified against Claude Code `2.1.170`; plan mode and
the effort/thinking controls are version-specific surface — confirm with `claude --help` / `/help` and see
[`meta/version-record.md`](../../../meta/version-record.md) if your version differs.

## Worked example

Here is the lab's feature — the stats endpoint — driven through the loop, with the artifacts that
matter shown the way you'd actually see them.

**Explore.** You open with the strong brief from the concept section. The useful part of what comes
back is a *checkable* restatement:

**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.

> **You:** Read the task and project routers and services, then restate: where a new
> `GET /projects/{id}/stats` route belongs, where the counting logic goes, and how ownership is
> enforced today. Don't write any code yet.
>
> **Claude:** Routes live in `app/api/routers/`, one module per resource. Domain logic belongs in
> `app/services/` per the project `CLAUDE.md` — routers just wire services up. Ownership is enforced
> in the service layer: `get_project` raises `NotFoundError` (→ 404) unless the project exists and
> belongs to the current user, and the task services route through it. So this feature wants a
> `project_task_stats` service function that calls `get_project` first, plus a thin route.

Before building on that answer, open `app/services/projects.py` and confirm `get_project` really does
what Claude says. It does — but the habit of checking is what makes the next step trustworthy.

**Plan — the gate where you steer.** Two plans Claude could plausibly propose for this feature. The
first is the kind you reject:

**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.

> **Claude (plan A):** I'll add a `stats` route to the tasks router that queries the task table,
> counts by status in the route handler, and returns a dict.
>
> **You:** Two problems. Counting is domain logic — it belongs in a service, not the route handler
> (CLAUDE.md). And the plan never says what happens when the project isn't mine. Re-plan: service
> function with the ownership check first, zero-filled counts for every status, thin route.
>
> **Claude (plan B):** (1) `ProjectStats` schema in `app/models/project.py`. (2)
> `project_task_stats(session, owner, project_id)` in `app/services/tasks.py` — `get_project` first
> (foreign/missing → 404), then one grouped count query, zero-filled across every `TaskStatus`.
> (3) Thin route `GET /projects/{project_id}/stats`. (4) Tests: per-status counts, zero-fill,
> foreign project → 404.

Plan A wasn't wasted — it surfaced both mistakes while each was one sentence to fix. That is the
whole value of the gate.

**Diff — the gate where you verify.** The reference solution's service hunk, exactly as `git diff`
shows it:

**Captured** — the solution's service-layer change, `git diff start/u05-lab1..solution/u05-lab1`
(excerpt; the full diff adds the `ProjectStats` schema, the thin route, and three tests):

```diff
+def project_task_stats(session: Session, owner: User, project_id: int) -> dict[str, int]:
+    """Count an owned project's tasks by status. ..."""
+    get_project(session, owner, project_id)
+
+    counts = {status.value: 0 for status in TaskStatus}
+    rows = session.exec(
+        select(Task.status, func.count())
+        .where(Task.project_id == project_id)
+        .group_by(Task.status)
+    ).all()
+    for status, count in rows:
+        key = status.value if isinstance(status, TaskStatus) else status
+        counts[key] = count
+    return counts
```

Reading it, you confirm what the plan promised: the ownership check runs *before* any counting (first
line of the body), every status is zero-filled, and nothing outside the feature moved. Then the suite:

**Captured** — `pytest` on the solution branch (2026-06-09):

```text
....................................                                   [100%]
39 passed in 12.06s
```

Green plus a read diff is the exit condition. (This repository is itself the loop's heavyweight
cousin — built spec-driven with a review gate per phase, taught in **Spec-driven dev**; its `specs/`
tree is the provenance behind this example.)

Read the baseline [`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md) before the lab —
its "new behavior usually belongs in a service, with the router just wiring it up" is the constraint
plan A violated.

## Lab

**Goal:** ship a new feature into `taskflow-api` end-to-end via explore → plan → code → commit, and prove
it with the diff, the test suite, and the lab verifier.

**The feature (your spec):** add a **project task-stats** endpoint.

- **Route:** `GET /projects/{project_id}/stats`, authenticated like the rest of the API.
- **Response (200):** `{"project_id": <id>, "total": <int>, "by_status": {"todo": <n>, "in_progress": <n>, "done": <n>}}`.
- **`by_status`** must include **every** task status, zero-filled (a status with no tasks reports `0`).
- **Counts** cover only that project's tasks.
- **Ownership:** a project the caller doesn't own (or that doesn't exist) returns **404**, consistent with
  the rest of the API — never an empty or forged count for someone else's project.

**Starting state:** `start/u05-lab1` (run `tools/reset-lab u05-lab1` to restore it) — the clean, green
primary codebase with no stats endpoint yet.

**Steps:**

1. `tools/reset-lab u05-lab1`, then start a session inside the codebase:
   `cd codebases/primary/taskflow-api && claude`.
2. **Explore — with your own brief.** Write the opening brief yourself (scope, constraints,
   deliverable, context — don't copy the worked example's): have Claude read the task and project
   routers/services and restate where the route goes, where the counting logic belongs, and how
   ownership is enforced. Spot-check its answer against the files — the plan is only as good as this.
3. **Plan (in plan mode).** Have Claude produce a plan for the feature above *without writing code*: the
   files it'll touch, the response shape, and how it'll be tested. **Review it against the contract and the
   service-layer convention** before approving. Redirect if logic is landing in the router or the 404 path
   is missing. **If the plan misses something your brief never mentioned** (the zero-fill, the 404),
   that's a brief problem, not just a plan problem — revise the brief once and re-plan, and notice the
   difference upstream wording makes downstream.
4. **Code.** Approve the plan and implement it in small steps. Have Claude add a test that pins the
   contract (counts by status, zero-fill, 404 for a foreign project).
5. **Commit (verify first).** Read the diff and run `pytest` (see *Verify* below). Then commit with a
   message that states the feature and why.

**Self-check (objective):** run `tools/verify-lab u05-lab1`. It passes only if the full pytest suite is
green **and** `GET /projects/{id}/stats` meets the contract above — correct per-status counts, zero-filled
statuses, and a 404 for a project the caller doesn't own.

**Reference solution:** branch `solution/u05-lab1` — attempt the lab unaided first, then diff your result
against it. (It threads the feature through the same layers the codebase already uses: a `ProjectStats`
schema, a `project_task_stats` service function that enforces ownership via `get_project`, and one thin
route. Yours may differ in shape and still pass — the verifier checks the contract, not your structure.)

**Verify (CV):** this lab has **two** gates, and they're the whole point.
- **The plan (step 3):** before any code exists, confirm the approach is right — correct layer, the 404
  case handled, scope not ballooning. Rejecting a bad plan here is free.
- **The diff (step 5):** before committing, read the diff (only the files the plan named? existing
  behavior intact?) and run `pytest`. A green suite plus a read diff — not the green suite alone — is what
  "verified" means.

**On your own repo (transfer — optional, bring-your-own, not verifiable by this course's tooling):**
pick a small real feature in a codebase you actually work on and run the same loop: your brief, an
explore restatement you spot-check, a plan you review against *your* project's conventions, a diff you
read before committing. The loop transfers; the conventions in the brief are the part you supply.

## Common pitfalls

- **Skipping straight to "code."** Asking for the feature without exploring or planning is how you get a
  confident, wrong implementation. The loop's value is entirely in the two gates you'd be skipping.
- **A one-line brief for a multi-layer feature.** "Add a stats endpoint" leaves scope, constraints, and
  the deliverable to be guessed. You'll spend the review gates correcting guesses your brief invited.
- **Rubber-stamping the plan.** Plan mode only helps if you *read* the plan. Approving a vague or
  wrong-layer plan just defers the problem to a more expensive moment.
- **Letting logic land in the router.** The baseline `CLAUDE.md` says domain logic lives in the service
  layer. A plan that counts tasks inside the route handler "works" but violates the convention — catch it
  in review. (This is also why **Memory & context** mattered: memory only steers if you let it.)
- **Forgetting the 404 / ownership case.** The happy path is easy; the security-relevant edge (someone
  else's project) is the one that distinguishes a real feature from a demo. The verifier checks it.
- **Committing on green tests alone.** Tests pass ≠ change is correct and scoped. Read the diff every
  time — the habit you built on one line in your first unit is the same habit here, where it actually protects you.
- **Reaching for extended thinking by reflex.** It's for genuinely hard problems; on routine features it
  just adds latency. Use it deliberately, not as a default.

## Going deeper

- **Next:** **TDD** tightens the loop by writing the failing test *first*; **Debugging** and **Git & PR**
  build on this same explore→plan→code→commit spine. Everything in the Daily Driver stage assumes you can
  run this loop fluently.
- [`meta/workflows.md`](../../../meta/workflows.md#w1--explore--plan--code--commit) — the generalized
  explore → plan → code → commit pattern (and the other workflows it connects to).
- Extended thinking / effort levels: Effort levels low, medium, high, xhigh, max (`--effort <level>`). Where version-specifics are recorded:
  [`meta/version-record.md`](../../../meta/version-record.md).
- The exploration habit from [Explore a codebase](../02-explore-a-codebase/unit.md) and the memory/context levers from
  [Memory & context](../04-memory-and-context/unit.md) are the inputs that make a *good* plan possible.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
