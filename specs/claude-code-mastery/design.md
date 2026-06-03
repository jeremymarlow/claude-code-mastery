# Design — Claude Code Mastery Course

**Spec:** `claude-code-mastery`
**Phase:** Design (Phase 2 of 3)
**Status:** ✅ **AUTHORED** (2026-05-29) — §0–§11 complete; capability map / catalog / coverage matrix
user-approved; §3,§5–§10 + capstone (§6.5) authored; traceability table (§11) fully populated.
Verified against CLI **2.1.158**. Ready for review → Phase 3 (Tasks).

> **Authored.** Each section states its purpose, inputs (requirements + decisions), and the concrete
> artifact(s) it produces — now filled with the approved design. The artifacts themselves (the
> machine-readable `meta/*` files, templates, tooling, codebases) are **generated in Phase 3 / P2–P6**
> from these specifications; the traceability table (§11) maps every R1–R15 to its design component.

---

## 0. Inputs to resolve first (with the user) — ✅ RESOLVED (2026-05-29)

- **Q1 ✅** — **Task/project-tracker domain.** Primary `taskflow-api` (FastAPI + SQLModel/SQLite,
  JWT auth, REST CRUD, pytest). Legacy `taskflow-cli` (argparse, god-module, no tests; seeded
  bugs/smells). Details → §7. Recorded in [`decisions.md`](./decisions.md) → Design session.
- **Q2 ✅** — **Capability map + use-case catalog approved** (§1, §2 below). **Unit count is
  content-driven, not pinned** (the original "~12" was relaxed by the user): **16 units**, est.
  ~15–25 hrs. Security unit **pulled forward to U3**. Light/deep onboarding split **kept** (U2/U9).
- **CLI version ✅** — verified **2.1.158** (`claude --version`, 2026-05-29) → anchors
  `meta/version-record.md` (§5).

---

## 1. Capability map  → produces `meta/capability-map.{yaml,json}`  [R1]  ✅ AUTHORED (2026-05-29)

The full set of **can-do statements** — outcome-phrased, observable, describing the work and never
ranking the person (R1.AC1/AC3) — grouped into the four neutral **stages** (R1.AC2). Each maps to
exactly one stage and to its home unit (R1.AC4); each will trace to ≥1 lab **and** ≥1 capstone-rubric
dimension (R1.AC5), enforced by the R13.AC5 check once §6/§8 land.

| Stage | ID | "I can …" | Home unit |
|---|---|---|---|
| **First Wins** | C1 | install, authenticate, and confirm a working Claude Code setup with a repeatable check | U1 |
| | C2 | explain the agentic loop and make a single, **verified** change to a real codebase | U1 |
| | C3 | use Claude to explore and explain an unfamiliar codebase and locate where to make a change | U2 |
| | C4 | operate Claude safely — choose permission modes, protect secrets, recognize prompt injection, limit blast radius | U3 |
| | C5 | steer Claude with project memory (`CLAUDE.md`) and deliberate context selection | U4 |
| **Daily Driver** | C6 | implement a feature end-to-end via explore→plan→code→commit and verify the result myself | U5 |
| | C7 | drive a change test-first (confirm a failing test, implement to green) | U6 |
| | C8 | diagnose and fix an unfamiliar failure, confirming root cause rather than guessing | U7 |
| | C9 | turn a body of work into clean commits and a reviewable PR with an accurate description | U8 |
| **Force Multiplier** | C10 | onboard to and execute a large multi-file refactor on a legacy codebase, keeping it green | U9 |
| | C11 | run a spec-driven workflow (requirements→design→tasks) against a real spec | U10 |
| | C12 | review a change for correctness **and** security with Claude | U11 |
| **Autonomy & Scale** | C13 | package repeatable work as custom commands & skills | U12 |
| | C14 | delegate focused / parallel sub-tasks to subagents | U13 |
| | C15 | automate guardrails and standards with hooks | U14 |
| | C16 | connect Claude to external tools/data via MCP and vet third-party extensions before installing | U15 |
| | C17 | run Claude headlessly / in CI and coordinate parallel agents via git worktrees | U16 |
| **Cross-cutting** | **CV** | verify Claude's output rigorously — read the diff, check the approach, spot-check edges — not merely trust green tests | every lab; consolidated U3 & U11 (R10.AC6) |

- **Output:** machine-readable `meta/capability-map.{yaml,json}` (`id`, `statement`, `stage`,
  `home_unit`), seeded in P2. The learner-facing progress checklist (R9.AC5) is **generated** from it.
- **CV is cross-cutting:** every workflow lab must include at least one explicit verification step
  (R10.AC7); CV is "advanced" by every unit and consolidated in U3 (safety) and U11 (review).

## 2. Use-case catalog  → produces `meta/use-case-catalog.yaml`  [R2]  ✅ AUTHORED (2026-05-29)

Prioritized jobs-to-be-done, one per unit. **Prioritization rationale (R2.AC2):** ordered primarily
by *frequency × leverage* (the daily loops a developer hits first and most often lead; rarer/higher-
ceiling jobs follow), then adjusted for *capability-map coverage* so the catalog collectively
exercises every can-do statement (C1–C17 + CV) and every coverage-matrix area (§4). All entries are
grounded in real, documented engineering practice (R2.AC4) — none invented. **Depth tier:** every
unit is **core** (each carries ≥1 hands-on lab); awareness-tier coverage is applied at the *feature*
level inside the coverage matrix (§4), per R4.AC4 / R5.AC4.

| Unit | Stage | Use case (job-to-be-done) | Success outcome | Workflow(s) (R3) / key features | Real-practice grounding (R2.AC4) | Advances |
|---|---|---|---|---|---|---|
| **U1** | First Wins | Get set up and make a first **verified** win against `taskflow-api` | doctor passes; one verified one-line change committed | agentic loop, verification intro; REPL, prompting (R11) | Anthropic first-run / onboarding guidance | C1, C2 |
| **U2** | First Wins | Understand a codebase I've never seen | learner can explain the app's architecture and locate a change site, unaided | onboarding *(light)*; codebase Q&A, search, `@`-refs | "explore before you change" practice | C3 |
| **U3** | First Wins | Operate Claude without leaking secrets or causing damage *(security unit, R10)* | learner observes a prompt-injection attempt in a sandbox and applies a defense; chooses an appropriate permission mode | permissions/modes, secret hygiene, prompt-injection lab, blast-radius, checkpoints | threat-modeling, least-privilege | C4, CV |
| **U4** | First Wins | Make Claude reliably follow my project's conventions | a `CLAUDE.md` + context choices measurably change Claude's behavior on a task | context engineering; `CLAUDE.md` memory, `/context` (R11.AC4 home) | context-management best practice | C5 |
| **U5** | Daily Driver | Ship a new feature in `taskflow-api` | feature implemented & verified end-to-end via a plan | **explore→plan→code→commit**; plan mode | Anthropic's flagship coding loop | C6 |
| **U6** | Daily Driver | Add behavior safely, test-first | a failing test is written/confirmed, then driven to green | **TDD** | classic TDD, AI-adapted | C7 |
| **U7** | Daily Driver | A test/endpoint is broken — find and fix it | root cause confirmed (not guessed); fix verified | **debugging an unfamiliar failure** | scientific debugging | C8 |
| **U8** | Daily Driver | Turn my work into a clean, reviewable PR | clean commits + accurate PR description; review-ready | **Git/PR workflow**; `gh` | trunk-based / PR-review practice | C9 |
| **U9** | Force Mult. | Onboard to the messy `taskflow-cli` and refactor it safely | architecture mapped; multi-file refactor lands with suite green | **onboarding (deep)** + **multi-file refactoring** | legacy-rescue / strangler-fig practice | C10 |
| **U10** | Force Mult. | Build a feature spec-first | reqs→design→tasks produced and used to drive the change | **spec-driven dev** — *this very spec is the worked example* (R3.AC2) | spec-/intent-driven development | C11 |
| **U11** | Force Mult. | Review a change for correctness **and** security | a review surfaces real correctness + security issues; verification beyond green tests | **code & security review**; `/code-review`, `/security-review` | code-review & threat-review practice | C12, CV |
| **U12** | Autonomy | Eliminate repetitive prompting | a reusable custom command and a skill replace a hand-typed routine | custom **slash commands**, **skills** | dogfooded authoring artifacts (R14) | C13 |
| **U13** | Autonomy | Delegate focused / parallel sub-tasks | a **subagent** performs a scoped task and returns a usable result | **subagents** | agent-delegation practice | C14 |
| **U14** | Autonomy | Enforce my standards automatically | a **hook** blocks/normalizes an action without manual effort | **hooks** — the course's own enforcement suite is the example (R13/R14) | policy-as-code / pre-commit practice | C15 |
| **U15** | Autonomy | Give Claude access to my tools & data — safely | an **MCP server** is connected and a third-party one is vetted before install | **MCP servers** + extension vetting (R10.AC5) | MCP integration; supply-chain trust | C16 |
| **U16** | Autonomy | Run Claude unattended and in parallel | a headless run executes in CI; ≥2 agents work isolated worktrees | headless `-p`, CI, **parallel agents via worktrees** | git-worktree parallelism; CI automation | C17 |

**Workflow reconciliation (R3.AC5/AC6):** all nine named R3 workflows map to ≥1 exercising use case
(none free-floating). The onboarding workflow is split deliberately — **light** exploration (U2,
primary repo) vs **deep** onboarding-for-refactor (U9, legacy repo) — so the legacy substrate's
authentic complexity is used where it matters. Final workflow→stage tags are confirmed against this
map in §3.

- This catalog → `meta/use-case-catalog.yaml` (P2) and the unit map (§6, one unit per row).
- Per-unit fast-path, skip-check, and dual time estimates (R5.AC2/AC3/AC6) are attached in §6.

## 3. Workflow methods  → produces `meta/workflows.md`  [R3]  ✅ AUTHORED (2026-05-29)

The nine named workflows (R3.AC1), each with a **decision criterion** (when to choose it over
alternatives, R3.AC3), an **expected verification step** (R3.AC3 + CV), its **confirmed stage**, and
the **exercising unit(s)** (R3.AC4–AC6). Stage tags match the R3.AC1 provisional set and the §1
capability map — no changes needed. Workflows are taught *inside* their use case, then generalized
(R3.AC4); none is a free-floating lesson (R3.AC5).

| # | Workflow | Stage | When to choose it | Expected verification (CV) | Unit(s) |
|---|---|---|---|---|---|
| W1 | explore → plan → code → commit | Daily Driver | Default for any non-trivial change | Review the **plan** before coding; read the diff + run tests before commit | U5 |
| W2 | test-driven development | Daily Driver | Behavior is specifiable as a test; regression-prone or bug-fix work | Confirm the test fails first **for the right reason** (red), then green; review the impl | U6 |
| W3 | debugging an unfamiliar failure | Daily Driver | Something is broken and the cause is unknown | Reproduce first; capture the bug in a failing test; confirm root cause, then that the fix doesn't regress | U7 |
| W4 | Git / PR workflow | Daily Driver | Turning work into shareable history/review | Review the staged diff; ensure message matches change; self-review the PR | U8 |
| W5 | multi-file refactoring | Force Multiplier | Cross-cutting change touching many files; rename/restructure | Behavior-preserving: full suite green **before and after**; diff-review for scope creep | U9 |
| W6 | code & security review | Force Multiplier | Before merging a significant or security-sensitive change | The workflow *is* verification — but cross-check findings, don't trust the review blindly (CV) | U11 |
| W7 | spec-driven development | Force Multiplier | Large/ambiguous feature where upfront alignment pays off | Each phase gate reviewed/approved before the next; trace requirements→design→tasks | U10 |
| W8 | onboarding to an unfamiliar/large codebase | First Wins *(light)* → Force Multiplier *(deep)* | Entering code you don't know | Validate Claude's architecture summary against the actual code (spot-check claims) | U2 (light), U9 (deep) |
| W9 | running parallel agents (git worktrees) | Autonomy & Scale | Multiple independent tasks that can run concurrently | Isolate each in a worktree; review each agent's diff independently before integrating | U16 |

- **R3.AC2 (spec-driven uses this spec):** W7/U10 uses **this very `specs/claude-code-mastery/`**
  (requirements → design → tasks, with approval gates) as its worked example.
- **R3.AC6 reconciliation:** W8 is intentionally two-tiered (light U2 / deep U9 — see §2); every
  workflow has ≥1 exercising unit, and no catalog row is better expressed as a workflow than a use case.
- Output: `meta/workflows.md` (this table + the generalized pattern write-up per workflow), referenced
  by the units rather than re-explained (R5.AC5).

## 4. Feature-coverage matrix  → produces `meta/coverage-matrix.yaml`  [R4]  🟨 SEEDED (2026-05-29)

**Canonical source of truth** for the capability-area set (R4.AC1 — prose does not re-list features).
Tiering by *frequency × leverage*: **high-leverage ⇒ ≥1 hands-on lab; awareness ⇒ named/shown once
with pointers** (R4.AC4). Below is the **Design seed**; `version-data` keys are placeholders finalized
in §5/P2, and the R13.AC4 check cross-validates this against the units once authored. Verified against
CLI 2.1.158; per-fact provenance is recorded in `version-data` at authoring time (R12.AC3/AC4).

| # | Capability area | Tier | Covered by | version-data key (planned) |
|---|---|---|---|---|
| 1 | REPL / prompting / slash-command basics | core | U1 (lab) | `vd:cli-basics` |
| 2 | Codebase Q&A, search, `@`-mentions | core | U2 (lab) | `vd:search-refs` |
| 3 | Permissions & permission modes (incl. bypass hazards) | core | U3 (lab) | `vd:permission-modes` |
| 4 | Secret-handling hygiene | core | U3 | `vd:secrets` |
| 5 | Prompt-injection awareness & defense | core | U3 (safety-fenced lab, R10.AC3) | `vd:untrusted-content` |
| 6 | Blast-radius: checkpoints/rewind, sandboxing, dry-runs | core | U3 (intro), U16 | `vd:checkpoint-rewind` |
| 7 | `CLAUDE.md` / memory | core | U4 (lab) | `vd:memory` |
| 8 | Context management (`/context`, `/compact`, `/clear`) | core | U4 | `vd:context-cmds` |
| 9 | Plan mode | core | U5 (lab) | `vd:plan-mode` |
| 10 | Extended thinking | awareness | U5 (mention + pointer) | `vd:thinking` |
| 11 | TDD support / running tests | core | U6 (lab) | `vd:test-run` |
| 12 | Debugging workflow | core | U7 (lab) | — |
| 13 | Git / PR / `gh` integration | core | U8 (lab) | `vd:git-pr` |
| 14 | Multi-file refactoring | core | U9 (lab) | — |
| 15 | Spec-driven workflow | core | U10 (lab — this spec) | — |
| 16 | Code review (`/code-review`) & security review (`/security-review`) | core | U11 (lab) | `vd:review-cmds` |
| 17 | Custom slash commands | core | U12 (lab) | `vd:custom-commands` |
| 18 | Skills | core | U12 (lab) | `vd:skills` |
| 19 | Subagents | core | U13 (lab) | `vd:subagents` |
| 20 | Hooks | core | U14 (lab — enforcement suite, R14) | `vd:hooks` |
| 21 | MCP servers | core | U15 (lab) | `vd:mcp` |
| 22 | Third-party / plugin / marketplace vetting | core | U15 (R10.AC5) | `vd:plugins` |
| 23 | Headless / print mode (`-p`) | core | U16 (lab) | `vd:headless` |
| 24 | CI integration (e.g. GitHub Actions) | core | U16 (lab) | `vd:ci` |
| 25 | Parallel agents / git worktrees | core | U16 (lab) | `vd:worktrees` |
| 26 | Settings / config (`settings.json`) | core | U4 (baseline est. U1, R11.AC4) | `vd:settings` |
| 27 | IDE integrations | awareness | mention + pointer (home unit TBD §6) | `vd:ide` |
| 28 | Output styles / response customization | awareness | mention + pointer | `vd:output-styles` |
| 29 | Enterprise / managed settings | awareness | conceptual only (A4 — learner may lack env) | `vd:managed-settings` |

**Intentional tiering notes (R4.AC5):** rows 10, 27, 28 are awareness-tier (lower frequency for the
target persona); row 29 is demonstrated conceptually per assumption A4. **No capability area is
silently excluded.** This seed is canonical for the area set; the version-resilient detail lives in
`version-data` (§5), not here, so a CLI change touches a bounded set (R12.AC8).

## 5. Version-resilience architecture  → produces `meta/version-data.*` + `meta/version-record.md`  [R12]  ✅ AUTHORED (2026-05-29)

**Version-data file** — `meta/version-data.yaml` (authoritative; `meta/version-data.json` generated for
tooling). Single store of every version-specific detail, referenced **by key**, never duplicated in
prose (R12.AC2/AC8). Schema per entry:

```yaml
permission-modes:                 # the key prose references
  kind: feature                   # command | flag | path | setting | feature | availability
  value: "default, acceptEdits, plan, bypassPermissions"
  provenance: "claude --help / docs"   # how it was checked (R12.AC4)
  verified_version: "2.1.158"          # CLI it was confirmed against
  verified_date: "2026-05-29"
  unverified: false               # true ⇒ rendered with an explicit "unverified" marker (R12.AC3)
  notes: ""
```

**Reference syntax (prose → version-data):** prose uses an inline token **`{{vd:key}}`** wherever a
version-specific value would otherwise be typed. The link-/reference-integrity check (R13.AC4, §8)
fails the build if a `{{vd:key}}` has no matching key. Because the token is plain text, an
unprocessed Markdown viewer still shows a legible placeholder (R15.AC2 graceful degradation).

**Callout convention:** rendered version details use a labelled blockquote, meaning carried by **text**
(not color/emoji alone, R15.AC6):

```markdown
> **⚙️ Version detail (CLI {{vd:_verified_version}}):** the permission modes are {{vd:permission-modes}}.
> *If your `claude --version` differs, see `meta/version-record.md`.* (R11.AC5)
```

**Version record** — `meta/version-record.md`: a table of *last-verified CLI version* + *date* +
*method*, seeded at **2.1.158 / 2026-05-29** (R12.AC5). Bumped on every refresh (R12.AC7).

**Drift-detection check** — `tools/check-version-drift` (§8): compares installed `claude --version`
to `version-record`; where feasible, diffs the current `claude --help` command list against the
committed CLI reference (`cli-reference.json`, §12 — the single recorded command surface) to surface
new/removed/renamed commands (R12.AC6). Doubles as a hooks/CI worked example
(R14.AC2). **Hard rule (R12.AC3):** no `{{vd:*}}` value is authored from model memory — each is
verified against the installed CLI (`--help`/`/help`/docs) or marked `unverified: true`.

**Bounded change surface (R12.AC8):** a CLI version bump touches principally `version-data.yaml`
(+ regen `.json`) and `version-record.md`; prose is principles-first and need not change.

**Exhaustive sibling (R16/R17 → §12):** the *curated* `version-data` (the subset prose references by
key) is complemented by a *generated, exhaustive* CLI reference (`meta/cli-reference.json` →
`course/reference/cli-reference.md`) and a *narrative* per-version **changelog digest**
(`meta/version-changelog.md`). All three are produced/refreshed by the **same drift trigger**; see §12.

## 6. Unit model & curriculum map  → produces `meta/unit-frontmatter.schema.json` + the unit list  [R5, R6]  ✅ AUTHORED (2026-05-29)

**Front-matter schema** — `meta/unit-frontmatter.schema.json` (JSON Schema, lintable by the R13.AC4
check). Every unit's YAML front matter conforms (R6.AC3):

```yaml
id: U5                       # unique, matches catalog
title: "Ship a feature in taskflow-api"
stage: daily-driver          # first-wins | daily-driver | force-multiplier | autonomy-scale
depth_tier: core             # core | awareness
use_case: "Ship a new feature in taskflow-api"
can_do: [C6]                 # capability-map IDs this unit advances (R1.AC4); CV allowed
workflows: [W1]              # workflow IDs exercised (R3); [] for non-workflow units
coverage_areas: [9]          # coverage-matrix row #s touched (R4)
prerequisites: [U2, U4]      # unit IDs (dependency graph, R6.AC5 / R9.AC2)
reading_time_min: 25         # R5.AC6
lab_time_min: 40             # R5.AC6
```

**Tier-adaptive templates** (R6.AC1/AC2) — files `meta/templates/unit-core.md`, `unit-awareness.md`:

| Section (in order) | Core | Awareness |
|---|---|---|
| Front matter (schema above) | ✓ | ✓ |
| Learning objectives (observable verbs, each → can-do, R6.AC4) | ✓ | ✓ |
| Fast-path / TL;DR (R5.AC2) | ✓ | optional |
| Skip-check ("skip if you can already…", as can-do, R5.AC3) | ✓ | optional |
| Concept exposition | ✓ | — |
| ≥1 worked example | ✓ | ✓ (≥1 example *or* mention) |
| ≥1 lab (R7) | ✓ | optional |
| Common pitfalls (learner mistakes on *this task*, R6.AC6) | ✓ | optional |
| Going-deeper pointers | ✓ | ✓ |

All 16 units are **core**-tier (each carries a lab); awareness tiering is applied at the *feature*
level inside the coverage matrix (§4), not by demoting whole units. Distinctions kept separate per
R6.AC6: **pitfalls** = learner mistakes on the task; **anti-patterns** = feature misuse (R4.AC3);
**hazards** = safety (R10). No graded per-unit gate (R6.AC7).

**Unit map & dependency graph** (R9.AC2) — default path is numeric U1→U16; `prerequisites` is the
authoritative ordering constraint (deviation allowed):

| Unit | Stage | Prereqs | Notes |
|---|---|---|---|
| U1 Onboarding & first win | First Wins | — | **onboarding unit (R11)**; establishes baseline `settings.json` + `CLAUDE.md` (R11.AC4) |
| U2 Explore a codebase | First Wins | U1 | light onboarding (W8) |
| U3 Operate safely | First Wins | U1 | **dedicated security unit (R10.AC1)**; pulled forward |
| U4 Memory & context | First Wins | U1 | home of config/memory teaching (R11.AC4) |
| U5 Ship a feature | Daily Driver | U2, U4 | W1 |
| U6 TDD | Daily Driver | U5 | W2 |
| U7 Debug a failure | Daily Driver | U5 | W3 |
| U8 Git/PR | Daily Driver | U5 | W4 |
| U9 Onboard + refactor legacy | Force Mult. | U2, U7 | W5 + W8(deep); legacy repo |
| U10 Spec-driven dev | Force Mult. | U5 | W7; uses this spec |
| U11 Code & security review | Force Mult. | U3, U5 | W6 |
| U12 Commands & skills | Autonomy | U4 | extension cluster |
| U13 Subagents | Autonomy | U12 | |
| U14 Hooks | Autonomy | U12 | enforcement suite = example (R14) |
| U15 MCP & vetting | Autonomy | U3, U13 | R10.AC5 |
| U16 Automate & scale | Autonomy | U8, U14 | W9; headless/CI/worktrees |

The default-path narrative + this graph → `course/units/` and feed the progress checklist (R9.AC5).

## 6.5 Capstone design  → produces `course/capstone/`  [R8]  ✅ AUTHORED (2026-05-29)

The single graded assessment (R8.AC1) — sole graded instrument; units stay instructional (R6.AC7).

- **Brief menu (R8.AC2):** a small menu of choose-your-own briefs (≥3), each a realistic non-trivial
  end-to-end job requiring **context engineering + ≥1 custom extension (command/subagent/skill/hook/MCP)
  + a non-trivial workflow + explicit verification** (R8.AC1). Candidate briefs: (a) add a substantial
  feature to `taskflow-api` spec-first with a custom authoring command; (b) rescue/refactor a slice of
  `taskflow-cli` with a subagent + hook guardrail; (c) build a small MCP integration for the app and
  vet it. Briefs are a Design list, refined in P6.
- **Exemplar (R8.AC2 / R14.AC4):** the "how this course was built with Claude Code" **build case study**
  doubles as the worked exemplar so the learner never faces a blank page.
- **Rubric (R8.AC3/AC4):** dimensions collectively cover **every** can-do C1–C17 + CV; grades the
  **work product** per can-do as *demonstrated / partially / not yet* (never ranks the learner);
  **self-applicable** by a solo learner. Built from `meta/capability-map` so coverage is checkable (R13.AC5).
- **Optional AI-assisted self-grade (R8.AC5):** learner may have Claude score the capstone, then must
  **critique** that grade (trust-but-verify, CV/R10).
- **Verification reflection (R8.AC6):** required structured prompts — one catch, one justified accept,
  one override/redirect.
- **Optional mid-course checkpoint (R8.AC7):** ungraded self-scored challenge after the Daily-Driver
  stage; does not alter capstone-only status.

## 7. Lab & solution architecture  [R7]  ✅ AUTHORED (2026-05-29)

**Primary — `codebases/primary/` (`taskflow-api`)** — FastAPI + SQLModel/SQLite, JWT auth; non-trivial
but tractable (~2–4k LOC), with a real **pytest** suite that starts green (R7.AC1/AC2):

```
taskflow-api/
├─ app/
│  ├─ main.py                # FastAPI app + router wiring
│  ├─ api/routers/           # auth.py users.py projects.py tasks.py
│  ├─ models/                # SQLModel entities (User, Project, Task)
│  ├─ services/              # task/project domain logic
│  ├─ core/                  # config.py security.py (JWT, hashing)
│  └─ db/                    # session, migrations/seed
├─ tests/                    # pytest, fixtures, factory data
└─ pyproject.toml
```
Domain: projects contain tasks (status, assignee, due date); CRUD + filtering/pagination + auth.
Mostly clean; per-lab defects are introduced on lab branches, not baked into `main`.

**Legacy — `codebases/legacy/` (`taskflow-cli`)** — a deliberately messy argparse CLI that "predates"
the API and stores tasks in a JSON file. Authentic accreted complexity for W5/W8 (R7.AC1): one
~800-line god-module, global mutable state, duplicated logic, inconsistent naming, dead code, **no
tests**, and a few real bugs (e.g., naive date parsing, off-by-one in listing, a swallowed exception).
Used by U7 (debug), U9 (onboard + refactor).

**Lab format (R7.AC3):** each lab states **goal · starting state · steps/prompts · objective
self-check**. Conventions:
- **Starting state:** a tagged commit `start/uNN-labM` (clean, reproducible).
- **Reference solution (R7.AC4):** a branch `solution/uNN-labM` (inspectable diff), kept separate from
  the prompt so the learner attempts unaided first.
- **Automated verification (R7.AC5):** `tools/verify-lab.sh uNN-labM` runs the lab's check (e.g.
  `pytest -k`, or a script); where automation is infeasible, the prose self-check (R7.AC3) suffices.
- **Reset (R7.AC6):** `tools/reset-lab.sh uNN-labM` restores the `start/...` tag so the next lab begins
  clean.
- **Offline/mock (R7.AC7):** no required external service or credential; MCP/web labs ship a local mock
  server/fixtures so they run standalone.
- **BYO variant (R7.AC8):** optional stretch on the learner's own repo, clearly marked
  **non-verifiable** (no objective self-check) and never the required path.

**Seeded-defect inventory:** `codebases/SEEDED.md` (maintainer-facing) maps each lab → its seeded
bug/smell and the expected fix, so defects are tracked, not silently scattered. Safety-fenced labs
(e.g. the U3 prompt-injection lab, R10.AC3/AC8) carry an explicit safety note + safe-by-default path.

## 8. Tooling & enforcement  → produces `tools/`  [R11, R12, R13]  ✅ AUTHORED (2026-05-29)

Implemented as a small **Python** `tools/` package (matches the codebases' stack), each check runnable
standalone and via `make check`. The checks are themselves the **worked examples** the hooks/CI units
reference (R14.AC2), so they must be real and clean.

| Tool | Purpose | Req |
|---|---|---|
| `tools/doctor` (+ manual checklist fallback) | Preflight: install, version-floor, auth, a first command (pass/fail). Doubles as a scripting-Claude example. | R11.AC2 |
| `check-frontmatter` | Validate every unit's front matter against `unit-frontmatter.schema.json` | R13.AC4a |
| `check-coverage` | Every can-do (C1–C17+CV) **and** every coverage-matrix area is covered by ≥1 unit/lab | R13.AC4b |
| `check-links` | Internal/external link checking | R13.AC4c |
| `check-version-refs` | Every `{{vd:key}}` in prose resolves to a key in `version-data` | R13.AC4d |
| `check-traceability` | Every R-ID referenced by ≥1 artifact; every can-do → ≥1 lab **and** ≥1 rubric dimension | R13.AC5 |
| `check-version-drift` | Installed `claude --version` vs `version-record`; surface new/removed commands | R12.AC6 |
| `verify-lab` / `reset-lab` | Per-lab automated check + clean reset (see §7) | R7.AC5/AC6 |
| `render-cli-reference` | Generate `meta/cli-reference.json` from recursive `claude --help` ∪ supplement; render `course/reference/cli-reference.md`; `--check` verifies render-freshness + schema + provenance **offline** (§12) | R16 |
| `check-version-changelog` | The recorded verified version has a matching `meta/version-changelog.md` digest entry | R17.AC5 |

**Wiring (R13.AC6):** the same suite runs as **local hooks** (fast authoring feedback — Claude Code
hooks for in-session feedback + a git `pre-commit` hook) **and** in **CI** (GitHub Actions backstop
gate). `check-version-drift` additionally runs on a schedule/trigger to prompt refresh (R12.AC7).
Build order note: **P3 builds these before the content (P5)** so they guard authoring from day one.

**Resilience over hardcoding (R13.AC5, added P8):** `check-traceability` discovers the requirement set
**dynamically** from `requirements.md` (the `### Rn` headings — the single source of truth), not a
hardcoded `R#` range, so a new requirement needs **zero** tool edits; other checks are audited for the
same. The **can-do set stays the closed `C1–C17+CV`** (closed by R1; only the requirement enumeration
grows). See §12.8.

## 9. Repository structure & conventions  [R13, R15]  ✅ AUTHORED (2026-05-29)

Adopted layout (user delegated judgement; adjustable):

```
claude-training/
├─ README.md                      # learner-facing course landing (R1.AC6)
├─ CLAUDE.md                      # dogfooding: project memory (R14.AC1)
├─ specs/claude-code-mastery/     # this spec
│  ├─ requirements.md design.md tasks.md
│  ├─ decisions.md IMPLEMENTATION.md README.md
│  └─ tasks/                      # chunked per-section task files
├─ course/
│  ├─ units/NN-slug/unit.md       # NN = 01..16 (core template; awareness template if ever needed)
│  ├─ capstone/                   # briefs, exemplar (build case study), rubric (§6.5)
│  ├─ progress-checklist.md       # generated from capability-map (R9.AC5)
│  ├─ stuck.md                    # "when you're stuck" recovery (R9.AC4)
│  └─ maintainer-guide.md         # add/update a unit; author-with-Claude recipe (R13.AC3)
├─ codebases/
│  ├─ primary/                    # taskflow-api (R7)
│  ├─ legacy/                     # taskflow-cli (R7)
│  └─ SEEDED.md                   # maintainer-facing defect inventory (§7)
├─ meta/                          # single-source machine-readable artifacts (R13.AC2)
│  ├─ capability-map.{yaml,json}  use-case-catalog.yaml  coverage-matrix.yaml
│  ├─ version-data.{yaml,json}  version-record.md  workflows.md
│  ├─ glossary.md  conventions.md  unit-frontmatter.schema.json  templates/
├─ tools/                         # doctor, checks, drift detection, verify/reset-lab (R13/R12/R7)
├─ .claude/                       # dogfooding: commands, skills, hooks, settings.json (R14)
└─ .github/workflows/             # CI backstop running the check suite (R13.AC6)
```

**P8 additions (§12):** `meta/cli-reference.json` (generated), `meta/cli-reference-supplement.yaml`
(authored), `meta/cli-reference.schema.json`, `meta/version-changelog.md`;
`course/reference/cli-reference.md` (generated); `tools/render-cli-reference`,
`tools/check-version-changelog`.

**Naming conventions (R13.AC1):** units `course/units/NN-slug/` (zero-padded `NN`); meta files
kebab-case; lab tags/branches `start/uNN-labM` and `solution/uNN-labM`; tools kebab-case;
version-data keys kebab-case (`{{vd:key}}`). Documented in `meta/conventions.md`.

**Accessibility & portability (R15):** author in **CommonMark** for core meaning; GitHub
callouts/Mermaid only as graceful-degrading enhancement (R15.AC1/AC2). Diagrams/images carry text
equivalents; **no meaning by color or emoji alone**; semantic headings/lists (R15.AC6). Labs are
**portable-by-default** (macOS/Linux, **WSL** as the v1 Windows story; native Windows out of scope),
platform-specific steps quarantined into marked sections (R15.AC3/AC4). No required lab depends on a
second paid service; Claude Code itself is the exempt prerequisite A1 (R15.AC5).

## 10. Dogfooding plan  [R14]  ✅ AUTHORED (2026-05-29)

Only **authentic** artifacts — genuinely used to build/maintain the course, never props (R14.AC3).
Each is referenced by the unit that teaches its feature (R14.AC2), and references are kept accurate by
`check-links`/`check-version-refs` (R14.AC6):

| Authentic artifact | Referenced by | Req |
|---|---|---|
| **This spec** (`specs/claude-code-mastery/`) | U10 spec-driven dev (the worked example) | R3.AC2, R14.AC1 |
| `CLAUDE.md` (project memory) | U4 memory & context | R14.AC1 |
| Course-authoring **command/skill** | U12 commands & skills; maintainer guide (R13.AC3) | R14.AC1 |
| Enforcement **hooks** + check suite (§8) | U14 hooks | R14.AC2 |
| `check-version-drift` | U12/U16 + U10 maintenance discussion | R12.AC6, R14.AC2 |
| **MCP** config + local mock | U15 MCP & vetting | R14.AC2 |
| `doctor` script | U1 onboarding | R11.AC2, R14.AC2 |
| CI workflow (`.github/workflows/`) | U16 automate & scale | R14.AC2 |
| **Decision log** (`decisions.md`) | maintainers; optional teaching material | R14.AC7 |
| **CLI reference** (`meta/cli-reference.json` → `course/reference/cli-reference.md`) | U4 (single-source version data); U10 (spec-driven build) | R16, R14.AC2 |
| **Version changelog digest** (`meta/version-changelog.md`) | U4 / maintainer refresh trail | R17, R14.AC2/AC7 |

- **Build case study (R14.AC4):** "how this course was built and is maintained with Claude Code"
  (spec-driven workflow + R12.AC7 refresh process) → lives in `course/capstone/` and **doubles as the
  capstone exemplar** (R8.AC2, §6.5).
- **AI-authorship transparency note (R14.AC5):** a short, honest disclosure that parts were authored
  with Claude Code, modeling the responsible-output guidance of R10.AC9.
- **Conflict-of-interest disclosure (R14.AC8):** where the course assesses its own quality — most
  acutely the R18 self-evaluation (Claude assessing a build Claude co-authored) — the prose discloses
  the conflict of interest, what mitigates it, and that it is not eliminated, so a reader calibrates
  rather than trusts. Satisfied in `course/case-studies/collaboration-retrospective.md` (and the build
  case study's framing); a prose-level guarantee, no new check.

## 11. Traceability table  [§8 of requirements]
Fill as sections are completed — every R1–R15 → the design component(s) and artifact(s) that satisfy
it. The R13.AC5 check automates the inverse (every requirement referenced; every can-do → lab + rubric).
**Status:** ✅ = design authored; rows without a mark await their section.

| Requirement | Design section(s) | Primary artifact(s) |
|---|---|---|
| R1 ✅ | §1, §6 | capability-map (C1–C17, CV), progress-checklist |
| R2 ✅ | §2 | use-case-catalog (U1–U16) |
| R3 ✅ | §3, §6, §7 | workflows.md (W1–W9), units, labs (all 9 mapped in §2) |
| R4 ✅ | §4 | coverage-matrix (29 areas seeded) |
| R5 ✅ | §6 | front-matter schema (time estimates, tiers), templates (fast-path/skip-check) |
| R6 ✅ | §6 | front-matter schema, core/awareness templates |
| R7 ✅ | §7 | codebases (taskflow-api/-cli), lab format, solution branches, reset, SEEDED.md |
| R8 ✅ | §6.5 | capstone brief menu, exemplar (build case study), self-applicable rubric |
| R9 ✅ | §6, §6.5 | dependency graph, progress-checklist (gen), stuck.md, self-applicable rubric |
| R10 ✅ | §2, §3, §6, §7 | security unit U3, injection lab (§7), woven CV verification (§1/§3) |
| R11 ✅ | §6, §8 | doctor (§8), onboarding unit U1, baseline config (R11.AC4) |
| R12 ✅ | §5, §8 | version-data, version-record (2.1.158), drift check, `{{vd:key}}` convention |
| R13 ✅ | §8, §9 | check + traceability suite, conventions, maintainer guide |
| R14 ✅ | §10 | dogfooding inventory, build case study, transparency note, COI disclosure (AC8 → collaboration retrospective) |
| R15 ✅ | §9 | CommonMark/a11y/portability conventions |
| R16 ✅ | §12, §8 | `render-cli-reference`, `cli-reference.json` + supplement + schema, `course/reference/` page |
| R17 ✅ | §12, §8 | `version-changelog.md` + `check-version-changelog`, refresh-process step |
| R18 🟨 | §13 | persona panel (`.claude/agents/`), `log/evaluations/**` (matrix: leaf + per-session + per-reviewer globals + overall corner), `course/case-studies/collaboration-retrospective.md`; referenced by U13 + §10 |
| R19 ⏳ | _design deferred_ | breadcrumb nav — approved requirement; design pending (deferred by user until R18 ships) |

## 12. Exhaustive CLI reference & version-change digest  → produces `meta/cli-reference.*`, `course/reference/cli-reference.md`, `meta/version-changelog.md`  [R16, R17]  ✅ AUTHORED (2026-05-31)

Two composing version-resilience enhancements, both fired by the **same drift trigger** as §5. **R16**
produces an *exhaustive, generated* CLI option reference — the structural complement to §5's *curated*
`version-data`; **R17** produces a *narrative* per-version changelog digest. **Scoping (R16/R17 are infra
+ dogfooding):** neither adds a new can-do, lab, or coverage area, so §4 / §6.5, `check-coverage`, and
traceability *part B* (can-do → lab + rubric) are untouched (§12.8). Future enhancements get their **own**
requirement + phase, never bolted onto R16.

### 12.1 Pipeline & tool modes (R16)

```
claude --help (recursive over subcommands) ─┐
                                            ├─►[--generate]─► meta/cli-reference.json ─►[--render]─► course/reference/cli-reference.md
meta/cli-reference-supplement.yaml ─────────┘                (authoritative, merged,                 (learner-facing,
        (hand-authored doc-only surface)                      provenance-tagged, byte-stable)          generated)
```

One tool — `tools/render-cli-reference` — with explicit modes, so the **expensive** recursive
introspection is isolated from the **pure/offline** render and never duplicated:

| Mode | Action | Needs CLI? |
|---|---|---|
| `--generate` | Introspect `claude --help` recursively ∪ supplement → write `meta/cli-reference.json` | yes |
| `--render` | Read the json **+ `meta/version-changelog.md`** → write `course/reference/cli-reference.md` | no |
| `--all` | `--generate` then `--render` (the drift/refresh entrypoint, R16.AC5) | yes |
| `--check` *(default)* | Offline: re-render from committed json + changelog + diff vs committed md; validate json vs schema + provenance present. The `make check` gate. | no |
| `--check --cli` | Also re-introspect + diff the json (machine freshness); refresh/strict path only | yes |

The costly `claude --help` sweep runs **only** in `--generate`/`--all`; every gate path (`--check`) reads
the committed json, so `make check` stays cheap and offline-safe (R16.AC6).

### 12.2 Machine artifact — `meta/cli-reference.json` (generated, committed, authoritative; R16.AC1/AC4)

The fully-merged union other tooling reads as the single source of CLI-surface truth:

```json
{
  "schema_version": 1,
  "cli_version": "2.1.158",
  "root": {
    "name": "claude", "path": [], "usage": "...", "description": "...",
    "source": "cli-help", "provenance": "claude --help",
    "flags": [ { "names": ["-p","--print"], "arg": null, "description": "...",
                 "choices": null, "default": null, "source": "cli-help", "provenance": "claude --help",
                 "added_in": null } ],
    "commands": [ { "name": "mcp", "path": ["mcp"], "usage": "...", "description": "...",
                    "source": "cli-help", "provenance": "claude mcp --help", "added_in": null,
                    "flags": [ ], "commands": [ ] } ]
  },
  "supplement_sections": [
    { "title": "In-REPL slash commands", "provenance": "<doc URL> (retrieved 2026-05-31)",
      "entries": [ { "name": "/rewind", "description": "...", "source": "supplement",
                     "provenance": "<doc URL> (retrieved 2026-05-31)" } ] }
  ]
}
```

**Byte-stability (R16.AC6):** the artifact carries `cli_version` (stable per version) but **no
generated-date** — the date lives in `version-record.md` (its existing home, §5). Same CLI + same
supplement ⇒ byte-identical output. Emission: `json.dumps(indent=2, ensure_ascii=False, sort_keys=True)`;
**lists preserve CLI/file order** (deterministic per version); single trailing newline. Validated against
a committed `meta/cli-reference.schema.json` (JSON Schema, lintable like `unit-frontmatter.schema.json`).

**Inline "new since the last version" marking (`added_in`; decision P8-added-in):** each command and
flag carries an optional `added_in: <version>` — the CLI version at which it first appeared — so a new
option is flagged **inline in its own table row** (§12.5), not only in the top "What's new" digest. The
generator computes it by **diffing the freshly-introspected tree against the previously-committed
`cli-reference.json`** (matching commands by `path`, flags by `path` + `names`): an entry absent from the
prior reference, when `cli_version` has bumped, is stamped `added_in: <new cli_version>`; existing
markers are **carried forward** unchanged. This is **verified by construction** — it reflects a real
introspected-surface delta, not memory (R12.AC3) — and stays byte-stable (regenerating at the same
version diffs against the now-current committed json ⇒ no new entries, markers preserved ⇒ identical
bytes, R16.AC6). `added_in` is **omitted when null** (so adding the field doesn't perturb the current
artifact); on the first generation (no prior reference) nothing is marked.

### 12.3 Authored supplement — `meta/cli-reference-supplement.yaml` (R16.AC3/AC4)

The **only** hand-edited file in the pipeline; mirrors `version-data.yaml`'s provenance discipline. Holds
**doc-only surface** `claude --help` cannot see (in-REPL slash commands, output styles, …), grouped into
titled sections, each entry tagged with a **doc URL + retrieval date**. The generator marks introspected
entries `source: cli-help` and supplement entries `source: supplement`; it never invents CLI flags. **No
entry from model memory (R12.AC3).**

### 12.4 Generator algorithm

Reuses (and lifts into `tools/_common.py`) the `Commands:`-section parser already in `check-version-drift`:
1. `claude --help` → parse `Usage:`, description, `Options:` (flags), `Commands:` (subcommands). Flag
   rows: 2-space-indented lines starting `-`; deeper-indented wrapped descriptions folded in.
2. For each subcommand, `claude <path…> --help`, recursing (e.g. `claude mcp add --help`). Depth-capped;
   skip the `help` pseudo-command; per-call timeout; tolerant of help-shape drift (records the raw
   `usage` even when a sub-section doesn't parse).
3. Union the supplement; write the json. The `--check --cli` freshness diff is the **canary** when a new
   CLI version changes the help shape.
4. **Delta-mark (`added_in`):** before writing, diff the new tree against the previously-committed
   `cli-reference.json` and stamp `added_in` on commands/flags that newly appeared at a bumped
   `cli_version`, carrying existing markers forward (§12.2). Pure data step over the two committed
   artifacts — no extra CLI calls.

### 12.5 Human render — `course/reference/cli-reference.md` (R16.AC2 + R17 learner surface)

Rendered from committed machine sources — `meta/cli-reference.json` (the exhaustive option reference,
R16) **and** `meta/version-changelog.md` (the version-change digest, R17); the page is never
hand-edited. CommonMark (R15): a "⚙️ Generated — do not edit; regenerate via `tools/render-cli-reference
--all`" banner carrying `cli_version` in **text**; a **"What's new" section** near the top surfacing the
latest changelog entry + a link to the full digest (the R17 learner-facing surface — decision
P8-r17-surface); a TOC; nested command sections (heading depth = command depth) with **flag tables**;
then supplement sections with doc-URL provenance inline (introspected vs doc-sourced visible in text,
R16.AC3). Valid anchors (passes `check-links`). Commands/flags carrying `added_in` (§12.2) are flagged
**inline** with a text marker (e.g. `🆕 new in 2.1.x`, plus a word so meaning isn't emoji-only, R15) in
their heading / table row — so a new option is visible at its point of use, complementing the top
"What's new" digest.

**On R16.AC2 ("rendered from the machine source alone"):** the *option reference* (commands / flags /
arguments / supplement) is still a pure function of the json; the "What's new" section is the **R17**
digest's rendered view, co-located on the same page per the learner-visibility decision. The two
requirements stay distinct — each keeps its own ACs and check (R16's freshness gate; R17's
`check-version-changelog`) — only their learner-facing *views* share one page, and both inputs are
committed machine truth, so the page remains generated, never hand-authored.

### 12.6 Version-change digest — `meta/version-changelog.md` (R17)

A running, maintainer-facing digest, companion to the bare `version-record.md` table. Per refresh, a
**cumulative** entry spanning every version strictly after the last recorded verified version through the
new one (R17.AC2), each carrying the **changelog/release-notes URL + retrieval date** (R17.AC3); an
unreachable source is **marked, not fabricated**. Each entry **flags content-affecting changes** —
new/removed/renamed commands or flags, changed defaults, deprecations — cross-referenced to the affected
`{{vd:key}}` and the regenerated reference (R17.AC4), bounding the review surface. Entry shape:

```markdown
## 2.1.158 → 2.3.10  (digest retrieved 2026-09-01 from <changelog URL>)
- **2.2.0** — <synopsis>. _Course impact:_ none.
- **2.3.0** — new `claude foo` command; `--bar` default changed. _Course impact:_ {{vd:permission-modes}}, cli-reference regen.
```

The first recorded version takes a **baseline** entry (no prior to diff against):
`## 2.1.158 (baseline — <date>, from <changelog URL>)`.

Sourcing uses WebFetch of the official notes at refresh time (R12.AC3 provenance). **Enforced** by
`tools/check-version-changelog` (R17.AC5): the top `version-record.md` version has a matching digest
entry — a version bump without its synopsis fails the suite. Because the check keys off the **recorded**
verified version, the digest must always carry a matching entry for it (the baseline above, until the
first real bump).

**Learner-facing surface (decision P8-r17-surface):** beyond the maintainer digest, the render lifts the
digest's latest entry into the **"What's new" section** atop `course/reference/cli-reference.md` (§12.5)
so learners see version changes alongside the reference. The digest file stays the single source — the
page reads it, never duplicates it.

### 12.7 Drift & refresh integration (R16.AC5, R17.AC1)

The R12.AC7 refresh process (in `version-record.md`) gains two standing steps: **(a)**
`tools/render-cli-reference --all` — regenerate the machine reference + re-render the page; **(b)** add
the cumulative `version-changelog.md` digest entry. Both touch only generated/maintainer artifacts
(R12.AC8); the reference is **bootstrapped by the drift trigger, not hand-maintained**.
`check-version-drift`'s cheap top-level command-list diff reads its recorded surface directly from
`cli-reference.json` (the former names-only `cli-commands.snapshot` was folded into it — L10 closed);
the full `render-cli-reference --check --cli` re-introspection is the deeper freshness gate.

### 12.8 Enforcement & resilience (R13, R16.AC6, R17.AC5)

New gates joined to `make check` / the Claude Code hook / CI (R13.AC4/AC6): `render-cli-reference --check`
(offline render-freshness + schema + provenance) and `check-version-changelog` (R17.AC5). `--check --cli`
joins `check-version-drift --strict` on the refresh/scheduled trigger only (offline-safe CI).

**Resilience over hardcoding (the generalization, R13.AC5).** Rather than bump `check-traceability`'s
hardcoded `R1–R15` regex per new requirement, **generalize it to discover the requirement set dynamically
from `requirements.md`** (the `### Rn` headings — single source of truth). New requirements (R18, R19, …)
then need **zero** tool edits. Other checks are audited for hardcoded `R#` ranges and given the same
treatment. The **can-do set stays the closed `C1–C17+CV`** — closed by R1's design; only the *requirement*
enumeration grows, so only it goes dynamic. This is an R13 robustness improvement *triggered by* R16/R17,
**not** part of R16's feature scope.

### 12.9 Dogfooding & enhancement playbook (R14, R13.AC3)

Two **light** titled cross-ref pointers (authored in `unit.src.md`, re-rendered via `render-units`; no
bare codes, per the P7 prose conventions): **U10** — a callout that this reference was built spec-driven
(R16/R17 → §12 → `tasks/P8` → implementation), a *process* example; **U4** — a pointer to
`meta/cli-reference.json` as the exhaustive single-source sibling of `version-data.yaml`, an *artifact*
example. New §10 inventory rows (above). A new **"Adding a post-v1 enhancement"** subsection in
`course/maintainer-guide.md` codifies the repeatable pattern — additive requirement → new `tasks/P{N}`
file → `decisions.md` entry + 🔓 ledger → *generalized*, not hardcoded, enforcement; the §12.6 changelog
step — so the process is resilient to future enhancements (R13.AC3).

### 12.10 Repo additions (§9)

```
meta/cli-reference.json              # generated machine truth (R16.AC1)
meta/cli-reference-supplement.yaml   # authored doc-only surface + provenance (R16.AC4)
meta/cli-reference.schema.json       # JSON Schema for the machine artifact
meta/version-changelog.md            # per-version changelog digest (R17)
course/reference/cli-reference.md    # generated learner-facing page (R16.AC2)
tools/render-cli-reference           # generate | render | all | check (§12.1)
tools/check-version-changelog        # digest-entry-exists check (R17.AC5)
```

## 13. Collaboration retrospective  → produces `.claude/agents/*`, `log/evaluations/**`, `course/case-studies/collaboration-retrospective.md`  [R18]  🟨 PROPOSED (2026-05-31)

A multi-perspective, self-evaluating retrospective of how this course was actually built with Claude
Code: a panel of **subjective persona subagents** (plus a no-persona control) reads the real session transcripts and renders
verbose, evidence-cited, candid insights — what the **human author** and **Claude** each did well, did
okay on, and could improve, across **process/workflow** and **human-language communication** (R18.AC1).
It is **authentic dogfooding** (R14): the reviewers are real `.claude/agents/` the repo runs, and the
build itself follows the post-v1 enhancement playbook (R13.AC3).

### 13.1 Two deliverables, the evaluation matrix (R18.AC6/AC8)

| Deliverable | Audience | Lives in |
|---|---|---|
| **Evaluation corpus** (the leaf evals + syntheses) | maintainer / internal record | `log/evaluations/**` |
| **Case study** (derived narrative) | learner (capstone exemplar) | `course/case-studies/collaboration-retrospective.md` |

The Tier-1 evals form a **23-session × 11-reviewer matrix**, summarized along both margins and then to a
bottom line (R18.AC6); each artifact is derived from and traceable to the ones beneath it:

```
LEAF (cells)    log/evaluations/<session>/<reviewer>.md   — CACHED, immutable once written
MARGIN · rows   log/evaluations/<session>/_synthesis.md   — all reviewers × one session  (per-session synthesis)
MARGIN · cols   log/evaluations/_global/<reviewer>.md     — one reviewer × all sessions  (each synthesizes its OWN 22 leaves)
CORNER          log/evaluations/_global/_overall.md       — blends the per-reviewer globals → bottom line
                  └─► course/case-studies/collaboration-retrospective.md   (learner-facing render of the corner)
```

`<session>` = the transcript filename stem (e.g. `2026-05-30_0816-p4-sample-codebases`); `<reviewer>` =
the persona id (e.g. `process-architect`). "Cached" = a leaf eval is written once, committed, and
treated as immutable evidence; it is **not** regenerated (re-running a persona is a new, dated file, not
an overwrite). Every synthesis (both margins + the corner) carries verbose cross-cutting insights **and**
roll-up grades (R18.AC2/AC3/AC6).

### 13.2 The persona panel (R18.AC4) — proposed

Eleven reviewers, each a real `.claude/agents/<id>.md`: **ten personas** that each span **both axes** and
judge **both parties** through a distinct, opinionated lens, plus **one no-persona control** (below). The
cut is balanced across the two R18 axes — **5 process · 3 communication · 2 cross-cutting** — and merges
the redundant overlaps. Remaining deliberate overlaps (e.g. verification vs. safety) are a feature: two
perspectives on the same moment make the Tier-2 synthesis richer.

| Reviewer id | Persona | Axis | Primary lens (what it praises / faults) |
|---|---|---|---|
| `process-architect` | The Process Architect | process | Spec-driven discipline: planning before building, holding gates, state hygiene (decisions/ledger/§3 upkeep), slicing |
| `context-engineer` | The Context Engineer | process | Memory (`CLAUDE.md`) & context-window management: priming, slicing per unit, avoiding context dumps, cross-session continuity |
| `verification-hawk` | The Verification Hawk | process | Verify-don't-trust: checking claims, reading diffs, the no-version-from-memory rule, **verifying before acting**, honest uncertainty |
| `tooling-economist` | The Tooling Economist | process | CLI/feature fluency **and** economy: right tool at the right time (subagents, hooks, plan mode, headless, MCP), model fit (opus-vs-sonnet), wasted turns / rework / tool-call batching, missed opportunities |
| `safety-steward` | The Safety Steward | process | Responsible use: approval discipline (no commit/push without go-ahead), blast radius, untrusted input, reversibility |
| `intent-alignment` | The Alignment Reviewer | communication | Converging on **what** to build: ambiguity, the clarifying-question-vs-assumption dynamic, requirement elicitation, scope agreement, convergence speed |
| `dialogue-clarity` | The Communication Coach | communication | Clarity of the **exchange, both directions** — the human's instruction quality (scope, decisiveness, feedback) **and** Claude's replies (tradeoffs surfaced, concision/structure, honest failure reporting, **no sycophancy**) |
| `collaboration-partner` | The Pair-Programming Partner | communication | The working relationship: autonomy calibration (delegate vs. over-ask), the correction loop, trust calibration, momentum vs. derailment |
| `outcome-auditor` | The Outcome Auditor | cross-cutting | The work **product**, not just the process: did the spec/code/prose come out correct and sound; bugs or sloppy artifacts that slipped through |
| `devils-advocate` | The Devil's Advocate | cross-cutting | Contrarian stress-test: challenges rosy reads, hunts what the other reviewers missed, guards against over-generous grading |
| `control` | _(no persona — baseline)_ | — | **Control instrument.** Default Claude given **only** the evaluation task + the output contract — **no persona lens, no candor mandate** — to measure the marginal effect of the persona scaffolding on the other 10 |

**On the control (R18.AC5 scope note).** The control is a deliberate baseline: it follows the §13.4
output contract (so it is comparable) but intentionally **omits** the persona lens and the
subjective/candor mandate of R18.AC5. R18.AC5's "every reviewer" is read as the **ten persona
reviewers**; the control sits alongside the panel as a baseline instrument, not a persona reviewer. This
scoped exception is recorded in `decisions.md` (it does not require amending the approved R18 — but AC5
can be tightened to "every persona reviewer" if preferred). Corpus scale: **11 reviewers × 23 sessions =
253 leaf evals**, accreted one session at a time (the maintainer's stated workflow). (Corpus frozen at
the 23 sessions present at P9 start, 2026-05-31.)

This panel **retires the gap noted in decision P5-U13-example** (the repo had no authentic subagent to
show in U13); it now does, so U13 references the panel as its real worked example (R14.AC2, R18.AC4).

### 13.3 Agent definition format (R18.AC4/AC5; R12.AC3)

Each reviewer is a file `.claude/agents/<id>.md`: front matter (`description` — *when the orchestrator
dispatches it*; `tools: [Read, Grep, Glob, Write]` — **least-privilege**: it reads transcripts and writes its one leaf file, nothing more (no Bash/Edit/network), blast-radius fenced per U13/U3; a `model`),
and a body carrying the **shared reviewer mandate** + its **persona lens**. The shared mandate (single-
sourced wording, repeated per agent since agents don't `include`):

- **Subjective and candid (R18.AC5).** Render a real opinion through your lens. Do **not** flatter,
  soften to please, or discourage. Praise what genuinely worked; name what genuinely didn't. Accuracy
  and thoroughness over diplomacy.
- **Evidence-grounded (R18.AC5).** Every insight cites transcript evidence — the session slug + a
  locator (turn heading or a short quoted snippet). Never assert from memory; if the transcript doesn't
  show it, don't claim it.
- **Both parties, both directions.** Assess the human author **and** Claude; cover strengths **and**
  weaknesses (no one-sided reviews).
- **Output contract** (§13.4): verbose, significance-ordered insights + a compact grade block.

> **Version-currency (R12.AC3).** The `.claude/agents/<name>.md` path and front-matter fields are a
> filesystem **convention** (per U13 / `{{vd:subagents}}`); confirm the exact schema against
> `claude --help` and the docs at build time rather than authoring it from memory.

### 13.4 What a reviewer reads, and the leaf-eval format

**Evidence source.** Primary = the **rendered** transcript `log/transcripts/rendered/<session>.md` (the
full turn-by-turn human↔Claude exchange, readable and citable by heading). A reviewer **may** consult
the raw `log/transcripts/raw/<session>.jsonl` for a specific turn when the rendered view is insufficient
(thinking is collapsed and tool output truncated to 40 lines in the render). Each dispatch is told the
session's **verified model attribution** (R18.AC7), read from the raw `.jsonl` `.message.model` field —
not assumed. Verified 2026-05-31: **all 23 sessions ran on `claude-opus-4-8`**, except the foundational
`2026-05-29_1845…` session, which is **mixed/opus-dominant** (sonnet-4-6 for its first 2 turns, then
opus for the remaining 222) — the only mixed-model session, attributed opus with a sonnet-start flag.
(An earlier "foundational = sonnet" reading was an assumption and was wrong; see decision `P9-model-attr`.)

**Leaf file = `log/evaluations/<session>/<reviewer>.md`.** A small machine-parseable YAML front matter
(for Tier-2/3 aggregation) over a verbose prose body:

```
---
session: 2026-05-30_0816-p4-sample-codebases
reviewer: process-architect
model_evaluated: claude-opus-4-8
grades:                      # did-well | did-okay | could-improve  (R18.AC3)
  human:   { process: did-well, communication: did-okay }
  claude:  { process: did-okay, communication: did-well }
  overall: did-okay
---
## Insights (ordered by significance)        # the substance — R18.AC2
1. **<headline>** — <verbose reasoning>. _Evidence:_ <session locator / quote>.  [human|claude] [process|comms]
2. ...
## What worked / what didn't  (both parties)
## Bottom line
```

The grade block is a scannable **summary** that never replaces the prose (R18.AC3). The body is
free-length: as long as the evidence warrants.

### 13.5 Producing each tier

- **Leaf (cells).** The main session (orchestrator) dispatches each panel agent on one session;
  each agent **writes its own leaf file** (to a predetermined path) and returns only a short receipt, so the
  evaluation never round-trips through the orchestrator (the token + latency fix — decision **P9-leaf-write**,
  which relaxes the original read-only contract to least-privilege `+Write`); the orchestrator validates the
  written files and re-dispatches any that fail, and **commit stays the maintainer's call** (agents write, never
  commit). The human drives this **one session at a time** (their stated
  workflow), so the corpus accretes per session and stays reviewable.
- **Per-session synthesis (reviewer-axis margin).** Once a session's reviewers all exist, consolidate
  them into `_synthesis.md`: the cross-cutting story, where reviewers **agreed and disagreed**,
  consolidated per-party/per-axis grades, both parties. Cites the leaves (traceable, R18.AC6).
- **Per-reviewer global (session-axis margin).** Once **all** sessions' leaves exist, **each reviewer is
  re-dispatched over its own ~23 leaves** to write `_global/<reviewer>.md`: the longitudinal arc in *its*
  lens (did this dimension improve across the sessions? recurring strengths/failure modes per party; the
  sonnet-vs-opus caveat). Reading only its own leaves (~55k tokens) keeps each global **deep and cheap**,
  and the lens voice survives to the global level instead of being averaged away. The control does the
  same over its own leaves (extending the baseline experiment to the longitudinal view).
- **Overall global (corner).** A final pass blends the per-reviewer globals (+ control) into
  `_global/_overall.md`: the bottom line and the top did-well/okay/could-improve themes across the whole
  project. The learner-facing `course/case-studies/collaboration-retrospective.md` is the **teaching
  render** of this corner (R18.AC8), cross-referenced as capstone-exemplar material (R8.AC2, R14.AC4)
  alongside the existing build case study.

### 13.6 Orchestration (dogfood) — adopted

A thin **`/evaluate-session <session-slug>`** command (`.claude/commands/`) dispatches the panel
over one session; each reviewer **writes its own leaf file** (least-privilege `+Write`, decision **P9-leaf-write**) — an authentic R14 dogfood (commands, U12) that also
exercises subagents (U13) and parallel delegation (U16). The command also records the session's verified
model attribution (§13.4) so each reviewer is told which model it is judging. A sibling
**`/evaluate-global`** command runs the margin/corner passes once every session's leaves exist: it
re-dispatches **each reviewer over its own ~23 leaves** to write `_global/<reviewer>.md`, then a final
pass writes the corner `_global/_overall.md`. Both commands dispatch reviewers **in parallel** (U16) for
wall-clock — not token — savings.

### 13.7 Cost & feasibility (grounded, 2026-05-31)

Measured against the actual `log/transcripts/rendered/` corpus (not estimated):

- Rendered corpus ≈ **1.11M tokens** across 23 sessions; mean ≈ 48k/session; range ≈ 14k (smallest, the
  L1 verification session) to ≈ 127k (the P7 closeout session, a 494 KB outlier). (token ≈ bytes/4 —
  rough, and a likely **floor** for markdown + code + tool output. Re-measured 2026-05-31 over the frozen
  23-session corpus.)
- **Subagents do not share the orchestrator's context** — each runs in its own fresh window — so a
  session transcript is read once **per reviewer**. Leaf tier, whole corpus: 11 × 1.11M ≈ **~12M
  tokens** of transcript input; with per-subagent overhead and the two synthesis tiers, the full
  one-time pass is on the order of **~13–17M tokens**.
- **Fit is not a constraint:** the largest transcript (≈127k) is **12.7%** of a single 1M window — ample
  headroom. The cost here is *spend*, not overflow.
- **Never one big run:** the pass is driven session-by-session, so each invocation is one session's
  panel (≈159k–1.4M tokens) — an ordinary run.
- **The global tier is cheap:** each per-reviewer global reads only its own ~23 leaves (~55k tokens) →
  ~11 × 55k ≈ **~0.7M tokens** for the whole column margin; the corner blends eleven short globals
  (negligible). So the per-reviewer-global structure (§13.5) adds only ~5% to the pass — well worth the
  preserved lens depth, and far cheaper than a single agent re-reading all 253 leaves (~630k in one
  shallow-blending context).

**Independence vs. economy — a deliberate call.** A single agent reading each transcript once and
emitting all eleven evals would be ~11× cheaper, but the personas would anchor on one another and the
**control would see the persona evals**, destroying both reviewer independence and the control
experiment (§13.2). We therefore **keep one fenced subagent per reviewer** and accept the ~11× read cost
as the price of the rigor R18 is built on. Two economy guards are load-bearing: **rendered-primary,
raw-on-demand** (§13.4 — reading raw `.jsonl` whole would be ~8.9M × 11, untenable) and **tightly-fenced
agents writing their own leaves** (least-privilege `Read, Grep, Glob, Write` — no Bash/network churn, and the
leaf never round-trips through the orchestrator; decision **P9-leaf-write**). Reviewers may be dispatched **in
parallel** per session (U16) for wall-clock — not token — savings.

### 13.8 Honesty, provenance, safety & enforcement (R18.AC5/AC9/AC10)

- **Provenance.** Insights cite the transcript; the model attribution is read from the `.jsonl`, not
  assumed. References to `log/transcripts/` stay accurate (R14.AC6, `check-links`).
- **Secrets.** The transcripts already passed the capture workflow's secret-scan gate; the new eval
  files quote already-scanned material — run `tools/scan-secrets` over `log/evaluations/**` before each
  commit anyway (R18.AC10), human-reviewing any flag.
- **Enforcement, generalized (R18.AC9; playbook step 5).** `check-traceability` already discovers `R18`
  from its `### R18` heading and requires it be referenced by a delivered artifact — satisfied by the
  case study, U13's panel reference, and the §10 dogfooding rows. **Plus a completeness gate,
  `tools/check-evaluations`** — discovery-based (expected sessions from `log/transcripts/rendered/*.md`,
  expected reviewers from `.claude/agents/*.md`; no hardcoded lists): every session has all reviewer
  leaves + a `_synthesis.md`, and once all sessions are covered, a `_global/<reviewer>.md` per reviewer +
  the `_global/_overall.md` corner. It follows the repo's `PEND`/`--strict` pattern — an **informational
  progress readout** (non-failing) in `make check` so the legitimate incremental build stays green, and a
  **hard fail in `make check-strict`** until the corpus is whole. This covers what traceability cannot:
  `check-traceability` is satisfied the moment R18 is *referenced* (even by an empty corpus); the gate
  makes a *complete* corpus the real "R18 done" signal, and self-maintains as transcripts or the roster
  change.

### 13.9 Repo additions (§9) and dogfooding/traceability updates

```
.claude/agents/<11 reviewers>.md                      # 10 persona reviewers + 1 no-persona control (R18.AC4)
.claude/commands/evaluate-session.md                  # leaf-tier orchestration dogfood (§13.6)
.claude/commands/evaluate-global.md                   # margin/corner orchestration dogfood (§13.6)
log/evaluations/<session>/<reviewer>.md               # leaf evals — cells (cached)
log/evaluations/<session>/_synthesis.md               # per-session synthesis (reviewer-axis margin)
log/evaluations/_global/<reviewer>.md                 # per-reviewer global (session-axis margin)
log/evaluations/_global/_overall.md                   # overall global (corner) -> case study
log/evaluations/README.md                             # corpus orientation + protocol
course/case-studies/collaboration-retrospective.md    # learner-facing render of the corner (R18.AC8)
tools/check-evaluations                               # corpus completeness gate (PEND in check / fail in strict)
```

§10 dogfooding inventory gains: **persona panel** (`.claude/agents/`) → referenced by **U13**
(R14.AC2, R18.AC4); **collaboration retrospective case study** → capstone exemplar (R8.AC2, R14.AC4).
`meta/conventions.md` gains the `log/evaluations/` layout + `<session>/<reviewer>.md` naming (R13.AC1).
Build plan: `tasks/P9-collaboration-retrospective.md`.
