<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U13
title: "Delegate a scoped task to a subagent"
stage: autonomy-scale
depth_tier: core
use_case: "Delegate focused / parallel sub-tasks"
can_do: [C14]
workflows: []
coverage_areas: [19]
prerequisites: [U12]
reading_time_min: 13
lab_time_min: 20
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Delegate a scoped task to a subagent

# Delegate a scoped task to a subagent

## Learning objectives

By the end of this unit you can:

- **Hand a self-contained task to a subagent and use the result it returns** — a separate Claude
  instance, with its own context window, that does the work and reports back a conclusion rather than
  its whole transcript.
- **Recognize when delegation pays off** — a context-heavy exploration you don't want polluting your
  main thread, two independent tasks worth running in parallel, or work worth fencing to a restricted
  toolset.
- **Scope a task so a subagent can finish it without you** — a crisp, self-contained brief with a
  defined deliverable, distinct from a routine you reuse in your own context (a skill, [Commands & skills](../12-commands-and-skills/unit.md)).
- **Verify what comes back** — a subagent returns a conclusion you didn't watch it derive, so you
  check the result against the code instead of trusting that an agent ran.

## Fast path (TL;DR)

> A **subagent** is a second Claude the main session spins up to handle one scoped task. It has its
> **own context window** and can be given its **own restricted tools** — it does the work and returns a
> *result* (a summary, an answer, a diff), not its entire transcript. You delegate for three reasons:
> **context isolation** (its 30-file search stays in *its* context, only the conclusion lands in
> yours), **parallelism** (independent tasks run at once), and **fencing** (a read-only explorer can't
> write). Define a custom agent inline with `--agents <json>` or as a file under `.claude/agents/`,
> each with a `description` that tells the main agent when to reach for it. The
> catch: delegation is *trust delegation* — **verify the result**, don't merge a diff or quote a claim
> you didn't check. The lab has you fence a read-only explorer, delegate a real mapping task on
> `taskflow-api`, and spot-check what it returns.

## Skip-check

**Skip this unit if you can already:** hand a self-contained task to a subagent — a separate Claude
instance with its own context window and (optionally) a restricted toolset — choosing to do so because
the work is context-heavy, parallelizable, or worth fencing; scope the brief so it finishes without
back-and-forth; and verify the returned result against the code rather than trusting that the agent
ran. If that's already habit, skim the pitfalls and move on.

## Concept

[Commands & skills](../12-commands-and-skills/unit.md) packaged a routine so you stop re-typing it. A subagent is the
next move in the Autonomy stage: instead of *reusing a prompt in your own context*, you **hand a whole
task to a separate Claude and use what it gives back**.

**1 — What a subagent is.** When the main session delegates, it starts a *fresh* Claude instance with
its **own context window**, its own instructions, and (optionally) its own restricted set of tools and
permissions. That instance works the task on its own and returns a **result** — a summary, an answer, a
patch — to the main session. The key word is *separate*: the subagent's work happens in its context,
not yours, and only the conclusion crosses back. You are not watching it think; you are receiving its
report.

**2 — Why delegate.** Three distinct payoffs, and you should be able to name which one you're after:

- **Context isolation.** Answering "where is ownership enforced across this API?" might mean reading
  thirty files. Do that in your main session and those thirty files are now wedged in your context
  window, crowding out the actual work. Delegate it and the reading happens in the subagent's context —
  only the *answer* (file:line list + a sentence) returns. This is the highest-value reason in a long
  session: it keeps your main thread clean.
- **Parallelism.** Independent scoped tasks can run at the same time — map three subsystems at once
  rather than one after another — which is wall-clock faster.
- **Fencing (blast radius).** A subagent can be handed a *narrower* toolset than your session has: a
  read-only explorer that literally cannot edit or run destructive commands. That's the
  [Operate safely](../03-operate-safely/unit.md) blast-radius discipline applied to delegation — give the helper
  only the tools its task needs.

**3 — How it works in Claude Code.** The main agent invokes a subagent through its task/agent tool;
you rarely call it by hand, you *describe a task* and let the main agent dispatch it. You can define
**custom** agents two ways: inline for a session with `--agents <json>` (the `--help` example is
`{"reviewer": {"description": "Reviews ..."}}`), or persistently as a file under `.claude/agents/`. A
file-form agent's front matter needs a **`name`** (its identity — *not* the filename) and a
**`description`** (*when* the main agent should reach for it), plus optionally an allowed-tools list and
a model. **Tools are opt-out, not opt-in:** omit the tools list and the agent **inherits every tool the
main session has** — so fencing a read-only helper means naming its tools explicitly (`Read`, `Grep`,
`Glob`), never just leaving them off. The `description` is the trigger, exactly as it was for a skill in
[Commands & skills](../12-commands-and-skills/unit.md): vague description, never dispatched at the right moment;
sharp description naming the situation, picked up when it fits. Background/dispatched agents are managed
with the `agents` subcommand. The version-specific surface is the flags, the subcommand, and the on-disk
format: `--agent <agent>` / `--agents <json>` set session agents; the `agents` subcommand manages background agents.

**4 — Subagent vs. skill.** Both package work; they differ in *where the work runs*:

- A **skill/command** ([Commands & skills](../12-commands-and-skills/unit.md)) expands into **your** context — it's a
  reusable prompt or capability you run in the session you're in.
- A **subagent** runs the work in a **separate** context and hands back a result.

So reach for a subagent when the task is **context-heavy** (lots of reading you don't want in your main
thread), **parallelizable** (independent of what you're doing), or **worth fencing** (should run with
fewer tools than you hold). Reach for a skill when you just want to reuse a prompt right here. A useful
tell: if you mostly care about the *answer* and not the steps, delegate; if you want the work done
*in front of you* in the current thread, don't.

**5 — Delegation is trust delegation.** The subagent returns a conclusion you didn't watch it reach.
That makes verification non-optional: a returned diff gets **read** before it's kept; a returned claim
("ownership is checked in all five mutation routes") gets **spot-checked** against the code. "An agent
ran and reported success" is not verification — it's the thing you verify. This is the same
verify-don't-trust habit from [Operate safely](../03-operate-safely/unit.md), and it's the bridge to the trust
question you'll face again when you delegate to *third-party* code (MCP servers) later in this stage.

**Version currency.** Verified against Claude Code 2.1.159. The inline `--agents`
flag, the `--agent` selector, and the `agents` subcommand are `--help`-verified; the persistent
on-disk location (e.g. `.claude/agents/<name>.md`) and its front-matter fields are a filesystem
**convention** — confirm the exact path and format against `claude --help` and the docs before relying
on a detail. `--agent`/`--agents <json>` plus the `agents` subcommand Tracked in [`meta/version-record.md`](../../../meta/version-record.md).

## Worked example

Here is a delegation worth making on `taskflow-api`: *"Across the whole codebase, where is a request's
ownership of a project or task actually enforced? Give me the file:line of each check and one line on
what it guards."* That's a genuinely context-heavy question — the honest way to answer it is to read
the services, the routes, and the dependency wiring. You do **not** want all of that reading sitting in
your main context if your real job today is adding a feature.

So you fence a read-only explorer and hand it the task. Inline, that's the verified `--agents` shape:

```json
{
  "explorer": {
    "description": "Read-only codebase mapper. Use to answer 'where/how is X done across the code?' without polluting the main context. Returns file:line citations + a one-line note each; never edits.",
    "tools": ["Read", "Grep", "Glob"]
  }
}
```

The same agent kept around for reuse lives as a file under `.claude/agents/explorer.md` (the on-disk
**convention** — confirm the path/front-matter against the docs), with that
`description` as its front matter and any standing instructions in the body.

Two things make this a *good* delegation, and they map straight onto the concept:

- **The toolset is fenced to the task.** `explorer` gets `Read`/`Grep`/`Glob` and nothing that writes.
  Even if the task drifted, it *cannot* change the codebase — blast radius designed to zero
  ([Operate safely](../03-operate-safely/unit.md)).
- **The brief is self-contained with a defined deliverable.** "file:line of each ownership check + one
  line each" is a crisp finish line. The subagent doesn't need to come back and ask you anything; it
  can run to completion on its own. That's the difference between a task you can delegate and one you
  can't.

What returns is a short report — say, `app/services/projects.py:41 get_project enforces owner_id`,
`app/services/tasks.py:33 …`, and so on — costing your main context a dozen lines instead of a dozen
files. **Then you verify**: open *two* of the cited lines and confirm the check is really there and
really guards what the note claims. You're not re-reading everything — you're spot-checking the
conclusion you were handed, because a confident summary of code that isn't there is exactly the failure
mode delegation can hide.

(The built-in agent types your CLI ships — a read-only explorer, a planning agent — are the same idea
pre-packaged; defining your own, as above, is how you fence and brief one for *your* task. Confirm what
ships with `claude --help`.)

**A real panel in this repo.** The `explorer` above is illustrative; for a genuine, in-use example this
course ships a **panel of 11 subagents** under [`.claude/agents/`](../../../.claude/agents/) — ten
critique "personas" plus a lens-free control — that read this build's own session transcripts and each
write one independent evaluation (the [collaboration retrospective](../../case-studies/collaboration-retrospective.md)
is what they produced). Open one: it's a `.claude/agents/<id>.md` with `name` + `description` front
matter and an explicit `tools` line — the file form your lab needs. It also corrects a tempting
half-truth about fencing: **least-privilege means *the tools the job needs*, not "always read-only."**
The reviewers began pure read-only (`Read`, `Grep`, `Glob`); they were then **deliberately** widened to
add a single scoped `Write` — still no Bash, no edits, no network — once it was clear each reviewer
should persist its own one-file verdict instead of routing it back through the main session. That is the
rule done honestly: the *minimum* toolset the task needs, widened on purpose and for a stated reason —
not a reflexive label.

## Lab

> **This lab has no automated verifier.** The artifact you produce — a subagent definition — lives in
> your own `.claude/`, and whether a delegation is *well-scoped* is a judgment call, not a diff.
> So the self-check is an objective checklist you apply to what you built and to the
> result you got back, with the worked example's `explorer` as the reference pattern.

**Goal:** define a **scoped, read-only subagent**, delegate a real context-heavy task to it against
`taskflow-api`, use the result it returns, and **verify that result** against the code — so you can say
*why* the work belonged in a subagent rather than inline or in a skill.

**Starting state:** the clean primary codebase. `cd codebases/primary/taskflow-api`; create your agent
definition under that project's `.claude/` (e.g. `.claude/agents/explorer.md`) so it's scoped to the
project. Confirm the path and front-matter format against `claude --help`/the docs rather than
authoring it from memory. **One operational catch:** an agent file written directly to disk may not be
dispatchable until the session *loads* it — start a fresh session (or use the in-session `/agents` flow)
after creating the file, the same reload caveat hooks have. Confirm the current behavior against the docs.

**Steps:**

1. **Define the agent.** Write a read-only explorer: a `description` that states *when* to use it
   (specific enough that the main agent would pick it for a "where/how is X done?" question) and a
   toolset restricted to reading/searching — no edit or run-destructive tools. Lean on the worked
   example as your template.
2. **Pick a context-heavy task and write the brief.** Something whose honest answer means reading
   several files — e.g. *"List every place pagination/sorting is applied to a list endpoint:
   file:line + the parameter that controls it,"* or *"Map the auth flow from login to a protected
   route: each hop, file:line."* Make the deliverable crisp so the subagent can finish without asking
   you anything.
3. **Delegate it** and let the subagent run in its own context. Note what comes back: a short
   result, not the files it read.
4. **Verify the result (the required step).** Open **at least two** of the cited locations and confirm
   each claim holds — the line exists and does what the report says. If a citation is wrong or vague,
   that's the finding; the report was a *lead*, not a verdict.
5. **(Optional stretch — parallelism.)** Give the explorer two *independent* briefs at once (e.g. map
   pagination **and** map the auth flow) and notice they can proceed in parallel because neither needs
   the other's output. Dependent tasks can't — that's the boundary of "parallelizable."

**Self-check (objective checklist):** you're done when **all** hold:

- [ ] The agent is defined with a `description` that states **when** to use it (a situation the main
      agent could match), and a **read-only toolset** appropriate to the task — it cannot edit or run
      destructive commands.
- [ ] The task you delegated was **self-contained with a defined deliverable** — the subagent finished
      without needing to ask you a follow-up.
- [ ] You **used the returned result** (the conclusion came back to your main session; you didn't have
      to re-do the work yourself).
- [ ] You **verified the result** — opened ≥2 cited locations and confirmed each claim against the
      code, treating the report as a lead rather than trusting it on faith.
- [ ] You can **articulate why this was a subagent** — context-heavy, parallelizable, and/or worth
      fencing — rather than a skill (reuse a prompt in your own context) or just doing it inline.
- [ ] Nothing in the definition **hardcodes a version-specific format from memory** — the path and
      front-matter were confirmed against `claude --help`/docs.

**Reference:** there's no `solution/` branch — the agent is *yours*. The worked example's `explorer`
definition above is the reference pattern; compare your definition and your verification step against it
and the checklist.

## Common pitfalls

- **Delegating work you need to watch.** If the *reasoning* matters to you — a subtle design call, a
  risky change — running it in a subagent hides exactly what you wanted to see. Delegate when you care
  about the *result*; keep it inline when you need to follow the steps.
- **A vague agent description.** Same failure as a vague skill ([Commands & skills](../12-commands-and-skills/unit.md)):
  "helps explore code" never gets dispatched at the right moment. Name the *situation* the agent is for
  so the main agent can match it.
- **Trusting the result because an agent ran.** "It came back green / it said it's done" is not
  verification — read the returned diff, spot-check the returned claim. A confident summary of code
  that isn't there is the delegation-specific way to get burned.
- **An unscoped brief.** A task that needs back-and-forth ("explore the code and let me know what you
  find, then we'll decide") can't be delegated cleanly — the subagent stalls or guesses. Give it a
  finish line it can reach alone.
- **Over-broad tools / permissions.** Handing a subagent edit or bypass permissions it doesn't need
  widens blast radius for no reason ([Operate safely](../03-operate-safely/unit.md)). Fence it to the tools its
  task requires — read-only for an explorer. Watch the default: **omitting** the tools list inherits
  *every* tool, so fence by naming tools explicitly, not by leaving them off.
- **"Parallelizing" dependent tasks.** Two subagents only run in parallel if neither needs the other's
  output. If task B consumes task A's result, it isn't parallel — it's a sequence.
- **Authoring the agent format from memory.** The flags, the subcommand, and the on-disk path/front
  matter are the version-specific surface — confirm against `claude --help` and the docs rather than
  trusting recall.

## Going deeper

- **Next in the Autonomy stage:** **Hooks** automates *enforcement* — and this repo's own `make check`
  suite is its worked example; **MCP & vetting** extends today's trust-delegation lesson to
  *third-party* tools you connect and must vet before relying on; **Automate & scale** runs delegated
  work headlessly and across parallel worktrees.
- **Subagent vs. skill/command** — the form distinction is the [Commands & skills](../12-commands-and-skills/unit.md)
  line: reuse a prompt in your own context (skill/command) vs. run a task in a separate context and use
  its result (subagent).
- **Fencing & verifying delegation** builds directly on [Operate safely](../03-operate-safely/unit.md) (blast
  radius, verify-don't-trust).
- The flags, `agents` subcommand, and on-disk format: `--agent`/`--agents <json>` plus the `agents` subcommand Version-specifics in
  [`meta/version-record.md`](../../../meta/version-record.md). Confirm with `claude --help`.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
