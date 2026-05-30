# P5 — Units (author one at a time)

**Goal:** author the 16 units. **Context-management protocol (IMPLEMENTATION.md §5):** author **one
unit per session/slice**, loading only that unit's row below, the front-matter schema + core template,
`meta/workflows.md` for its workflow(s), and the cross-cutting `meta/*` it references — not the other
units. Spin up a per-unit working file `tasks/P5-units/NN-slug.md` from the template below if helpful.

**Inputs:** `design.md` §6 (template/schema/graph), §7 (labs), §3 (workflows), §1/§2/§4 (mappings).
**Gate:** P2 + P3 + P4 done (the checks must exist and the codebases must build before a unit's lab can verify).

---

## Per-unit task template (repeat for every unit)
- [ ] `course/units/NN-slug/unit.md` from the **core** template (all 16 are core-tier). [R6.AC1]
- [ ] Valid front matter (schema-conformant) — passes `check-frontmatter`. [R6.AC3, R13.AC4a]
- [ ] Learning objectives as observable verbs, each mapped to the unit's can-do statement(s). [R6.AC4]
- [ ] Fast-path/TL;DR + skip-check (as can-do statements) + two time estimates (reading/lab). [R5.AC2/AC3/AC6]
- [ ] Concept exposition (principles-first; version-specifics only via `{{vd:key}}`). [R12.AC2]
- [ ] ≥1 worked example — prefer an **authentic dogfooding artifact** where one exists. [R6.AC1, R14.AC2]
- [ ] ≥1 lab: goal / starting state / steps / objective self-check; `start/` tag + `solution/` branch +
      `verify-lab` check + reset. [R7.AC3/AC4/AC5/AC6]
- [ ] **Woven verification (CV):** ≥1 explicit verification step in every workflow lab. [R10.AC7]
- [ ] "Common pitfalls" = learner mistakes on *this task* (distinct from anti-patterns/hazards). [R6.AC6]
- [ ] "Going deeper" pointers. [R6.AC1]
- [ ] Verify every version-specific detail vs installed CLI; add/confirm `{{vd:*}}` entries + provenance. [R12.AC3/AC4]
- [ ] Run `make check` (frontmatter, coverage, links, version-refs, traceability) green for this unit.

## Per-unit specifics

| Unit / slug | Stage | Can-do | Workflow(s) | Prereqs | Lab focus (codebase) | Special requirements |
|---|---|---|---|---|---|---|
| U1 `01-onboarding-first-win` | First Wins | C1,C2 | — | — | one verified one-line change (primary) | **onboarding (R11)**: `doctor` + first-success artifact (R11.AC3) + **establish** baseline `settings.json`/`CLAUDE.md` (R11.AC4, establish-not-teach) |
| U2 `02-explore-a-codebase` | First Wins | C3 | W8 (light) | U1 | explain architecture + locate change site (primary) | validate Claude's summary vs code |
| U3 `03-operate-safely` | First Wins | C4,CV | — | U1 | **safety-fenced prompt-injection lab** + defense (sandbox) | **dedicated security unit (R10.AC1)**: permission modes + bypass hazards (R10.AC2), secrets, injection (R10.AC3), blast-radius/checkpoints (R10.AC4), define verification (R10.AC6); risky steps fenced (R10.AC8) |
| U4 `04-memory-and-context` | First Wins | C5 | — | U1 | `CLAUDE.md` + context choices change behavior (primary) | **home** of config/memory teaching (R11.AC4); `/context` etc. |
| U5 `05-ship-a-feature` | Daily Driver | C6 | W1 | U2,U4 | implement a feature via plan mode (primary) | flagship loop; extended thinking mentioned (awareness, row 10) |
| U6 `06-tdd` | Daily Driver | C7 | W2 | U5 | red→green a new behavior (primary) | confirm test fails for the right reason |
| U7 `07-debug-a-failure` | Daily Driver | C8 | W3 | U5 | diagnose+fix a seeded bug (legacy or primary) | reproduce → root cause → no-regress |
| U8 `08-git-and-pr` | Daily Driver | C9 | W4 | U5 | clean commits + PR description (primary); `gh` | |
| U9 `09-onboard-refactor-legacy` | Force Mult. | C10 | W5 + W8 (deep) | U2,U7 | map + multi-file refactor (legacy), suite green | uses the messy legacy repo authentically |
| U10 `10-spec-driven-dev` | Force Mult. | C11 | W7 | U5 | run reqs→design→tasks on a small feature | **uses THIS spec as the worked example (R3.AC2)** |
| U11 `11-code-and-security-review` | Force Mult. | C12,CV | W6 | U3,U5 | review surfaces correctness **+** security issues | `/code-review`, `/security-review`; CV consolidation |
| U12 `12-commands-and-skills` | Autonomy | C13 | — | U4 | build a custom command + a skill | dogfood: course authoring command/skill (R14.AC1) |
| U13 `13-subagents` | Autonomy | C14 | — | U12 | a subagent performs a scoped task | |
| U14 `14-hooks` | Autonomy | C15 | — | U12 | a hook blocks/normalizes an action | dogfood: **the course's own check suite** (R13/R14.AC2) |
| U15 `15-mcp-and-vetting` | Autonomy | C16 | — | U3,U13 | connect an MCP server (mock) + **vet** a third-party one | R10.AC5 trust-delegation; offline mock (R7.AC7) |
| U16 `16-automate-and-scale` | Autonomy | C17 | W9 | U8,U14 | headless `-p` in CI + ≥2 parallel worktree agents | dogfood: CI workflow (R14.AC2) |

## Definition of Done (P5)
- [ ] All 16 `unit.md` exist, schema-valid, each with ≥1 lab + reference solution + reset. [R6, R7]
- [ ] Every can-do C1–C17+CV is practiced by ≥1 lab; every coverage area covered at its tier. [R1.AC5, R4.AC2]
- [ ] Every workflow lab contains an explicit verification step (CV). [R10.AC7]
- [ ] Security woven beyond U3 (reinforced in later units, not unit-3-only). [R10.AC1]
- [ ] `make check` green across all units (frontmatter, coverage, links, version-refs, traceability). [R13.AC4/AC5]
