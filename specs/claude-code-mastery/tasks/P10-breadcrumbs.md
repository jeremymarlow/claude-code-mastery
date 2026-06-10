# P10 — Breadcrumb navigation (R19)

**Goal:** give every learner-facing document a top-of-page breadcrumb trail per `design.md` §14 —
one shared trail-derivation helper, four generators emitting it, hand-authored docs migrated to the
canonical format, and a hard-fail `tools/check-breadcrumbs` gate so trails can't rot (R19.AC1–AC5).
Post-v1, **not release-blocking** — but it closes the last `make check-strict` gap (R19 unreferenced),
so at close-out **strict goes fully green for the first time since R19 was approved**.

**Status:** 📋 **DRAFT — awaiting tasks-gate approval** (not yet executed). Requirements ✅ (R19,
2026-05-31). Design ✅ **APPROVED** (§14, 2026-06-09). Execute top-to-bottom on `main` in slices
(P9 precedent); `make check` green after each slice; **present each slice for review — ask before
any commit, never push without explicit confirmation** (CLAUDE.md working agreement).

**Inputs:** `design.md` §14 (the authoritative HOW) · `requirements.md` R19 (+ R13/R15/R6 anchors) ·
existing artifacts to extend: `tools/_common.py`, `tools/render-units` (its hardcoded `BREADCRUMB`),
`tools/render-index` (the `‹` back-link), `tools/render-cli-reference` (`MD_BREADCRUMB`),
`tools/render-checklist` (no trail yet), `tools/check-links` (already validates the links resolve),
`meta/conventions.md`, `Makefile` (`check` / `check-strict` / `render` targets).

## Ordering constraint (important)

`tools/check-breadcrumbs` is built **first** (10.1) so its red output is the authoritative worklist,
but it is **not wired into `make check` until 10.4**, after the generated (10.2) and hand-authored
(10.3) trails exist — wiring it earlier would fail `make check` mid-build (and the `check-on-edit`
hook runs `make check` on every `course/`/`meta/` edit, so a mid-build wire-up would block the very
edits that fix it). Run it standalone between slices to watch the failure list shrink.

## Tasks

### 10.1 Shared helper + the gate  [R19.AC3, R19.AC5; §14.3, §14.5]
- [ ] `tools/_common.py` — add the trail derivation: parent chain = nearest `README.md` walking up
      the directory tree (a `README.md`'s parent is the next one up; repo-root `README.md` = home,
      terminus); segment labels from each ancestor's H1 (first `# ` line outside front matter /
      leading comment); relative-link computation. Expose it so both the check and the generators
      consume one implementation (the generators pass the current doc's title themselves where the
      final file doesn't exist yet at render time).
- [ ] `tools/check-breadcrumbs` — discovery-based scope per §14.4: every `*.md` under `course/`
      **minus** the named exemptions (`maintainer-guide.md`, `units/*/unit.src.md`,
      `labs/u03-lab1/untrusted-bug-report.md`); expected trail via the shared helper; actual = the
      doc's first content line (after generated-comment and/or front matter). **Hard fail** on
      missing/stale/mismatched — no PEND mode (§14.5). Reporter idiom + exit codes like the other
      `check-*` tools. Exemption list lives in the tool with a pointer to `meta/conventions.md`.
- [ ] Run it standalone: confirm it's **red on exactly the expected set** (the 6 trail-less docs +
      the format-divergent ones) and green on `cli-reference.md` (already canonical). That listing
      is 10.2/10.3's worklist. `make check` still green (gate not yet wired).

### 10.2 Generators adopt the helper  [R19.AC5 single-sourcing; §14.5.1]
- [ ] `tools/render-units` — replace the hardcoded `BREADCRUMB` constant with the helper; the trail
      gains the missing final segment (the unit's H1 / front-matter title, plain text).
- [ ] `tools/render-index` — replace the `[‹ Claude Code Mastery]` back-link with the canonical
      trail (`… › Course units`).
- [ ] `tools/render-cli-reference` — replace `MD_BREADCRUMB` with the helper (label becomes the
      page's actual H1, `Claude Code CLI reference`).
- [ ] `tools/render-checklist` — emit a trail (`… › Progress checklist`), placed after the
      GENERATED comment, before the H1.
- [ ] `make render` — regenerate all four surfaces (16 × `unit.md`, `course/units/README.md`,
      `course/reference/cli-reference.md`, `course/progress-checklist.md`); diffs are
      breadcrumb-line-only (eyeball one of each class). `make check` green (each generator's
      existing `--check` now expects the new trails); `check-breadcrumbs` standalone: generated
      docs all pass.

### 10.3 Hand-authored docs  [R19.AC1, R19.AC2; §14.1, §14.4]
- [ ] Add trails to the six trail-less docs: `course/stuck.md`,
      `course/capstone/{README,briefs,rubric,case-study}.md` — capstone children link through
      `[Capstone](./README.md)`.
- [ ] Migrate the two format-divergent case-study docs: `course/case-studies/README.md` (`‹` →
      canonical) and `collaboration-retrospective.md` (gains its final current-doc segment).
- [ ] `check-breadcrumbs` standalone: **fully green**. `make check` green (`check-links` revalidates
      every new relative link for free, R19.AC2).

### 10.4 Wire the gate + record the convention  [R19.AC3, R19.AC5; §14.5–§14.6, R13.AC1/AC4/AC6]
- [ ] `Makefile` — add `check-breadcrumbs` to `check` **and** `check-strict` (hard fail in both;
      pre-commit + CI inherit it for free).
- [ ] `meta/conventions.md` — new **Breadcrumb navigation** subsection: the format line, placement
      rule, filesystem-derivation rule, exemption list (mirrors §14.2–§14.4) — cites **R19** (this
      plus the tool satisfies `check-traceability`'s dynamic discovery, R13.AC5, zero check edits).
- [ ] `make check` green end-to-end; confirm `check-traceability` now reports **no pending
      requirements** (R19 referenced).

### 10.5 Close-out — state sync + the strict gate
- [ ] `design.md` §11 — flip the R19 row ⏳→✅ (→ §14); §14 heading 🟨 PROPOSED → ✅ BUILT.
- [ ] `decisions.md` — append the P10 entry (non-obvious calls: home-README exemption as designed,
      filesystem-derived hierarchy, H1-as-label, hard-fail-no-PEND); **strike ledger L12**.
- [ ] `tasks.md` — check the P10 index entry; update the status header.
- [ ] `IMPLEMENTATION.md` §3 — add the P10 line at the phase boundary.
- [ ] **`make check-strict` — fully green** (first time since R19 was approved; the post-R18
      Definition-of-Done gate). Present the complete diff for review; commit/push only on explicit
      go-ahead.
