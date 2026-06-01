# P9 — Collaboration retrospective (multi-agent, self-evaluating dogfood)

**Goal:** build the R18 collaboration retrospective specced in `design.md` §13 — a panel of **11
subjective reviewers** (10 fenced read-only personas + 1 no-persona control) that read the real session
transcripts and produce a **session × reviewer matrix** of verbose, evidence-cited evaluations (leaf
cells → per-session synthesis + per-reviewer global → overall corner), delivered as **both** an internal
evaluation corpus (`log/evaluations/`) and a learner-facing case study (`course/case-studies/`). Post-v1,
**not release-blocking**. R19 (breadcrumbs) is a **separate** requirement, design deferred — not built here.

**Status:** 📋 **DRAFT — awaiting tasks-gate approval** (not yet executed). Requirements ✅ (R18, incl.
the AC6 matrix amendment, `82e4a8b`). Design ✅ **APPROVED & committed** (§13 + §11 row, `ef7fc05`).
Branch **`feat/collaboration-retrospective`** (pushed). Execute top-to-bottom; `make check` green after
each slice; commit in slices; **ask before push/merge** (CLAUDE.md working agreement).

**Inputs:** `design.md` §13 (the authoritative HOW) · `requirements.md` R18 (+ R3/R8/R10/R14 anchors) ·
`decisions.md` → "P9 …" (locked calls; written at close-out) · the corpus to evaluate:
`log/transcripts/rendered/*.md` (primary evidence) + `log/transcripts/raw/*.jsonl` (on-demand deep reads
+ the `model` field for attribution) · tooling to reuse: `tools/scan-secrets` (the R18.AC10 gate),
`tools/render-units`/`render-index` (the committed-rendered + breadcrumb convention the case study
follows) · the U13 subagent surface (`{{vd:subagents}}`, `--help`-verified @ **2.1.159**) for the agent
format. Measured corpus size: ~1.05M tokens across 22 sessions (`design.md` §13.7).

## Ordering constraints (important)

1. **Agents → command → pilot → run.** The panel files (9.1) must exist before `/evaluate-session`
   (9.3) can dispatch them; the command + leaf-format must exist before the pilot (9.4); the pilot must
   pass before the full leaf pass (9.5). All leaves must exist before per-reviewer globals (9.6); globals
   before the corner (9.6); the corner before the case study (9.7).
2. **R18 stays PEND (non-failing) until wired.** `check-traceability` already discovers R18 from its
   `### R18` heading (post-P8 generalization), but R18 is not *referenced* by a course artifact until the
   case study (9.7) + the U13/§10 dogfood pointers (9.8) land. So plain `make check` stays **green**
   (R18 shows `PEND`) throughout the build; **`make check-strict` fails on R18 until 9.7–9.8**. Gate
   "done" on strict only after wiring — do not treat the mid-build PEND as a regression. Likewise
   `tools/check-evaluations` (9.2) PENDs in `make check` while the corpus is in progress and hard-fails
   only under `--strict`, so **strict green = R18 referenced *and* corpus complete** (end of 9.6 + the
   9.7–9.8 wiring).
3. **Verify the agent format before authoring (R12.AC3).** 9.1 confirms the `.claude/agents/<name>.md`
   path + front-matter schema against `claude --help`/docs first; the repo has **zero** agents today, so
   nothing is authored from memory.

## Tasks

### 9.1 Verify agent format + author the 11-reviewer panel  [R18.AC2/AC4/AC5; §13.2/§13.3]
- [ ] **Confirm the `.claude/agents/<name>.md` schema** (front-matter fields: `description`, tools,
      model; body) against `claude --help` + docs (R12.AC3); record the confirmed shape. The inline
      `--agents <json>` form is `--help`-verified (`{{vd:subagents}}`); the on-disk path/front-matter is
      a *convention* to confirm before relying on a detail.
- [ ] Author a **shared reviewer mandate** snippet (subjective & candid — no flatter/please/discourage;
      evidence-grounded with session + locator; both parties, both directions; the §13.4 output contract)
      and reuse it verbatim in each persona body (agents don't `include`; single-source the wording).
- [ ] Author the **10 persona agents** under `.claude/agents/`, each **read-only** (`Read, Grep, Glob`):
      `process-architect`, `context-engineer`, `verification-hawk`, `tooling-economist`, `safety-steward`
      (process); `intent-alignment`, `dialogue-clarity`, `collaboration-partner` (communication);
      `outcome-auditor`, `devils-advocate` (cross-cutting). Each: a sharp `description` (when to dispatch)
      + the shared mandate + its persona lens (§13.2 table).
- [ ] Author the **`control`** agent: the §13.4 output contract **only** — **no persona lens, no candor
      mandate** (the deliberate baseline; R18.AC5 scope note). Same read-only tools.
- [ ] `make check` green (agents live under `.claude/`, scanned by traceability; harmless until wired).

### 9.2 Corpus conventions + completeness gate + model-attribution map + README  [R18.AC6/AC7/AC9/AC10; §13.1/§13.4/§13.8]
- [ ] `meta/conventions.md` — add the `log/evaluations/` layout + naming: `<session>/<reviewer>.md`
      (leaf), `<session>/_synthesis.md` (per-session margin), `_global/<reviewer>.md` (per-reviewer
      global margin), `_global/_overall.md` (corner). `<session>` = transcript filename stem; `<reviewer>`
      = agent id (R13.AC1).
- [ ] **Per-session model attribution**, derived from each `.jsonl`'s `model` field (R18.AC7, **not**
      assumed): record the map in `log/evaluations/README.md`. Known split — the foundational
      `2026-05-29_1845-requirements-and-design-spec-creation` ran on **`claude-sonnet-4-6`**; the other
      21 on **`claude-opus-4-8`** (a session may switch models mid-stream — attribute from the file, flag
      if mixed).
- [ ] `log/evaluations/README.md` — corpus orientation: the matrix, the grade vocabulary
      (**did well / did okay / could improve**, per party × axis + overall), the leaf front-matter schema
      (§13.4), the candor mandate, the model-attribution map, and the run protocol (rendered-primary,
      raw-on-demand; secret-scan before commit).
- [ ] `tools/check-evaluations` — discovery-based completeness gate: expected sessions from
      `log/transcripts/rendered/*.md`, expected reviewers from `.claude/agents/*.md` (no hardcoded
      lists); asserts every session has all reviewer leaves + `_synthesis.md`, and — once all sessions
      are covered — a `_global/<reviewer>.md` per reviewer + `_global/_overall.md`. **`PEND` progress
      readout in `make check`; hard-fail in `make check-strict`** (new `evaluations` target). Verify it
      PENDs cleanly against the empty/partial corpus now.

### 9.3 Leaf format + `/evaluate-session` orchestration command  [R18.AC2/AC3/AC6; §13.4/§13.6]
- [ ] Pin the **leaf-eval format** (§13.4): YAML front matter (`session`, `reviewer`, `model_evaluated`,
      `grades.{human,claude}.{process,communication}` + `grades.overall`) over a verbose, significance-
      ordered, evidence-cited prose body (`## Insights`, `## What worked / what didn't`, `## Bottom line`).
- [ ] `.claude/commands/evaluate-session.md` — dispatches all 11 reviewers over one session (parallel,
      U16), passing each the **rendered** transcript path + the session's model attribution; collects each
      returned eval and **writes** `log/evaluations/<session>/<reviewer>.md` (subagents don't write — the
      command's main session persists the files, U13). Authentic R14 dogfood (commands, U12).
- [ ] `make check` green.

### 9.4 Pilot one session (de-risk before the full run)  [R18.AC2/AC3/AC5]
- [ ] Run `/evaluate-session` on **one** representative mid-size session; eyeball ≥3 leaves **incl. the
      control**: is the prose verbose & insight-led (not a grade dump)? are claims **cited to the
      transcript**? is it candid (neither flattering nor harsh)? does it cover **both parties**? does the
      control read materially different from the personas (the experiment is working)?
- [ ] Adjust the mandate / persona bodies / leaf contract as needed, re-run, confirm. **This is a real
      gate** — do not start the full pass until a pilot session reads well. Note adjustments for the
      close-out decision entry.

### 9.5 Leaf pass — all 22 sessions + per-session syntheses  [R18.AC2/AC6; §13.5]
- [ ] For each session (incremental, **one at a time** — the maintainer's workflow): run
      `/evaluate-session`, caching the 11 leaves; then write `<session>/_synthesis.md` — the cross-cutting
      story, where reviewers **agreed/disagreed**, consolidated per-party/per-axis grades, both parties;
      cites the leaves.
- [ ] `tools/scan-secrets log/evaluations/<session>/**` before committing each session's batch (R18.AC10),
      human-reviewing any flag. Commit per session (cached = immutable once written).
- [ ] Watch `tools/check-evaluations` (built in 9.2) as the **live progress readout** as sessions
      accrete; also note status in the 🔓 ledger.

### 9.6 Global pass — per-reviewer globals + overall corner  [R18.AC6; §13.5/§13.6]
- [ ] `.claude/commands/evaluate-global.md` — re-dispatch **each reviewer over its own ~22 leaves** to
      write `_global/<reviewer>.md`: the longitudinal arc in *its* lens (did this dimension improve across
      sessions? recurring per-party strengths/failure modes; the sonnet-vs-opus caveat). Control does the
      same over its own leaves.
- [ ] Final corner pass → `_global/_overall.md`: blends the 11 per-reviewer globals into the bottom line
      + top did-well/okay/could-improve themes; notes where the **control** diverged from the personas
      (the experiment's result). `scan-secrets` over `_global/**`; commit.

### 9.7 Learner-facing case study  [R18.AC6/AC8; R8.AC2, R14.AC4; §13.5]
- [ ] `course/case-studies/collaboration-retrospective.md` — the **teaching render** of the corner: an
      honest, candid account of what effective (and ineffective) human+Claude co-authorship looked like
      across this build, framed for a learner. Cross-reference as capstone-exemplar material alongside the
      existing build case study (`course/capstone/case-study.md`); link both ways.
- [ ] Add a **breadcrumb** following the existing learner-doc convention (e.g.
      `[Claude Code Mastery](../../README.md) › [Case studies](…)`) — matching what units already do, so
      the new doc is forward-compatible with R19 (whose mechanization is deferred). CommonMark; no meaning
      by emoji/color alone (R15).
- [ ] `make check` green (the case study now **references R18**, flipping it from PEND toward satisfied).

### 9.8 Dogfood wiring + traceability flip  [R18.AC4/AC9, R14.AC2; §13.9/§10]
- [ ] U13 `unit.src.md` — reference the **real persona panel** as the worked subagent example, **retiring
      decision P5-U13-example** (the repo previously had no authentic subagent to show; now it does).
      Light titled pointer, P7 house style (no bare codes); `make render`; eyeball; reading-time unaffected.
- [ ] `design.md` §10 dogfooding inventory — add the **persona panel** (→ U13) and the **collaboration
      retrospective case study** (→ capstone exemplar) rows.
- [ ] Confirm `check-traceability` now finds **R18 referenced** (case study + U13 + §10); `make check`
      green and **`make check-strict`** no longer fails on R18.

### 9.9 Close-out  [continuity hygiene]
- [ ] `make check` **and** `make check-strict` green — strict green now confirms **R18 referenced *and*
      the corpus complete** (`tools/check-evaluations` passes); `scan-secrets` clean across
      `log/evaluations/**` + the case study.
- [ ] `decisions.md` — **P9-complete** entry (the panel roster + the merges, the matrix structure, the
      independence-vs-economy call, the control's AC5 scope, any 9.4 pilot adjustments); refresh the 🔓
      ledger (R18 build done; **R19 still deferred**). Add the **P9 index row + status header** to
      `tasks.md`; mark `IMPLEMENTATION.md` §3 (P9 ✅).
- [ ] Final commit on `feat/collaboration-retrospective`; then open PR / merge to `main` — **ask before
      push/merge** (CLAUDE.md). ⟵ awaiting go-ahead.

## Locked decisions (from the requirements + design gates — do not re-litigate)

- **Panel = 11 reviewers** — 10 fenced read-only personas + 1 no-persona control; balanced **5 process /
  3 communication / 2 cross-cutting**. Roster fixed (`tooling-economist` = power-user + efficiency;
  `dialogue-clarity` = prompt-critic + clarity-coach; `intent-alignment` added; safety/verification
  de-overlapped).
- **Matrix, not linear tiers** — leaf cells + per-session margin + per-reviewer global margin + corner
  (R18.AC6). Each reviewer globals its **own** leaves; one corner pass blends them.
- **Independence over economy** — one subagent per reviewer (separate contexts; ~11× transcript reads
  accepted) to keep reviews independent and the control valid. **Rendered-primary, raw-on-demand.**
- **The control omits the lens + candor mandate** — deliberate baseline; R18.AC5's "every reviewer" reads
  as the 10 persona reviewers.
- **No new can-do** — R18 extends the requirement set only; the `C1–C17+CV` taxonomy stays closed.
- **Completeness gate `tools/check-evaluations`** — discovery-based (sessions from `log/transcripts/`,
  reviewers from `.claude/agents/`); `PEND` in `make check`, hard-fail in `--strict`. Covers
  *completeness* — the gap `check-traceability` (which only checks R18 is *referenced*) leaves.
- **Model attribution from the `.jsonl`** — never assumed (R18.AC7).

## Traceability (this phase)

| Req | Task(s) |
|---|---|
| R18.AC1 | 9.3 (leaf contract: both parties, both axes) |
| R18.AC2 | 9.1 (mandate), 9.3 (verbose body), 9.4 (pilot gate), 9.5/9.6 (syntheses) |
| R18.AC3 | 9.2 (grade vocabulary), 9.3 (grade block) |
| R18.AC4 | 9.1 (real `.claude/agents/` panel), 9.8 (U13 reference) |
| R18.AC5 | 9.1 (mandate + control), 9.4 (candor check) |
| R18.AC6 | 9.2 (layout), 9.5 (leaf + per-session), 9.6 (globals + corner) |
| R18.AC7 | 9.2 (attribution map), 9.3 (passed per dispatch) |
| R18.AC8 | 9.5/9.6 (corpus), 9.7 (case study) |
| R18.AC9 | 9.2 (`check-evaluations` gate), 9.8 (traceability flip), 9.1/9.3/9.6 (spec-driven, dogfooded build) |
| R18.AC10 | 9.2 (protocol), 9.5/9.6/9.9 (`scan-secrets` gate) |
