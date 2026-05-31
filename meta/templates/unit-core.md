<!--
TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.src.md and fill every section.
Sections are REQUIRED and must appear IN THIS ORDER (R6.AC1). Front matter must validate
against meta/unit-frontmatter.schema.json (R6.AC3). Delete these HTML comments when authoring.
Author in CommonMark; no meaning by color/emoji alone (R15.AC6). Reference version-specific
values only as {{vd:key}} — never hardcode them (R12.AC2).
The committed, learner-facing unit.md is GENERATED from unit.src.md by tools/render-units (which
resolves the {{vd:key}} tokens); run `make render` after editing. Edit unit.src.md, never unit.md.
-->
---
id: U0
title: "<imperative outcome, e.g. Ship a feature in taskflow-api>"
stage: daily-driver            # first-wins | daily-driver | force-multiplier | autonomy-scale
depth_tier: core
use_case: "<job-to-be-done from meta/use-case-catalog.yaml>"
can_do: [C0]                   # capability-map IDs advanced (R1.AC4); CV allowed
workflows: [W0]                # workflow IDs exercised (R3); [] if none
coverage_areas: [0]            # coverage-matrix area #s touched (R4)
prerequisites: [U0]            # prerequisite unit IDs (R6.AC5)
reading_time_min: 0            # R5.AC6
lab_time_min: 0                # R5.AC6
---

# <Unit title>

## Learning objectives
<!-- Observable behaviors (action verbs), each mapped to the can-do statement it advances (R6.AC4). -->
By the end of this unit you can:
- **<verb + observable outcome>** — advances `C0`.

## Fast path (TL;DR)
<!-- R5.AC2: the essential commands + the lab, for a confident reader who wants to skim then practice. -->
> If you just want to do it: <1–3 line speedrun pointing straight at the lab>.

## Skip-check
<!-- R5.AC3: phrased as can-do statements (R1). -->
**Skip this unit if you can already:** <can-do phrasing of this unit's outcomes>.

## Concept
<!-- R5.AC1/AC5: durable, principles-first exposition. Teach the concept ONCE here; reference
     meta/workflows.md and other units rather than re-explaining (R5.AC5). AI/Claude-Code concepts
     ARE in scope; general SWE basics are not. -->

## Worked example
<!-- R6.AC1: at least one. Show the real artifact where one exists in this repo (R14.AC2). -->

## Lab
<!-- R7.AC3: state goal, starting state, steps/prompts, and OBJECTIVE self-check. Every workflow
     lab includes at least one explicit verification step (R10.AC7 / CV). Fence risky steps with a
     safety note + safe-by-default path (R10.AC8). -->
**Goal:** <what the learner will accomplish>
**Starting state:** `start/uNN-labM` (run `tools/reset-lab uNN-labM` to restore it).
**Steps:**
1. <prompt/step>
**Self-check (objective):** <how the learner confirms success unaided — e.g. `tools/verify-lab uNN-labM`>.
**Reference solution:** branch `solution/uNN-labM` (attempt unaided first).
**Verify (CV):** <the explicit verification step — read the diff / confirm root cause / spot-check edges>.

## Common pitfalls
<!-- R6.AC6: LEARNER mistakes on THIS task only. Distinct from feature anti-patterns (R4.AC3)
     and safety hazards (R10). -->
- **<mistake>** — <why it happens and how to avoid it>.

## Going deeper
<!-- R6.AC1: pointers (other units, meta/workflows.md, official docs). -->
- <pointer>
