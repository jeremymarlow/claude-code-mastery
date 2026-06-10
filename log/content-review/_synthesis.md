# Synthesis — holistic unit-content review (2026-06-09)

**Inputs:** the five reviewer files in this directory (see `README.md` for method). Reviewers ran in
fresh contexts, unanchored (the dispatch brief carried the maintainer's raw concern only, no
hypotheses). **Verification status:** every mechanical claim below marked *[verified]* was re-checked
directly against the files by the orchestrator before inclusion; judgment findings are attributed to
the reviewers who concur, not asserted as fact. **Conflict of interest** (the R14.AC8 habit): the unit
prose under review was authored by Claude and this synthesis is written by Claude; the fresh-eyes
panel with a candor mandate is the mitigation. Notably, the orchestrator read U1 and U5 in full
*before* dispatching the panel and missed the tool-call residue the panel caught — the blind spot the
panel exists for, recorded here as evidence it is real.

## What converged

**S1 — The course never shows the tool being used. (5/5 reviewers; the headline finding.)**
Across ~3,300 lines of unit prose there are ~6 code blocks, 1 simulated Claude reply, 0 diffs,
0 example plans, 0 sample test output, 0 diagrams (examples-critic's tally). The course's
self-declared #1 skill is "read the diff" — no diff is ever shown. U5 calls plan mode "the unit's
central tool" — no plan, good or bad, appears anywhere; the learner is told to reject vague plans
without seeing one. Demonstration density is *inverted against importance*: the flagship Daily Driver
units (U5–U8) contain zero demonstrations, while U2 and U13 demonstrate well (the in-house model to
copy). Six of sixteen "Worked example" sections (U5–U9, U11) are course-build anecdotes or pointers —
provenance substituting for demonstration. Curriculum-designer: this is precisely the worked-example
effect, and it bites a subject-novice audience hardest. Severity: **high**.

**S2 — Shipped rendering defects undermine the course's own thesis. (5/5; [verified])**
(a) Literal AI tool-call residue — `</content>` / `</invoke>` — is committed at the end of **U1, U2,
U3, U5**, in both `unit.src.md` and rendered `unit.md` *[verified by grep]*. (b) `{{vd:*}}` token
rendering splices reference-card strings mid-sentence, breaking grammar (U4:56 "Project memory via
CLAUDE.md, auto-discovered at startup (auto-memory). A `CLAUDE.md` is a file…"), and pastes the same
~70-word blob verbatim **three times within U12** (lines 65/97/217) *[verified by inspection]*.
(c) No check in the suite catches either class — they survived P7's per-unit render-and-eyeball pass.
Target-learner: for a skeptical senior engineer, these read as exactly the unread AI output the course
warns against — trust-destroying on the learner's first page. Severity: **high**, mechanically fixable.

**S3 — The operator half of the craft is missing. (elite-practitioner lead; target-learner +
curriculum-designer concur.)** Three named gaps: **brief/prompt craft** is never taught — every lab
hands the learner a pre-written prompt; no unit has them author one, watch it underperform, and fix it.
**Context-window / session-lifecycle intuition** is one U4 paragraph never reinforced — no degradation
signals, no compact-vs-clear-vs-restart judgment, no multi-session work pattern, despite U9's 40-minute
refactor needing exactly that. **Recovery** — reading a derailed session, when to interrupt, when to
start over — is absent (stuck.md is adjacent but procedural). Distinction preserved from the review:
these are *absent or one-paragraph thin*, not merely under-drilled. Severity: **high** for the course's
"elite practitioner" promise. **This is also where the only taxonomy question lives** (see below).

**S4 — One rhetorical register, saturated. (technical-editor lead; target-learner +
curriculum-designer concur.)** ~99 ", not X" antithesis constructions across the units; "green tests
are necessary, not sufficient" verbatim five times; an epigram closing nearly every paragraph; bold
spans up to 88 per unit; inline cross-reference load escalating to 22 in U16. Each sentence is fine;
the formula becomes white noise by mid-course, emphasis stops carrying information, and the prose
reads machine-assembled. Severity: **medium-high** (fatigue + trust, not correctness).

**S5 — No consolidation or transfer arc. (curriculum-designer lead; elite-practitioner concurs.)**
Nothing between U1 and the capstone verifies that habits took hold (skip-checks are skip decisions,
not retrieval; the checklist is honor-system), and nothing bridges from `taskflow` to the learner's
own repo — the senior engineer's natural consolidation move. Later units assert "you can now…" on
habits nothing ensured. Severity: **medium**.

**Credit, so it isn't lost:** all five reviewers independently praised the lab design (U3 injection,
U7 three-copy bug, U9 don't-fix discipline, U11 IDOR + planted false positive — "the best
verify-don't-trust teaching I've encountered" — target-learner), the CV through-line, and the
skip-check/fast-path respect for a senior's time. The architecture is sound; the gap is the
exposition layer. The maintainer's instinct ("labs good, units missing something") is confirmed
precisely.

## Enhancement slate (proposals for the spec phase)

| # | Proposal | Fixes | Shape & cost | Spec treatment |
|---|---|---|---|---|
| E0 | **Residue hotfix** — strip the committed `</content>`/`</invoke>` lines from the 4 units | S2a | Done in working tree this session (7 lines + re-render), uncommitted | None (defect fix); the *gate* belongs to E2 |
| E1 | **Demonstration layer** — annotated, clearly-marked-illustrative session artifacts: a real plan (vague vs good + the redirect message), a diff being read, failing-test output, transcript excerpts; rewrite the six provenance worked examples into worked *interactions*; priority order U5–U8 → U1/U3/U4 → rest; convention for the callout form recorded in `meta/conventions.md`; presence enforced by a check | S1 | The flagship; largest item — per-unit authoring against a new convention | **New requirement** (e.g. R20: every core unit demonstrates its skill with ≥1 concrete artifact) + design § + tasks |
| E2 | **Rendering correctness** — grammatical `{{vd:*}}` inline form (short inline text per key; full reference rendered once per unit, deduped), plus a residue/garble lint in `make check` | S2b/S2c | Small-medium: `render-units`/`version-data` shape + one new check | Traces existing R12/R15/R13; design amendment, no new R |
| E3 | **Register de-intensification pass** — editorial sweep cutting antithesis/epigram saturation, bold/em-dash diet, varied paragraph shapes; editor's file is the per-unit punch list | S4 | Medium: 16-unit editorial pass (P7-style) | No new R (R5/R15 prose quality); tasks only |
| E4 | **Operator-craft content** — teach brief composition (author → critique → revise loop), context lifecycle depth (signals, compact/clear/restart, resume, multi-session), recovery moves; lands as expanded U4/U5/U13 + a possible new section/lab step | S3 | Medium-large: new teaching content, possibly touching labs | **Taxonomy decision point** — teachable within existing can-dos (C5/C6/C14 territory) per the panel, but if first-class assessment is wanted it's a new outcome → R1/R2 gate |
| E5 | **Consolidation & transfer** — end-of-stage recap/retrieval prompts + "on your own repo" transfer exercises (BYO-marked, non-verifiable per R7.AC8) | S5 | Small-medium: 4 stage-boundary inserts + per-unit transfer prompts | Likely no new R (R9 family); tasks only |

**Recommended packaging:** one phase (P11) executing the accepted subset in slices, spec-first per the
maintainer-guide playbook — E2 early (it gates E1's new prose from shipping garbled), E1 as the
centerpiece, E3 woven per-unit as E1 touches each unit (one pass per unit, not two).

## Taxonomy assessment (the "decide after findings" call)

The panel found **no missing outcome** in S1/S2/S4/S5 — those are teaching-quality gaps inside
promised capabilities. S3 is the only candidate: "compose and iterate an effective brief" and "manage
a session/context lifecycle" are real expert skills the can-do set doesn't name. The panel's own
read (elite-practitioner's out-of-scope flags) is that both can be taught and practiced *within*
C5/C6/C14 without reopening the R1/R2 gate — at the cost that the capstone never first-class-assesses
them. Recommendation: teach within existing outcomes in P11; revisit taxonomy only if the capstone
rubric later feels blind to operator craft.
