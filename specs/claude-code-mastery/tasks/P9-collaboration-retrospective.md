# P9 — Collaboration retrospective (multi-agent, self-evaluating dogfood)

**Goal:** build the R18 collaboration retrospective specced in `design.md` §13 — a panel of **11
subjective reviewers** (10 fenced read-only personas + 1 no-persona control) that read the real session
transcripts and produce a **session × reviewer matrix** of verbose, evidence-cited evaluations (leaf
cells → per-session synthesis + per-reviewer global → overall corner), delivered as **both** an internal
evaluation corpus (`log/evaluations/`) and a learner-facing case study (`course/case-studies/`). Post-v1,
**not release-blocking**. R19 (breadcrumbs) is a **separate** requirement, design deferred — not built here.

**Status:** 🟢 **APPROVED & EXECUTING** — tasks-gate approved & committed; **9.1–9.5 ✅ done** (253/253
leaves + 23/23 per-session syntheses), **9.6 globals/corner next** (see `IMPLEMENTATION.md` §3 / ledger **L11**). Requirements ✅
(R18, incl. the AC6 matrix amendment, `82e4a8b`). Design ✅ **APPROVED & committed** (§13 + §11 row, `ef7fc05`).
Branch **`feat/collaboration-retrospective`** (pushed). Execute top-to-bottom; `make check` green after
each slice; commit in slices; **ask before push/merge** (CLAUDE.md working agreement).

**Inputs:** `design.md` §13 (the authoritative HOW) · `requirements.md` R18 (+ R3/R8/R10/R14 anchors) ·
`decisions.md` → "P9 …" (locked calls; written at close-out) · the corpus to evaluate:
`log/transcripts/rendered/*.md` (primary evidence) + `log/transcripts/raw/*.jsonl` (on-demand deep reads
+ the `model` field for attribution) · tooling to reuse: `tools/scan-secrets` (the R18.AC10 gate),
`tools/render-units`/`render-index` (the committed-rendered + breadcrumb convention the case study
follows) · the U13 subagent surface (`{{vd:subagents}}`, `--help`-verified @ **2.1.159**) for the agent
format. Measured corpus size: ~1.05M tokens across 22 sessions (`design.md` §13.7) — **now 23
sessions** (the `2026-05-31_1908-r18-retrospective…` planning session was captured after this plan was
drafted). **Corpus frozen at these 23** (reconfirm 2026-05-31): the evaluated set is whatever is in
`log/transcripts/rendered/` today; P9's own build sessions are captured at close-out (9.9) and are
deliberately **out** of the evaluated corpus — `check-evaluations` will flip back to `PEND` for them,
which is informational, not a regression. **Refresh the stale figures (22→23 sessions, ≈242→253 leaves,
"other 21"→"other 22" on opus) in `design.md` §13.1/§13.2/§13.7 and ledger L11 as part of 9.2** (which
re-measures the corpus for the attribution map anyway).

## Ordering constraints (important)

1. **Agents → command → pilot → run.** The panel files (9.1) must exist before `/evaluate-session`
   (9.3) can dispatch them; the command + leaf-format must exist before the pilot (9.4); the pilot must
   pass before the full leaf pass (9.5). All leaves must exist before per-reviewer globals (9.6); globals
   before the corner (9.6); the corner before the case study (9.7).
2. **R18 traceability flips at 9.2; the binding "done" gate is `check-evaluations`.** This plan first
   predicted R18 would stay traceability-`PEND` until the case study (9.7) + U13/§10 (9.8). **In practice
   9.2 itself references R18** — `meta/conventions.md` documents the corpus layout (citing R18.AC7/AC10)
   and `tools/check-evaluations` implements R18.AC9 — both genuine built-course artifacts, so
   `check-traceability` legitimately stops flagging R18 from **9.2** on. That does **not** mean R18 is
   done: the real completeness gate is **`tools/check-evaluations`**, which shows a non-failing `PEND`
   progress readout in `make check` (so the one-session-at-a-time build stays green) and **hard-fails in
   `make check-strict` until the matrix is whole** (end of 9.6). The case study (9.7) is the R18.AC8
   learner deliverable. **Do not scrub R18 from genuine implementing artifacts to force a `PEND`** — the
   gate that matters is corpus completeness, not the traceability mention. (Contrast 9.1, where an `R18`
   token in an *agent's rationale comment* was incidental and correctly reworded out.)
3. **Verify the agent format before authoring (R12.AC3).** 9.1 confirms the `.claude/agents/<name>.md`
   path + front-matter schema against `claude --help`/docs first; the repo has **zero** agents today, so
   nothing is authored from memory. **Confirmed (2026-05-31, official docs):** project scope
   `.claude/agents/*.md` (committed to VCS) is the supported, recommended mechanism — no user/machine
   scope needed; required front matter is `name` + `description`; `tools` is a comma-separated allowlist
   that **inherits all tools if omitted** (so read-only fencing must list `Read, Grep, Glob` explicitly);
   `model` ∈ `sonnet|opus|haiku|<id>|inherit`. Recorded in `vd:subagents` notes.
4. **On-disk agents load at session start (operational).** Agent files authored directly on disk are
   **not dispatchable until a session restart / `/agents` reload** (only `/agents`-created ones load
   live). So the 9.1 authoring session can't itself dispatch the panel; the **9.4 pilot must run in a
   fresh/reloaded session** that has the committed agents loaded. Same watcher caveat as the U14 hook.

## Tasks

### 9.1 Verify agent format + author the 11-reviewer panel  [R18.AC2/AC4/AC5; §13.2/§13.3]  ✅ DONE (2026-05-31)
- [x] **Confirm the `.claude/agents/<name>.md` schema** (front-matter fields: `description`, tools,
      model; body) against `claude --help` + docs (R12.AC3); record the confirmed shape. The inline
      `--agents <json>` form is `--help`-verified (`{{vd:subagents}}`); the on-disk path/front-matter is
      a *convention* to confirm before relying on a detail. — Confirmed @ 2.1.159 against official docs
      (`code.claude.com/docs/en/sub-agents`): required `name` + `description`; `tools` comma-list (inherits
      all if omitted → read-only fencing must list `Read, Grep, Glob`); `model` ∈ `sonnet|opus|haiku|<id>|inherit`.
      Recorded in `vd:subagents` notes (provenance + verified_date 2026-05-31). **U13 gaps found → ledger L13.**
- [x] Author a **shared reviewer mandate** snippet (subjective & candid — no flatter/please/discourage;
      evidence-grounded with session + locator; both parties, both directions; the §13.4 output contract)
      and reuse it verbatim in each persona body (agents don't `include`; single-source the wording).
- [x] Author the **10 persona agents** under `.claude/agents/`, each **read-only** (`Read, Grep, Glob`):
      `process-architect`, `context-engineer`, `verification-hawk`, `tooling-economist`, `safety-steward`
      (process); `intent-alignment`, `dialogue-clarity`, `collaboration-partner` (communication);
      `outcome-auditor`, `devils-advocate` (cross-cutting). Each: a sharp `description` (when to dispatch)
      + the shared mandate + its persona lens (§13.2 table). All `model: opus` (holds the model constant
      across the panel + control, so the only variable vs. the control is the prompt scaffolding).
- [x] Author the **`control`** agent: the §13.4 output contract **only** — **no persona lens, no candor
      mandate** (the deliberate baseline; R18.AC5 scope note). Same read-only tools.
- [x] `make check` green (agents live under `.claude/`, scanned by traceability; harmless until wired).
      _Note:_ a literal `R18.AC5` in the control's rationale comment first tripped `check-traceability`
      (flipping R18 → referenced prematurely); reworded to cite decision `P9-control` so R18 stays `PEND`
      until the real 9.7–9.8 wiring.

### 9.2 Corpus conventions + completeness gate + model-attribution map + README  [R18.AC6/AC7/AC9/AC10; §13.1/§13.4/§13.8]
### 9.2 Corpus conventions + completeness gate + model-attribution map + README  [R18.AC6/AC7/AC9/AC10; §13.1/§13.4/§13.8]  ✅ DONE (2026-05-31)
- [x] `meta/conventions.md` — add the `log/evaluations/` layout + naming: `<session>/<reviewer>.md`
      (leaf), `<session>/_synthesis.md` (per-session margin), `_global/<reviewer>.md` (per-reviewer
      global margin), `_global/_overall.md` (corner). `<session>` = transcript filename stem; `<reviewer>`
      = agent id (R13.AC1). — Added a dedicated section + `log/` rows in the layout/naming tables.
- [x] **Per-session model attribution**, derived from each `.jsonl`'s `.message.model` field (R18.AC7,
      **not** assumed): map recorded in `log/evaluations/README.md`. **Verified result: all 23 sessions
      ran on `claude-opus-4-8`**, except the foundational `2026-05-29_1845-requirements-and-design-spec-creation`,
      which is **mixed/opus-dominant** — its first 2 assistant turns were `claude-sonnet-4-6`, then opus
      for the remaining 222 (the "flag if mixed" case). **The earlier "foundational = sonnet" was an
      assumption and was wrong** → corrected decision `P9-model-attr`, design §13.4, and the pilot rationale.
- [x] **Refresh the corpus figures** to the frozen 23 sessions: `design.md` §13.1 (23-session matrix),
      §13.2 (253 leaves), §13.7 (≈1.11M tokens re-measured; ≈12M leaf-tier; min 14k/max 127k) + the §13.5
      "~23 leaves" globals; ledger L11 (≈253). Per the freeze decision.
- [x] `log/evaluations/README.md` — corpus orientation: the matrix, the grade vocabulary
      (`did-well`/`did-okay`/`could-improve`, per party × axis + overall), the leaf front-matter schema
      (§13.4), the candor mandate, the verified model-attribution map (+ a regen one-liner), and the run
      protocol (rendered-primary, raw-on-demand; secret-scan before commit).
- [x] `tools/check-evaluations` — discovery-based completeness gate: expected sessions from
      `log/transcripts/rendered/*.md`, expected reviewers from `.claude/agents/*.md` (no hardcoded
      lists); asserts every session has all reviewer leaves + `_synthesis.md`, and — once all sessions
      are covered — a `_global/<reviewer>.md` per reviewer + `_global/_overall.md`. **`PEND` progress
      readout in `make check`; hard-fail in `make check-strict`** (new `evaluations` target, wired into
      both). Verified: PENDs cleanly (0/253 leaves, 0/23 syntheses, global deferred) at exit 0 in default;
      FAILs at exit 1 under `--strict`; real misconfig (no sessions/reviewers) fails in both modes.

### 9.3 Leaf format + `/evaluate-session` orchestration command  [R18.AC2/AC3/AC6; §13.4/§13.6]  ✅ DONE (2026-05-31)
- [x] Pin the **leaf-eval format** (§13.4): YAML front matter (`session`, `reviewer`, `model_evaluated`,
      `grades.{human,claude}.{process,communication}` + `grades.overall`) over a verbose, significance-
      ordered, evidence-cited prose body (`## Insights`, `## What worked / what didn't`, `## Bottom line`).
      — Single-sourced: it lives verbatim in every agent's "Output contract" (9.1) and in the
      `log/evaluations/README.md` schema; the command (step 4) validates returned leaves against it.
- [x] `.claude/commands/evaluate-session.md` — dispatches all 11 reviewers over one session (parallel,
      U16), passing each the **rendered** transcript path + the session's model attribution; collects each
      returned eval and **writes** `log/evaluations/<session>/<reviewer>.md` (subagents don't write — the
      command's main session persists the files, U13). Authentic R14 dogfood (commands, U12). Also:
      verifies attribution from the raw `.message.model` field (R18.AC7), treats existing leaves as
      cached/immutable (no overwrite), scan-secrets reminder + **no auto-commit** (maintainer's call),
      and notes the load-at-session-start caveat as a precondition. `_synthesis.md` is left to 9.5.
- [x] `make check` green.

### 9.4 Pilot one session (de-risk before the full run)  [R18.AC2/AC3/AC5]  ✅ DONE — PASS (2026-05-31)
- [x] Ran `/evaluate-session` on **`2026-05-29_1845-requirements-and-design-spec-creation`** — all 11
      reviewers dispatched in parallel, 11 leaves persisted, scan-secrets clean, `check-evaluations` shows
      the column complete (11/253). **Gate PASS on substance:** leaves are verbose, evidence-cited, both
      parties, correct grade vocab; the **control reads materially different** (generalist, no sharp lens)
      from the personas; **`devils-advocate` dissented** (`did-okay`) against the mild generosity of the
      rest — the experiment is working; strong inter-reviewer agreement on concrete findings (batch
      cancellations, redundant reads, the human's verbatim-ratification drift).
- [x] **Adjustments applied** (the gate's "adjust as needed"): (a) tightened all 11 agent output
      contracts to forbid preamble / surrounding ``` fence (reviewers added them despite "return only");
      (b) **quoted `model_evaluated`** in the leaf template + README + all 11 pilot leaves — unquoted, the
      "(mixed: …)" colon made the YAML front matter fail to parse (caught on render); (c) command step 4
      strips preamble/fence on persist + step 5 uses `scan-secrets …/*.md` (file args, not a dir).
      **Open finding:** `/evaluate-session`'s `$1` did **not** substitute when launched via the Skill tool
      (rendered `…/.md`); verify the REPL `/evaluate-session <slug>` form substitutes before relying on it.
- [x] **Cost reality (measured):** one session's 11 reviewers ≈ **1.1M tokens** → the full 23-session
      pass projects to **~25M** (vs. the §13.7 ~13–17M estimate; reviewers read more thoroughly). Surfaced
      to the maintainer.

### 9.5 Leaf pass — all 23 sessions + per-session syntheses  [R18.AC2/AC6; §13.5]  ✅ COMPLETE — leaves 253/253 + syntheses 23/23 (2026-06-02)
> **Workflow (superseded 2026-06-01 by decision `P9-leaf-workflow`):** the original "one evaluated-session
> per _fresh_ Claude session" ritual is **retired**. With the `P9-leaf-write` redesign the reviewers write
> their own leaves and return only short receipts, so a full 11-reviewer pass costs the orchestrator only
> the receipts + post-write validation reads (no leaf round-trips through the master context). Remaining
> passes therefore run as **ordinary work**, closing/compacting context by **standard context-management
> practice** — not a one-session-per-fresh-context rule. **Per-session steps (unchanged):**
> 1. (optional) `/prime-context` to orient.
> 2. `/evaluate-session <slug>` — dispatches the 11 reviewers; each **writes its own leaf** and returns a
>    receipt (the orchestrator no longer re-emits leaves). Uses `$ARGUMENTS` (the `$1` bug is fixed; see
>    **P9-cmd-args**).
> 3. Validate the leaves (first line `---`; front matter parses; `model_evaluated` quoted; grade vocab;
>    evidence-cited) — re-dispatch any substantive failure; never hand-author a reviewer's prose.
> 4. Write `log/evaluations/<slug>/_synthesis.md` — the per-session synthesis (cross-cutting story,
>    agreements/disagreements, consolidated per-party/per-axis grades; cites the leaves).
> 5. `tools/scan-secrets log/evaluations/<slug>/*.md`, human-review any flag (R18.AC10).
> 6. Present the batch for commit (+ push on a separate explicit ask); `tools/check-evaluations` shows progress.
>
> **Note (2026-06-01): leaf and synthesis stages run as _separate_ passes** — `/evaluate-session` persists
> leaves only (it states the synthesis is "the next step"). So leaf-complete sessions can outrun their syntheses.
> **Leaf pass ✅ COMPLETE (23/23, 253/253 leaves, 2026-06-01):** every rendered session has a full
> 11-reviewer pass; `check-evaluations` leaf-present gate passes.
> **Synthesis pass ✅ COMPLETE (23/23, 2026-06-02):** every session now has its `_synthesis.md`
> (`check-evaluations` confirms "all 23 per-session syntheses present"). Written as a single follow-on pass
> by reading each session's 11 leaves directly (not re-dispatched). See decision **P9-synthesis-pass**.
> **Next:** 9.6 per-reviewer globals + corner (`_global/<reviewer>.md` + `_overall.md`, **0/11** — the only
> `check-evaluations` PEND left) → 9.7 case study → 9.8 dogfood wiring → 9.9 close-out. Nothing else in flight.
> **Caveat for 9.6:** the syntheses consolidate *what the leaves say*; the recurring cross-session patterns
> they surface are provisional inputs only — the per-reviewer globals are the authoritative longitudinal view
> (§13.5) and must be derived fresh, not anchored on the syntheses (or `_observations-provisional.md`).
- [ ] For each session (incremental, **one at a time** — the maintainer's workflow): run
      `/evaluate-session`, caching the 11 leaves; then write `<session>/_synthesis.md` — the cross-cutting
      story, where reviewers **agreed/disagreed**, consolidated per-party/per-axis grades, both parties;
      cites the leaves.
- [ ] `tools/scan-secrets log/evaluations/<session>/**` before committing each session's batch (R18.AC10),
      human-reviewing any flag. **Commit per session** (cached = immutable once written) — **batch
      commit go-ahead granted** (reconfirm 2026-05-31): commit each clean-scanned session batch
      uninterrupted; **push remains a separate explicit ask** (CLAUDE.md).
- [ ] Watch `tools/check-evaluations` (built in 9.2) as the **live progress readout** as sessions
      accrete; also note status in the 🔓 ledger.

### 9.6 Global pass — per-reviewer globals + overall corner  [R18.AC6; §13.5/§13.6]
- [ ] `.claude/commands/evaluate-global.md` — re-dispatch **each reviewer over its own ~23 leaves** to
      write `_global/<reviewer>.md`: the longitudinal arc in *its* lens (did this dimension improve across
      sessions? recurring per-party strengths/failure modes; the sonnet-vs-opus caveat). Control does the
      same over its own leaves.
- [ ] Final corner pass → `_global/_overall.md`: blends the 11 per-reviewer globals into the bottom line
      + top did-well/okay/could-improve themes; notes where the **control** diverged from the personas
      (the experiment's result). `scan-secrets` over `_global/**`; commit.

> **🟢 PILOT DONE (3/11, 2026-06-02) — full run greenlit; resume here.** Ran a 3-reviewer global pilot
> (`control`, `devils-advocate`, `process-architect`) to test whether the lenses diverge enough to justify
> the full matrix. **They do, decisively** — same 23 leaves, three different *verdicts*: control = "sound,
> high-trust collaboration"; process-architect = "high plateau, one failure signature, governance
> self-sharpened"; devils-advocate = **re-grades the corpus to a did-okay center of gravity** ("green checks
> were theatre; the human + luck carried it, not the process"). They agree on facts (human steady / Claude
> mixed; human is the error-corrector; tool-batching pathology never improved) but diverge on valence — so a
> single "default-perspective" global would have produced ≈ the control's read and **erased the contrarian
> re-grade**, the most valuable cell. **Cost surprise:** each global ≈ 75–115k *subagent* tokens (reads only
> its own ~23 leaves, ~55k — NOT the transcripts), so all 11 ≈ **~1.1M**, not the 13–16M §13.7 feared (that
> was the leaf pass, done). The global tier is cheap.
>
> **Next session — finish 9.6:** `/prime-context`, then dispatch the **remaining 8** reviewers
> (collaboration-partner, context-engineer, dialogue-clarity, intent-alignment, outcome-auditor,
> safety-steward, tooling-economist, verification-hawk) as fresh subagents, **then the corner**. Best to
> first lift the contract below into `.claude/commands/evaluate-global.md` (the unchecked task above) so the
> run is mechanical, not ad-hoc.
>
> **Dispatch contract (validated by the pilot — use verbatim per reviewer):**
> - Dispatch each via its `subagent_type`; it runs in a **fresh** context.
> - **Reads ONLY its own 23 leaves:** Glob `log/evaluations/*/<reviewer>.md`. Must NOT read other reviewers'
>   leaves, any `_synthesis.md`, `_observations-provisional.md`, or transcripts — keeps the lens pure + the
>   experiment valid.
> - **Model caveat to pass:** 22 sessions `claude-opus-4-8`; foundational `2026-05-29_1845` is mixed/
>   opus-dominant (sonnet-start) — honor each leaf's `model_evaluated`, never assume.
> - **Personas** keep their lens + candor mandate (one-line lens reminder in the prompt). **`control` gets a
>   neutral, lens-free, candor-free prompt** (task only) — it is the baseline; do not inject a lens.
> - **Writes** `log/evaluations/_global/<reviewer>.md` beginning at `---`, returns only a receipt. Shape:
>   front matter `reviewer / scope / model_note / trajectory{human,claude}` → `## The longitudinal arc` →
>   `## Recurring patterns (ordered by significance)` (each cites ≥2 of its own slugs, `[human|claude]`) →
>   `## Per party — recurring strengths & failure modes` → `## Bottom line`. (The 3 pilot files are the
>   exemplars.)
> - **Corner** (`_overall.md`): dispatch one pass (or orchestrator) that reads all 11 globals → bottom line +
>   top themes + **where the control diverged from the personas**, and **reconcile the gap** between
>   devils-advocate's stricter did-okay re-grade and the panel's modal did-well (that gap is a real finding,
>   not an error). Then `scan-secrets log/evaluations/_global/**`; present for commit.

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

**Reconfirmation calls (2026-05-31, before execution):**
- **Corpus frozen at 23 sessions** — the set in `log/transcripts/rendered/` today, incl. the
  `2026-05-31_1908-r18-retrospective…` planning session. P9's own build sessions (captured at 9.9) are
  out of the evaluated corpus; `check-evaluations` returning to `PEND` for them afterward is expected.
  Stale §13/L11 figures (22→23, ≈242→253, other-21→other-22) refreshed in 9.2.
- **Batch commit go-ahead** — commit each clean-scanned session batch in 9.5 uninterrupted; **push is
  still a separate explicit ask.**
- **Pilot = `2026-05-29_1845-requirements-and-design-spec-creation`** — the only sonnet-4-6 session;
  also de-risks model attribution + the communication personas.

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
