# P7 — Quality pass & learner-experience remediation

**Goal:** a systematic post-v1 quality pass (8 lenses) and the remediation of what it found. The
product was verified **mechanically and functionally clean**; findings are confined to learner-facing
prose ergonomics and one version-token rendering gap. **Polish + gap-closure — not release-blocking.**

**Status:** ✅ **COMPLETE (2026-05-31).** Gate approved; the full editorial rollout landed. **All 16
units** migrated to `unit.src.md` + rendered and prose-de-coded; the cross-cutting sweep (capstone +
`stuck.md`) and the convention docs are done; L2 reading-time bumps applied; per-unit render-and-eyeball
fixed the version-token garbles. `make check` green; committed in slices on `spec/quality-pass-phase`.
No new requirements. **T2** (optional unit-dir rename) — the lone remaining follow-up — is now **closed
as won't-do** (2026-05-31, decision P7-T2-close); P7 has **no outstanding items**.

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
- **T2** unit dir slug `01-onboarding-first-win` ≠ title — **closed as won't-do** (2026-05-31,
  P7-T2-close): cosmetic, with real path/link/history churn for zero functional gain (slugs are short
  stable identifiers; the index links titles directly; meta is slug-agnostic). [non-blocking]
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

### 7.3 Navigation index + breadcrumbs [R9.AC2] — ✅ DONE
- [x] `tools/render-index`: generates `course/units/README.md` (stage-grouped TOC linking each
      `unit.md`, read/lab times) from front matter; `--check` drift gate in `make check`.
- [x] Top README "How it's structured" + "How to start" route through the index.
- [x] **Up-navigation breadcrumbs** (added at close-out, 2026-05-31): `tools/render-units` injects
      `[Claude Code Mastery](../../../README.md) › [Course units](../README.md)` above each unit's H1
      (generated, so all 16 + future units get it for free, drift-gated); `tools/render-index` adds a
      matching `[‹ Claude Code Mastery]` up-link atop the index. Every page now climbs back to the root.

### 7.4 U1 pilot prose [R5/R6/R15] — ✅ DONE
- [x] M1 (drop `R#`), M2 (codes→titles, title-only), L3 (`CV` expanded), light L1; title T1 fixed.
- [x] Fixed the backticked-`{{vd:settings}}` garble surfaced by rendering.

### 7.5 GATE — design approval before rollout — ✅ APPROVED (2026-05-31)
- [x] User approved the committed-rendered pattern, the per-unit rollout procedure, and the U1 voice
      (incl. title-only cross-refs; "your first unit" for U1 back-refs). Rollout unblocked.

### 7.6 Roll out to U2–U16 [R5/R6/R15] — ✅ DONE (all 16 units)
Per-unit procedure (render-and-read, not a mechanical `git mv`):
- [x] **U2 · U3 · U4** (pilot precedent)
- [x] **U5 · U6 · U7 · U8** (workflow-header + CV + prose-ref de-code; `test-run`/`git-pr` garbles fixed)
- [x] **U9 · U10 · U11** (U10 keeps teaching `R1`/`R2.AC3`/`R1`–`R15`, drops breadcrumb cites; U11 consolidates CV)
- [x] **U12 (rt 8→10) · U13 (rt 8→12) · U14 (rt 8→11) · U15 · U16** (L2 bumps + multi-clause token garbles fixed; index regenerated)

### 7.7 Cross-cutting prose sweep — ✅ DONE
- [x] `course/capstone/{README,briefs,rubric,case-study}.md`, `course/stuck.md` swept (M1/M2 with
      judgment). Kept the load-bearing rubric `[Cn]`/`[CV]` tags and case-study's descriptive `R1–R15`.

### 7.8 Convention docs for the unit.src.md split — ✅ DONE
- [x] `course/maintainer-guide.md` (new "Rendered units" invariant + add/update/recipe steps),
      `meta/templates/unit-*.md`, and the `close-unit` command updated: authored file is `unit.src.md`;
      `make render` regenerates `unit.md` + the index. (Version tokens illustrated as `{{vd:<key>}}`,
      which the `check-version-refs` key charset excludes.)

### 7.9 Close-out — ✅ DONE
- [x] `make check` green; reading times recomputed; clean commits on `spec/quality-pass-phase`; **L8
      struck** in `decisions.md`; `tasks.md` P7 + `IMPLEMENTATION.md` §3 marked complete. T2 **closed as
      won't-do** (2026-05-31, P7-T2-close).

### 7.10 Closeout amendment — session-transcript corpus ✅ (post-close, 2026-05-31)
- [x] Added transcript-capture tooling (`tools/render-transcript`, `tools/scan-secrets`, the
      `capture-session` skill — non-destructive, robust to multi-machine/concurrent sessions) and
      **back-filled the 14 substantial historical sessions** into `log/transcripts/{raw,rendered}/`
      (self-describing date+content names), each behind the secret-scan gate (0 high-confidence hits;
      all flags were taskflow-api auth code + the documented dev `secret_key` placeholder). **Removed**
      the lossy `/export` `.txt` logs (superseded). Full rationale: `decisions.md` → **P7-amendment**.
      Does not reopen L8.

## Per-unit grid

Legend: ✅ done · 🔗 link-anchors+advances auto-de-coded (script) · ⬜ prose codes + migration pending.

| Unit | state | notes for the prose pass |
|------|-------|--------------------------|
| U1 onboarding        | ✅ | pilot |
| U2 explore           | ✅ | |
| U3 operate-safely    | ✅ | settings/permission-modes/checkpoint-rewind garbles fixed |
| U4 memory-context    | ✅ | home unit for memory/settings — tokens taught here (sentence-position) |
| U5 ship-feature      | ✅ | workflow header + CV + U1/U2/U4/U10 refs de-coded; `thinking` token garble fixed |
| U6 tdd               | ✅ | workflow header + CV; U5/U7 refs; `test-run` (sentence-valued) repositioned ×3 |
| U7 debug             | ✅ | workflow header + CV; U5/U6/U9 refs; "the W2 reflex" → "red→green reflex from TDD" |
| U8 git-pr            | ✅ | workflow header + CV; U5–U7/U9/U16 refs; R7.AC3/AC7/AC8 dropped; `git-pr` garbles ×4 fixed |
| U9 legacy-refactor   | ✅ | W8/W5 labels dropped; CV; U2/U5/U7/U8 refs; R7.AC3 dropped; "deep onboarding" dup fixed |
| U10 spec-driven      | ✅ | **kept teaching** `R1`/`R2.AC3`/`R1`–`R15`/`[R3]`; dropped breadcrumb R3.AC2/R7.AC3; W7; U5/U11 refs; CV |
| U11 review           | ✅ | irregular "advances `C12`/consolidates `CV`" tail removed; CV consolidated; W6; refs; `review-cmds` garbles fixed |
| U12 commands-skills  | ✅ | multi-line "Advances `C13`" removed; R14/R7.AC3 dropped; U13 refs; **rt 8→10**; `custom-commands`/`skills` garbles fixed |
| U13 subagents        | ✅ | "the U12 line" dropped; R7.AC3 dropped; **rt 8→12**; `subagents` garbles fixed |
| U14 hooks            | ✅ | "the C15 move" reworded; R14/R13 dropped; U15 refs; **rt 8→11**; `hooks` (3-sentence) garbles fixed |
| U15 mcp-vetting      | ✅ | R10.AC5 ×4 dropped; U16 refs; `mcp`/`plugins` garbles fixed |
| U16 automate-scale   | ✅ | `(W9)` stripped; R14/R12.AC7/R15 dropped; U14 refs; `headless`/`ci`/`worktrees`/`checkpoint-rewind` garbles fixed |

## Locked decisions (do not re-litigate)

- **Front matter stays the machine layer** — `can_do`/`coverage_areas`/`prerequisites` are
  schema-bound and consumed by the checks; not humanized. No "At a glance" block.
- **Cross-ref style: title-only** — "the **Operate safely** unit", never bare `U3`.
- **Committed-rendered units** — `unit.src.md` authored, `unit.md` generated+committed, drift-gated.
- **T2 dir rename — closed as won't-do** (2026-05-31, P7-T2-close): cosmetic, with real
  path/link/history churn for zero functional gain. The slugs stay as-is.

Full rationale: `decisions.md` → "P7 — Quality pass".

## Resume state (⚠️ SUPERSEDED — P7 is complete; kept for historical reference)

> The rollout below is **done** (all 16 units migrated + de-coded, 2026-05-31). This section is the
> procedure that was followed; it is no longer a live to-do. See the Status header at the top.


**Branch:** `spec/quality-pass-phase` (local only, not pushed). **Done & committed:** the P7 spec, the infra
(`render-units`/`render-index` + Makefile gates), U1 pilot, navigation index, and U2–U4 fully
migrated/de-coded, plus this WIP checkpoint. `make check` is green.

**Already auto-applied to U5–U16 `unit.md` (do NOT redo):**
1. Cross-ref **link anchors** de-coded: `[U#](../NN-slug/unit.md)`→`[Title](…)`, `[W#](…workflows.md#…)`→`[name](…)` (88 total).
2. **`advances \`C#\`` objective tails** removed (em-dash + sentence forms; 18 total).
These units are **still `unit.md` (un-migrated)** and still contain raw `{{vd:}}` tokens + remaining **prose** codes.

**Remaining per U5–U16 (the editorial pass).** Regenerate the live worklist with:
```bash
for n in 05 06 07 08 09 10 11 12 13 14 15 16; do f=$(ls course/units/${n}-*/unit.md); \
  echo "== $f =="; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'; done
```
Then for each unit: edit prose **in place** (stays green/hook-silent — unit not yet migrated), then
**migrate** (recipe below), `tools/render-units`, **eyeball the rendered `unit.md`**, `make check`.

**Per-unit migration recipe (Bash — no edit-hook, ends green):**
```bash
d=course/units/NN-slug
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN
```

**Locked rollout rules (from U1–U4 precedent):**
- **Cross-ref style = title-only.** U1 back-refs = "your first unit" (its title is long). Short titles:
  U2 Explore a codebase · U3 Operate safely · U4 Memory & context · U5 Ship a feature · U6 TDD ·
  U7 Debugging · U8 Git & PR · U9 Refactor legacy · U10 Spec-driven dev · U11 Code & security review ·
  U12 Commands & skills · U13 Subagents · U14 Hooks · U15 MCP & vetting · U16 Automate & scale.
- **`**The workflow — W#.**` headers → `**The workflow.**`** (next sentence names+links it).
- **`CV`:** expand "cross-cutting verification (CV)" on first use per unit, de-backtick `` `CV` ``.
- **`R#` breadcrumbs:** drop in prose (e.g. "(R7.AC3)", "(R14)", "(R10.AC5)"). **EXCEPTION U10:** keep
  the *teaching* backticked `R1`/`R2.AC3`/`R1`–`R15`/`R*.AC*`; drop only the breadcrumb cites.
- **L2 reading times:** U12 8→10, U13 8→12, U14 8→11 (edit `reading_time_min` in `unit.src.md`; then
  run **`make render`** — not just render-units — so the index `course/units/README.md` regenerates too).
- **Garble rule (M4):** vd values are full sentences / contain backticks. Use them in **sentence
  position** ("Label. {{vd:key}} Next sentence…"), never backtick-wrapped and never as a mid-sentence
  noun. `{{vd:_verified_version}}` (→ `2.1.158`) is the one safe backticked token.

**Still TODO after U5–U16 prose:**
- **7.7** cross-cutting sweep: `course/capstone/{README,briefs,rubric,case-study}.md`, `course/stuck.md`
  (keep rubric `[Cn]` tags; maintainer-guide may keep `R#`).
- **7.8** convention docs: `course/maintainer-guide.md`, `meta/templates/unit-*.md`, `.claude/skills`/
  `close-unit` — authored file is now `unit.src.md`; `make render` regenerates `unit.md`.
- **7.9** close-out: final `make check`; strike **L8** in `decisions.md`; mark P7 done in `tasks.md` +
  `IMPLEMENTATION.md` §3; final commit(s). Ask before any `git push`.
