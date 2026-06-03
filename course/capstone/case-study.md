# Case study: how this course was built and is maintained with Claude Code

This is the **worked exemplar** for your capstone — and it is real. This course was itself
built end-to-end with Claude Code, spec-driven, against the same discipline the units teach. Read it
before you start your capstone so you have a concrete picture of a non-trivial job done well: context
engineered deliberately, custom extensions built and used, a real workflow followed, and Claude's
output verified at every step rather than trusted.

It is also the course's standing dogfooding record: if we teach a feature, we point at the
real artifact we used, never a prop. Its candid companion,
[an honest retrospective of the collaboration](../case-studies/collaboration-retrospective.md), is a
panel's self-assessment of how the build *actually* went — the recurring failure modes alongside the
strengths, flagged as a self-evaluation to weigh rather than trust. Read both: this one for the
workflow, that one for an honest reckoning with the collaboration.

## 1. The job

Take a seasoned developer who is new to AI-assisted coding to elite Claude Code practitioner — as a
self-paced, hands-on course organized around real use cases, tiered for fast learners, and resilient
to a fast-moving CLI. That is a large, ambiguous brief with no single right answer, exactly the kind
of work where ad-hoc prompting falls apart and a deliberate process pays for itself.

## 2. The workflow: spec-driven, with real gates

We ran the [Kiro-style spec workflow](../units/10-spec-driven-dev/unit.md) the course teaches,
on the course itself. The artifacts are not illustrations — they are the spec we actually built from:

- **Requirements** ([`requirements.md`](../../specs/claude-code-mastery/requirements.md)) — R1–R17 in
  EARS form, with stable IDs. Approved turn-by-turn **before** any design work began.
- **Design** ([`design.md`](../../specs/claude-code-mastery/design.md)) — architecture, the unit
  model, the version-resilience mechanism, the lab/codebase plan, and a traceability table mapping
  every requirement to the component that satisfies it. Approved **before** tasks.
- **Tasks** ([`tasks.md`](../../specs/claude-code-mastery/tasks.md)) — the ordered build plan, chunked
  into phases (scaffold → tooling → codebases → units → finalize) so each could be executed in a
  bounded context window.

The gates were genuine, not ceremony: requirements were locked before design, design before tasks. A
held gate is the difference between a spec and a wish — when a requirement felt arbitrary later, the
reasoning was already recorded rather than re-litigated. That "why" lives in
[`decisions.md`](../../specs/claude-code-mastery/decisions.md), the build's decision log,
which a fresh session reads to recover context it never had.

**Context was engineered, not dumped.** Each unit was authored in its own slice, loading only the
relevant requirements, the one design section, and the cross-cutting `meta/` artifacts it referenced —
never the whole spec. Project memory ([`CLAUDE.md`](../../CLAUDE.md), the **Memory & context** example) carries the
working agreements into every session so they did not have to be re-stated.

## 3. The custom extensions we built and use

These are authentic — each one earns its place by doing a job in the real build loop:

| Artifact | What it does | Taught in |
|---|---|---|
| [`prime-context` skill](../../.claude/skills/prime-context/SKILL.md) | Loads full project context at the start of a fresh session (read order + live status + open loops). | [Commands & skills](../units/12-commands-and-skills/unit.md) |
| [`close-unit` command](../../.claude/commands/close-unit.md) | Runs the post-authoring state-sync chore (update status, check off tasks, log the decision, run the checks). | [Commands & skills](../units/12-commands-and-skills/unit.md) |
| [Enforcement hook](../../.claude/settings.json) + check suite | A `PostToolUse` hook runs `make check` on edits under `course/`/`meta/` and blocks in-session on failure. | [Hooks](../units/14-hooks/unit.md) |
| [`tools/check-version-drift`](../../tools/check-version-drift) | Flags when the installed CLI has drifted from the verified record (the refresh trigger). | [Automate & scale](../units/16-automate-and-scale/unit.md) |
| [MCP server + config](../../codebases/fixtures/taskflow_mcp.py) | A real, connectable local stdio MCP server over taskflow data, plus its project config. | [MCP & vetting](../units/15-mcp-and-vetting/unit.md) |
| [`tools/doctor`](../../tools/doctor) | Preflight: install, version floor, auth, a first command. | [Onboarding](../units/01-onboarding-first-win/unit.md) |
| [CI workflow](../../.github/workflows/checks.yml) | Runs the full check suite on every push (the backstop gate). | [Automate & scale](../units/16-automate-and-scale/unit.md) |

`prime-context` and `close-unit` **bookend the real authoring loop**: prime at session start, close
the unit when its prose is done. That is the same shape your capstone should take — package the work
you repeat into a command or skill rather than retyping it.

## 4. Verification was the through-line

The thesis the whole course defends — verify, don't trust — is what kept the build honest:

- **Never author a version-specific value from memory.** Every command, flag, and settings key was
  verified against the installed CLI and quarantined into
  [`meta/version-data.yaml`](../../meta/version-data.yaml), referenced by key. When verification
  contradicted memory, verification won (the `--permission-mode` value set turned out broader than the
  first draft assumed). Keys that could not be confirmed headlessly were marked `unverified` rather
  than faked.
- **Labs verify behavior, not wording.** Each automated `verify.sh` asserts the contract (and that the
  full suite stays green), so any convention-respecting solution passes and a plausible-but-wrong one
  fails — the same standard you should hold Claude's output to.
- **The checks gate the build.** Front-matter, coverage, link, version-reference, and traceability
  checks run at three layers (in-session hook, git pre-commit, CI). `make check-strict` going green is
  the single mechanical signal that the Definition of Done's structural obligations are met.

## 5. Maintenance: keeping it current as the CLI changes

The course is built to be refreshed, not rewritten, when Claude Code moves. The process — run
it whenever the CLI updates — is:

1. Run [`tools/check-version-drift`](../../tools/check-version-drift) to compare the installed
   `claude --version` against [`meta/version-record.md`](../../meta/version-record.md) and surface
   new/removed commands.
2. Re-verify each flagged version-specific detail against the installed CLI (`--help`, in-REPL
   `/help`, docs) — never from memory.
3. Update **only** [`meta/version-data.yaml`](../../meta/version-data.yaml) (and the rare prose it
   genuinely affects); because version-specifics are referenced by key rather than inlined, a version
   bump touches a bounded set of files, not the prose.
4. Bump [`meta/version-record.md`](../../meta/version-record.md) with the new verified version and date.
5. Re-run the enforcement suite (`make check`) until green.

The [maintainer guide](../maintainer-guide.md) covers adding or updating a unit without breaking the
catalog/matrix/map.

## 6. AI-authorship transparency

This course — its units, labs, spec, and tooling — was authored collaboratively with Claude Code,
under human direction and review at every gate. That is the point, not a caveat: the course teaches a
way of working, and it was built that way.

In the spirit of the responsible-output guidance the course itself teaches: AI-assisted
authorship does not lower the bar for correctness or attribution. Everything here was reviewed by a
human, version-specific claims were verified against the real tool rather than asserted from a model's
memory, and the reasoning behind non-obvious choices was recorded so it can be checked rather than
trusted. When you ship work produced with Claude — including your capstone — hold it to that same
standard: you are accountable for the output, so verify it and disclose the assistance honestly.
