[Claude Code Mastery](../../README.md) › [Capstone](README.md) › Capstone briefs

# Capstone briefs

Pick **one** brief. Each is a realistic, non-trivial, end-to-end job — not a fixed project — so you
have room to make it yours while facing the same kind of work the course prepared you for.

Whichever you choose, your capstone must demonstrate all four of these:

1. **Context engineering** — deliberate use of `CLAUDE.md` and context selection to steer Claude.
2. **At least one custom extension** — a command, subagent, skill, hook, or MCP connection that you
   build and actually use in the work.
3. **A non-trivial workflow** — a real multi-step workflow from the course
   ([`meta/workflows.md`](../../meta/workflows.md)), not a one-shot prompt.
4. **Explicit verification** — you verify Claude's output (read the diff, check the approach,
   spot-check edges), not merely trust green tests.

You will grade the result against the [rubric](./rubric.md), and the
[build case study](./case-study.md) is your worked exemplar so you never start from a blank page.

---

## Brief A — Ship a substantial feature, spec-first

**Substrate:** [`taskflow-api`](../../codebases/primary/taskflow-api) (primary).

**Goal.** Add a substantial, multi-layer feature to the API — one big enough to be worth a spec.
Good candidates: task **dependencies / blocked-by** (with cycle handling), **recurring tasks**, an
**activity/audit log**, or **saved filters/views**. The feature must touch models, services, routes,
and tests, and respect the app's ownership/auth rules.

**What makes it capstone-worthy.** It is ambiguous enough that jumping straight to code fails — the
design decisions (data model, edge cases, error contracts) are the real work.

**Shape.**
- **Workflow:** spec-driven to pin down requirements → design → tasks, then explore → plan →
  code → commit to build it.
- **Custom extension:** build a **custom command** (or skill) that automates a routine in this
  loop — e.g. scaffolding a route + schema + test stub, or running and triaging the test suite.
- **Context engineering:** use the project `CLAUDE.md` and targeted context so Claude follows the
  app's conventions (services → exceptions → routes).
- **Verification:** the suite stays green; you read the diff; and you confirm the **ownership/404
  boundary** holds for the new endpoints (a foreign user cannot touch another user's data).

**Done when.** The feature works against a real request, the full pytest suite is green, your spec and
the implementation are traceable to each other, and your verification reflection is complete.

---

## Brief B — Rescue a slice of the legacy CLI

**Substrate:** [`taskflow-cli`](../../codebases/legacy/taskflow-cli) (legacy — messy by design).

**Goal.** Take a meaningful slice of the legacy monolith and make it materially better **without
changing its behavior**: extract a cohesive module (or de-duplicate a repeated concern), add the
characterization tests it lacks, and leave it green. Optionally then fix one real bug as a *separate*
change once the safety net is in place.

**What makes it capstone-worthy.** The legacy code has no tests, global state, and duplication —
refactoring it safely is exactly the high-stakes "don't silently change behavior" job.

**Shape.**
- **Workflow:** onboard to the unfamiliar code to map it, then multi-file refactor,
  behavior-preserving. If you fix a bug, do it test-first *after* the refactor.
- **Custom extension:** build **two** here if you can — a read-only **subagent** to map the module
  for you, and a **hook** guardrail (e.g. run the tests on edit, or block a risky action) so your
  refactor cannot regress unnoticed.
- **Context engineering:** scope Claude tightly to the slice you are changing; resist whole-file
  rewrites.
- **Verification:** a **behavior-equivalence** check — characterization tests (or a before/after
  transcript) prove behavior is unchanged. A "helpful" bug-fix mixed into the refactor must show up
  as a deliberate, separate, verified change — not a silent diff.

**Done when.** The slice is cleaner and still behaves identically (proven, not assumed), the new tests
pass, your hook demonstrably fires, and your verification reflection is complete.

---

## Brief C — Integrate and vet an external tool (MCP)

**Substrate:** [`taskflow-api`](../../codebases/primary/taskflow-api) + an MCP integration.

**Goal.** Connect Claude to an external tool or data source for a real task against the app, and **vet
before you trust**. Use the course's local MCP server
([`codebases/fixtures/taskflow_mcp.py`](../../codebases/fixtures/taskflow_mcp.py)) as your connectable
target (no network or credentials required), or a third-party server you have vetted. Then use the
connection to do something useful — e.g. answer a question about task data, or drive a change informed
by it.

**What makes it capstone-worthy.** Extending Claude's reach is powerful and is exactly where
trust-but-verify matters most — an unvetted extension is a real risk.

**Shape.**
- **Workflow:** review-and-vet the extension, then use it; coordinate the run if you go
  headless or parallel.
- **Custom extension:** the **MCP connection** itself is the extension (configure it, confirm
  `✓ Connected`); optionally add a command that wraps the task you repeat with it.
- **Context engineering:** decide deliberately what the tool may see and do (least privilege).
- **Verification:** confirm the connection health-checks, **verify a tool result** against known data
  (don't assume the server is honest), and produce an explicit **vetting verdict** (source, scope,
  transport, secrets, least-privilege → connect / don't-connect, with reasons).

**Done when.** The connection is verified working, you used it for a real task and checked its output,
your vetting verdict is written and justified, and your verification reflection is complete.
