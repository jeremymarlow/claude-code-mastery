<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Package a repeatable routine as a custom command and a skill

# Package a repeatable routine as a custom command and a skill

*Reading: ~11 min · Lab: ~20 min · Prerequisites: [Steer Claude with project memory and deliberate context](../04-memory-and-context/unit.md)*

## Learning objectives

By the end of this unit you can:

- **Turn a routine you keep hand-typing into a custom slash command** — a saved, argument-taking
  prompt you trigger with `/name` — so the routine is one keystroke instead of a paragraph.
- **Package a structured, reusable capability as a skill** — a named `SKILL.md` whose *description*
  tells Claude when it applies — so the capability is available across tasks, not retyped per session.
 
- **Choose correctly between the two** — reach for a command when *you* deliberately trigger a prompt,
  and a skill when a multi-step capability is worth naming and letting Claude recognize.
- **Scope each one deliberately** — project (`.claude/`, committed, shared) vs. personal (`~/.claude/`),
  the same source distinction you met for settings in [Memory & context](../04-memory-and-context/unit.md).

## Fast path (TL;DR)

> Stop re-typing the same prompt. A **custom slash command** is a saved prompt in a markdown file
> under `.claude/commands/` — its filename becomes `/name`, and it can take arguments.
> A **skill** is a packaged capability in `.claude/skills/<name>/SKILL.md` with a `name` + a
> `description` that lets Claude pull it in when it fits. Rule of thumb: a prompt *you*
> trigger on demand → command; a structured capability worth naming and reusing across tasks → skill.
> This repo ships both as worked examples — `/close-unit` (command) and `prime-context` (skill). The lab has
> you build one of each against `taskflow-api`; the self-check is a checklist on the two artifacts.

## Skip-check

**Skip this unit if you can already:** take a routine you repeat by hand and package it two ways — as a
custom slash command (a saved, argument-taking prompt you invoke with `/name`) and as a skill (a named
`SKILL.md` with a when-to-use description Claude can act on) — and explain which form fits which routine
and why, rather than re-typing the same instructions into every session.

## Concept

Up to here you've been *typing* every instruction. The Autonomy stage is about the opposite move:
**packaging** work so a routine you've proven runs again without re-deriving it. The two lightest-weight
packages are the subject of this unit — custom **commands** and **skills**. Both kill repetitive
prompting; they differ in how they're triggered and how much structure they carry.

**1 — A custom slash command is a saved prompt.** It's a markdown file under `.claude/commands/`; the
filename is the command, so `close-unit.md` becomes `/close-unit`. Invoking it expands the file's contents
into the conversation exactly as if you'd typed them — including any arguments you pass (`$ARGUMENTS` for
the whole string, or by position — and positions are 0-based, so `$0` is the *first* argument, `$1` the
second). That's the whole model: a *prompt template you trigger deliberately*. Reach for a command
when you catch yourself re-typing the same paragraph — a scaffolder, a "draft release notes from the
diff," a "review this against our checklist" pass. The invocation and argument syntax is the
version-specific part:

> **Version surface (commands):** Custom slash commands are user-defined skills, invoked as /name (file `.claude/commands/<name>.md` becomes `/<name>`); `--disable-slash-commands` turns all skills off. Arguments: `$ARGUMENTS` expands to the full argument string; positional access is 0-based — `$0` is the first argument, `$1` the second (shorthand for `$ARGUMENTS[N]`); declare named args via an `arguments:` frontmatter list for `$name` substitution. Gotcha: `$1` is the SECOND arg, not the first — a single-arg command must use `$ARGUMENTS` or `$0`.

**2 — A skill is a packaged capability Claude can reach for.** It's a `SKILL.md` under
`.claude/skills/<name>/`, with front matter carrying a `name` and — critically — a `description`. You
can still invoke it explicitly (`/skill-name`), but the description is what lets Claude recognize *when
the skill applies* and pull it in on its own. Reach for a skill when a routine has enough structure to
be worth naming: several steps, conditions, references to specific tools or files — a capability you
want available across many tasks rather than triggered by one keystroke.

> **Version surface (skills):** Skills resolve via /skill-name; reusable packaged capabilities.

**3 — Choosing between them.** Same goal — stop re-typing — so the line is about *trigger* and
*structure*:

- **Command** when the routine is a *prompt you fire on demand*, usually with an argument. Lightest
  weight: it's literally a prompt with placeholders. You decide exactly when it runs.
- **Skill** when the routine is a *capability worth a name and a when-to-use description*. Slightly more
  structure, and Claude can surface it for you when the situation matches the description. The
  description is the skill's most important line — a vague one means Claude never recognizes the moment.

Don't agonize: many routines work as either, and the cost of picking "wrong" is small. The mistakes that
actually bite are packaging a routine you *don't* repeat (over-automation) and writing a skill with a
description so vague it never fires.

**4 — Scope: project vs. personal.** Both live in `.claude/` (project-scoped — committed to the repo,
shared with everyone who clones it) or `~/.claude/` (personal — your habits across every project). This
is the same source distinction you met for `settings.json` in [Memory & context](../04-memory-and-context/unit.md):
put a command/skill the *team* should have in the project; keep your personal shortcuts in `~/.claude/`.
A team scaffolder committed to `.claude/commands/` means every contributor scaffolds the same way — that
is exactly why *this* repo commits `close-unit` and `prime-context`.

**Version currency.** Verified against Claude Code `2.1.170`. The on-disk locations
(`.claude/commands/`, `.claude/skills/<name>/SKILL.md`) are filesystem **conventions** — confirm the
exact paths and the invocation/argument syntax against `claude --help` and the docs before relying on a
detail. Commands: custom slash commands (`.claude/commands/<name>.md` becomes `/<name>`) Skills: Skills resolve via /skill-name; reusable packaged capabilities. Tracked in
[`meta/version-record.md`](../../../meta/version-record.md).

## Worked example

This repository carries one of each, and they are the real tools used to build the course — read them
as your templates (`cat` them as you follow along).

**The skill — [`.claude/skills/prime-context/SKILL.md`](../../../.claude/skills/prime-context/SKILL.md).**
Its front matter is two lines that do the work: `name: prime-context`, and a `description` that names
*when* to use it — "at the start of a fresh session, before any other work, whenever you start or
resume a session on this repo." That description is the trigger, and a sharp one: a fresh session is a
crisp, recognizable situation, so Claude can reach for the skill the moment a session opens rather than
waiting to be told. The body is the structured part a bare prompt wouldn't carry well — read the spec
in its canonical order (IMPLEMENTATION §3 live status, then the open-loops ledger), check git state,
then report a tight "where we are / what's next." It's a *capability* ("orient on this project"), named
and described so it can fire on a situation — which is what makes it a skill rather than a one-off
prompt.

**The command — [`.claude/commands/close-unit.md`](../../../.claude/commands/close-unit.md).** Here is
its actual head, so you can see how little ceremony a command needs:

**Captured** — `.claude/commands/close-unit.md` (first lines):

```text
---
description: Sync every project state file after a unit's prose is authored, then run the checks
argument-hint: <NN>
---

Close out unit **U$0** — bring every state-tracking file in sync now that
`course/units/$0-*/unit.src.md` is authored ..., then verify. Pull specifics
from the files, not memory; follow `meta/conventions.md`.
```

Its front matter is a `description` and an `argument-hint: <NN>`. The body is a prompt that uses that argument
(`$0` — the first positional argument; `$1` would be the *second*) and walks Claude through the chore of
*closing out a finished unit*: update `IMPLEMENTATION.md`
§3, check the `tasks.md` box and its detail bullet, add the `decisions.md` rationale + refresh the
open-loops ledger, verify version currency, and run `make check`. You run it deliberately —
`/close-unit 13` the moment that unit's prose is done — and it expands into that checklist. It's a *prompt you
trigger*, with an argument, so it's a command, not a skill. (It's the real state-sync routine used to
land every unit in this course — authentic dogfooding.)

Side by side: the skill is named and self-describing so Claude can pull it in; the command is a saved
prompt you fire on demand with arguments. Same intent — never type the routine again — different
trigger. Note that `prime-context` sits closer to the line than a mid-task skill would: *you* usually
type it at session start, which is command-shaped. It earns "skill" because its whole reason to exist is
a recognizable **situation** (a session opening) that a description can name — and naming a situation so
Claude can act on it is exactly what a skill is for. When a routine could honestly be either, classify
it by its primary trigger: a fixed prompt you fire → command; a capability tied to a situation → skill.

## Lab

> **This lab has no automated verifier.** Whether a command or skill is *good* is a judgment call, and
> the artifacts you produce live in your own `.claude/`. So the self-check is an objective
> checklist you apply to what you built, with this repo's `close-unit` / `prime-context` as the reference
> patterns to compare against.

**Goal:** take two routines you'd otherwise hand-type while working in `taskflow-api` and package each
in the form that fits — **one custom command and one skill** — so each runs without re-typing, and so
you can say *why* each took the form it did.

**Starting state:** the clean primary codebase. `cd codebases/primary/taskflow-api`; create your
artifacts under that project's `.claude/` so they're scoped to it (nothing here is pushed for you).

**Build these two:**

1. **A custom command** — a *prompt you trigger*, with at least one argument. Suggested:
   `/scaffold-route <name>` → a saved prompt that scaffolds a new FastAPI route + schema + a test stub
   following `taskflow-api`'s existing conventions, for the resource you name. Put it in
   `.claude/commands/scaffold-route.md` and invoke `/scaffold-route reports`.
2. **A skill** — a *named capability with a when-to-use description*. Suggested: `api-test-triage` →
   runs `pytest`, and when something fails, summarizes which tests broke and the likely cause. Put it in
   `.claude/skills/api-test-triage/SKILL.md`; write the `description` so it states the situation
   ("after editing the API, to confirm the suite is green and triage failures") — specific enough that
   Claude would reach for it on its own.

**Steps:**

1. Pick the two routines (the suggestions above, or two of your own you genuinely repeat).
2. For each, decide *command or skill first* — is this a prompt I fire on demand (command), or a named
   capability worth a when-to-use description (skill)? Write down the reason.
3. Author the files. Lean on the two repo artifacts as templates; don't author the front-matter or
   invocation format from memory — check the current convention against `claude --help`.
4. Run each: invoke `/scaffold-route ...`, and trigger the skill, and confirm each produces the routine's
   outcome with less typing than doing it by hand.

**Self-check (objective checklist):** you're done when **all** hold:

- [ ] The command file exists under `.claude/commands/`, and invoking `/name` expands its prompt; it
      takes **at least one argument** and uses it.
- [ ] The skill exists at `.claude/skills/<name>/SKILL.md` with a `name` and a `description` that states
      **when** to use it (not just what it does) — specific enough that Claude could surface it unasked.
- [ ] Each genuinely **replaces a routine you were hand-typing** — running it yields the same outcome
      with materially less typing.
- [ ] You can **articulate why each is a command vs. a skill** (on-demand prompt + arguments → command;
      named, described, reusable capability → skill) — not a coin flip.
- [ ] Neither **hardcodes a version-specific value**; both reference `taskflow-api`'s own
      files/conventions rather than restating them, and version-specifics are confirmed against
      `claude --help` rather than baked in.

**Reference:** there's no `solution/` branch — the artifacts are *yours*. The repo's
[`close-unit`](../../../.claude/commands/close-unit.md) and
[`prime-context`](../../../.claude/skills/prime-context/SKILL.md) are the reference patterns; compare your two
against them and the checklist above.

## Common pitfalls

- **Building a "skill" that's really a command (or vice-versa).** A `SKILL.md` with no when-to-use
  description is just a prompt in the wrong place; a command that needs Claude to *recognize* when to run
  it wants to be a skill. Decide on trigger + structure first, then pick the form.
- **A vague skill description.** "Helps with tests" never fires — Claude can't match it to a moment.
  Name the *situation* ("after editing the API, to confirm the suite is green") so the description earns
  its keep.
- **Automating a routine you don't actually repeat.** Packaging a one-off costs more than it saves and
  rots. Package what you've typed three times, not what you might type once.
- **Hardcoding what should be an argument or a project reference.** A command that bakes in one resource
  name, or restates conventions instead of pointing at the code, only works for the case you wrote it
  for. Parameterize; reference the source.
- **Authoring the format from memory.** Front-matter fields, argument syntax, and on-disk paths are the
  version-specific surface — copy the working repo artifacts and confirm against `claude --help` rather
  than trusting recall.
- **Scope confusion.** A personal shortcut committed to project `.claude/` gets pushed onto the whole
  team; a team scaffolder left in `~/.claude/` never reaches them. Decide project vs. personal on
  purpose ([Memory & context](../04-memory-and-context/unit.md)).

## Going deeper

- **Next:** the rest of the Autonomy stage extends "package the work." **Subagents** delegates a
  scoped task to a subagent; **Hooks** automates enforcement with hooks — and this repo's own
  `make check` suite is that unit's worked example; **Automate & scale** runs these packaged routines
  headlessly and in parallel.
- **Scope & sources** — project vs. personal `.claude/` is the same distinction as settings sources in
  [Memory & context](../04-memory-and-context/unit.md).
- The invocation, argument, and resolution surfaces: custom slash commands (`.claude/commands/<name>.md` becomes `/<name>`) Skills resolve via /skill-name; reusable packaged capabilities.
  Version-specifics in [`meta/version-record.md`](../../../meta/version-record.md). Confirm with
  `claude --help`.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
