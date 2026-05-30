# Design — Claude Code Mastery Course

**Spec:** `claude-code-mastery`
**Phase:** Design (Phase 2 of 3)
**Status:** 🟨 **SKELETON — UNBLOCKED** (Requirements approved 2026-05-29). Ready to author;
content gated only on resolving Q1-domain / Q2-catalog with the user (see §0). Authored in the
implementation session.

> This is a *ready-to-fill outline*, not a stub. Every section below states its purpose, its
> inputs (requirements + open decisions), and the concrete artifact(s) it produces. Fill top to
> bottom; each filled section should end by updating the traceability table (§10) and checking the
> matching item in `tasks.md`.

---

## 0. Inputs to resolve first (with the user)

Design content for §1, §2, §3, §6 **cannot be finalized** until these are decided (see
[`decisions.md`](./decisions.md) → Open decisions). Do not guess.

- **Q1** — primary & legacy codebase stack/domain (criteria: R7.AC2).
- **Q2** — concrete use-case catalog (R2.AC2); concrete capability map — can-do statements + stage
  assignments (R1); course size / unit count / time budget.

When resolved: record in `decisions.md`, then fill the dependent sections.

---

## 1. Capability map  → produces `meta/capability-map.{yaml,json}`  [R1]
Define the full set of **can-do statements** (outcome-phrased, observable; describe the work, never
the person) and group them into the four neutral **stages** (First Wins → Daily Driver → Force
Multiplier → Autonomy & Scale). No person-ranking labels (R1.AC3).
- Output: machine-readable map (id, statement, stage); the learner-facing progress checklist (R9.AC5)
  is generated from this.
- Each can-do statement must later trace to ≥1 lab and ≥1 rubric dimension (R1.AC5) — enforced by R13.AC5.

## 2. Use-case catalog  → produces `meta/use-case-catalog.yaml`  [R2]
Prioritized list of jobs-to-be-done, selected primarily by *frequency × leverage*, secondarily by
*capability-map coverage* (R2.AC2). Each entry: job, realistic scenario, success definition,
workflow(s) + feature(s) used (R2.AC3), citable real-practice grounding (R2.AC4), depth tier.
- This catalog → the unit map (one unit per use case, §6).

## 3. Workflow methods  → woven into units; documented in `meta/workflows.md`  [R3]
The nine named workflows (R3.AC1), each: decision criteria (when to choose it), expected verification
step (R3.AC3), stage tag (confirm provisional tags against the final capability map), and the use
case(s) that exercise it (R3.AC5–AC6). Spec-driven dev points at *this very spec* (R3.AC2).

## 4. Feature-coverage matrix  → produces `meta/coverage-matrix.yaml`  [R4]
**Canonical source of truth** for the capability-area set (R4.AC1 — do not re-list features in prose).
Columns: capability area → unit(s)/example(s)/lab(s) → depth tier (core/awareness) → version-data keys.
Tiering by frequency × leverage; high-leverage ⇒ ≥1 hands-on lab (R4.AC4). Record any intentional
exclusion + rationale (R4.AC5). Seed it here; the R13.AC4 check validates it.

## 5. Version-resilience architecture  → produces `meta/version-data.*` + `meta/version-record.md`  [R12]
- **Version-data file:** single machine-readable store of every version-specific detail (commands,
  flags, paths, settings keys, feature availability), each with **verification provenance** (R12.AC4).
  Prose references these **by key**; callouts render them; no duplication (R12.AC2/AC8).
- **Version record:** last-verified CLI version + date (R12.AC5).
- **Drift-detection check** (tool, §8): installed version vs recorded; surfaces new/removed commands (R12.AC6).
- Define the callout convention and the reference syntax prose uses.

## 6. Unit model & curriculum map  → produces `meta/unit-frontmatter.schema.json` + the unit list  [R5, R6]
- **Front-matter schema** (machine-readable, lintable): title, stage, can-do statements advanced,
  use case, prerequisites (dependency graph), reading-time, lab-time, depth tier (R6.AC3).
- **Tier-adaptive templates:** full (core) vs reduced (awareness) — define both (R6.AC1/AC2).
- **Unit map:** ordered units (from §2), each mapped to one stage + its can-do statements; the
  dependency graph that governs ordering (R9.AC2). Include the dedicated **security unit** (R10.AC1)
  and the **onboarding** unit (R11, First Wins).

## 7. Lab & solution architecture  [R7]
- The two codebases (primary + legacy): structure, seeded bugs/smells, test suites (R7.AC1–AC2).
- Lab format: goal / starting state / steps / objective self-check (R7.AC3); reference solution as a
  git branch/tag/diff (R7.AC4); reset mechanism (R7.AC6); offline/mock fallback (R7.AC7); optional
  non-verifiable BYO variant (R7.AC8). Automated verification where feasible (R7.AC5).

## 8. Tooling & enforcement  → produces `tools/`  [R11, R12, R13]
- `doctor` preflight script + manual fallback (R11.AC2).
- Required check suite: front-matter validation, coverage/map cross-validation, link check,
  version-data reference integrity (R13.AC4); traceability checks (R13.AC5).
- Drift-detection check (R12.AC6). Wire as local hooks **and** CI (R13.AC6). These double as the
  worked examples the hooks/CI units reference (R14.AC2).

## 9. Repository structure & conventions  [R13, R15]
Proposed layout (confirm in implementation session):

```
claude-training/
├─ README.md                      # learner-facing course landing
├─ CLAUDE.md                      # dogfooding: project memory (R14.AC1)
├─ specs/claude-code-mastery/     # this spec
│  ├─ requirements.md design.md tasks.md
│  ├─ decisions.md IMPLEMENTATION.md README.md
│  └─ tasks/                      # chunked per-section task files
├─ course/
│  ├─ units/<nn-slug>/            # unit.md (+ reduced template for awareness)
│  ├─ capstone/                   # briefs, exemplar, rubric
│  ├─ progress-checklist.md       # generated from capability-map (R9.AC5)
│  └─ stuck.md                    # "when you're stuck" recovery (R9.AC4)
├─ codebases/{primary,legacy}/    # lab substrates (R7)
├─ meta/                          # single-source machine-readable artifacts (R13.AC2)
│  ├─ capability-map.*  use-case-catalog.yaml  coverage-matrix.yaml
│  ├─ version-data.*  version-record.md  workflows.md
│  ├─ glossary.md  conventions.md  unit-frontmatter.schema.json
├─ tools/                         # doctor, checks, drift detection (R13/R12)
└─ .claude/                       # dogfooding: commands, skills, hooks, settings (R14)
```
Naming/style conventions (R13.AC1); CommonMark core + graceful degradation, a11y, portability (R15).

## 10. Dogfooding plan  [R14]
Enumerate the authentic artifacts the build produces that units will reference (the enforcement
hooks, drift check, authoring command/skill, MCP config, this spec). The build case study (R14.AC4,
doubles as capstone exemplar) and the AI-authorship transparency note (R14.AC5).

## 11. Traceability table  [§8 of requirements]
Fill as sections are completed — every R1–R15 → the design component(s) and artifact(s) that satisfy
it. The R13.AC5 check automates the inverse (every requirement referenced; every can-do → lab + rubric).

| Requirement | Design section(s) | Primary artifact(s) |
|---|---|---|
| R1 | §1, §6 | capability-map, progress-checklist |
| R2 | §2 | use-case-catalog |
| R3 | §3, §6, §7 | workflows.md, units, labs |
| R4 | §4 | coverage-matrix |
| R5 | §6 | front-matter schema, templates |
| R6 | §6 | schema, templates |
| R7 | §7 | codebases, labs, solutions |
| R8 | (add) | capstone briefs, exemplar, rubric |
| R9 | §6, §10-course | dependency graph, stuck.md, progress-checklist |
| R10 | §3, §6, §7 | security unit, injection lab |
| R11 | §8, §6 | doctor, onboarding unit, baseline config |
| R12 | §5, §8 | version-data, version-record, drift check |
| R13 | §8, §9 | check suite, conventions |
| R14 | §10 | dogfooding artifacts, case study |
| R15 | §9 | conventions, a11y/portability rules |
