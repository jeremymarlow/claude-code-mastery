# Requirements — Claude Code Mastery Course

**Spec:** `claude-code-mastery`
**Phase:** Requirements (Phase 1 of 3) — ✅ **APPROVED** (2026-05-29); Design unblocked
**Target product:** Claude Code CLI — **current/latest version** (version-resilient; see R12)
**Last updated:** 2026-05-29
**Status:** ✅ APPROVED — IDs frozen; changes now require a recorded decision (see `decisions.md`)

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for a self-contained training course — **"Claude Code Mastery"** — that takes a *seasoned software developer who is new to AI-assisted coding* and brings them to *elite Claude Code practitioner*: someone who fluently handles real-world use cases with Claude Code, choosing the right workflow and feature for each job, using industry-tested best practices.

### 1.2 Product summary
The course is delivered as a **single Git repository** containing:
- **Markdown units**, each built around a real-world **use case** (job-to-be-done),
- **Hands-on labs** run against two sample codebases (a primary and a small legacy repo) the learner clones and modifies,
- **Reference solutions** for every lab (as inspectable git artifacts),
- A single **graded capstone** (the sole assessment), with a rubric covering the full capability map.

The course is **self-paced and solo**, **outcome-driven**, **tiered for experienced engineers**, and **version-resilient** (it targets the latest CLI and is built to be refreshed as the tool evolves — using this very spec).

### 1.3 Scope
**In scope:** the use-case curriculum, workflow methods, the feature-coverage guarantee, lab design, the sample codebases, the capstone and rubric, learner-facing docs, and the course's own update/maintenance machinery.

**Out of scope:** building Claude Code itself; hosting/LMS; video production; paid certification/proctoring; facilitator/cohort/instructor materials; per-unit graded assessments; teaching general programming, Git, or terminal basics; localization (English only for v1).

### 1.4 Target persona
**"Sam," the learner:** 5+ years professional software development; fluent with the terminal, Git, and at least one mainstream language; a quick study who resents hand-holding; has used a chat LLM casually but never an agentic coding tool in earnest; skeptical of AI output and wants to learn to *verify*, not merely *trust*. Sam works through the course **alone** and **values their time**.

### 1.5 Definition of "elite" (the bar this course must clear)
An elite practitioner can, without hand-holding: select and execute the right workflow for a real use case; engineer context deliberately; extend Claude Code with custom commands, subagents, skills, hooks, and MCP servers; automate it headlessly and in CI; operate it safely (permissions, secrets, prompt-injection awareness); critically verify its output; and reason about *when and why* to use each capability.

---

## 2. Definitions & conventions

| Term | Meaning |
|---|---|
| **The course** | The product being specified (the "system" in EARS statements). |
| **Use case** | A real-world job-to-be-done the learner accomplishes with Claude Code (e.g., "onboard to an unfamiliar codebase"). The **primary** organizing axis. |
| **Unit** | A top-level curriculum module, each centered on one use case. |
| **Workflow** | A reusable method/pattern (e.g., explore→plan→code→commit, TDD, spec-driven) used to accomplish use cases. |
| **Feature** | A Claude Code capability (command, subagent, skill, hook, MCP, etc.) — a *tool* used within workflows. |
| **Lab** | A runnable practice exercise (ungraded) with objective self-check success criteria. |
| **Capstone** | The single, end-to-end, graded project — the **sole** assessment. |
| **Can-do statement** | An outcome-phrased capability the learner can demonstrate (e.g., "I can run a multi-file change end-to-end and verify the result myself"). Describes *the work*, never ranks the person. The atomic unit of progress. |
| **Capability map** | The full set of can-do statements, the territory the course covers (replaces the earlier "ladder"; no person-ranking). |
| **Stage** | A neutral grouping of can-do statements named for the *relationship with the tool* — **First Wins → Daily Driver → Force Multiplier → Autonomy & Scale** — used for shape/orientation, not as a verdict on the learner. |
| **Depth tier** | A unit's coverage level: **core** (deep, hands-on) or **awareness** (brief, named, pointers). |
| **Version-specific detail** | An exact command, flag, path, settings key, or feature-availability claim that can change between CLI versions. |

**EARS keywords:** `THE COURSE SHALL` (ubiquitous), `WHEN … THE COURSE SHALL` (event), `WHILE … THE COURSE SHALL` (state), `IF … THEN THE COURSE SHALL` (unwanted condition), `WHERE … THE COURSE SHALL` (optional/feature-gated).

**IDs** (`R<n>` / `R<n>.AC<m>`) are frozen as of this revision for traceability into `design.md` and `tasks.md`.

---

## 3. Functional requirements

### R1 — Capability map (outcome-based, non-ranking)
**User story:** As Sam, I want to track what I can now accomplish without being labeled or ranked, so that I stay oriented and motivated rather than judged.

**Rationale:** Progress is described by *the work the learner can do*, not by a competence verdict on the person. Person-ranking labels (novice/intermediate/elite) are deliberately avoided in all learner-facing material because lower rungs read as judgments and alienate a capable learner. "Elite practitioner" (§1.5) remains the course's internal *design target*, not a label shown to Sam.

**Acceptance criteria**
- R1.AC1 — THE COURSE SHALL express progress as a **capability map of "can-do" statements** — outcome-phrased, observable capabilities ("I can …") that describe the work, never the learner.
- R1.AC2 — THE COURSE SHALL group can-do statements into neutral **stages** named for the relationship with the tool (**First Wins → Daily Driver → Force Multiplier → Autonomy & Scale**), used only for shape and orientation, NOT as a ranking of the learner.
- R1.AC3 — THE COURSE SHALL NOT use person-ranking labels (e.g., novice/beginner/intermediate/advanced/elite) in learner-facing material to describe the learner's level.
- R1.AC4 — THE COURSE SHALL map every unit to exactly one stage and to the specific can-do statements it advances, stated in the unit's front matter.
- R1.AC5 — THE COURSE SHALL ensure every can-do statement is (a) practiced by at least one lab and (b) assessed by at least one dimension of the capstone rubric.
- R1.AC6 — THE COURSE SHALL state, in the top-level README, the entry capabilities assumed and the full set of can-do statements the course delivers.

### R2 — Use-case-driven curriculum (primary organizing axis)
**User story:** As Sam, I want to learn by doing the jobs I'll actually use Claude Code for, so that the skills transfer directly to my work.

**Acceptance criteria**
- R2.AC1 — THE COURSE SHALL be organized primarily around real-world use cases (jobs-to-be-done), with each unit centered on a realistic scenario and its outcome — NOT around a feature checklist.
- R2.AC2 — THE COURSE SHALL maintain a prioritized **use-case catalog** selected primarily by *frequency × leverage* (most common and most powerful first) and secondarily by *capability-map coverage* (the catalog SHALL collectively exercise every can-do statement in R1 and every capability area in R4), recording the prioritization rationale.
- R2.AC3 — WHEN a use case is taught, THE COURSE SHALL state: the job, the realistic scenario, the definition of a successful outcome, and the workflow(s) and feature(s) it employs.
- R2.AC4 — THE COURSE SHALL ground each use case in real, observed engineering practice (a documented or industry-recognized workflow), NOT in a contrived or invented scenario, and SHALL be able to cite the practice it reflects.
- R2.AC5 — THE COURSE SHALL give the most common and most powerful use cases full depth, WHERE rarer use cases MAY be covered at awareness level (see R5).
- R2.AC6 — THE COURSE SHALL treat the concrete use-case catalog as a Design deliverable; this requirement fixes the *selection method*, not the specific list.

### R3 — Workflow methods
**User story:** As Sam, I want to learn the reusable methods behind the use cases, so that I can adapt them to jobs the course didn't explicitly cover.

**Acceptance criteria**
- R3.AC1 — THE COURSE SHALL teach, applied within use cases (not in isolation), at minimum these workflow patterns, each tagged with the stage at which it is introduced (final stage assignments confirmed in Design against the capability map):
  - explore→plan→code→commit — *Daily Driver*
  - test-driven development — *Daily Driver*
  - debugging an unfamiliar failure — *Daily Driver*
  - Git/PR workflow — *Daily Driver*
  - multi-file refactoring — *Force Multiplier*
  - code review & security review — *Force Multiplier*
  - spec-driven development — *Force Multiplier*
  - onboarding to an unfamiliar/large codebase — *Force Multiplier*
  - running parallel agents (e.g., via git worktrees) — *Autonomy & Scale*
- R3.AC2 — THE COURSE SHALL present spec-driven development as a first-class workflow and SHALL use this very course's spec (`requirements.md`/`design.md`/`tasks.md`) as the worked example.
- R3.AC3 — WHEN a workflow is taught, THE COURSE SHALL state its decision criteria (when to choose it over alternatives) and its expected verification step.
- R3.AC4 — THE COURSE SHALL introduce each workflow in the context of a use case that needs it, then generalize the pattern.
- R3.AC5 — THE COURSE SHALL map every named workflow to the specific use case(s) that exercise it, so no workflow is taught as a free-floating abstract lesson; a workflow with no exercising use case SHALL be treated as a gap to resolve.
- R3.AC6 — THE COURSE SHALL reconcile this workflow list against the Design use-case catalog (R2.AC6), resolving any item that is better expressed as a use case rather than a workflow, or vice versa.

### R4 — Feature coverage guarantee (secondary; tiered)
**User story:** As Sam, I want assurance that no major Claude Code capability is a blind spot, even though the course is organized around jobs rather than features.

**Acceptance criteria**
- R4.AC1 — THE COURSE SHALL maintain a **feature-coverage matrix** as the single canonical source of truth for the set of Claude Code capability areas the course tracks; the matrix SHALL be the authoritative list (this requirement deliberately does NOT duplicate the enumerated list inline, supporting version resilience per R12). The matrix SHALL be created/seeded in Design and kept current per the R12 refresh process.
- R4.AC2 — THE COURSE SHALL ensure every capability area in the matrix is covered somewhere in the course at a depth appropriate to its tier (see R4.AC4), and the matrix SHALL map each area to the unit(s)/example(s)/lab(s) that include it and to its depth tier.
- R4.AC3 — THE COURSE SHALL teach features in service of use cases — never as a standalone checklist — and SHALL state, for each high-leverage feature, when/why to use it plus at least one anti-pattern or failure mode.
- R4.AC4 — THE COURSE SHALL tier feature coverage by *frequency × leverage* (mirroring R2): **high-leverage** capabilities SHALL be covered by at least one hands-on lab; **awareness-level** capabilities MAY be covered by at least one worked example or mention (named, shown once, with pointers). Each capability's tier SHALL be recorded in the matrix; tier assignments are a Design deliverable.
- R4.AC5 — IF a capability is intentionally excluded, THEN THE COURSE SHALL record the exclusion and its rationale in the matrix rather than omitting it silently.

### R5 — Tiered depth & pacing for experienced engineers
**User story:** As Sam, I want the course to respect my time and experience, so that I learn fast and am never patronized.

**Acceptance criteria**
- R5.AC1 — THE COURSE SHALL assume an experienced, fast-learning software engineer and SHALL NOT teach *general software-engineering* basics (general programming, Git fundamentals, terminal basics). This exclusion SHALL NOT extend to AI-assisted-development and Claude Code concepts (e.g., context windows, non-determinism, the agentic loop, verification discipline, tool/permission models), which are **core content** the persona is new to; first-run onboarding/setup is covered by R11.
- R5.AC2 — THE COURSE SHALL give every unit a **fast path** (a concise TL;DR/speedrun: the essential commands plus the lab) distinct from the full exposition, so a confident reader can skim then practice.
- R5.AC3 — THE COURSE SHALL give every unit an optional **skip-check**: a brief "you can skip this unit if you can already …" self-assessment phrased as can-do statements (R1), so an experienced reader can decide whether to skip the unit entirely.
- R5.AC4 — THE COURSE SHALL tier depth explicitly: core/high-leverage material is deep and hands-on; awareness material is brief and clearly labeled as such.
- R5.AC5 — THE COURSE SHALL teach each concept once in its home unit and reference it elsewhere; WHERE independent readability (R6.AC3) requires context from another unit, a one-line recap plus a reference is permitted, but full re-explanation is not.
- R5.AC6 — THE COURSE SHALL provide, per unit, two separate time estimates — **reading time** and **lab time** — so a learner can budget and skip deliberately.

### R6 — Unit content standard
**User story:** As Sam, I want every unit to follow a predictable structure, so that the material is easy to navigate and skim.

**Acceptance criteria**
- R6.AC1 — THE COURSE SHALL require every **core-tier** unit to contain, in order: front matter; learning objectives; a fast-path/TL;DR; a skip-check (R5.AC3); concept exposition; at least one worked example; at least one lab; a "common pitfalls" section; and a "going deeper" pointer set.
- R6.AC2 — THE COURSE SHALL allow **awareness-tier** units a reduced template: front matter; learning objectives; at least one worked example or mention; and a "going deeper" pointer set (fast-path, skip-check, lab, and pitfalls OPTIONAL). The required template per unit SHALL follow the unit's depth tier (R4.AC4 / R5.AC4).
- R6.AC3 — THE COURSE SHALL provide every unit machine-readable front matter conforming to a defined schema (keys for: title, stage, can-do statements advanced, use case, prerequisites, reading-time estimate, lab-time estimate, depth tier); the exact schema SHALL be defined in Design and SHALL be lintable (supports R13.AC4).
- R6.AC4 — THE COURSE SHALL state learning objectives as observable behaviors (action verbs), not topics, and SHALL map each objective to the specific can-do statement(s) (R1) it advances.
- R6.AC5 — THE COURSE SHALL keep each unit independently readable, declaring any cross-unit dependency explicitly in front matter; per R5.AC5, independent readability is satisfied by a one-line recap plus a reference, not by re-teaching.
- R6.AC6 — THE COURSE SHALL scope the "common pitfalls" section to *learner mistakes when performing this unit's task*; this is distinct from feature misuse/anti-patterns (R4.AC3) and from safety hazards (R10), which are covered by their respective requirements.
- R6.AC7 — THE COURSE SHALL NOT gate progression on a graded per-unit check; units are instructional and labs are practice (assessment is the capstone only — see R8).

### R7 — Hands-on labs against a real codebase
**User story:** As Sam, I want to practice on a realistic project, so that the skills transfer to my actual work.

**Acceptance criteria**
- R7.AC1 — THE COURSE SHALL provide two version-controlled sample codebases as lab substrates: (a) a **primary codebase** of non-trivial but tractable size used by most labs, and (b) a small, deliberately messy **secondary "legacy" codebase** used by the onboarding/refactor/debug workflows (R3) where authentic unfamiliarity and accreted complexity matter.
- R7.AC2 — THE COURSE SHALL select each codebase against stated criteria: widely readable stack, realistic structure, an existing test suite, and (for the relevant labs) seeded bugs/smells/under-documentation that make debugging, refactoring, and onboarding authentic. The concrete stack/domain pick is a Design deliverable (Open Q1); this requirement fixes only the criteria.
- R7.AC3 — THE COURSE SHALL ensure every lab states: its goal, the starting state, the exact steps/prompts to attempt, and **objective self-check success criteria** the learner can confirm unaided.
- R7.AC4 — THE COURSE SHALL provide a reference solution for every lab as an **inspectable real artifact** (e.g., a git branch, tag, or committed diff), not prose alone, and SHALL separate it from the lab prompt so the learner can attempt it unaided first.
- R7.AC5 — THE COURSE SHALL provide, WHERE feasible, an **automated verification** the learner can run to confirm lab success (a test, script, or check); WHERE automation is infeasible, an objective prose self-check (R7.AC3) SHALL suffice.
- R7.AC6 — WHEN a lab modifies a codebase, THE COURSE SHALL provide a clean reset path so the next lab starts from a known state.
- R7.AC7 — IF a lab requires external services or credentials, THEN THE COURSE SHALL provide a no-credential or mocked fallback so it is completable offline/standalone.
- R7.AC8 — THE COURSE MAY offer a **bring-your-own-codebase** variant as an explicitly optional stretch; WHERE offered, it SHALL be clearly marked as non-verifiable (no objective self-check) and SHALL NOT be the required path for any lab.

### R8 — Capstone (sole assessment)
**User story:** As Sam, I want a realistic final project, so that I can prove (to myself and others) end-to-end mastery.

**Acceptance criteria**
- R8.AC1 — THE COURSE SHALL provide exactly one capstone as the sole graded assessment; it SHALL require the learner to handle a realistic, non-trivial use case end-to-end, combining context engineering, at least one custom extension (command/subagent/skill/hook/MCP), a non-trivial workflow, and explicit verification of Claude's output.
- R8.AC2 — THE COURSE SHALL frame the capstone as a **choose-your-own brief** selected from a small menu (rather than a single fixed project) and SHALL provide at least one worked **exemplar** so the learner does not face a blank page. The concrete brief menu and exemplar(s) are a Design deliverable.
- R8.AC3 — THE COURSE SHALL provide a capstone grading rubric whose dimensions collectively cover every can-do statement in the R1 capability map; the rubric SHALL grade the **work product** against each can-do statement (demonstrated / partially demonstrated / not yet demonstrated), NOT rank the learner.
- R8.AC4 — THE COURSE SHALL make the rubric self-applicable, so a solo learner can grade their own capstone against the can-do statements without an external evaluator.
- R8.AC5 — THE COURSE MAY offer an optional **AI-assisted self-grade** in which the learner uses Claude Code to score their capstone against the rubric; WHERE offered, THE COURSE SHALL require the learner to critically review and critique the AI-produced grade rather than accept it, consistent with the trust-but-verify thesis (R10).
- R8.AC6 — THE COURSE SHALL require the capstone deliverable to include the learner's own reflection on verification, structured by explicit prompts — at minimum: one place they caught Claude producing something wrong/suboptimal; one place they accepted Claude's output and the evidence that justified it; and one place they overrode or redirected Claude.
- R8.AC7 — THE COURSE MAY provide an optional, **ungraded mid-course checkpoint** challenge (self-scored against can-do statements) so gaps surface before the capstone; this SHALL NOT constitute a graded per-unit assessment and SHALL NOT alter the capstone's status as the sole graded assessment (R6.AC7).

### R9 — Self-paced solo path
**User story:** As Sam, I want to complete the entire course alone at my own pace, so that I need no instructor.

**Acceptance criteria**
- R9.AC1 — THE COURSE SHALL be fully completable by a solo learner with no facilitator, cohort, or instructor-only content of any kind.
- R9.AC2 — THE COURSE SHALL provide a **default path** through the units, while explicitly permitting deviation; the authoritative ordering constraint SHALL be the per-unit dependency graph declared in front matter (R6.AC5), and time budgeting SHALL use the per-unit estimates from R5.AC6 (this AC references those mechanisms rather than restating them).
- R9.AC3 — WHILE a learner progresses, THE COURSE SHALL ensure the self-check mechanisms defined elsewhere — lab success criteria and automated verification (R7.AC3/R7.AC5), unit skip-checks (R5.AC3), and the self-applicable capstone rubric (R8.AC4) — together suffice to confirm progress without external grading.
- R9.AC4 — THE COURSE SHALL provide a **"when you're stuck" recovery mechanism**: hints separated from full solutions, a troubleshooting/FAQ resource, and explicit guidance on using Claude Code itself to diagnose and get unstuck.
- R9.AC5 — THE COURSE SHALL provide a learner-facing **progress checklist** derived from the capability map (R1), so a solo learner can tangibly track which can-do statements they have achieved.
- R9.AC6 — THE COURSE SHALL write all prose for a self-directed reader (no instructor framing).

### R10 — Responsible & safe use
**User story:** As Sam, I want to use Claude Code safely and responsibly, so that I avoid leaking secrets, running dangerous commands, or shipping unverified code.

**Acceptance criteria**
- R10.AC1 — THE COURSE SHALL provide a **dedicated security unit** that establishes the threat model and mental models once (permissions, secrets, prompt injection, blast-radius, third-party trust), AND SHALL reinforce these through woven practice in subsequent units rather than relying on the dedicated unit alone.
- R10.AC2 — THE COURSE SHALL teach permission modes and the risk trade-offs of each, including the explicit hazards of bypassing permission prompts (e.g., auto-accept / skip-permission modes).
- R10.AC3 — THE COURSE SHALL teach secret-handling hygiene and prompt-injection awareness when Claude consumes untrusted content (web/files/tool output), and SHALL include at least one **hands-on, safety-fenced lab** in which the learner observes a prompt-injection attempt against Claude in a sandbox and then applies a defense.
- R10.AC4 — THE COURSE SHALL teach **blast-radius / reversibility discipline** — limiting potential damage via branches/worktrees, checkpointing/rewind, sandboxing, and dry-runs — as the practical complement to permission management.
- R10.AC5 — THE COURSE SHALL teach how to **vet third-party extensions** (MCP servers, plugins, marketplace items) before installing them, treating each as a trust-delegation decision.
- R10.AC6 — THE COURSE SHALL define what counts as **verification** — at minimum reading the diff, checking the approach/design, and spot-checking edge cases — so that "verification" is not satisfied by a passing test suite alone.
- R10.AC7 — THE COURSE SHALL embed a "trust-but-verify" discipline throughout, requiring at least one explicit verification step (per R10.AC6) in every workflow lab.
- R10.AC8 — IF a lab demonstrates a risky capability, THEN THE COURSE SHALL fence it with an explicit safety note and a safe-by-default alternative.
- R10.AC9 — THE COURSE SHALL include a light-touch note on responsible use of AI-generated output (e.g., licensing/attribution awareness and extra scrutiny for security-sensitive generated code); this is a mention, not a full unit.

### R11 — Onboarding & setup
**User story:** As Sam, I want a frictionless start, so that I reach my first success quickly without a patronizing setup tour.

**Acceptance criteria**
- R11.AC1 — THE COURSE SHALL provide a concise preflight that verifies a supported/recent CLI install, authentication, and a working first command before the feature units. The onboarding unit maps to the **First Wins** stage (R1). Version-specific auth steps and the supported-version floor are NOT fixed here; they live in the quarantined version layer / version record (R12).
- R11.AC2 — THE COURSE SHALL provide the preflight as a **runnable check ("doctor") script** that reports pass/fail for install, version, authentication, and a first command, WITH a short manual checklist fallback; the script SHALL double as a dogfooding artifact and a worked example of scripting Claude Code (R14, R4).
- R11.AC3 — WHEN preflight completes, THE COURSE SHALL have the learner produce a verifiable **"first success" artifact that is a real (if tiny) win against the sample codebase** — e.g., having Claude explain a file or make a single verified one-line change — NOT a contrived "hello world".
- R11.AC4 — THE COURSE SHALL establish a **known-good baseline configuration** during onboarding (e.g., a recommended `settings.json` and a starter `CLAUDE.md`) that later units extend; onboarding SHALL only *establish* this baseline, deferring the *teaching* of configuration concepts to their home unit (context/memory) to avoid front-loading.
- R11.AC5 — IF the installed CLI version differs from the version the content was last verified against, THEN THE COURSE SHALL instruct the learner how to detect this and where version-specific differences are documented (see R12).

---

## 4. Non-functional requirements

### R12 — Version resilience & update process (critical)
**User story:** As the course maintainer (and Sam), I want the course to track the latest Claude Code and be cheaply updatable as the tool changes, so that it never teaches stale behavior.

**Acceptance criteria**
- R12.AC1 — THE COURSE SHALL be **latest-targeting but verified-anchored**: its content SHALL track the current/latest Claude Code CLI and SHALL NOT hard-pin to a single fixed version, while being authored/verified against a known reference version (the recorded verified version, R12.AC4) and designed to tolerate newer versions gracefully.
- R12.AC2 — THE COURSE SHALL be written principles-first: durable concepts and mental models in the body, with **version-specific details isolated** into a single source-of-truth, machine-readable **version-data file** (commands, flags, paths, settings keys, feature-availability), which the prose references **by key** rather than restating; clearly-marked callouts SHALL render these values. No version-specific value SHALL be duplicated in prose.
- R12.AC3 — WHEN content is authored or refreshed, THE COURSE SHALL verify each version-specific detail against the actually-installed CLI (`--help`, `/help`, official docs/changelog). Shipping a version-specific claim from model memory alone is **non-conformant**; any detail that cannot be verified SHALL be explicitly marked as unverified rather than presented as fact.
- R12.AC4 — THE COURSE SHALL record, for each version-specific fact, a lightweight **verification provenance** (its source — e.g., `--help` output, official docs, changelog), so a maintainer can re-check it quickly.
- R12.AC5 — THE COURSE SHALL maintain a **version record** of the CLI version the content was last verified against and the verification date, updating it on each refresh.
- R12.AC6 — THE COURSE SHALL provide an **automated drift-detection check** that flags when the installed CLI version differs from the recorded verified version (and, where feasible, surfaces new/removed/renamed commands), so refresh is tool-prompted rather than relying on memory; this check SHALL double as a worked example of hooks/CI (R14).
- R12.AC7 — THE COURSE SHALL provide a documented **update/refresh process** — driven by this spec — that a maintainer follows when the CLI changes: re-verify version-specific details, update the bounded set of affected locations, and bump the verified-version record. The course SHOULD trigger this process on each relevant CLI release (a trigger, not a fixed schedule).
- R12.AC8 — THE COURSE SHALL be structured so that a version change touches a bounded, enumerated set of locations (principally the version-data file of R12.AC2).

### R13 — Maintainability of the course
**Acceptance criteria**
- R13.AC1 — THE COURSE SHALL keep a consistent, documented directory and file-naming convention.
- R13.AC2 — THE COURSE SHALL centralize cross-cutting facts (version record, glossary, conventions, use-case catalog, capability map, coverage matrix) so each is defined once and referenced, not duplicated, and SHALL store each such artifact in a **machine-readable** form so the checks in R13.AC4/AC5 can read it (consistent with R6.AC3 and R12.AC2).
- R13.AC3 — THE COURSE SHALL include a contributor/maintainer guide describing how to add or update a unit without breaking the use-case catalog, coverage matrix, or capability map; the guide SHALL include a recipe for **authoring a unit with Claude Code** using the course's own authoring command/skill (R14).
- R13.AC4 — THE COURSE SHALL provide a **required minimal enforcement suite** of automated checks: (a) unit front-matter schema validation (R6.AC3); (b) coverage/capability-map cross-validation — every capability area (R4) and every can-do statement (R1) is actually covered; (c) link checking; (d) version-data reference integrity — every prose reference resolves to a key in the version-data file (R12.AC2). Additional checks MAY be added where practical.
- R13.AC5 — THE COURSE SHALL provide **automated traceability checks** asserting that every requirement ID is referenced by at least one unit/artifact and that every can-do statement traces to at least one lab and at least one capstone-rubric dimension (automating §8).
- R13.AC6 — THE COURSE SHALL run the checks in R13.AC4/AC5 both as **local hooks** (fast authoring feedback) and in **CI** (backstop gate); these checks SHALL themselves serve as worked examples of hooks/CI (R14).

### R14 — Self-demonstrating ("dogfooding")
**Acceptance criteria**
- R14.AC1 — THE COURSE SHALL itself be a worked artifact of the practices it teaches; at minimum this spec, a `CLAUDE.md`, and at least one course-authoring custom command/skill SHALL exist and be referenced as living examples.
- R14.AC2 — WHERE the course teaches a feature for which a genuine artifact exists in this repository (e.g., the enforcement hooks of R13, the drift check of R12, an authoring subagent/skill, an MCP configuration), THE COURSE SHALL reference that real artifact as the worked example ("if we built the course with it, show it").
- R14.AC3 — THE COURSE SHALL use only **authentic** self-examples — artifacts genuinely used to build or maintain the course — and SHALL NOT fabricate contrived "prop" artifacts solely to have an example (consistent with R2.AC4).
- R14.AC4 — THE COURSE SHALL include a "how this course was built and is maintained with Claude Code" **case study**, covering the spec-driven workflow and the update process (R12.AC7); this case study SHALL be cross-referenced as exemplar material for the capstone (R8.AC2).
- R14.AC5 — THE COURSE SHALL include a light, honest **AI-authorship transparency note** disclosing that parts were authored with Claude Code, modeling the responsible-output guidance of R10.AC9.
- R14.AC6 — WHERE the course references its own artifacts as examples, THE COURSE SHALL keep those references accurate to the repository's actual contents (enforced via R13.AC4).
- R14.AC7 — THE COURSE MAY maintain a **decision/build log** (e.g., the evolution of this spec and key decisions) as an aid to maintainers and optional teaching material.

### R15 — Accessibility & portability
**Acceptance criteria**
- R15.AC1 — THE COURSE SHALL be readable as plain Markdown in any standard viewer with no proprietary tooling required (any generated site is optional and derived from the Markdown source).
- R15.AC2 — THE COURSE SHALL author content in **CommonMark-compatible** Markdown for its core meaning; richer rendering features (e.g., GitHub callouts, Mermaid diagrams) MAY be used only as enhancement and SHALL degrade gracefully so comprehension never depends on them.
- R15.AC3 — THE COURSE SHALL keep labs runnable on macOS and Linux, with **WSL as the supported Windows story for v1**; native Windows (PowerShell/cmd) is documented as out-of-scope for v1 rather than silently unsupported. Platform-specific divergence SHALL be noted.
- R15.AC4 — THE COURSE SHALL author labs **portable-by-default**, preferring cross-platform commands/scripts and isolating any unavoidable platform-specific steps into clearly-marked sections (mirroring the quarantine pattern of R12.AC2).
- R15.AC5 — THE COURSE SHALL avoid hard dependencies on paid third-party services for any required (non-optional) lab. Claude Code access itself is the assumed course prerequisite (A1) and is exempt from this rule; this AC governs *additional, incidental* paid dependencies — no required lab SHALL depend on a second paid service.
- R15.AC6 — THE COURSE SHALL meet baseline **accessibility**: diagrams and images SHALL have text equivalents; meaning SHALL NOT be conveyed by color or emoji alone; and document structure (headings, lists) SHALL be used semantically for navigability.

### R16 — Exhaustive, generated CLI reference (version-resilient)
**User story:** As a learner (and the course maintainer), I want an exhaustive, always-current reference of the Claude Code CLI surface generated directly from the installed tool, so that I have an authoritative options reference that never drifts from the actual CLI and that the course's own tooling can rely on. *(Added post-v1, 2026-05-31; anchors additively to R12/R13/R14/R5–R6.)*

**Acceptance criteria**
- R16.AC1 — THE COURSE SHALL maintain an **exhaustive, machine-readable CLI reference** (every command, subcommand, and flag with its description) generated by recursively introspecting the installed CLI (`claude --help` over subcommands), stored as a single committed source-of-truth artifact in `meta/`.
- R16.AC2 — THE COURSE SHALL render a **human-readable, learner-facing** reference (committed) **from the machine artifact alone** — never re-introspecting or hand-restating values — following the committed-rendered generation pattern (R12.AC2), drift-gated by the enforcement suite (R13.AC4).
- R16.AC3 — Every reference entry SHALL carry **verification provenance** (R12.AC4): live `--help` output for introspected entries, or a documentation URL + retrieval date for entries sourced from the curated supplement. No entry SHALL be authored from model memory (R12.AC3).
- R16.AC4 — WHERE the CLI surface includes capabilities not exposed by `claude --help` (e.g., in-REPL slash commands), THE COURSE MAY enrich the reference from a **single curated supplement file** carrying its own provenance; the generator SHALL union introspected and supplement entries deterministically and mark each entry's source.
- R16.AC5 — WHEN version drift is detected (R12.AC6), the refresh process (R12.AC7) SHALL **regenerate the machine reference from the installed CLI and re-render the human page** — bootstrapped by the drift trigger rather than maintained by hand — touching only the generated artifacts (R12.AC8).
- R16.AC6 — Generation and rendering SHALL be **deterministic and offline-safe for CI**: given the same installed CLI and supplement, output SHALL be byte-stable, and the rendered artifact's freshness SHALL be verifiable by a regenerate-and-diff check in the enforcement suite (R13.AC4).
- R16.AC7 — THE COURSE SHALL **dogfood** this feature as a worked example (R14.AC1/AC2): the spec-driven build of the reference SHALL be referenced from **U10** (spec-driven development) and the artifact itself from **U4** (memory & context / single-source version data) as living examples; references SHALL stay accurate (R14.AC6, enforced by R13.AC4).

---

## 5. Assumptions & dependencies
- A1 — The learner can install and authenticate a recent Claude Code CLI independently of this course (the course verifies, not provisions).
- A2 — The learner has a working terminal, Git, and a code editor, and is a proficient software engineer.
- A3 — Both sample codebases' language/stack (primary + legacy) will be selected in Design (candidate: a small, widely-readable stack to minimize language-specific friction); see R7.AC2.
- A4 — Some capabilities (e.g., enterprise managed settings) may be demonstrated conceptually where a learner lacks the environment to run them; such cases fall under R4.AC4/R4.AC5.

## 6. Out of scope (v1)
- Facilitator/cohort/instructor materials; per-unit graded assessment; teaching general programming, Git, or terminal basics; native Windows (PowerShell/cmd — WSL is the v1 Windows story, R15.AC3); localization; video/audio production; LMS/hosting; paid certification/proctoring; building or modifying Claude Code or the underlying models.

## 7. Open questions
**Carried into Design:**
- Q1 — Sample-codebase stack & domain for both the primary and legacy repos (R7.AC2); affects every lab.
- Q2 — The contents of the prioritized use-case catalog (R2.AC2), the concrete capability map / stages, and total course size/time budget.

**Resolved during requirements review (2026-05-29):**
- Q3 — *Resolved:* choose-your-own brief from a small menu + worked exemplar, with optional critiqued AI-assisted self-grade (R8.AC2/AC5).
- Q4 — *Resolved:* macOS/Linux/WSL for v1; native Windows out-of-scope for v1 (R15.AC3).

## 8. Traceability
Each requirement ID (`R1`–`R16`) will be referenced by the corresponding component(s) in `design.md` and by tasks in `tasks.md`. No requirement may be dropped without an explicit, recorded decision.
