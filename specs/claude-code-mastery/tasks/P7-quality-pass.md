# P7 — Quality pass & learner-experience remediation

**Goal:** a systematic post-v1 quality pass (8 lenses) and the remediation of what it found. The
product was verified **mechanically and functionally clean**; findings are confined to learner-facing
prose ergonomics and one version-token rendering gap. **Polish + gap-closure — not release-blocking.**

**Status:** 🚧 **IN PROGRESS (opened 2026-05-31).** Findings triaged; vd-rendering infra + navigation
index built and green; U1 migrated + polished as the **pilot**. **Design gate pending** (user approval
of the pattern + rollout procedure) before propagating to U2–U16. See `decisions.md` → "P7 — Quality
pass". This phase adds **no new requirements** — every item traces to an existing R-ID.

**Inputs:** the in-session 8-lens findings report · existing requirements R5/R6 (unit altitude &
template), R9.AC2 (navigation), R12.AC2 (version-data single-source/"build step"), R15 (graceful
degradation) · `meta/version-data.yaml` · the existing generated-artifact pattern (`render-checklist`).

## Lenses & verdict

| Lens | Verdict |
|------|---------|
| 1 Lab integrity (functional run) | ✅ clean — all 6 mutating verifiers fail-clean/pass-on-solution; u03 zero-side-effects passes |
| 2 Substrate code quality | ✅ clean — taskflow-api 36 tests green; legacy authentically messy; doctor green |
| 3 Content accuracy & version-currency | ✅ clean — 2 unverified keys (`ci`,`managed-settings`) match L1; no hardcoded version literals |
| 4 Pedagogical quality | ⚠️ findings M1, M2, L1 (below) |
| 5 Consistency & conventions | ✅ clean — uniform 8-section template; all `depth_tier: core` |
| 6 Learner experience & IDs | ⚠️ findings M2, T1, T2, M5 (below) |
| 7 Authenticity (dogfooding R14) | ✅ clean — all dogfood artifacts present & accurate |
| 8 Accessibility (R15) | ⚠️ finding M4 (custom token doesn't degrade) — earlier "clean" call corrected |

## Findings → tasks

- **M1** spec requirement-IDs (`R#`/`R#.AC#`) leak into learner prose (no learner key). [R6/R15]
- **M2** bare taxonomy codes (`U#`/`C#`/`W#`/`CV`) where titles read better; also drive the choppy
  texture. House style: **title-only** cross-refs. [R5/R6]
- **M4** `{{vd:key}}` tokens rendered raw to learners (R15 graceful-degradation miss) — **fixed** via
  the committed-rendered pattern (`render-units`). Sub-finding: backticked *sentence-valued* tokens
  garble on render (`` `{{vd:settings}}` ``) — fix at rollout (known sites: U3:75, U3:202; eyeball
  U3:57). [R12.AC2/R15]
- **M5** navigation: README linked only the bare units dir — **fixed** via generated
  `course/units/README.md` index (`render-index`). [R9.AC2]
- **T1** U1 title was the lone non-conforming title — **fixed**. Others already conform. [R6]
- **T2** unit dir slug `01-onboarding-first-win` ≠ title — **deferred/optional** (slugs are short
  identifiers; the index links titles directly; meta is slug-agnostic). [non-blocking]
- **L1** density in some `Concept` passages — light editorial relief, no reading-time bloat. [R5]
- **L2** `reading_time_min` under-declared on U12 (8→~10), U13 (8→~12), U14 (8→~11) — recompute. [R5.AC6]
- **L3** `CV` unexpanded on first use per unit — expand once, then the code is fine. [R6]

## Tasks

### 7.1 Findings & triage — ✅ DONE
- [x] 8-lens pass (functional run + content); severity-ranked findings report delivered.

### 7.2 Version-token rendering — committed-rendered pattern [R12.AC2, R15] — ✅ DONE (mechanism), pilot only
- [x] `tools/render-units`: authored `unit.src.md` → committed `unit.md` (resolves `{{vd:key}}`);
      `--check` drift gate wired into `make check`/`check-strict`; write-mode into `make render`.
- [x] U1 migrated (`git mv unit.md unit.src.md`; generated `unit.md` with `GENERATED` header).
- [x] Verified: renders clean, drift gate fails on manual `unit.md` edits + passes on re-render, green.

### 7.3 Navigation index [R9.AC2] — ✅ DONE
- [x] `tools/render-index`: generates `course/units/README.md` (stage-grouped TOC linking each
      `unit.md`, read/lab times) from front matter; `--check` drift gate in `make check`.
- [x] Top README "How it's structured" + "How to start" route through the index.

### 7.4 U1 pilot prose [R5/R6/R15] — ✅ DONE
- [x] M1 (drop `R#`), M2 (codes→titles, title-only), L3 (`CV` expanded), light L1; title T1 fixed.
- [x] Fixed the backticked-`{{vd:settings}}` garble surfaced by rendering.

### 7.5 GATE — design approval before rollout
- [ ] User approves the committed-rendered pattern + the per-unit rollout procedure (below) and the
      U1 pilot voice. **Do not start 7.6 until approved.** (Reinstates the phase gate.)

### 7.6 Roll out to U2–U16 [R5/R6/R15] — ⏳ PENDING GATE
Per-unit procedure (M4 sub-finding means this is render-and-read, not a mechanical `git mv`):
1. `git mv .../unit.md .../unit.src.md`; add the leading SOURCE comment.
2. Apply M1/M2/L1/L3 (+ L2 where due) to `unit.src.md`; fix any backticked sentence-valued tokens.
3. `tools/render-units` → **eyeball** the generated `unit.md` for garble/grammar.
4. `make check` green.
- [ ] U2 · U3 (fix `{{vd:settings}}` ×2 + eyeball `permission-modes`) · U4 · U5 · U6 · U7 · U8
- [ ] U9 · U10 (keep the teaching `R1`/`R2.AC3`; strip `R3.AC2`/`R7.AC3`) · U11
- [ ] U12 (L2 rt→~10) · U13 (L2 rt→~12) · U14 (L2 rt→~11) · U15 · U16

### 7.7 Cross-cutting prose sweep — ⏳ PENDING GATE
- [ ] `course/capstone/{README,briefs,rubric,case-study}.md`, `course/stuck.md` — same M1/M2 sweep
      with judgment (keep load-bearing rubric `[Cn]` tags). Maintainer-guide may legitimately keep `R#`.

### 7.8 Convention docs for the unit.src.md split — ⏳ PENDING GATE
- [ ] Update `course/maintainer-guide.md`, `meta/templates/unit-*.md`, and the `close-unit` skill:
      authored file is `unit.src.md`; `make render` regenerates `unit.md`.

### 7.9 Close-out
- [ ] `make check` green; reading times recomputed; clean commits on a branch; L8 struck in
      `decisions.md`; `tasks.md` P7 + `IMPLEMENTATION.md` §3 marked complete.

## Per-unit grid

Legend: M1 = has `R#` leak · M2/L3 = all units · L2 = reading-time fix · ✅ = done.

| Unit | M1 (R#) | M2 | L1 | L2 | L3 | render-migrate | done |
|------|---------|----|----|----|----|----------------|------|
| U1 onboarding        | R14 ✅ | ✅ | ✅ | ok | ✅ | ✅ | ✅ PILOT |
| U2 explore           | — | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U3 operate-safely    | — (but `{{vd:settings}}`×2 garble) | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U4 memory-context    | R14×2 | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U5 ship-feature      | — | ⬜ | ok | ok | ⬜ | ⬜ | ⬜ |
| U6 tdd               | — | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U7 debug             | — | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U8 git-pr            | — | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U9 legacy-refactor   | R7.AC3 | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U10 spec-driven      | keep R1/R2.AC3; strip R3.AC2/R7.AC3 | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U11 review           | R7.AC3 | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U12 commands-skills  | R14,R7.AC3×2 | ⬜ | review | **8→10** | ⬜ | ⬜ | ⬜ |
| U13 subagents        | R7.AC3×2 | ⬜ | review | **8→12** | ⬜ | ⬜ | ⬜ |
| U14 hooks            | R14,R13×2 | ⬜ | review | **8→11** | ⬜ | ⬜ | ⬜ |
| U15 mcp-vetting      | — | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |
| U16 automate-scale   | R14,R12,R15 | ⬜ | review | ok | ⬜ | ⬜ | ⬜ |

## Locked decisions (do not re-litigate)

- **Front matter stays the machine layer** — `can_do`/`coverage_areas`/`prerequisites` are
  schema-bound and consumed by the checks; not humanized. No "At a glance" block.
- **Cross-ref style: title-only** — "the **Operate safely** unit", never bare `U3`.
- **Committed-rendered units** — `unit.src.md` authored, `unit.md` generated+committed, drift-gated.
- **T2 dir rename deferred** — optional; `01-setup-and-first-change` if ever wanted.

Full rationale: `decisions.md` → "P7 — Quality pass".
