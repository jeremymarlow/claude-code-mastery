<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U4
title: "Steer Claude with project memory and deliberate context"
stage: first-wins
depth_tier: core
use_case: "Make Claude reliably follow my project's conventions"
can_do: [C5]
workflows: []
coverage_areas: [7, 8, 26, 28]
prerequisites: [U1]
reading_time_min: 9
lab_time_min: 18
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md)

# Steer Claude with project memory and deliberate context

## Learning objectives

By the end of this unit you can:

- **Write and place a `CLAUDE.md` that measurably changes how Claude behaves on a task** — encode a
  project's conventions once and have Claude follow them.
- **Treat the context window as a managed resource** — inspect what's loaded, select what's relevant,
  and clear what isn't.
- **Locate where settings live** (project vs user) and recognize that the permission rules from **Operate safely**
  are configured here.
- **Verify that your memory/context change actually took effect** before trusting the behavior change —
  the cross-cutting verification (CV) reflex applied to configuration.

## Fast path (TL;DR)

> Two levers steer Claude beyond the words you type. **(1) Project memory** — a short, true
> `CLAUDE.md` that's auto-loaded so Claude knows your conventions without being told each time.
> **(2) Context** — the finite window of what Claude can currently see; more isn't better, *relevant*
> is. Inspect it, select into it (`@`-mentions, from **Explore a codebase**), and clear it when you switch tasks. The lab
> has you change one line of `CLAUDE.md` and watch Claude's answer change — then confirm via the
> context inspector that your file is actually loaded.

## Skip-check

**Skip this unit if you can already:** write a `CLAUDE.md` that reliably makes Claude follow your
project's conventions, place it where it'll actually load (and confirm it did), and manage the
context window deliberately — selecting what's relevant and clearing what isn't — rather than hoping
more context helps.

## Concept

You've now driven a change, explored code, and operated safely. What you haven't done
yet is make Claude *reliably yours* — follow your conventions without being re-told every session.
That's two distinct levers, and conflating them is the usual mistake: **memory** is what Claude knows
by default; **context** is what Claude can see right now.

**1 — Project memory (`CLAUDE.md`).** Project memory via CLAUDE.md, auto-discovered at startup (auto-memory). A `CLAUDE.md` is a file Claude auto-discovers and
loads as standing instructions — your project's conventions, architecture, and gotchas, stated once.
The baseline you were handed in your first unit (`codebases/primary/taskflow-api/CLAUDE.md`) is a working example;
this unit is where you learn to *shape* one. The principles are what matter, and they're version-
independent:

- **Short and true beats long and aspirational.** Memory is loaded into every session's context, so
  every line costs attention and tokens. A tight file of real conventions outperforms an essay. A
  line that's *false* (says tests are `pytest` after they moved) is worse than no line — it actively
  misleads. **Treat `CLAUDE.md` like code:** keep it current, or delete the stale part.
- **Encode decisions, not documentation.** "New domain logic goes in `app/services/`, not routers" is
  worth a line because it changes what Claude *does*. A restatement of what the framework already
  makes obvious is not.
- **Memory is layered.** Project memory (committed, shared with the team) is distinct from your
  personal/user memory (your machine, your habits). Put team conventions in the project file so
  everyone — and every session — gets them.

> **This course dogfoods it:** the repo's own root
> [`CLAUDE.md`](../../../CLAUDE.md) *is* the project memory used to build this course, and it's
> deliberately short — what the repo is, how it's organized, the working agreements. Read it as a
> real specimen, not a toy.

**2 — Context is a finite, managed resource.** The context window is everything Claude can see at this
moment: the system prompt, your `CLAUDE.md`, the files and output pulled in this session, and the
conversation so far. Two consequences:

- **More context is not better context.** Dumping the whole repo "to be safe" crowds out the few
  files that matter and degrades answers. **Select deliberately:** anchor with `@`-mentions,
  start from the right directory, and don't drag in what the task doesn't need.
- **Inspect and reset it.** In-REPL slash commands: /context, /compact, /clear (inspect and manage the context window). You can see what's currently loaded, compact a long
  session, or clear it to start clean when you switch tasks. A session that's been wandering for an
  hour is carrying a lot of irrelevant context — clearing it is often the fastest fix for "Claude
  seems confused."

**3 — Settings (`settings.json`) — where config (incl. permissions) lives.** `--settings <file-or-json>` loads settings; `--setting-sources user,project,local` selects which sources load. The
permission allow/deny rules you *chose* postures for in **Operate safely** are *configured* here. The baseline
[`.claude/settings.json`](../../../codebases/primary/taskflow-api/.claude/settings.json) in the
primary codebase auto-approves a few safe, routine commands — running the test suite, the DB seed
script, and the dev server — so lab work doesn't prompt on every step, while anything outside that
allow-list still goes through the permission gate. Settings resolve from more than one source
(project vs user); project settings are committed and shared, so put team-wide rules there.
*(Enterprise/managed settings can override these — see **Operate safely**.)*

> **Awareness — output styles.** Claude's response style/verbosity is itself configurable:
> Output styles customize Claude's response behavior: the Default (standard SWE system prompt) plus three built-in styles — Proactive (acts immediately, prefers action over planning), Explanatory (adds educational 'Insights'), and Learning (collaborative; adds TODO(human) markers for you to implement). Select via `/config` -> Output style (saved to `.claude/settings.local.json`), or set the `outputStyle` settings field directly. Useful to know it exists; not something this course drills.

**4 — Verify the change took effect (CV).** Memory and context edits are *changes*, and the unit's
through-line applies: don't assume, confirm. The classic failure is editing the *wrong* `CLAUDE.md`
(your user file instead of the project file, or the wrong repo) so it never loads — and then puzzling
over why Claude "ignored" it. Before you trust a behavior change, **inspect the context to confirm
your file is actually loaded.** That 10-second check is the difference between steering Claude and
imagining you are.

**Version currency.** This unit was verified against Claude Code `2.1.159`; the
context-management commands are in-REPL and may shift between releases — confirm them with `/help` and
see [`meta/version-record.md`](../../../meta/version-record.md) if your version differs.

## Worked example

The repo's root [`CLAUDE.md`](../../../CLAUDE.md) is the authentic specimen. Notice what it
does and doesn't do:

- It states **what the repo is** and **how it's organized** in a few lines, then points at the
  single-source-of-truth files (`meta/*`, the spec) rather than restating them — *"cross-cutting
  facts live once… reference it; don't inline."* That's context discipline encoded as memory.
- It records **working agreements** that change behavior ("never author a version-specific value from
  memory"; "keep state current") — decisions, not documentation.
- It's short. Every line earns its place in every session's context.

The codebase baseline ([`taskflow-api/CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md))
is the same idea scoped to one app: what it is, where logic lives, the services→exceptions→main
convention, how to run tests. When you ask Claude "where does this new logic go?", *that* file is why
it answers "the service layer" instead of guessing.

## Lab

**Goal:** prove to yourself that project memory **measurably** changes Claude's behavior — by changing
one line of `CLAUDE.md` and watching the answer change — and confirm the file is actually loaded.

**Starting state:** the clean primary codebase with its baseline `CLAUDE.md`
(`codebases/primary/taskflow-api/`). This lab makes a small, reversible edit to that `CLAUDE.md`;
restore it at the end with `git restore codebases/primary/taskflow-api/CLAUDE.md` (there's no code
change to reset).

**Steps:**

1. `cd codebases/primary/taskflow-api && claude` (plan mode is fine — this lab doesn't need to write
   code).
2. **Baseline behavior.** Ask: *"I want to add validation that a project's name can't be empty. Which
   layer does that belong in, and how should the error reach the client?"* A good answer cites the
   **service layer** + a **domain exception** mapped in `main.py` — because the baseline `CLAUDE.md`
   says so. Note how specific the answer is.
3. **Confirm the file is loaded (CV).** Inspect the loaded context and verify the
   project `CLAUDE.md` is actually present. This is the check most people skip.
4. **Change the memory.** Add one concrete, checkable convention to `CLAUDE.md`, e.g. under
   *Conventions*: *"Validation failures must raise the project's domain `ValidationError`; never raise
   `HTTPException` from a service."* Save it.
5. **Observe the behavior change.** Re-ask a related question (*"how should I signal a validation
   failure from a service?"*). Claude's answer now reflects your new rule. That shift — caused by one
   line you wrote — is the whole point of the unit.
6. **A/B to be sure (optional).** Temporarily comment the line out (or `/clear` and ask in a fresh
   session without it); the specific guidance disappears. Restore the file.

**Self-check (objective):** you pass if **(a)** you can point to the exact line in `CLAUDE.md` that
caused Claude's answer to change between steps 2/5 (and 6), and **(b)** you confirmed via the context
inspector (step 3) that the project `CLAUDE.md` was loaded. If the answer *didn't* change, the file
almost certainly isn't being loaded — recheck step 3 before concluding "memory doesn't work."

**Reference:** there's no `solution/` branch — the lab's artifact is a *behavior change*, not a diff
(your `CLAUDE.md` edit is reverted at the end). The reference is the reasoning above: a specific,
true, behavior-changing line, confirmed loaded.

**Verify (CV):** the load-bearing habit here is step 3 — **never trust that a `CLAUDE.md` edit took
effect without inspecting the context.** Editing the wrong file (user vs project) is the #1 reason
memory "doesn't work," and it's invisible unless you look.

## Common pitfalls

- **Editing the wrong `CLAUDE.md`.** Project vs user memory are different files; a change to one won't
  show up if Claude is loading the other. Confirm with the context inspector, not by faith.
- **Writing an essay.** A long `CLAUDE.md` dilutes the conventions that matter and burns context every
  session. Short, imperative, true. Cut anything the framework already makes obvious.
- **Letting memory go stale.** A `CLAUDE.md` that describes how the project *used* to work actively
  misleads Claude. Update it in the same change that breaks its assumptions — treat it like code.
- **Hoarding context.** Loading more files "to be safe" makes answers worse, not safer. Select what's
  relevant; `/clear` between unrelated tasks instead of letting one session accrete.
- **Assuming the change worked.** A behavior that didn't change usually means the file didn't load —
  diagnose that first, don't keep rewording the convention.

## Going deeper

- **Next:** **Ship a feature** puts this to work — a sharp `CLAUDE.md` plus plan mode is what makes
  the explore→plan→code→commit loop reliable. Everything from here assumes you can steer Claude with
  memory and context.
- [`CLAUDE.md`](../../../CLAUDE.md) (this repo's own) and [`meta/`](../../../meta/) — the living
  example of "facts live once, referenced not duplicated."
- The `@`-mention selection habit from [Explore a codebase](../02-explore-a-codebase/unit.md) is the
  context lever in miniature; the permission *postures* from [Operate safely](../03-operate-safely/unit.md)
  are configured in the `settings.json` discussed here.
- [`meta/version-record.md`](../../../meta/version-record.md) — where context/memory version-specifics
  are recorded if your CLI differs.
- **The exhaustive CLI reference.** Beyond the handful of version-specifics this course pins as
  version-data tokens, the *full* surface of `claude`'s commands and flags is generated once into
  [`meta/cli-reference.json`](../../../meta/cli-reference.json) — the machine single-source sibling of
  [`meta/version-data.yaml`](../../../meta/version-data.yaml) — and rendered for reading as the
  [CLI reference](../../reference/cli-reference.md). Same "facts live once" discipline: need a flag this
  course didn't drill? Look there rather than guessing.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
