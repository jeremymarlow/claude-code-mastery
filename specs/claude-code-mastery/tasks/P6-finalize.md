# P6 — Capstone, case study & finalization

**Goal:** the sole graded assessment, the dogfooding case study, learner/maintainer docs, and the
final green run that satisfies the Definition of Done.

**Inputs:** `design.md` §6.5 (capstone), §10 (dogfooding) · `meta/capability-map` (rubric source).

## Tasks

### 6.1 Capstone (design §6.5) → `course/capstone/`
- [ ] Brief **menu** (≥3 choose-your-own briefs); each requires context engineering + ≥1 custom
      extension + a non-trivial workflow + explicit verification. [R8.AC1/AC2]
- [ ] Worked **exemplar** = the build case study (6.3), so no blank page. [R8.AC2]
- [ ] **Rubric** — dimensions cover **every** can-do C1–C17+CV; grades the work product
      (demonstrated/partial/not-yet); **self-applicable** by a solo learner. [R8.AC3/AC4]
- [ ] Optional **AI-assisted self-grade** that the learner must critique. [R8.AC5]
- [ ] Required **verification-reflection** prompts: one catch / one justified accept / one override. [R8.AC6]
- [ ] Optional ungraded **mid-course checkpoint** (after Daily Driver), self-scored. [R8.AC7]

### 6.2 Maintainer & contributor docs
- [ ] `course/maintainer-guide.md` — add/update a unit without breaking catalog/matrix/map; includes a
      **"author a unit with Claude Code"** recipe using the course's own command/skill. [R13.AC3]

### 6.3 Dogfooding narrative (design §10)
- [ ] Build **case study**: "how this course was built & is maintained with Claude Code" — spec-driven
      workflow + the R12.AC7 refresh process; cross-referenced as the capstone exemplar. [R14.AC4]
- [ ] AI-authorship **transparency note** (light, honest). [R14.AC5]

### 6.4 Learner-facing finalization
- [ ] Finalize top-level `README.md` (entry capabilities + full can-do set + default path). [R1.AC6, R9.AC2]
- [ ] Confirm `course/progress-checklist.md` regenerates from `capability-map`; `course/stuck.md` complete. [R9.AC4/AC5]

### 6.5 Green-gate & version stamp
- [ ] Re-verify version-specific details against the installed CLI; bump `meta/version-record.md` if needed. [R12.AC3/AC5]
- [ ] Full enforcement + traceability suite **green** locally **and** in CI. [R13.AC4/AC5/AC6]

## Definition of Done (v1 — IMPLEMENTATION.md §6, all must hold)
- [ ] 1. Every R1–R15 satisfied and referenced by ≥1 artifact (traceability green). [R13.AC5]
- [ ] 2. Every can-do → ≥1 lab **and** ≥1 rubric dimension. [R1.AC5]
- [ ] 3. Every coverage area covered at its assigned tier (high-leverage ⇒ lab). [R4.AC2]
- [ ] 4. Every unit conforms to its tier template w/ valid front matter. [R6, R13.AC4]
- [ ] 5. Every lab: objective self-check + inspectable solution + reset path. [R7]
- [ ] 6. Capstone + brief menu + exemplar + self-applicable rubric exist. [R8]
- [ ] 7. Both codebases exist and pass their suites. [R7.AC1/AC2]
- [ ] 8. Enforcement + traceability checks green locally and in CI. [R13.AC4/AC6]
- [ ] 9. Version-data + version-record + drift check exist and pass. [R12]
- [ ] 10. Dogfooding artifacts exist + accurately referenced; case study + transparency note exist. [R14]
- [ ] 11. "When you're stuck" resources + learner progress checklist exist. [R9.AC4/AC5]
