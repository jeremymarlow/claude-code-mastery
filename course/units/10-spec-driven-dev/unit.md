<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U10
title: "Build a feature spec-first: requirements → design → tasks"
stage: force-multiplier
depth_tier: core
use_case: "Build a feature spec-first"
can_do: [C11]
workflows: [W7]
coverage_areas: [15]
prerequisites: [U5]
reading_time_min: 13
lab_time_min: 35
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Build a feature spec-first: requirements → design → tasks

# Build a feature spec-first: requirements → design → tasks

## Learning objectives

By the end of this unit you can:

- **Run a spec-driven workflow for a feature whose cost-of-wrong is high** — drive Claude through
  **requirements → design → tasks** with an explicit approval gate between phases.
- **Write requirements that pin behavior, not implementation** — testable acceptance criteria with
  stable IDs, so "done" is objective and every later artifact has something to trace back to.
- **Hold the phase gates** — review and approve each phase *before* the next begins, rather than
  letting Claude race from a one-line prompt straight to code.
- **Keep the spec traceable** — every design choice serves a requirement, every task builds a design
  element, so you can answer "why does this code exist?" by walking back up the chain (cross-cutting verification, CV).

## Fast path (TL;DR)

> Spec-driven development ([spec-driven development](../../../meta/workflows.md#w7--spec-driven-development)) is the
> heavyweight cousin of **Ship a feature**'s explore→plan→code: for a feature where building the *wrong* thing is
> expensive, you align **before** writing code by producing three reviewed artifacts in order —
> **requirements** (the WHAT, as testable criteria), **design** (the HOW), **tasks** (the ordered
> build plan) — with an **approval gate** between each. The discipline is *gates and traceability*:
> don't start design until requirements are approved, and make every design choice and task trace
> back to a requirement. **This course's own [`specs/`](../../../specs/claude-code-mastery/) is the
> worked example** — you're reading a thing built this way. The lab has you run a mini spec for one
> small `taskflow-api` feature and grade it against a rubric (spec quality is a judgment call, so
> there's no automated verifier — the rubric *is* the skill).

## Skip-check

**Skip this unit if you can already:** take an ambiguous, higher-stakes feature and drive it
spec-first — write testable requirements with stable IDs, get them reviewed and **approved before
designing**, produce a design that traces to those requirements and a task plan that traces to the
design, and only then build — rather than jumping from a vague prompt to code and discovering the
requirements by arguing about the diff.

## Concept

**Ship a feature** taught the everyday loop: explore, plan, code, commit. Plan mode there is a *lightweight* gate —
one plan, reviewed, then you build. Spec-driven development is what you reach for when that's not
enough: a feature that's **large, ambiguous, or expensive to get wrong**, where the most costly
mistake isn't a bug, it's *building the wrong thing correctly.* The cure is to make alignment an
explicit, reviewable, phased artifact instead of an assumption buried in a prompt.

**The workflow.** The generalized pattern lives once in
[`meta/workflows.md`](../../../meta/workflows.md#w7--spec-driven-development); read it there. The
short version: **requirements → design → tasks, with an approval gate between phases, and each later
artifact traceable to the one before.** The rest of this section is what's specific to running it with
Claude.

**1 — Requirements: pin the WHAT as testable criteria.** Have Claude help you write what the feature
must do — as **acceptance criteria you could turn into tests**, each with a **stable ID** — not how
it'll be coded. "The list endpoint SHALL exclude archived projects unless `include_archived=true`" is
a requirement; "add an `if` in the query builder" is not. The discipline that makes this pay off:
requirements describe *observable behavior and constraints*, and they get IDs (`R1`, `R2.AC3`…) so
that everything downstream can point at them. The single most common failure is letting an
implementation detail masquerade as a requirement — it pre-decides the design and smuggles in
assumptions no one reviewed.

**2 — The gate is the point: review and approve before moving on.** Spec-driven development is only
worth the overhead if the gates are real. **Read the requirements and approve them before Claude
designs anything; read the design and approve it before it writes tasks.** An AI will happily produce
all three phases in one breath — and then you've reviewed nothing and bought none of the benefit. A
gate is a *decision*: redirect a wrong requirement while it's one sentence, not after it's load-bearing
in the design. (This course enforces exactly this rule on itself — requirements were approved before
design began, design before tasks.)

**3 — Design and tasks: each must trace back.** The **design** says *how* — architecture, data shapes,
the pieces you'll build — and every meaningful choice should name the requirement it serves. The
**tasks** are the ordered, chunked build plan, each task implementing part of the design. Traceability
is the through-line: if a design element serves no requirement it's scope creep; if a requirement has
no design and no task, it's unbuilt. Being able to walk *requirement → design → task → code* (and back)
is what lets a reviewer — or future-you — answer "why does this exist?" without archaeology.

**4 — Then build against the spec, and verify against it (CV).** With the spec approved, implementation
is the **Ship a feature** loop (explore→plan→code→commit) — but now the plan is largely written and the acceptance
criteria *are* your test list. Verification closes the loop back to the top: the change is done when it
satisfies the requirements you wrote, the tests mirror the acceptance criteria, and the traceability
holds. "It works" isn't the bar; "it does what `R-whatever` said, provably" is.

> **A spec you didn't review is theater.** The entire value of spec-driven development is the
> *reviewed alignment* — three artifacts Claude generated and you rubber-stamped are worse than no
> spec, because they look like alignment without being it. Spend the attention at the gates; that's
> where the leverage is.

**When NOT to reach for it.** Spec-driven is overhead, and overhead is only worth it when the cost of
building the wrong thing is high. A one-line fix or an obvious endpoint doesn't need three phases — use
**Ship a feature**'s plan mode. Reserve the full ceremony for genuinely ambiguous or expensive work; misapplying it to
trivial changes teaches your team that the process is bureaucracy.

**Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — spec-driven development is a
*method* (you can run it with files Claude reads and writes via the normal tools; some setups add spec
commands, but none are required). See [`meta/version-record.md`](../../../meta/version-record.md) if
your CLI differs.

## Worked example

**You are reading a course built this way, and its spec is open for you to study.** Everything in
[`specs/claude-code-mastery/`](../../../specs/claude-code-mastery/) is the worked example:

- [`requirements.md`](../../../specs/claude-code-mastery/requirements.md) — the WHAT as **EARS-style**
  acceptance criteria with stable IDs (`R1`–`R15`, `R*.AC*`). Notice they describe behavior and
  constraints ("THE COURSE SHALL…"), and that the IDs are frozen so design and tasks can cite them.
- [`design.md`](../../../specs/claude-code-mastery/design.md) — the HOW. Each section is tagged with the
  requirement it serves (e.g. *"§3 Workflow methods → `meta/workflows.md` [R3]"*) — that bracketed
  `[R…]` is traceability you can see.
- [`tasks.md`](../../../specs/claude-code-mastery/tasks.md) — the ordered, chunked build plan (the very
  plan this unit is a task within).
- [`decisions.md`](../../../specs/claude-code-mastery/decisions.md) — the *why*, including rejected
  alternatives, so a later session doesn't re-litigate settled calls.

The gates were real: requirements were reviewed and **approved before** design started, design before
tasks — the same rule step 2 asks of you. And the repo's own [`CLAUDE.md`](../../../CLAUDE.md) names
the spec as the source of truth and tells every session to read
[`IMPLEMENTATION.md`](../../../specs/claude-code-mastery/IMPLEMENTATION.md) first. Read these before the
lab: they're what a *good* small spec is scaled up from, and the shape you're imitating.

**What a testable requirement actually looks like.** One line from this repo's spec, verbatim:

**Captured** — `specs/claude-code-mastery/requirements.md`, R19.AC2:

```text
R19.AC2 — Each ancestor breadcrumb segment SHALL be a working relative link that
resolves to an existing document (enforced by the link check, R13.AC4); the final
segment SHALL identify the current document and need not be a link.
```

A stable ID, an observable behavior, and a named enforcement hook — you could write the check for it
without asking a single follow-up question (the repo did: `tools/check-breadcrumbs`). Compare that
with the kind of line a first draft produces for the lab's feature, and the revision the gate review
should force:

**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.

> **Weak:** "Tasks should support dependencies, and blocked tasks shouldn't be completable."
>
> **Strong:** "R1.AC2 — WHEN a task is marked `done` WHILE it has ≥1 blocking task not yet `done`,
> THE API SHALL reject the request with **409** and identify the blocking task ids in the error body."

The weak line hides four decisions (what's "blocked"? rejected how? told why? what status code?) that
would otherwise get made silently at implementation time — which is exactly the failure spec-driven
work exists to prevent.

## Lab

> **This lab has no automated verifier.** Whether a requirement is well-formed, a design is traceable,
> or a gate was genuinely held are **judgment calls** no script can grade — and the point of
> spec-driven development is the reviewed alignment, not a passing test. So the self-check is an objective **rubric** you
> apply to your own spec; applying it *is* the skill. (Precedent: **Explore a codebase**, **Memory & context**, **Git & PR**.)

**Goal:** run a **miniature spec-driven workflow** — requirements → design → tasks, with a real gate
between phases — for one small feature in `taskflow-api`, then build it against your spec.

**The feature (deliberately a little ambiguous — that's why it earns a spec):** add **task
dependencies** — a task can be "blocked by" one or more other tasks, and a blocked task can't be marked
`done` until its blockers are done. The ambiguity is the point; your requirements have to *decide*
things like: What happens on a dependency cycle? Can a task depend on one in another project? What's
the error when you try to complete a blocked task? Does deleting a blocker unblock its dependents? None
of these has an obvious answer — which is exactly when spec-first beats jumping to code.

**Steps:**

1. **Requirements (then gate).** Have Claude draft acceptance criteria for the feature — testable,
   ID'd (`R1`, `R2`…), describing behavior not implementation, and resolving the ambiguities above.
   **Review them. Approve them out loud before continuing.** Redirect anything vague or
   implementation-flavored now.
2. **Design (then gate).** From the *approved* requirements, have Claude propose the design — the schema
   change (how dependencies are stored), the validation (cycle/cross-project rules), the service and
   route changes — with **each choice naming the requirement it serves**. Review for traceability and
   for the service-layer convention from [Ship a feature](../05-ship-a-feature/unit.md)'s `CLAUDE.md`. Approve.
3. **Tasks.** Have Claude break the design into an ordered task list, each task pointing at a design
   element. This is your build plan.
4. **Build against the spec.** Implement following the tasks with the **Ship a feature** loop
   (explore→plan→code→commit), using your acceptance criteria as the test list. Run `pytest`.
5. **Verify against the spec (CV).** Confirm each requirement is satisfied by a test, the design choices
   all trace to a requirement, and nothing was built that no requirement asked for.

**Self-check (objective rubric):** your spec-driven run is sound when **all** hold:

- [ ] Requirements are **testable acceptance criteria with stable IDs**, describing *behavior/
      constraints*, not implementation — and they **decide** the ambiguous cases (cycles, cross-project,
      the blocked-completion error, blocker deletion).
- [ ] The phases were produced **in order with a real gate** — you reviewed and approved requirements
      *before* design existed, and design *before* tasks. (You didn't generate all three at once.)
- [ ] **Traceability holds both ways:** every design choice and task names a requirement it serves, and
      every requirement has at least one design element + task. No orphans either direction.
- [ ] The implementation **satisfies the requirements**, with tests that mirror the acceptance criteria;
      `pytest` is green.
- [ ] Nothing was built that **no requirement asked for** (scope creep is visible as an untraceable
      diff).

**Reference:** there's no `solution/` branch — the artifact is *your* spec-and-process, and the rubric
is how you grade it. For the *shape* of each artifact, compare against this repo's own
[`requirements.md`](../../../specs/claude-code-mastery/requirements.md) /
[`design.md`](../../../specs/claude-code-mastery/design.md) /
[`tasks.md`](../../../specs/claude-code-mastery/tasks.md) — scaled down, your three should rhyme with
those three.

## Common pitfalls

- **Generating all three phases in one shot.** The most common way to "do spec-driven development" and
  get none of its value: ask for requirements+design+tasks at once, skim, and start coding. You reviewed
  nothing. The gates are the product.
- **Requirements that are really implementation.** "Add a `blocked_by` column" pre-decides the design.
  Write the *behavior* ("a task SHALL NOT be completable while a blocker is open") and let design choose
  the column.
- **Untraceable design.** A design choice that serves no requirement is scope creep; a requirement with
  no design is unbuilt. If you can't draw the line both ways, the spec isn't done.
- **Spec-driving a trivial change.** Three phases for a one-line fix is bureaucracy that teaches people
  to resent the process. Match the ceremony to the cost-of-wrong; small/obvious → **Ship a feature**'s plan mode.
- **Letting the build silently diverge from the spec.** If implementation teaches you the spec was
  wrong (it happens), *update the spec* and re-approve — don't just drift, or the traceability you built
  becomes a lie.

## Going deeper

- **Next:** **Code & security review** is how a reviewed spec's implementation gets a final
  correctness/security pass before merge; together these three are the Force-Multiplier disciplines —
  rescue (refactor), build-right (spec), and gate-before-merge (review).
- [`meta/workflows.md`](../../../meta/workflows.md#w7--spec-driven-development) — generalized spec-driven
  development, the heavyweight cousin of [Ship a feature](../05-ship-a-feature/unit.md)'s explore→plan→code.
- The whole [`specs/claude-code-mastery/`](../../../specs/claude-code-mastery/) tree — the dogfooded
  worked example; start at
  [`IMPLEMENTATION.md`](../../../specs/claude-code-mastery/IMPLEMENTATION.md), as every session here does.
- **A post-v1 enhancement, built the same way.** The course's own
  [CLI reference](../../reference/cli-reference.md) was added *after* v1 by running this exact chain — a
  new requirement, a [`design.md`](../../../specs/claude-code-mastery/design.md) §12 that traces to it,
  an ordered [task plan](../../../specs/claude-code-mastery/tasks/P8-cli-reference.md), then the
  generator that implements it. Proof the gates-and-traceability discipline scales to real, incremental
  work — not just greenfield.
- The phase-gate discipline is the same one in this repo's [`CLAUDE.md`](../../../CLAUDE.md) working
  agreements; the build-against-spec step reuses [Ship a feature](../05-ship-a-feature/unit.md)'s loop.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
