---
id: U14
title: "Enforce a standard automatically with a hook"
stage: autonomy-scale
depth_tier: core
use_case: "Enforce my standards automatically"
can_do: [C15]
workflows: []
coverage_areas: [20]
prerequisites: [U12]
reading_time_min: 8
lab_time_min: 22
---

# Enforce a standard automatically with a hook

## Learning objectives

By the end of this unit you can:

- **Wire a hook that runs automatically on a lifecycle event** — a command the *harness* fires before
  or after a tool call (not something you or Claude choose to invoke), configured in `settings.json`.
 
- **Use the two moves a hook makes** — **block** an action that violates a standard (a `PreToolUse`
  hook that denies it) and **react** to one that already happened (a `PostToolUse` hook that formats,
  tests, or checks, and feeds failures back).
- **Choose a hook over a command/skill/subagent** — reach for a hook when something **must always** or
  **must never** happen, because only a hook is enforced deterministically rather than left to anyone's
  judgment.
- **Verify a hook actually fires** — drive it with a synthetic event payload and confirm it blocks or
  reacts as intended, instead of trusting that a config entry works.

## Fast path (TL;DR)

> A **hook** is a command Claude Code runs **for you, automatically, on a lifecycle event** —
> configured in `settings.json` as `hooks.<Event>: [{ "matcher": "...", "hooks": [{ "type":
> "command", "command": "..." }] }]`. The two you'll use most: **`PreToolUse`** (runs before a tool —
> can **block** the action) and **`PostToolUse`** (runs after — format, test, or check, and feed
> failures back). The hook reads the event as JSON on stdin (`tool_input.file_path`, …) and steers via
> its output ({{vd:hooks}}). The thing that makes a hook different from a command/skill/subagent: **the
> harness fires it deterministically** — it can't be forgotten — which is exactly why it's the tool for
> *guardrails and standards*. This repo's own `make check` suite runs as a `PostToolUse` hook (the
> worked example below); the lab has you wire and **prove** one in `taskflow-api`.

## Skip-check

**Skip this unit if you can already:** configure a `settings.json` hook on the right lifecycle event
(e.g. `PreToolUse` to block, `PostToolUse` to react), have it read the event payload and steer via exit
code / JSON output, choose a hook over a command/skill when a standard must be enforced automatically
rather than invoked, and verify it fires by driving it with a synthetic payload. If that's habit, skim
the worked example (it's this repo's real hook) and the pitfalls.

## Concept

The Autonomy stage so far has been about *packaging work you choose to run*: a command you fire
([Commands & skills](../12-commands-and-skills/unit.md)), a skill Claude reaches for ([Commands & skills](../12-commands-and-skills/unit.md)),
a subagent you delegate to ([Subagents](../13-subagents/unit.md)). A **hook** is the opposite kind of thing:
**you don't invoke it — the harness does, automatically, every time a lifecycle event happens.** That
single property is the whole point.

**1 — What a hook is.** A hook is a command wired into `settings.json` to run at a defined moment in
Claude Code's lifecycle. The structure is an event name mapping to matchers and commands:

```json
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Write|Edit",
        "hooks": [ { "type": "command", "command": "your-command" } ] }
    ]
  }
}
```

The **event** says *when* (before a tool, after a tool, at session start, before compaction, …); the
**matcher** narrows it (here, only the `Write` and `Edit` tools); the **command** is what runs. The
event names and the exact shape are the version-specific surface — {{vd:hooks}}.

**2 — The two moves: block and react.** Hooks earn their keep in two ways:

- **Block** — a **`PreToolUse`** hook runs *before* the tool and can **deny** the action. This is the
  guardrail: refuse an edit to a generated file, refuse a `git push --force`, refuse a write outside an
  allowed path. The action never happens.
- **React** — a **`PostToolUse`** hook runs *after* a successful tool and does follow-up work: format
  the file that was just written, run the tests, run a linter — and **feed the result back** so Claude
  fixes what it broke. The action happened; the hook keeps it honest.

**3 — How a hook communicates.** When it fires, the hook receives the event as JSON on **stdin** — the
tool name, the `tool_input` (including `file_path` for an edit), and, for `PostToolUse`, the
`tool_response`. It steers what happens next through its **output**: a `PreToolUse` hook can deny the
call; a `PostToolUse` hook can return `{"decision": "block", "reason": "..."}` to push a failure back
into the conversation so Claude addresses it. (Exact field names and options: {{vd:hooks}}.) A hook
that reads `file_path` and exits quietly when the file is irrelevant is the normal shape — react only
to what matters.

**4 — Why a hook, not a command/skill/subagent.** Everything else in this stage is *chosen*: you fire a
command, Claude reaches for a skill or dispatches a subagent **if it judges the moment right**. A hook
removes the judgment: the harness runs it on the event, every time, whether or not anyone remembered.
So the line is:

- **Command / skill / subagent** → "I (or Claude) *want* to run this." Reusable work, invoked.
- **Hook** → "this *must always* happen, or *must never* happen." Enforced, not invoked.

That determinism is also the **safety** property ([Operate safely](../03-operate-safely/unit.md)): a standard that
depends on the model remembering will eventually be forgotten; a standard wired as a hook cannot be.
Hooks are how you turn "we always run the checks / we never touch the generated file" from an intention
into policy-as-code.

**Version currency.** Verified against Claude Code {{vd:_verified_version}}. The hook **event-name
enum** and the `settings.json` `{matcher, hooks:[{type, command}]}` structure are verified against the
settings schema; the full event list is large and grows, so this unit teaches the common events and
defers the authoritative enum and output-field details to {{vd:hooks}} (tracked in
[`meta/version-record.md`](../../../meta/version-record.md)). Confirm event names against the docs
before wiring an uncommon one — don't author them from memory.

## Worked example

**This course enforces its own standards with the very mechanism this unit teaches (R14).** Open this
repo's [`.claude/settings.json`](../../../.claude/settings.json): alongside the permissions, there is a
`PostToolUse` hook on `Write|Edit` that runs [`tools/check-on-edit`](../../../tools/check-on-edit).

Read the wrapper — it's deliberately thin. On every `Write`/`Edit` it:

1. reads the event JSON on stdin and pulls `tool_input.file_path`;
2. **returns immediately** unless the edited file lives under `course/` or `meta/` — the authored
   content the suite actually guards (no point running checks after an edit to a `tools/` script);
3. runs `make check` — the course's whole enforcement suite (front-matter, coverage, links,
   version-refs, traceability — the [Spec-driven dev](../10-spec-driven-dev/unit.md)/[Code & security review](../11-code-and-security-review/unit.md)
   machinery, R13);
4. on green, stays **silent**; on failure, prints `{"decision": "block", "reason": "<the failing
   output>"}` so the break is fed straight back into the session.

Two design choices worth copying:

- **The policy isn't duplicated in the hook.** The hook *calls* the existing `make check`; it doesn't
  re-implement any rule. The standard lives in one place (R13); the hook is just a new *trigger* for it.
- **It's defense in depth, not redundancy.** The same suite runs three ways, each catching the previous
  one's escapes: this **in-session `PostToolUse` hook** (fastest — the moment a unit is edited), the
  [`.githooks/pre-commit`](../../../.githooks/pre-commit) gate (at commit time), and
  [GitHub Actions CI](../../../.github/workflows/checks.yml) (the backstop that doesn't depend on any
  local config). A standard you actually rely on is wired at more than one layer.

That is the C15 move in one artifact: a standard (the checks) that *used to* depend on someone
remembering to run `make check` is now enforced automatically, the instant the relevant content
changes.

## Lab

> **This lab has no `start/`/`solution/` refs** — the artifact you build is a hook in *your own*
> `settings.json`, not a change to a codebase (precedent: [Commands & skills](../12-commands-and-skills/unit.md)/[Subagents](../13-subagents/unit.md)).
> But a hook's behavior **is** objectively checkable: you'll **drive it with a synthetic event
> payload** and confirm it fires correctly — a stronger self-check than prose, and the same way the
> repo's own hook was verified.

**Goal:** wire a hook in `taskflow-api` that **enforces a standard automatically** — and prove it fires
on the events that should trigger it and stays silent on those that shouldn't.

**Starting state:** the clean primary codebase. `cd codebases/primary/taskflow-api`. You'll edit that
project's `.claude/settings.json` (create the `hooks` block; preserve any existing keys). Confirm the
event name and structure against the docs / the settings schema rather than memory ({{vd:hooks}}).

**Build one of these (pick the move you want to practice):**

1. **React — `PostToolUse` runs the tests.** On `Write|Edit`, when the edited file is under `app/`, run
   `pytest -q` and, on failure, return a `decision: "block"` with the output so the break is surfaced
   in-session. (Mirrors the worked example, scaled to one project.)
2. **Block — `PreToolUse` denies a dangerous action.** On the `Bash` tool, **block** a `git push`
   (or `--force` push, or a write outside `app/`) so the action is refused before it runs — the
   [Operate safely](../03-operate-safely/unit.md) blast-radius guardrail as policy-as-code.

**Steps:**

1. Decide **block or react**, and therefore the **event** (`PreToolUse` to block, `PostToolUse` to
   react). Confirm the event name + the `{matcher, hooks:[{type,command}]}` shape against the docs
   ({{vd:hooks}}) — don't author it from memory.
2. Write the command. Keep it thin: read the event JSON on stdin (e.g. `jq -r '.tool_input.file_path'`),
   gate on what's relevant, then run the underlying tool the way this project runs it (`pytest`). Put
   any real logic in a small script rather than a one-liner buried in JSON (as the repo's
   `tools/check-on-edit` does).
3. **Prove it fires (the required verification step).** *Before* trusting the config, pipe a synthetic
   payload straight into your command and check both exit behavior and side effect:
   - a **matching** event (e.g. `echo '{"tool_name":"Edit","tool_input":{"file_path":"app/main.py"}}' | your-command`)
     → the hook runs the check / blocks, as intended;
   - a **non-matching** event (an unrelated file, or a benign `Bash`) → the hook stays **silent / no-op**
     (it must not fire on everything).
   - For a block hook, also confirm a **compliant** action is *allowed* through.
4. Validate the JSON wiring: `jq -e '.hooks' .claude/settings.json` parses and shows your block. (A
   malformed `settings.json` silently disables *all* of that file's settings.)

**Self-check (objective — you drove it, you didn't assume):** you're done when **all** hold:

- [ ] The hook is configured under a **verified event name** with a `matcher`, and `jq -e '.hooks'`
      confirms `settings.json` still parses.
- [ ] Driven with a **matching** synthetic payload, the hook **does its job** — blocks the action
      (`PreToolUse`) or runs the check and surfaces failure (`PostToolUse`) — observed, not assumed.
- [ ] Driven with a **non-matching** payload, the hook is a **silent no-op** (no false firing on
      unrelated tools/files).
- [ ] You can state **why this is a hook** — a standard that must be enforced automatically — rather
      than a command/skill/subagent you'd choose to invoke.
- [ ] Nothing about the **event name or schema was authored from memory** — it was confirmed against
      the settings schema / docs ({{vd:hooks}}).

**Reference:** there's no `solution/` branch — the hook is *yours*. The repo's
[`.claude/settings.json`](../../../.claude/settings.json) hook + [`tools/check-on-edit`](../../../tools/check-on-edit)
are the reference pattern (a `PostToolUse` reactor); compare your wiring and your pipe-test against them
and the checklist.

## Common pitfalls

- **Treating a hook like a command.** A hook isn't something you invoke — if the work only needs to run
  *when you decide*, it's a command or skill ([Commands & skills](../12-commands-and-skills/unit.md)). Reach for a
  hook only when it must run **automatically, every time**.
- **Assuming the config works without driving it.** A `settings.json` entry that parses can still never
  fire (wrong event, wrong matcher, a command that errors on the real payload). **Pipe a synthetic
  event through it** and watch the effect — that's the unit's verification step, not an optional extra.
- **A hook that fires on everything.** Forgetting to gate on `file_path`/tool means a `PostToolUse`
  reactor runs your whole suite after *every* edit, including irrelevant ones — slow and noisy. Return
  early for anything the hook shouldn't care about.
- **Duplicating the policy in the hook.** Re-implementing a rule inside the hook command means two
  places to maintain. **Call** the existing check/formatter/test runner; the hook is a trigger, not a
  second copy of the standard (as `check-on-edit` calls `make check`).
- **Malformed `settings.json`.** Invalid JSON silently disables *all* settings in that file — not just
  the hook. Validate with `jq -e` after editing.
- **Authoring event names from memory.** The event enum is version-specific and large; a guessed name
  just never fires. Confirm against the settings schema / docs ({{vd:hooks}}).

## Going deeper

- **Next:** U15 (MCP & vetting) connects external tools and asks how far to trust them; U16 (automate &
  scale) runs Claude **headlessly** (`-p`) in CI and across parallel worktrees — where deterministic
  hooks like this one become the standards that hold without a human watching.
- **The three layers** — this in-session `PostToolUse` hook, the [`.githooks/pre-commit`](../../../.githooks/pre-commit)
  gate, and [CI](../../../.github/workflows/checks.yml) all run the same `make check`; defense in depth
  is the point.
- **Hooks as the safety thesis automated** — the deterministic enforcement here is the
  [Operate safely](../03-operate-safely/unit.md) guardrail/verification discipline turned into policy-as-code.
- The event enum, matcher syntax, and output fields — {{vd:hooks}}; version-specifics in
  [`meta/version-record.md`](../../../meta/version-record.md). Confirm with the settings schema / docs.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
