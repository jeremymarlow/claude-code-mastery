<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U15
title: "Connect an MCP server and vet it before trusting it"
stage: autonomy-scale
depth_tier: core
use_case: "Give Claude access to my tools & data — safely"
can_do: [C16]
workflows: []
coverage_areas: [21, 22]
prerequisites: [U3, U13]
reading_time_min: 11
lab_time_min: 22
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Connect an MCP server and vet it before trusting it

# Connect an MCP server and vet it before trusting it

## Learning objectives

By the end of this unit you can:

- **Connect an MCP server to Claude Code** — a local stdio server (a subprocess) or a remote HTTP one —
  so Claude can call tools and read data beyond its built-ins.
- **Treat connecting as a trust-delegation decision** — recognize that an MCP server, plugin, or
  marketplace item runs code or sees data on your behalf, so installing one grants it trust (the
  [Subagents](../13-subagents/unit.md) lesson, now applied to *third-party* code).
- **Vet a third-party extension before installing it** — evaluate source, scope/permissions, transport,
  and secrets against a checklist, and reach an explicit connect / don't-connect decision.
- **Use the approval gate, and verify the results** — leave a `.mcp.json` server *pending* until you've
  vetted it, and check what a connected server returns rather than trusting it because it connected.

## Fast path (TL;DR)

> **MCP** (Model Context Protocol) lets Claude Code connect to external **servers** that expose tools
> and data. Add a local one (runs as a subprocess) with `claude mcp add <name> -- <command>`, or a
> remote one with `claude mcp add --transport http <name> <url>`; `claude mcp get`/`list` health-check
> them, and a project `.mcp.json` server stays **`⏸ Pending approval`** until you approve it.
> The catch: connecting a server — or installing a plugin/marketplace item — is a **trust-delegation
> decision**. It runs code or sees data for you, so **vet it first**: source, scope, transport,
> secrets. This repo ships a real, offline stdio server you connect in the lab
> (`codebases/fixtures/taskflow_mcp.py`, verified `✓ Connected`); the other half is vetting a
> third-party server against a checklist and deciding.

## Skip-check

**Skip this unit if you can already:** connect an MCP server to Claude Code (local stdio or remote
HTTP) and confirm it's connected; treat installing any third-party extension (MCP server, plugin,
marketplace item) as a trust-delegation decision; vet one against source / scope / transport / secrets
and decide whether to connect it, using the `.mcp.json` approval gate; and verify what a connected
server returns rather than trusting it because the handshake succeeded.

## Concept

[Subagents](../13-subagents/unit.md) ended on a rule: *delegation is trust delegation — verify the result.*
There, the delegate was another Claude. This unit applies the same rule to **external tools and
third-party code**: connecting an MCP server is delegation to something you may not have written.

**1 — What MCP is.** The Model Context Protocol is a standard way for Claude Code to talk to external
**servers**. A server exposes **tools** (callable actions) and data; once connected, Claude can use
them just like its built-in tools — query your issue tracker, hit an internal API, read a database.
It's how you give Claude access to *your* world beyond the files in the repo.

**2 — How you connect one.** Two transports:

- **Local (stdio)** — the server is a subprocess on your machine: `claude mcp add <name> -- <command>`.
  It runs with *your* privileges but needs no network. Good for wrapping local tools/data.
- **Remote (HTTP)** — the server lives elsewhere: `claude mcp add --transport http <name> <url>`. It
  sees whatever you send it, over the network.

`claude mcp get`/`list` **health-check** a connection (so you can confirm it actually connected, not
just that you typed a command), and a project-scoped server in a committed **`.mcp.json`** shows as
**`⏸ Pending approval`** until you approve it. The exact commands and config shape are the
version-specific surface: `claude mcp add <name> -- <cmd>` adds a local stdio server (subprocess); `--transport http <url>` adds a remote one. `claude mcp get`/`list` health-check connections; a project `.mcp.json` server shows as `⏸ Pending approval` until approved. `--mcp-config <files>` loads per-session; `--strict-mcp-config` ignores others.

**3 — Connecting is a trust-delegation decision.** This is the unit's thesis. An MCP server,
a plugin, a marketplace item — each one **runs code or sees data on your behalf**:

- a **remote** server receives whatever Claude sends it (your prompts, code snippets, data) — that's a
  data-exfiltration surface;
- a **local** stdio server runs a subprocess **with your privileges** — that's arbitrary-code-execution
  trust;
- a **plugin / marketplace** install is supply-chain trust: you're running someone else's code in your
  environment.

So "install this handy MCP server" is never free — it's the same blast-radius question from
[Operate safely](../03-operate-safely/unit.md), aimed at third-party code.

**4 — Vet before you connect (the checklist).** Before connecting a third-party extension, work through:

- **Source / provenance** — who publishes it? Is this the *real* package (not a typosquat), from a
  reputable, maintained source? Can you read its code?
- **Scope / permissions** — what tools does it expose, and over what data? Does it *write* or only read?
  Does it touch anything sensitive (secrets, prod, the filesystem)?
- **Transport** — local stdio (your privileges, no network) vs. remote HTTP (your data leaves the
  machine). What does it send out, and to where?
- **Secrets** — does it want an API token or credentials? Where do those go, and is that acceptable?
- **Least privilege** — can you connect it with the narrowest scope that does the job, rather than
  granting everything by default?

A clean checklist run ends in an explicit **connect / don't-connect** decision tied to what you found —
not "looks fine." The version-specific surface for plugins/marketplace vetting: `claude plugin|plugins` manages plugins; `--plugin-dir <path>` / `--plugin-url <url>` load a plugin for one session.

**5 — The approval gate is where vetting happens.** The `⏸ Pending approval` state for `.mcp.json`
servers is not a nuisance — it's the **moment to vet**. Approving blind defeats it. This is
verify-don't-trust ([Operate safely](../03-operate-safely/unit.md)) applied to extensions: the gate makes you stop
before you delegate.

**6 — Connected ≠ correct.** Even a server you trust returns data Claude then acts on. A healthy
handshake says the *pipe* works, not that the *answer* is right — so verify the results a tool returns,
exactly as you verified a subagent's report ([Subagents](../13-subagents/unit.md)).

**Version currency.** Verified against Claude Code 2.1.159. The `claude mcp`
subcommands and the `.mcp.json` shape were confirmed live (a stdlib stdio server connected `✓
Connected`); confirm them against `claude mcp --help` before relying on a detail. The
extension-vetting surface: `claude plugin|plugins` (or `--plugin-dir`/`--plugin-url` for one session) Tracked in
[`meta/version-record.md`](../../../meta/version-record.md).

## Worked example

This repo ships a **real, offline MCP server** you can connect right now —
[`codebases/fixtures/taskflow_mcp.py`](../../../codebases/fixtures/taskflow_mcp.py). It's a
zero-dependency, stdlib-only **stdio** server: it speaks the protocol over a subprocess, needs no
network and no credentials, and exposes two read-only tools (`list_tasks`, `task_stats`) over canned
task-tracker data. Connect it:

```bash
claude mcp add taskflow-local -- python3 codebases/fixtures/taskflow_mcp.py
claude mcp get taskflow-local      # → Status: ✓ Connected
# ...use it, then:
claude mcp remove taskflow-local
```

And here is the health-check succeeding for real — this exact fixture, connected live:

**Captured** — `claude mcp get taskflow-demo` immediately after a live `mcp add` of this fixture
(2026-06-09):

```text
taskflow-demo:
  Scope: Local config (private to you in this project)
  Status: ✔ Connected
  Type: stdio
  Command: python3
  Args: /home/.../codebases/fixtures/taskflow_mcp.py
```

That `✔ Connected` is the **health-check** — proof the handshake worked, captured against this exact CLI
(it's how the [version record](../../../meta/version-record.md) verified the `mcp` surface). The
project-scoped equivalent is [`codebases/fixtures/taskflow.mcp.json`](../../../codebases/fixtures/taskflow.mcp.json):
the committed `.mcp.json` form, which is exactly the kind of entry that lands as **`⏸ Pending
approval`** in a fresh checkout — the trust gate in action.

Now read it as a trust decision. This server is **stdio/local** (a subprocess, your privileges, no
network) and **you can read every line** — low-risk, fully vettable. Contrast a hypothetical
*third-party remote* server — say a `tasktracker-pro` HTTP server that wants an API token and broad
scope: now your data leaves the machine, a credential is in play, and you can't read the code. Same
"connect a server" mechanic; completely different trust profile. The mechanics are easy; the judgment
is the skill.

## Lab

> **No `start/`/`solution/` refs** — what you produce is a connection in *your own* config plus a
> vetting decision, not a codebase change (precedent: [Hooks](../14-hooks/unit.md)). But the connect half
> is **objectively checkable** (`claude mcp get` health-checks it), and the vetting half is graded by an
> objective checklist.

**Goal:** connect the repo's local MCP server and confirm Claude can use it, then **vet a third-party
server** against the checklist and reach a defensible connect / don't-connect decision.

**Starting state:** the repo, from its root. The local server needs nothing installed (stdlib only).
Confirm every command against `claude mcp --help` rather than typing it from memory.

**Part A — connect (the mechanic):**

1. Add the local server: `claude mcp add taskflow-local -- python3 codebases/fixtures/taskflow_mcp.py`.
2. **Confirm it connected:** `claude mcp get taskflow-local` shows `✓ Connected`. (If not, that's the
   finding — a server that doesn't health-check isn't connected, no matter what you typed.)
3. **Use it and verify the result:** ask Claude to call `task_stats` (or `list_tasks`), and check the
   returned counts against the canned data in
   [`taskflow_mcp.py`](../../../codebases/fixtures/taskflow_mcp.py) — confirm the *answer*, not just
   that a tool ran.
4. Clean up: `claude mcp remove taskflow-local`.

**Part B — vet (the judgment):** consider a third-party MCP server you're tempted to install —
either a real one you'd actually use, or this scenario: *"`tasktracker-pro` — a remote HTTP MCP server
that syncs your tasks; install with an API token; exposes read **and** write tools over all your
projects."* Work the checklist:

- **Source** — who publishes it; is it the genuine, maintained package; can you read the code?
- **Scope** — which tools, over what data; read vs. write; anything sensitive?
- **Transport** — stdio (local) or HTTP (remote)? What leaves your machine, to where?
- **Secrets** — what credential does it want, and where does it go?
- **Least privilege** — can you connect it more narrowly, or not at all?

Reach an explicit **connect / don't-connect** verdict tied to those findings, and note how the
`⏸ Pending approval` gate lets you hold the decision until you've vetted.

**Self-check (objective — you observed it, you didn't assume):** you're done when **all** hold:

- [ ] The local server reported **`✓ Connected`** via `claude mcp get`, and you **called a tool and
      verified its result** against the fixture's canned data — not "a tool ran."
- [ ] You vetted the third-party server against **all** checklist dimensions (source, scope/permissions,
      transport, secrets, least privilege) — each answered, not skimmed.
- [ ] You reached an **explicit connect / don't-connect decision** justified by those findings, not a
      vibe ("seems fine").
- [ ] You can explain why connecting is a **trust-delegation** decision and how the `⏸ Pending approval`
      gate enforces vetting before trust.
- [ ] No `claude mcp` command or config shape was **authored from memory** — each was confirmed against
      `claude mcp --help` / the docs.

**Reference:** there's no `solution/` branch — the connection and the decision are *yours*. The repo's
[`taskflow_mcp.py`](../../../codebases/fixtures/taskflow_mcp.py) +
[`taskflow.mcp.json`](../../../codebases/fixtures/taskflow.mcp.json) are the reference pattern for a
connectable server and its config; compare your connect + vetting run against them and the checklist.

## Common pitfalls

- **Treating "it connected" as "it's safe."** The health-check proves the pipe works, not that the
  server is trustworthy or its data correct. Vet *before* connecting; verify results *after*.
- **Approving a `.mcp.json` server blind.** The `⏸ Pending approval` gate only protects you if you
  actually vet at it. Reflexively approving is the supply-chain mistake.
- **Ignoring the transport.** A remote HTTP server sees whatever Claude sends it — a real exfiltration
  surface. "It's just a task tool" still means your data leaves the machine.
- **Over-scoping a credential.** Handing a third-party server a broad API token "to be safe" is the
  opposite of safe. Grant the narrowest scope that does the job ([Operate safely](../03-operate-safely/unit.md)).
- **Typosquat / wrong source.** Installing `tasktracker-pr0` instead of the real one is how
  supply-chain attacks land. Confirm the publisher and that it's the genuine package.
- **Authoring the commands from memory.** `claude mcp` subcommands, transports, and the `.mcp.json`
  shape are version-specific — confirm against `claude mcp --help` rather than recall.

## Going deeper

- **Next:** **Automate & scale** runs Claude **headlessly** and in parallel — where a connected MCP
  server (and the discipline of having vetted it) becomes part of an automated pipeline with no human at
  the approval gate, raising the stakes on getting the trust decision right up front.
- **Trust delegation** is the through-line: a subagent ([Subagents](../13-subagents/unit.md)) → third-party
  code here, all governed by verify-don't-trust ([Operate safely](../03-operate-safely/unit.md)).
- **The shipped server** — [`taskflow_mcp.py`](../../../codebases/fixtures/taskflow_mcp.py) and its
  [`.mcp.json`](../../../codebases/fixtures/taskflow.mcp.json); the fixtures
  [README](../../../codebases/fixtures/README.md) shows how to connect and remove it.
- The `mcp` subcommands and extension-vetting surface: the `claude mcp add`/`get`/`list` subcommands and the project `.mcp.json` `claude plugin|plugins` (or `--plugin-dir`/`--plugin-url` for one session)
  Version-specifics in [`meta/version-record.md`](../../../meta/version-record.md). Confirm with
  `claude mcp --help`.
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
