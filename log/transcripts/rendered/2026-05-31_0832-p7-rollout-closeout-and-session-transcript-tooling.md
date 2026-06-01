# Session transcript

- **Session:** `18010791-8af3-4a98-aaba-9b5373df76eb`
- **Title:** Editorial pass on U5 with reference diffs
- **Source:** rendered from the raw `.jsonl` by `tools/render-transcript` (thinking collapsed; tool output truncated to 40 lines). The sibling `.jsonl` is the complete, machine-parseable record.

---

## 🧑 User

<command-message>prime-context</command-message>
<command-name>/prime-context</command-name>

## 🧑 User

Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/prime-context

# Prime context

Bring a fresh session up to speed on this repo before doing anything else. The spec is the source of
truth; the auto-loaded project memory is only a pointer — trust the files for specifics.

Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state surfaced):

1. **Read `specs/claude-code-mastery/IMPLEMENTATION.md`** — the orientation hub. Note §2 (read order)
   and especially **§3 (live phase/unit status)** — the single most important "where are we."
2. **Read `specs/claude-code-mastery/decisions.md`** — focus on the canonical **🔓 open-loops ledger**
   (deferred work; per-lab status **L7**; version debt **L1**) and the most recent `P5-*` entries.
3. **Skim as the task needs:** `requirements.md` (the WHAT, R1–R15, EARS), `design.md` (the HOW +
   traceability), `tasks.md` (ordered build plan; the P5 unit table).
4. **Check git state:** current branch and what's uncommitted — `git status` and `git log --oneline -5`.

Then report a tight summary, not a full audit:

- **Where we are** — current phase + unit from §3 (e.g. "P5: U1–U12 done, U13 next").
- **Open loops** — anything live in the 🔓 ledger that bears on the next step.
- **Working state** — branch, uncommitted changes, anything mid-flight.
- **Next action** — the obvious next task, framed so the user can confirm or redirect.

Honor the working agreements in `CLAUDE.md`: source of truth is the files; never author a
version-specific value from memory; keep §3 and the ledger current as you work.

## 🤖 Assistant

I'll prime context by reading the spec in canonical order and checking git state.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
1	# Start Here — Implementation Guide
2	
3	**Spec:** `claude-code-mastery`
4	**Audience:** a Claude Code session (and its human) picking up this spec to build or maintain
5	the course. **You likely have no memory of how this spec was written** — this document and
6	[`decisions.md`](./decisions.md) are how that context is restored.
7	
8	---
9	
10	## 1. What this project is (in one paragraph)
11	
12	A self-paced, solo, hands-on **course** that takes a seasoned developer who is new to
13	AI-assisted coding to elite Claude Code practitioner. It is **outcome-driven** (organized around
14	real use cases, not a feature tour), **tiered** for fast-learning senior engineers, and
15	**version-resilient** (targets the latest CLI; built to be refreshed as the tool changes — using
16	this spec). Assessment is a single capstone. See [`requirements.md`](./requirements.md) §1.
17	
18	## 2. Read order (do this first, every fresh session)
19	
20	1. **This file** — orientation + how to work within context limits.
21	2. [`decisions.md`](./decisions.md) — *why* the spec is the way it is; the rejected alternatives.
22	   Read before "improving" any requirement.
23	3. [`requirements.md`](./requirements.md) — the authoritative WHAT (R1–R15, EARS). Stable IDs.
24	4. [`design.md`](./design.md) — the HOW (architecture, schemas, artifact inventory, traceability).
25	5. [`tasks.md`](./tasks.md) — the ordered, chunked build plan.
26	
27	The persistent project memory (auto-loaded each session) also points here. Trust the **files**
28	over memory for specifics; memory is a pointer, the spec is the source of truth.
29	
30	## 3. Current state
31	
32	> **Update obligation:** this dashboard is the **first thing a fresh session reads** — keep it
33	> **terse** and refresh it at every phase/unit boundary (and the matching `tasks.md` status header).
34	> Per-unit and per-decision detail is **not** duplicated here; it lives in `tasks.md` (§P5) and the
35	> `decisions.md` ledger. A stale §3 silently misleads the next session.
36	
37	| Phase | Status |
38	|---|---|
39	| 1. Requirements (`requirements.md`) | ✅ **APPROVED** (2026-05-29) — turn-by-turn review; gap-free IDs |
40	| 2. Design (`design.md`) | ✅ **APPROVED & merged to `main`** (2026-05-29) — §0–§11; design gate passed |
… [+88 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
<system-reminder>[Truncated: PARTIAL view — showing lines 1-389 of 511 total (27877 tokens, cap 25000). Call Read with offset=390 limit=389 for the next page, or Grep to find a specific section. Do NOT answer from this page alone if the answer may be further in the file.]</system-reminder>

1	# Decision Log — Claude Code Mastery Course
2	
3	**Spec:** `claude-code-mastery`
4	**Purpose:** Persist the *reasoning* behind the requirements so it survives session
5	boundaries. A fresh implementation/maintenance session has none of the original
6	conversation; this file is where the "why" lives. Satisfies R14.AC7.
7	
8	**How to use:** When implementing, if an acceptance criterion seems arbitrary, find its
9	decision here before "fixing" it — the rationale and the rejected alternatives are recorded.
10	When maintaining (CLI changes), check whether a decision's premise still holds.
11	
12	**Status legend:** ✅ decided · 🔓 deliberately deferred to the implementation session (with your input).
13	
14	---
15	
16	## Foundational choices (session 1)
17	
18	| # | Decision | Rationale | Rejected alternatives |
19	|---|---|---|---|
20	| D0.1 | **Deliverable:** Markdown curriculum + hands-on labs against real codebases + reference solutions | Claude Code is terminal-native; competence is forged by doing, not reading | Lessons-only (weak transfer); video/workshop scripts (needs a presenter; out of scope) |
21	| D0.2 | **Spec methodology:** Kiro-style — requirements/design/tasks with EARS + approval gates | Maximum rigor & traceability; the spec itself becomes a teaching artifact (R3.AC2) | Lightweight PRD (looser traceability) |
22	| D0.3 | **Assessment:** capstone-only (sole graded instrument) | One realistic end-to-end proof; units stay instructional, labs are ungraded practice | Per-module grading (rejected by user); self-assessment-only (too weak for a domain novice) |
23	| D0.4 | **Audience:** self-paced solo only | Matches the stated goal (a dev brings *themselves* up to speed); no facilitator overhead | Facilitator overlay / cohort (explicitly out of scope) |
24	
25	## The three structural forks (session 1)
26	
27	| # | Fork | Decision | Why | Ripple |
28	|---|---|---|---|---|
29	| F1 | Organizing axis | **Outcome-driven** — use cases are the spine; features are a *secondary* coverage guarantee | Skills must transfer to real jobs, not be a feature tour; ensure common+powerful cases covered, then guarantee every feature appears ≥1× | Reshaped R2 (spine), R3 (methods), R4 (features→coverage matrix) |
30	| F2 | Breadth vs depth | **Tiered depth for experienced, fast-learning engineers** | Respect a senior dev's time; deep on high-leverage, awareness-level on niche; no SWE basics | Created R5; made R6 template tier-adaptive |
31	| F3 | Versioning | **Version-resilient, NOT pinned** — target the *latest* CLI; quarantine version-specifics; refresh via this spec | User gave "2.1.157" only to signal "use the latest"; the spec must be the instrument that updates the course as the CLI evolves | Rewrote R12 entirely; drives R13 automation, R11 onboarding |
32	
33	> **Note on "2.1.157":** This number was a *signal to target the current/latest CLI*, not a
34	> version to hard-pin. Do not bake it into content. See R12 and `meta/version-record.md`.
35	
36	## Per-requirement decisions (session 2, turn-by-turn review)
37	
38	- **R1 — Non-ranking progress.** Dropped novice/intermediate/elite labels entirely from
… [+351 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
git status && echo "---LOG---" && git log --oneline -5
```

<details><summary>tool result</summary>

```
On branch spec/quality-pass-phase
nothing to commit, working tree clean
---LOG---
8e9f477 Add quality-pass-session-1 log
0d35846 P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
79ba027 P7: committed-rendered units + navigation index (U1 pilot)
f12e692 P7: add quality-pass spec (findings, design, tasks)
179cd30 Add implementation-session-11 log
```

</details>

## 🤖 Assistant

Let me read the rest of the P7 decisions and the task file's resume state.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
390	`--check` drift gate is wired into `make check`/`check-strict`, write-mode into `make render`. Proven
391	on U1.
392	**Why:** finally realizes R12.AC2's "build step" for the *reader*, not just the author, while keeping
393	the single-source + drift guarantees. Mirrors the existing `render-checklist` generated-artifact +
394	drift-gate pattern (idiomatic for this repo). Rejected: humanizing the front matter (breaks the
395	schema/checks — R6); relocating front matter to file-bottom (our parser + GitHub table both require
396	top); a sidecar metadata file (contradicts R6, heavy). All confirmed against the parser + schema.
397	
398	**P7-garble ✅ (content bug the render exposed)** — Backticked *sentence-valued* tokens
399	(`` `{{vd:settings}}` `` / `` `{{vd:memory}}` ``) resolve a whole sentence inside inline-code →
400	garbled output, invisible while un-rendered. Fixed in U1 (those tokens were misused as noun-phrases;
401	U1 only *establishes* the baseline — the settings/memory mechanism belongs to U4). Rollout must
402	**render-and-eyeball** each unit; known sites U3:75/U3:202.
403	**Why:** rendering is what surfaced it — vindicates M4's fix doing double duty as a correctness check.
404	
405	**P7-index ✅** — Closed M5 (navigation). Generated `course/units/README.md` (new `tools/render-index`,
406	drift-gated) — a stage-grouped TOC linking each `unit.md` directly with read/lab times; top README
407	routes through it.
408	**Why:** R9.AC2 (navigable entry); a learner clicks a titled lesson and never browses the
409	`unit.md`/`unit.src.md` pair. Built from front matter so it can't drift (L2 fixes flow through).
410	
411	**P7-prose ✅ (U1 pilot) / ⏳ (rollout)** — Learner-prose ergonomics: strip spec requirement-IDs
412	(`R#`, M1 — no learner key; keep the U10 *teaching* use of `R1`/`R2.AC3`), convert bare taxonomy codes
413	to **title-only** cross-refs (M2), expand `CV` on first use (L3), light density relief (L1), recompute
414	under-declared reading times (L2, U12–U14), and the title fix (T1). Applied to U1; **gated** before
415	U2–U16.
416	**Why:** R5/R6/R15 — the codes have no learner key (`R#`) or assume an internalized map (`U#`/`C#`),
417	and the parenthetical breadcrumbs both confuse and chop the prose. Front matter keeps the codes for
418	the machine/traceability layer, so stripping them from prose costs nothing (traceability unaffected).
419	
420	**P7-frontmatter / P7-T2 ✅ (decided, not open)** — Front matter stays the machine layer (no
421	humanizing/relocating). Unit dir rename (T2) **deferred/optional** — slugs are short identifiers, the
422	index links titles, and meta is slug-agnostic (`use-case-catalog.yaml` keys on `U1`).
423	**Why:** see P7-render; T2 is cosmetic once the index exists.
424	
425	**P7-process ✅** — This phase was **retro-fitted into the spec methodology**: the freelance
426	`quality-pass.md` tracker was folded into the canonical `tasks/P7-quality-pass.md` + this section +
427	the `tasks.md` P7 index + `IMPLEMENTATION.md` §3, and a **design gate** reinstated before rollout.
428	**Why:** the project is spec-driven (D0.2) and mid-pass we had drifted into building infra + fixes
429	without the requirements→design→tasks→gate treatment; this restores it (honors the working agreements
… [+82 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
1	# P7 — Quality pass & learner-experience remediation
2	
3	**Goal:** a systematic post-v1 quality pass (8 lenses) and the remediation of what it found. The
4	product was verified **mechanically and functionally clean**; findings are confined to learner-facing
5	prose ergonomics and one version-token rendering gap. **Polish + gap-closure — not release-blocking.**
6	
7	**Status:** 🚧 **IN PROGRESS (2026-05-31).** Gate **approved** (pattern + U1 voice). **U1–U4 fully
8	done** (migrated to `unit.src.md` + rendered; prose de-coded; garbles fixed). **U5–U16: link anchors
9	+ `advances \`C#\`` tails already auto-de-coded by script — do NOT redo; but units are NOT migrated
10	and prose codes remain.** `make check` green. Work is a WIP checkpoint commit on branch
11	`spec/quality-pass-phase`. **NEXT SESSION: start at "## Resume state" below.** No new requirements.
12	
13	**Inputs:** the in-session 8-lens findings report · existing requirements R5/R6 (unit altitude &
14	template), R9.AC2 (navigation), R12.AC2 (version-data single-source/"build step"), R15 (graceful
15	degradation) · `meta/version-data.yaml` · the existing generated-artifact pattern (`render-checklist`).
16	
17	## Lenses & verdict
18	
19	| Lens | Verdict |
20	|------|---------|
21	| 1 Lab integrity (functional run) | ✅ clean — all 6 mutating verifiers fail-clean/pass-on-solution; u03 zero-side-effects passes |
22	| 2 Substrate code quality | ✅ clean — taskflow-api 36 tests green; legacy authentically messy; doctor green |
23	| 3 Content accuracy & version-currency | ✅ clean — 2 unverified keys (`ci`,`managed-settings`) match L1; no hardcoded version literals |
24	| 4 Pedagogical quality | ⚠️ findings M1, M2, L1 (below) |
25	| 5 Consistency & conventions | ✅ clean — uniform 8-section template; all `depth_tier: core` |
26	| 6 Learner experience & IDs | ⚠️ findings M2, T1, T2, M5 (below) |
27	| 7 Authenticity (dogfooding R14) | ✅ clean — all dogfood artifacts present & accurate |
28	| 8 Accessibility (R15) | ⚠️ finding M4 (custom token doesn't degrade) — earlier "clean" call corrected |
29	
30	## Findings → tasks
31	
32	- **M1** spec requirement-IDs (`R#`/`R#.AC#`) leak into learner prose (no learner key). [R6/R15]
33	- **M2** bare taxonomy codes (`U#`/`C#`/`W#`/`CV`) where titles read better; also drive the choppy
34	  texture. House style: **title-only** cross-refs. [R5/R6]
35	- **M4** `{{vd:key}}` tokens rendered raw to learners (R15 graceful-degradation miss) — **fixed** via
36	  the committed-rendered pattern (`render-units`). Sub-finding: backticked *sentence-valued* tokens
37	  garble on render (`` `{{vd:settings}}` ``) — fix at rollout (known sites: U3:75, U3:202; eyeball
38	  U3:57). [R12.AC2/R15]
39	- **M5** navigation: README linked only the bare units dir — **fixed** via generated
40	  `course/units/README.md` index (`render-index`). [R9.AC2]
… [+137 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Context loaded. Here's where things stand.

## Where we are
**P7 — Quality pass** (post-v1 learner-experience remediation), on branch `spec/quality-pass-phase`. v1 build is complete and mechanically clean (P1–P6 done, `make check-strict` green). This phase is **polish, not release-blocking**: a systematic 8-lens pass found the product functionally clean, with findings confined to learner-facing prose + one version-token rendering gap (now closed by the new `tools/render-units` committed-rendered pattern + `tools/render-index` navigation).

Progress on the rollout:
- **Infra done** — `render-units` (`unit.src.md` → committed `unit.md`, drift-gated), `render-index`, Makefile gates. Design gate **approved**.
- **U1–U4** — fully migrated + de-coded (prose codes stripped, garbles fixed).
- **U5–U16** — partially auto-de-coded by script (link anchors + `advances \`C#\`` tails, **don't redo**), but **not migrated** and prose codes + raw `{{vd:}}` tokens remain.

## Open loops bearing on next step
- **L8** (in progress) — the learner-prose rollout itself; the live task is task **7.6** (U5–U16 editorial pass), then **7.7** (capstone/stuck sweep), **7.8** (convention docs for the `.src.md` split), **7.9** (close-out).
- **L1** (mostly closed) — only `ci` and `managed-settings` version keys stay `unverified`, both blocked by access this env lacks (Gitea, not GitHub Actions; no enterprise account). Not blocking.

## Working state
Branch `spec/quality-pass-phase`, **working tree clean**, last commit is a WIP checkpoint (`8e9f477`). Local only — not pushed.

## Next action
Resume task **7.6** at **U5** (`05-ship-feature`). The recipe is locked in `tasks/P7-quality-pass.md` → "Resume state": for each unit, edit prose in place (title-only cross-refs, drop `R#` breadcrumbs, expand "cross-cutting verification (CV)" once, `**The workflow — W#.**` → `**The workflow.**`), then migrate via `git mv` + `make render`, **eyeball the rendered `unit.md`** for garbles, and confirm `make check` green. L2 reading-time bumps land at U12/U13/U14.

Want me to start the editorial pass on **U5**, or do a different slice first?

## 🧑 User

start the editorial pass on U5. Look at the diffs of the U1 and/or U2 and/or U3 to see an example of how the edit instructions were executed.

## 🤖 Assistant

I'll look at how U1–U4 were done, then start on U5. Let me check the diffs and read U5's current state.

## 🤖 Assistant

**→ Bash**

```
git show 0d35846 --stat | head -40
```

<details><summary>tool result</summary>

```
commit 0d35846c89a024ed3f386236d109433607fe1e6f
Author: jj <jj@marlow.home>
Date:   Sun May 31 01:49:12 2026 -0700

    P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
    
    Checkpoint of the in-progress P7 rollout (Stage C). Stopping point for the session;
    make check green. Resume guide: specs/claude-code-mastery/tasks/P7-quality-pass.md
    → "Resume state".
    
    - U2–U4: fully de-coded + migrated to unit.src.md (committed-rendered). Cross-ref
      codes → titles ("your first unit" for U1 back-refs), CV expanded, R# breadcrumbs
      dropped, and the {{vd:settings}}/permission-modes/checkpoint-rewind render garbles
      fixed (sentence-valued/backtick-containing tokens must not be backtick-wrapped or
      used mid-sentence as nouns).
    - U5–U16: two safe scripted passes applied to unit.md — 88 cross-ref link anchors
      de-coded and 18 `advances `C#`` objective tails removed. NOT yet migrated; prose
      codes (bare U#, "The workflow — W#." headers, R# breadcrumbs, CV) remain.
    - State synced: P7 task file (per-unit grid + full Resume state + locked rules),
      decisions.md L8/P7 status, IMPLEMENTATION.md §3.
    
    Remaining: 7.6 U5–U16 prose+migrate, 7.7 cross-cutting sweep, 7.8 convention docs,
    7.9 close-out. Branch local only (not pushed).
    
    Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

 course/units/02-explore-a-codebase/unit.md         |  36 ++--
 course/units/02-explore-a-codebase/unit.src.md     | 156 +++++++++++++++
 course/units/03-operate-safely/unit.md             |  52 ++---
 course/units/03-operate-safely/unit.src.md         | 215 +++++++++++++++++++++
 course/units/04-memory-and-context/unit.md         |  47 ++---
 course/units/04-memory-and-context/unit.src.md     | 198 +++++++++++++++++++
 course/units/05-ship-a-feature/unit.md             |  10 +-
 course/units/06-tdd/unit.md                        |   8 +-
 course/units/07-debug-a-failure/unit.md            |   8 +-
 course/units/08-git-and-pr/unit.md                 |   8 +-
 course/units/09-onboard-refactor-legacy/unit.md    |  22 +--
 course/units/10-spec-driven-dev/unit.md            |   8 +-
 course/units/11-code-and-security-review/unit.md   |  12 +-
 course/units/12-commands-and-skills/unit.md        |  10 +-
```

</details>

## 🤖 Assistant

**→ Bash**

```
ls course/units/05-*/
```

<details><summary>tool result</summary>

```
unit.md
```

</details>

## 🤖 Assistant

Let me look at the U2 diff as a worked example of the full transformation, plus U3 for the garble fixes.

## 🤖 Assistant

**→ Bash**

```
git show 0d35846 -- course/units/02-explore-a-codebase/unit.md
```

<details><summary>tool result</summary>

```
commit 0d35846c89a024ed3f386236d109433607fe1e6f
Author: jj <jj@marlow.home>
Date:   Sun May 31 01:49:12 2026 -0700

    P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
    
    Checkpoint of the in-progress P7 rollout (Stage C). Stopping point for the session;
    make check green. Resume guide: specs/claude-code-mastery/tasks/P7-quality-pass.md
    → "Resume state".
    
    - U2–U4: fully de-coded + migrated to unit.src.md (committed-rendered). Cross-ref
      codes → titles ("your first unit" for U1 back-refs), CV expanded, R# breadcrumbs
      dropped, and the {{vd:settings}}/permission-modes/checkpoint-rewind render garbles
      fixed (sentence-valued/backtick-containing tokens must not be backtick-wrapped or
      used mid-sentence as nouns).
    - U5–U16: two safe scripted passes applied to unit.md — 88 cross-ref link anchors
      de-coded and 18 `advances `C#`` objective tails removed. NOT yet migrated; prose
      codes (bare U#, "The workflow — W#." headers, R# breadcrumbs, CV) remain.
    - State synced: P7 task file (per-unit grid + full Resume state + locked rules),
      decisions.md L8/P7 status, IMPLEMENTATION.md §3.
    
    Remaining: 7.6 U5–U16 prose+migrate, 7.7 cross-cutting sweep, 7.8 convention docs,
    7.9 close-out. Branch local only (not pushed).
    
    Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

diff --git a/course/units/02-explore-a-codebase/unit.md b/course/units/02-explore-a-codebase/unit.md
index dac00ca..77569db 100644
--- a/course/units/02-explore-a-codebase/unit.md
+++ b/course/units/02-explore-a-codebase/unit.md
@@ -1,3 +1,4 @@
+<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
 ---
 id: U2
 title: "Explore and explain an unfamiliar codebase"
@@ -19,9 +20,9 @@ lab_time_min: 20
 By the end of this unit you can:
 
 - **Use Claude to explain an unfamiliar codebase's architecture and conventions, and pin down the
-  exact file(s) where a given change belongs** — advances `C3`.
… [+69 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Now let me read the current U5 `unit.md` in full and run the worklist scan to see what codes remain.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U5
3	title: "Ship a feature end-to-end with explore → plan → code → commit"
4	stage: daily-driver
5	depth_tier: core
6	use_case: "Ship a new feature in taskflow-api"
7	can_do: [C6]
8	workflows: [W1]
9	coverage_areas: [9, 10]
10	prerequisites: [U2, U4]
11	reading_time_min: 10
12	lab_time_min: 25
13	---
14	
15	# Ship a feature end-to-end with explore → plan → code → commit
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Drive a non-trivial feature through the explore → plan → code → commit loop** — orient Claude in
22	  the code, get an explicit plan, implement against it, and land a verified change.
23	- **Use plan mode as a review gate** — make Claude design *before* it writes, and reject or redirect a
24	  bad plan while it's still free to change.
25	- **Verify at the two points that matter** — review the *plan* before code exists, then read the diff
26	  and run the tests before you commit — the `CV` reflex applied to a real feature.
27	- **Recognize when to reach for extended thinking** (awareness) — and know it's a dial, not a default.
28	
29	## Fast path (TL;DR)
30	
31	> This is Anthropic's flagship coding loop ([explore → plan → code → commit](../../../meta/workflows.md#w1--explore--plan--code--commit)),
32	> and it's the default for any change bigger than a one-liner. **Explore** (have Claude read the code and
33	> restate the task), **plan** (in plan mode, so nothing is written until you approve), **code** (implement
34	> the approved plan in small steps), **commit** (read the diff, run `pytest`, then commit). The lab has you
35	> ship a real endpoint — `GET /projects/{id}/stats` — this way, and `tools/verify-lab u05-lab1` proves it.
36	> The two verification gates are the *plan* and the *diff*; skip either and you're back to hoping.
37	
38	## Skip-check
39	
40	**Skip this unit if you can already:** take a non-trivial feature from a cold start to a committed,
… [+149 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/05-*/unit.md); echo "== $f =="; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
== course/units/05-ship-a-feature/unit.md ==
13:  and run the tests before you commit — the `CV` reflex applied to a real feature.
34:You can now land a change (U1), read unfamiliar code (U2), operate safely (U3), and steer Claude with
35:memory and context (U4). This unit is where those combine into the **daily-driver loop** — the one you'll
40:**The workflow — W1.** The generalized pattern lives once in
47:to you** — the habit from U2, now load-bearing. For the lab's stats endpoint that means: where do routes
56:[`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md), from U4) — catch that in the plan and
70:This is the same diff-reading reflex from U1, now on a change big enough that it earns its keep.
85:any unit is authored (that's the heavy-weight cousin of W1, taught fully in U10). The everyday version is
119:   against the files (U2 habit) — the plan is only as good as this.
153:  in review. (This is also why U4 mattered: memory only steers if you let it.)
157:  time — the habit you built on one line in U1 is the same habit here, where it actually protects you.
163:- **Next:** U6 (TDD) tightens the loop by writing the failing test *first*; U7 (debugging) and U8 (Git/PR)
165:  run W1 fluently.
166:- [`meta/workflows.md`](../../../meta/workflows.md#w1--explore--plan--code--commit) — the generalized W1
167:  pattern (and W2–W9 it connects to).
```

</details>

## 🤖 Assistant

The auto-pass already de-coded the link anchors in "Going deeper." Now I need the prose codes. Let me check U3/U4 diffs for more patterns — especially CV expansion, workflow headers, and the garble fixes.

## 🤖 Assistant

**→ Bash**

```
git show 0d35846 -- course/units/03-operate-safely/unit.md course/units/04-memory-and-context/unit.md
```

<details><summary>tool result</summary>

```
commit 0d35846c89a024ed3f386236d109433607fe1e6f
Author: jj <jj@marlow.home>
Date:   Sun May 31 01:49:12 2026 -0700

    P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
    
    Checkpoint of the in-progress P7 rollout (Stage C). Stopping point for the session;
    make check green. Resume guide: specs/claude-code-mastery/tasks/P7-quality-pass.md
    → "Resume state".
    
    - U2–U4: fully de-coded + migrated to unit.src.md (committed-rendered). Cross-ref
      codes → titles ("your first unit" for U1 back-refs), CV expanded, R# breadcrumbs
      dropped, and the {{vd:settings}}/permission-modes/checkpoint-rewind render garbles
      fixed (sentence-valued/backtick-containing tokens must not be backtick-wrapped or
      used mid-sentence as nouns).
    - U5–U16: two safe scripted passes applied to unit.md — 88 cross-ref link anchors
      de-coded and 18 `advances `C#`` objective tails removed. NOT yet migrated; prose
      codes (bare U#, "The workflow — W#." headers, R# breadcrumbs, CV) remain.
    - State synced: P7 task file (per-unit grid + full Resume state + locked rules),
      decisions.md L8/P7 status, IMPLEMENTATION.md §3.
    
    Remaining: 7.6 U5–U16 prose+migrate, 7.7 cross-cutting sweep, 7.8 convention docs,
    7.9 close-out. Branch local only (not pushed).
    
    Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>

diff --git a/course/units/03-operate-safely/unit.md b/course/units/03-operate-safely/unit.md
index 0374f52..4f6c707 100644
--- a/course/units/03-operate-safely/unit.md
+++ b/course/units/03-operate-safely/unit.md
@@ -1,3 +1,4 @@
+<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
 ---
 id: U3
 title: "Operate safely while letting Claude act on your code"
@@ -19,13 +20,13 @@ lab_time_min: 20
 By the end of this unit you can:
 
 - **Choose the right permission mode for a task and explain when bypassing the permission model is
-  and isn't appropriate** — advances `C4`.
… [+270 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

I now have the full pattern. Let me confirm the exact source-file header and how `render-units` works before editing.

## 🤖 Assistant

**→ Bash**

```
head -5 course/units/02-explore-a-codebase/unit.src.md; echo "---RENDER-UNITS---"; sed -n '1,60p' tools/render-units
```

<details><summary>tool result</summary>

```
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
---
id: U2
title: "Explore and explain an unfamiliar codebase"
---RENDER-UNITS---
#!/usr/bin/env python3
"""render-units: generate each unit's learner-facing `unit.md` from its authored `unit.src.md`
by resolving {{vd:key}} tokens (R12.AC2 single-source rule).

This mirrors the render-checklist pattern (a committed generated artifact + a drift gate):
  - `unit.src.md` is authored — front matter + {{vd:key}} version-data tokens. Maintainers edit it.
  - `unit.md` is generated — the resolved prose a learner reads, with a leading GENERATED comment.

Usage:
  tools/render-units            # (re)write every unit.md from its unit.src.md
  tools/render-units --check    # verify each unit.md matches render(unit.src.md); drift => FAIL

Only units that have a `unit.src.md` are touched — units not yet migrated are left alone, so this
is safe to wire into `make check` during a gradual rollout.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _common import ROOT, UNITS, Reporter, load_version_data, render_vd  # noqa: E402

HEADER = (
    "<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. "
    "Edit unit.src.md, then run `make render`. -->\n"
)
LEADING_COMMENT_RE = re.compile(r"^<!--.*?-->\s*", re.DOTALL)


def sources():
    if not UNITS.exists():
        return []
    return sorted(UNITS.glob("*/unit.src.md"))

… [+26 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Everything's clear. The migration flow: edit prose in `unit.md` (unmigrated, hook-silent since `make check` stays green), then `git mv` to `unit.src.md`, prepend the SOURCE header, and `render-units` regenerates `unit.md`. U5's `{{vd:}}` tokens are already in safe sentence positions, so no garble risk.

Let me make the prose edits. Starting with the objectives, concept, and workflow header:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: and run the tests before you commit — the `CV` reflex applied to a real feature.
- new: and run the tests before you commit — the cross-cutting verification (CV) reflex applied to a real feature.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: You can now land a change (U1), read unfamiliar code (U2), operate safely (U3), and steer Claude with
- new: You can now land a change, read unfamiliar code, operate safely, and steer Claude with
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: **The workflow — W1.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). STOP what you are doing and wait for the user to tell you how to proceed.
```

</details>

## 🧑 User

[Request interrupted by user for tool use]

## 🧑 User

continue please, i accidently hit escape

## 🤖 Assistant

No problem. Let me re-apply the edits.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: and run the tests before you commit — the `CV` reflex applied to a real feature.
- new: and run the tests before you commit — the cross-cutting verification (CV) reflex applied to a real feature.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: You can now land a change (U1), read unfamiliar code (U2), operate safely (U3), and steer Claude with
- new: You can now land a change, read unfamiliar code, operate safely, and steer Claude with
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: **The workflow — W1.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the Concept body refs (U2 habit, U4 baseline, U1 diff-reflex, W1/U10 cousin):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: to you** — the habit from U2, now load-bearing.
- new: to you** — the habit from **Explore a codebase**, now load-bearing.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: [`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md), from U4) — catch that in the plan and
- new: [`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md), from **Memory & context**) — catch that in the plan and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: This is the same diff-reading reflex from U1, now on a change big enough that it earns its keep.
- new: This is the same diff-reading reflex from your first unit, now on a change big enough that it earns its keep.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: any unit is authored (that's the heavy-weight cousin of W1, taught fully in U10). The everyday version is
- new: any unit is authored (that's the heavy-weight cousin of this loop, taught fully in **Spec-driven dev**). The everyday version is
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the Lab step, two pitfalls, and the Going deeper section:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: against the files (U2 habit) — the plan is only as good as this.
- new: against the files — the plan is only as good as this.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: in review. (This is also why U4 mattered: memory only steers if you let it.)
- new: in review. (This is also why **Memory & context** mattered: memory only steers if you let it.)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: time — the habit you built on one line in U1 is the same habit here, where it actually protects you.
- new: time — the habit you built on one line in your first unit is the same habit here, where it actually protects you.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
- old: - **Next:** U6 (TDD) tightens the loop by writing the failing test *first*; U7 (debugging) and U8 (Git/PR)
- new: - **Next:** **TDD** tightens the loop by writing the failing test *first*; **Debugging** and **Git & PR**
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

All 12 prose edits applied. Let me verify no codes remain, then migrate to `unit.src.md` and render.

## 🤖 Assistant

**→ Bash**

```
f=course/units/05-ship-a-feature/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

Clean. Now migrate to `unit.src.md` and render:

## 🤖 Assistant

**→ Bash**

```
d=course/units/05-ship-a-feature
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

Render is GREEN and the tokens resolved cleanly in sentence position. Let me eyeball the rest of the rendered file (the lab/pitfalls/going-deeper tail) for any garbles:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
```

<details><summary>tool result</summary>

```
158	
159	## Common pitfalls
160	
161	- **Skipping straight to "code."** Asking for the feature without exploring or planning is how you get a
162	  confident, wrong implementation. The loop's value is entirely in the two gates you'd be skipping.
163	- **Rubber-stamping the plan.** Plan mode only helps if you *read* the plan. Approving a vague or
164	  wrong-layer plan just defers the problem to a more expensive moment.
165	- **Letting logic land in the router.** The baseline `CLAUDE.md` says domain logic lives in the service
166	  layer. A plan that counts tasks inside the route handler "works" but violates the convention — catch it
167	  in review. (This is also why **Memory & context** mattered: memory only steers if you let it.)
168	- **Forgetting the 404 / ownership case.** The happy path is easy; the security-relevant edge (someone
169	  else's project) is the one that distinguishes a real feature from a demo. The verifier checks it.
170	- **Committing on green tests alone.** Tests pass ≠ change is correct and scoped. Read the diff every
171	  time — the habit you built on one line in your first unit is the same habit here, where it actually protects you.
172	- **Reaching for extended thinking by reflex.** It's for genuinely hard problems; on routine features it
173	  just adds latency. Use it deliberately, not as a default.
174	
175	## Going deeper
176	
177	- **Next:** **TDD** tightens the loop by writing the failing test *first*; **Debugging** and **Git & PR**
178	  build on this same explore→plan→code→commit spine. Everything in the Daily Driver stage assumes you can
179	  run this loop fluently.
180	- [`meta/workflows.md`](../../../meta/workflows.md#w1--explore--plan--code--commit) — the generalized
181	  explore → plan → code → commit pattern (and the other workflows it connects to).
182	- Extended thinking / effort levels — Effort levels low, medium, high, xhigh, max (`--effort <level>`). — and where version-specifics are recorded:
183	  [`meta/version-record.md`](../../../meta/version-record.md).
184	- The exploration habit from [Explore a codebase](../02-explore-a-codebase/unit.md) and the memory/context levers from
185	  [Memory & context](../04-memory-and-context/unit.md) are the inputs that make a *good* plan possible.
186	- Stuck? [`course/stuck.md`](../../stuck.md) and the
187	  [progress checklist](../../progress-checklist.md).
188	</content>
189	</invoke>
190	
```

</details>

## 🤖 Assistant

Line 182 renders awkwardly — the `{{vd:thinking}}` value is a full sentence ending in a period, jammed between em-dashes ("— Effort levels … max (`--effort <level>`). — and where…"). That's the garble pattern (sentence-valued token used mid-sentence). I need to fix it in the **source** (`unit.src.md`), then re-render. Let me check the source line:

## 🤖 Assistant

**→ Bash**

```
grep -n 'vd:thinking' course/units/05-ship-a-feature/unit.src.md
```

<details><summary>tool result</summary>

```
88:> algorithm — you can have Claude think harder before answering: {{vd:thinking}} It's a dial you reach
183:- Extended thinking / effort levels — {{vd:thinking}} — and where version-specifics are recorded:
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.src.md
```

<details><summary>tool result</summary>

```
183	- Extended thinking / effort levels — {{vd:thinking}} — and where version-specifics are recorded:
184	  [`meta/version-record.md`](../../../meta/version-record.md).
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.src.md
- old: - Extended thinking / effort levels — {{vd:thinking}} — and where version-specifics are recorded:
- new: - Extended thinking / effort levels: {{vd:thinking}} Where version-specifics are recorded:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.src.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Expected — I edited the source but haven't re-rendered. Let me re-render and re-check:

## 🤖 Assistant

**→ Bash**

```
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/05-ship-a-feature/unit.md
```

<details><summary>tool result</summary>

```
182	- Extended thinking / effort levels: Effort levels low, medium, high, xhigh, max (`--effort <level>`). Where version-specifics are recorded:
183	  [`meta/version-record.md`](../../../meta/version-record.md).
184	- The exploration habit from [Explore a codebase](../02-explore-a-codebase/unit.md) and the memory/context levers from
```

</details>

## 🤖 Assistant

U5 is done and `make check` is green. Line 182 now reads cleanly.

## U5 complete — summary

**`05-ship-a-feature`** — migrated to the committed-rendered pattern (`unit.md` → `unit.src.md` + regenerated `unit.md`) and fully de-coded:

- **CV expanded** on first use: "the cross-cutting verification (CV) reflex" (objectives).
- **Breadcrumbs dropped** — Concept opener "You can now land a change (U1), read… (U2)…(U3)…(U4)" → plain prose (the descriptions already name the units).
- **`**The workflow — W1.**` → `**The workflow.**`** (next sentence names + links it).
- **Bare codes → titles** — U2→**Explore a codebase**, U4→**Memory & context**, U10→**Spec-driven dev**, U6/U7/U8→**TDD**/**Debugging**/**Git & PR**; U1 back-refs→"your first unit"; `W1`→"this loop" / "explore → plan → code → commit".
- **Garble fix (the eyeball caught one):** the "Going deeper" `{{vd:thinking}}` token was wedged between em-dashes, rendering a period mid-sentence — reworked to clean sentence position (`Extended thinking / effort levels: … Where version-specifics are recorded: …`).
- Verified all rendered `{{vd:}}` tokens land in sentence position (no backtick-wrapped sentences); `2.1.158` is the lone safe backticked token.

Files changed (uncommitted): `unit.src.md` (new, authored), `unit.md` (regenerated). No reading-time change for U5 (L2 bumps are U12–U14).

Next up is **U6 (TDD)** — its grid note flags `**The workflow — W2.**`, CV expansion, and U5/U7 prose refs. Want me to continue straight through U6, or commit U5 first?

## 🧑 User

continue through U6

## 🤖 Assistant

I'll apply the same pass to U6. Let me read it and scan for codes.

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U6
3	title: "Drive a new behavior test-first (red → green)"
4	stage: daily-driver
5	depth_tier: core
6	use_case: "Add behavior safely, test-first"
7	can_do: [C7]
8	workflows: [W2]
9	coverage_areas: [11]
10	prerequisites: [U5]
11	reading_time_min: 9
12	lab_time_min: 30
13	---
14	
15	# Drive a new behavior test-first (red → green)
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Drive a new behavior test-first through the red → green loop** — specify it as a failing test,
22	  confirm it fails, then implement just enough to pass.
23	- **Confirm the test fails for the *right* reason** — distinguish a real assertion failure (the
24	  behavior is genuinely missing) from a typo/import/collection error that fails for the wrong one.
25	- **Read the implementation, not just the green bar** — a test can be satisfied the wrong way
26	  (a hard-coded return, a too-broad query); the `CV` reflex applied to test-driven work.
27	- **Recognize when TDD earns its keep** — behavior you can pin as a test, or regression-prone /
28	  edge-case-heavy work — versus when it's overhead.
29	
30	## Fast path (TL;DR)
31	
32	> Test-driven development with Claude is [test-driven development](../../../meta/workflows.md#w2--test-driven-development):
33	> **write the test first, watch it go red, then make it green.** Have Claude write a test that pins the
34	> behavior you want, run it, and **confirm it fails for the right reason** (the behavior is missing —
35	> not a typo or a bad import). Then implement just enough to pass, and **read the implementation** to
36	> be sure the test wasn't satisfied the wrong way (a hard-coded value, a query that's too broad). The
37	> lab has you add an **`overdue` task filter** this way, and `tools/verify-lab u06-lab1` proves it.
38	
39	## Skip-check
40	
… [+160 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/06-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
13:  (a hard-coded return, a too-broad query); the `CV` reflex applied to test-driven work.
36:You can already ship a feature through explore → plan → code → commit (U5). TDD is that loop with the
44:**The workflow — W2.** The generalized pattern lives once in
68:U4/U5), with the route just wiring it up. Then run the suite and watch it go green.
75:Read the implementation diff the way U5 taught you to read any diff: does it compute the behavior, or
80:> U7). It's overhead for genuinely exploratory work where you don't yet know the shape of the answer,
169:- **Letting logic land in the router.** Same convention as U5: the overdue predicate is domain logic
176:- **Next:** U7 (debugging) reuses this loop in reverse — capture the bug as a failing test first, then
177:  fix to green — and U8 (Git/PR) turns the verified change into reviewable history. The red→green
179:- [`meta/workflows.md`](../../../meta/workflows.md#w2--test-driven-development) — the generalized W2
180:  pattern (and how it connects to W1 from U5 and W3 in U7).
```

</details>

## 🤖 Assistant

Let me check the `{{vd:test-run}}` value before editing, since U6 uses it three times in parens/mid-sentence — that's the garble risk to watch:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
for k in ['test-run','thinking']:
    print(repr(render_vd('{{vd:'+k+'}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
"Tests run through the Bash tool (e.g. `pytest`); no dedicated CLI flag — Claude invokes the project's existing test runner."
'Effort levels low, medium, high, xhigh, max (`--effort <level>`).'
```

</details>

## 🤖 Assistant

`test-run` renders to a full sentence (with internal parens, semicolon, and em-dash) and **no trailing period**. U6 uses it three times in awkward spots — wrapped in parens at L70, nested in parens at L97, and mid-clause at L194 — all of which will garble on render. I'll reposition those into clean sentence position as part of the pass.

Let me apply all U6 edits:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: (a hard-coded return, a too-broad query); the `CV` reflex applied to test-driven work.
- new: (a hard-coded return, a too-broad query); the cross-cutting verification (CV) reflex applied to test-driven work.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: You can already ship a feature through explore → plan → code → commit (U5). TDD is that loop with the
- new: You can already ship a feature through explore → plan → code → commit. TDD is that loop with the
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: **The workflow — W2.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: beginners skip and the one the unit is named for. Run the test ({{vd:test-run}}) and **read the
- new: beginners skip and the one the unit is named for. Run the test and **read the
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: [`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md) (the convention you internalized in
- new: [`CLAUDE.md`](../../../codebases/primary/taskflow-api/CLAUDE.md) (the convention you internalized in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: Read the implementation diff the way U5 taught you to read any diff: does it compute the behavior, or
- new: Read the implementation diff the way **Ship a feature** taught you to read any diff: does it compute the behavior, or
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: > is edge-case-heavy or regression-prone (exactly the lab's `overdue` rule, and most bug fixes — see
- new: > is edge-case-heavy or regression-prone (exactly the lab's `overdue` rule, and most bug fixes — see
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`; tests run
- new: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: - **Letting logic land in the router.** Same convention as U5: the overdue predicate is domain logic
- new: - **Letting logic land in the router.** Same convention as in **Ship a feature**: the overdue predicate is domain logic
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.md
- old: - **Next:** U7 (debugging) reuses this loop in reverse — capture the bug as a failing test first, then
- new: - **Next:** **Debugging** reuses this loop in reverse — capture the bug as a failing test first, then
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify no codes remain, then migrate and render:

## 🤖 Assistant

**→ Bash**

```
f=course/units/06-tdd/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/06-tdd
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

I see a double period at line 98 (`test runner..`) and the same issue will be in the going-deeper bullet — I misjudged: `{{vd:test-run}}` **does** end with its own period, so my added `.` doubled it. Let me fix both in the source:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
- old: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`.
- new: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`.
```

<details><summary>tool result</summary>

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
- old: - Running tests is ordinary tool-use: {{vd:test-run}}. Version-specifics live in
- new: - Running tests is ordinary tool-use: {{vd:test-run}} Version-specifics live in
```

<details><summary>tool result</summary>

```
<tool_use_error>File has not been read yet. Read it first before writing to it.</tool_use_error>
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
```

<details><summary>tool result</summary>

```
97	
98	**Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`.
99	{{vd:test-run}}. Confirm your project's runner (`taskflow-api` uses `pytest`) and see
100	[`meta/version-record.md`](../../../meta/version-record.md) if your version differs.
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
```

<details><summary>tool result</summary>

```
194	  test-driven-development pattern (and how it connects to the **Ship a feature** loop and **Debugging**).
195	- Running tests is ordinary tool-use: {{vd:test-run}}. Version-specifics live in
196	  [`meta/version-record.md`](../../../meta/version-record.md).
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
- old: {{vd:test-run}}. Confirm your project's runner (`taskflow-api` uses `pytest`) and see
- new: {{vd:test-run}} Confirm your project's runner (`taskflow-api` uses `pytest`) and see
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/06-tdd/unit.src.md
- old: - Running tests is ordinary tool-use: {{vd:test-run}}. Version-specifics live in
- new: - Running tests is ordinary tool-use: {{vd:test-run}} Version-specifics live in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.src.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/06-tdd/unit.src.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Expected drift — I edited the source but need to re-render. Let me re-render and check:

## 🤖 Assistant

**→ Bash**

```
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

Now eyeball the two corrected `test-run` renders:

## 🤖 Assistant

**→ Bash**

```
grep -n 'test runner' course/units/06-tdd/unit.md
```

<details><summary>tool result</summary>

```
98:Tests run through the Bash tool (e.g. `pytest`); no dedicated CLI flag — Claude invokes the project's existing test runner. Confirm your project's runner (`taskflow-api` uses `pytest`) and see
194:- Running tests is ordinary tool-use: Tests run through the Bash tool (e.g. `pytest`); no dedicated CLI flag — Claude invokes the project's existing test runner. Version-specifics live in
```

</details>

## 🤖 Assistant

Both render cleanly now — single period, natural sentence flow. U6 is done and `make check` is green.

## U6 complete — summary

**`06-tdd`** — migrated to `unit.src.md` + regenerated `unit.md`, fully de-coded:

- **CV expanded** on first use (objectives).
- **`**The workflow — W2.**` → `**The workflow.**`**; Concept opener breadcrumb `(U5)` dropped (the loop is named in-prose).
- **Codes → titles** — U5→**Ship a feature** (×3: convention ref, diff-reading ref, router pitfall), U4/U5→**Memory & context** and **Ship a feature**, U7→**Debugging** (×2), U8→**Git & PR**; the workflows bullet's `W2`/`W1`/`W3` chain rephrased to "test-driven-development pattern … **Ship a feature** loop and **Debugging**".
- **Garble fixes (3, all `{{vd:test-run}}`):** that token renders as a full sentence containing its own parens, semicolon, and em-dash. It was wrapped in parens at L70 (dropped — redundant with the version-currency note) and nested in parens at the version-currency note + wedged mid-clause in "Going deeper" (both repositioned to clean sentence position). Caught and corrected a double-period (`test runner..`) on the eyeball pass, since the value already ends in a period.

Files changed (uncommitted): `06-tdd/unit.src.md` (new), `unit.md` (regenerated).

That's **U5 and U6 done** this session (U1–U6 now complete). Next is **U7 (Debugging)** — grid note: `**The workflow — W3.**`, CV, U5/U6/U9 prose refs, and "the W2 reflex". Want me to continue to U7, or pause here to commit U5–U6?

## 🧑 User

continue to U7

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U7
3	title: "Debug an unfamiliar failure by confirming the root cause"
4	stage: daily-driver
5	depth_tier: core
6	use_case: "A test/endpoint is broken — find and fix it"
7	can_do: [C8]
8	workflows: [W3]
9	coverage_areas: [12]
10	prerequisites: [U5]
11	reading_time_min: 9
12	lab_time_min: 30
13	---
14	
15	# Debug an unfamiliar failure by confirming the root cause
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Debug an unfamiliar failure as a scientist, not a guesser** — reproduce it deterministically,
22	  confirm the *root cause* before changing anything, fix it, and prove the fix.
23	- **Capture the failure as a repro you can re-run** so "fixed" is objective, not a vibe.
24	- **Confirm the root cause rather than pattern-matching the symptom** — and resist the AI's pull
25	  toward a plausible-looking change that treats a symptom and leaves the cause (and its copies) intact.
26	- **Verify the fix *and* that nothing regressed** — the bug is gone, the repro passes, and the rest
27	  of the program still works (`CV`).
28	
29	## Fast path (TL;DR)
30	
31	> Debugging with Claude is [the debugging workflow](../../../meta/workflows.md#w3--debugging-an-unfamiliar-failure):
32	> **reproduce → capture → confirm root cause → fix → no-regress.** Get a deterministic repro first;
33	> have Claude (and you) **find the real cause** before touching code — the #1 failure mode is letting
34	> a confident AI patch a symptom. Then fix at the cause, re-run the repro to confirm it's gone, and
35	> check nothing else broke. The lab hands you a real bug in the messy `taskflow-cli`: **overdue tasks
36	> are never flagged.** You'll chase it to its root — and discover the cause is copy-pasted in three
37	> places, so a one-site "fix" leaves the bug alive. `tools/verify-lab u07-lab1` proves you got it.
38	
39	## Skip-check
40	
… [+146 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/07-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
14:  of the program still works (`CV`).
35:In U5 and U6 you *added* behavior; debugging is the inverse skill — something already works wrong and
42:**The workflow — W3.** The generalized pattern lives once in
55:is the W2 reflex (U6) pointed at a bug: the captured failure is what flips from red to green to *prove*
57:which means the repro you capture here is its *first* characterization test, a thread U9 picks up.)
94:confirming it before editing is what kept the check honest. (That exact failure happened authoring U6.)
164:- **Next:** U8 (Git/PR) turns the verified fix into reviewable history; U9 (onboard + refactor) returns
168:  W3 pattern, and how it reuses the failing-test reflex from [W2](../06-tdd/unit.md).
```

</details>

## 🤖 Assistant

U7 has **no `{{vd:}}` tokens** (version-currency explicitly says nothing version-specific), so no garble risk — a clean prose pass. Let me apply the edits:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: of the program still works (`CV`).
- new: of the program still works (cross-cutting verification, CV).
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: In U5 and U6 you *added* behavior; debugging is the inverse skill
- new: In **Ship a feature** and **TDD** you *added* behavior; debugging is the inverse skill
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: **The workflow — W3.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: command — a failing test, or at minimum a scripted command sequence with a known expected output. This
- new: command — a failing test, or at minimum a scripted command sequence with a known expected output. This
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: confirming it before editing is what kept the check honest. (That exact failure happened authoring U6.)
- new: confirming it before editing is what kept the check honest. (That exact failure happened while authoring the **TDD** unit.)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md
- old: - **Next:** U8 (Git/PR) turns the verified fix into reviewable history; U9 (onboard + refactor) returns
- new: - **Next:** **Git & PR** turns the verified fix into reviewable history; **Refactor legacy** returns
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/07-debug-a-failure/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/07-debug-a-failure/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/07-debug-a-failure
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U7 done, `make check` green. No `{{vd:}}` tokens, so no garble risk — straight prose pass.

## U7 complete — summary

**`07-debug-a-failure`** — migrated + de-coded:
- **CV expanded** in the objectives: `(\`CV\`)` → `(cross-cutting verification, CV)`.
- **`**The workflow — W3.**` → `**The workflow.**`**.
- **Codes → titles** — U5/U6→**Ship a feature** and **TDD** (Concept opener); "the W2 reflex (U6)" → "the red→green reflex from **TDD**"; U9→**Refactor legacy** (×2); the worked-example "authoring U6" → "authoring the **TDD** unit"; U8→**Git & PR**; and the workflows bullet's `W3 pattern` + link text `[W2](../06-tdd/unit.md)` → "debugging pattern" + `[TDD](…)`.

Files changed (uncommitted): `07-debug-a-failure/unit.src.md` (new), `unit.md` (regenerated).

**Progress:** U1–U7 now complete; U8–U16 remain. We've got 7 units' worth of uncommitted work on the branch (U5, U6, U7 from this session, plus the migrations). Want me to **continue to U8 (Git & PR)**, or **commit U5–U7** as a checkpoint first?

## 🧑 User

continue to U8

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U8
3	title: "Turn a body of work into clean commits and a reviewable PR"
4	stage: daily-driver
5	depth_tier: core
6	use_case: "Turn my work into a clean, reviewable PR"
7	can_do: [C9]
8	workflows: [W4]
9	coverage_areas: [13]
10	prerequisites: [U5]
11	reading_time_min: 9
12	lab_time_min: 25
13	---
14	
15	# Turn a body of work into clean commits and a reviewable PR
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Turn a pile of work into clean, logically atomic commits** with messages that explain *why*, and
22	  a PR whose description matches the actual diff.
23	- **Stage deliberately** — decide what belongs in each commit rather than `git add -A`-ing everything,
24	  and keep unrelated changes out of a feature's history.
25	- **Self-review the PR as if you were the reviewer** before requesting one — reading the full diff and
26	  confirming the description makes no claims the code doesn't back up (`CV` applied to shareable work).
27	- **Use Claude to draft the history and the PR, then verify it** — drive `git` and `gh` through the
28	  Bash tool, but own the final shape of the commits and the description.
29	
30	## Fast path (TL;DR)
31	
32	> The Git/PR workflow is [the Git/PR workflow](../../../meta/workflows.md#w4--git--pr-workflow): turn work into history
33	> someone can *review*. **Stage deliberately** (each commit is one logical change), **write messages
34	> that explain why** (not "fix stuff"), **open a PR whose description matches the diff**, and
35	> **self-review it first** — read the whole diff as the reviewer would. Claude can draft all of this —
36	> the commit splits, the messages, the PR body via {{vd:git-pr}} — but *you* confirm the description
37	> claims only what the code does. The lab has you take a real change in `taskflow-api` and make it
38	> review-ready; the self-check is a reviewer's checklist you apply to your own diff.
39	
40	## Skip-check
… [+148 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/08-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
13:  confirming the description makes no claims the code doesn't back up (`CV` applied to shareable work).
36:You can ship a verified change (U5–U7). U8 is about the last mile: making that change **reviewable** —
41:**The workflow — W4.** The generalized pattern lives once in
71:here is faster and cheaper than a review round-trip, and it's the same verification reflex from U5–U7
99:> needs a remote and `gh` that this course can't assume (R7.AC7). So the self-check below is an
100:> objective **reviewer's checklist** you apply to your own work — applying it *is* the skill W4
120:1. Drive the change with the loop you already know (explore → plan → code, U5; lean on tests, U6).
130:5. *(Optional stretch — BYO, non-verifiable, R7.AC8):* on your **own** fork/remote, push the branch and
133:**Self-check (objective checklist — R7.AC3):** your work is review-ready when **all** hold:
165:- **Next:** the Force-Multiplier stage (U9 refactor, U10 spec-driven, U11 review) all assume you can
166:  produce reviewable history; U11 (code & security review) is the other side of this coin — *being* the
167:  reviewer. U16 (automate & scale) drives PRs headlessly in CI.
168:- [`meta/workflows.md`](../../../meta/workflows.md#w4--git--pr-workflow) — the generalized W4 pattern.
```

</details>

## 🤖 Assistant

U8 has `{{vd:git-pr}}` tokens and the grid flags R7.AC3/AC7/AC8 breadcrumbs. Let me check the `git-pr` value before editing:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
print(repr(render_vd('{{vd:git-pr}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
'`--from-pr [value]` resumes a session linked to a PR by number/URL; PR creation uses the `gh` CLI via the Bash tool.'
```

</details>

## 🤖 Assistant

U8 uses `{{vd:git-pr}}` five times, and the value is a full sentence (starts with a backtick, has a semicolon, ends with a period). Four of those five placements will garble on render (wrapped in parens, jammed after "via", or producing `.;`). I'll reposition all of them, plus the prose codes and the R7.AC3/AC7/AC8 breadcrumbs.

Batch 1 — objectives, concept, workflow header, lab callout:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: confirming the description makes no claims the code doesn't back up (`CV` applied to shareable work).
- new: confirming the description makes no claims the code doesn't back up — cross-cutting verification (CV) applied to shareable work.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: You can ship a verified change (U5–U7). U8 is about the last mile: making that change **reviewable** —
- new: You can ship a verified change. This unit is about the last mile: making that change **reviewable** —
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: **The workflow — W4.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: here is faster and cheaper than a review round-trip, and it's the same verification reflex from U5–U7
- new: here is faster and cheaper than a review round-trip, and it's the same verification reflex from the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: > needs a remote and `gh` that this course can't assume (R7.AC7). So the self-check below is an
- new: > needs a remote and `gh` that this course can't assume. So the self-check below is an
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 2 — lab steps + Going deeper prose codes:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: 1. Drive the change with the loop you already know (explore → plan → code, U5; lean on tests, U6).
- new: 1. Drive the change with the loop you already know (explore → plan → code, from **Ship a feature**; lean on tests, from **TDD**).
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: 5. *(Optional stretch — BYO, non-verifiable, R7.AC8):* on your **own** fork/remote, push the branch and
- new: 5. *(Optional stretch — BYO, non-verifiable):* on your **own** fork/remote, push the branch and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: **Self-check (objective checklist — R7.AC3):** your work is review-ready when **all** hold:
- new: **Self-check (objective checklist):** your work is review-ready when **all** hold:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: - **Next:** the Force-Multiplier stage (U9 refactor, U10 spec-driven, U11 review) all assume you can
- new: - **Next:** the Force-Multiplier stage (**Refactor legacy**, **Spec-driven dev**, **Code & security
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 3 — the five `{{vd:git-pr}}` token placements:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: > **self-review it first** — read the whole diff as the reviewer would. Claude can draft all of this —
- new: > **self-review it first** — read the whole diff as the reviewer would. Claude can draft all of this —
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: **3 — Open a PR whose description matches the diff.** PR creation is `gh` through the Bash tool
- new: **3 — Open a PR whose description matches the diff.** PR creation is `gh` through the Bash tool;
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: here is faster and cheaper than a review round-trip, and it's the same verification reflex from the
- new: here is faster and cheaper than a review round-trip, and it's the same verification reflex from the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`; the `gh`
- new: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`. The
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
- old: - The `gh` integration and `--from-pr` — {{vd:git-pr}}; version-specifics in
- new: - The `gh` integration and `--from-pr`: {{vd:git-pr}} Version-specifics in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/08-git-and-pr/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/08-git-and-pr
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

Let me eyeball the Going deeper tail (the last `git-pr` placement and the prose-code edits there):

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/08-git-and-pr/unit.md
```

<details><summary>tool result</summary>

```
176	
177	## Going deeper
178	
179	- **Next:** the Force-Multiplier stage (**Refactor legacy**, **Spec-driven dev**, **Code & security
180	  review**) all assume you can produce reviewable history — and **Code & security review** is the other
181	  side of this coin: *being* the reviewer. **Automate & scale** drives PRs headlessly in CI.
182	- [`meta/workflows.md`](../../../meta/workflows.md#w4--git--pr-workflow) — the generalized Git/PR pattern.
183	- The `gh` integration and `--from-pr`: `--from-pr [value]` resumes a session linked to a PR by number/URL; PR creation uses the `gh` CLI via the Bash tool. Version-specifics in
184	  [`meta/version-record.md`](../../../meta/version-record.md).
185	- The verify-before-you-ship reflex traces straight back to [Ship a feature](../05-ship-a-feature/unit.md)'s diff
186	  review and [Debugging](../07-debug-a-failure/unit.md)'s "don't claim it's fixed until it's proven."
187	- Stuck? [`course/stuck.md`](../../stuck.md) and the
188	  [progress checklist](../../progress-checklist.md).
189	
```

</details>

## 🤖 Assistant

U8 done, `make check` green. All five `{{vd:git-pr}}` placements render cleanly in sentence position now.

## U8 complete — summary

**`08-git-and-pr`** — migrated + de-coded:
- **CV expanded** in objectives (`(\`CV\` applied…)` → `— cross-cutting verification (CV) applied…`).
- **`**The workflow — W4.**` → `**The workflow.**`**; Concept opener `(U5–U7). U8 is` → plain prose; "reflex from U5–U7" → "from the previous units".
- **Codes → titles** — lab step 1 `U5`/`U6` → **Ship a feature**/**TDD**; Going-deeper Next `U9/U10/U11/U16` → **Refactor legacy**/**Spec-driven dev**/**Code & security review**/**Automate & scale**; `W4 pattern` → "Git/PR pattern"; "skill W4 teaches" → "skill this workflow teaches".
- **R# breadcrumbs dropped** — `(R7.AC7)`, `(R7.AC8)`, `(R7.AC3)`.
- **Garble fixes (4 of 5 `{{vd:git-pr}}` uses):** the value is a full backtick-leading sentence with a semicolon. It was wedged after "via" (TL;DR), nested in parens (Concept §3 + version-currency), and producing a `.;` collision (Going deeper). Repositioned all into clean sentence position; the Concept §3 and TL;DR mentions became plain prose (the `--from-pr` token now lives in §4, version-currency, and Going deeper where it's actually relevant).

Files changed (uncommitted): `08-git-and-pr/unit.src.md` (new), `unit.md` (regenerated).

**Progress: U1–U8 done; U9–U16 remain.** Four units de-coded this session (U5–U8) plus their migrations are uncommitted on the branch. Want me to **continue to U9 (Refactor legacy)**, or **commit U5–U8** as a checkpoint first? U9 is one of the longer units, so a checkpoint here is a reasonable spot.

## 🧑 User

commit U5–U8 then continue to U9

## 🤖 Assistant

I'll commit U5–U8 first. Let me review what's staged and check the diffstat before committing.

## 🤖 Assistant

**→ Bash**

```
git status --short && echo "---" && git diff --stat HEAD
```

<details><summary>tool result</summary>

```
RM course/units/05-ship-a-feature/unit.md -> course/units/05-ship-a-feature/unit.src.md
RM course/units/06-tdd/unit.md -> course/units/06-tdd/unit.src.md
RM course/units/07-debug-a-failure/unit.md -> course/units/07-debug-a-failure/unit.src.md
RM course/units/08-git-and-pr/unit.md -> course/units/08-git-and-pr/unit.src.md
?? course/units/05-ship-a-feature/unit.md
?? course/units/06-tdd/unit.md
?? course/units/07-debug-a-failure/unit.md
?? course/units/08-git-and-pr/unit.md
---
 .../05-ship-a-feature/{unit.md => unit.src.md}     | 34 +++++++--------
 course/units/06-tdd/{unit.md => unit.src.md}       | 33 +++++++--------
 .../07-debug-a-failure/{unit.md => unit.src.md}    | 18 ++++----
 .../units/08-git-and-pr/{unit.md => unit.src.md}   | 48 +++++++++++-----------
 4 files changed, 70 insertions(+), 63 deletions(-)
```

</details>

## 🤖 Assistant

Staging both the renamed `.src.md` files and the new generated `unit.md` files, with a final green check:

## 🤖 Assistant

**→ Bash**

```
git add course/units/05-ship-a-feature course/units/06-tdd course/units/07-debug-a-failure course/units/08-git-and-pr
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
M  course/units/05-ship-a-feature/unit.md
A  course/units/05-ship-a-feature/unit.src.md
M  course/units/06-tdd/unit.md
A  course/units/06-tdd/unit.src.md
M  course/units/07-debug-a-failure/unit.md
A  course/units/07-debug-a-failure/unit.src.md
M  course/units/08-git-and-pr/unit.md
A  course/units/08-git-and-pr/unit.src.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
git commit -q -F - <<'MSG'
P7: roll learner-prose remediation through U5–U8 (migrate + de-code)

Continue the Stage-C editorial rollout (tasks/P7-quality-pass.md §7.6). U5–U8
migrated to the committed-rendered pattern (unit.src.md authored + generated
unit.md) and fully de-coded, matching the U1–U4 precedent:

- Cross-ref codes → titles ("your first unit" for U1 back-refs; bold unit
  titles elsewhere); "The workflow — W#." headers → "The workflow."; CV
  expanded once per unit; R# breadcrumbs dropped (U8: R7.AC3/AC7/AC8).
- Render-and-eyeball caught several version-token garbles, fixed at source:
  U5 {{vd:thinking}} wedged between em-dashes; U6 {{vd:test-run}} (sentence-
  valued) wrapped in parens / doubled-period; U8 {{vd:git-pr}} (backtick-
  leading sentence) jammed after "via", nested in parens, and ".;" collision.
  All repositioned to sentence position.

make check green. Branch local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (34.2KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bvjslxf02.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

The pre-commit hook ran the full check (that's the verbose output). Let me confirm the commit landed:

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
f18ed18 P7: roll learner-prose remediation through U5–U8 (migrate + de-code)
---
```

</details>

## 🤖 Assistant

Committed (`f18ed18`), working tree clean. Now on to **U9 (Refactor legacy)**:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U9
3	title: "Onboard a legacy codebase and refactor it without changing behavior"
4	stage: force-multiplier
5	depth_tier: core
6	use_case: "Map an unfamiliar legacy codebase and refactor it safely"
7	can_do: [C10]
8	workflows: [W5, W8]
9	coverage_areas: [14]
10	prerequisites: [U2, U7]
11	reading_time_min: 11
12	lab_time_min: 40
13	---
14	
15	# Onboard a legacy codebase and refactor it without changing behavior
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Onboard deeply to an unfamiliar, messy codebase** — drive Claude to map its architecture, data
22	  flow, and duplication, then *validate that map against the source* before trusting it.
23	- **Establish a green baseline before you refactor** — and when the code has no tests, build a
24	  **characterization safety net** (tests that pin *current* behavior, bugs included) so "behavior
25	  preserved" becomes objective rather than hopeful.
26	- **Run a multi-file, behavior-preserving refactor in reviewable increments** — split a god-module,
27	  de-duplicate, keep the suite green at every step.
28	- **Guard the refactor against scope creep** — refuse to mix a behavior change (even a tempting
29	  bug-fix) into a "pure" refactor, and diff-review specifically for behavior that snuck in (`CV`).
30	
31	## Fast path (TL;DR)
32	
33	> This unit combines two workflows: **deep onboarding** ([deep onboarding](../../../meta/workflows.md#w8--onboarding-to-an-unfamiliarlarge-codebase),
34	> the heavy version of U2's light explore) and **multi-file refactoring**
35	> ([multi-file refactoring](../../../meta/workflows.md#w5--multi-file-refactoring)). The discipline: **map the code and
36	> validate the map → establish a green baseline → refactor in increments → keep the suite green before
37	> *and* after → diff-review for scope creep.** The twist with legacy code is that there's often **no
38	> suite to stay green** — so your first move is to **write characterization tests** that pin today's
39	> behavior (including its bugs) before you touch structure. The lab hands you the ~700-line
40	> single-file `taskflow-cli` god-module and asks you to split and de-duplicate it **without changing
… [+198 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/09-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
16:  bug-fix) into a "pure" refactor, and diff-review specifically for behavior that snuck in (`CV`).
21:> the heavy version of U2's light explore) and **multi-file refactoring**
28:> one byte of observable behavior** — including the overdue bug from U7, which you must *not* fix here
48:**Part 1 — deep onboarding (W8, deep).** You met the light version in [Explore a codebase](../02-explore-a-codebase/unit.md):
57:**Part 2 — multi-file refactoring (W5).** A refactor is a **behavior-preserving** change: the code's
70:is green." (It's the U7 capture reflex — pin behavior so a change is measurable — pointed at a whole
78:Plan mode (U5) is the right gate here — get the decomposition plan and approve it *before* Claude
89:("I'm right here, I'll just fix it") is exactly the scope creep W5 warns about. **Don't.** A refactor
103:and its tests via the Bash tool, plan mode from U5). See
122:> refactor **preserved behavior exactly** (the W5 "green before and after," and it fails if you let a
141:2. **Onboard deeply (W8).** Ask Claude to map the file: the layers (storage / domain / formatting /
150:4. **Plan the decomposition, then refactor in increments (W5).** In plan mode, get a module split you
156:   increment for any behavior that moved. Commit the refactor as its own clean history (U8).
158:**Self-check (objective — R7.AC3):** run `tools/verify-lab u09-lab1`. It passes only if, driving your
211:- **Next:** U10 (spec-driven development) is the other force-multiplier discipline — building the *right*
212:  thing up front rather than rescuing the wrong thing later; U11 (code & security review) is how you'd
214:- [`meta/workflows.md`](../../../meta/workflows.md#w5--multi-file-refactoring) — generalized W5, and
218:  objective" / [TDD](../06-tdd/unit.md)'s red-green, scaled from one bug to a whole program — and U7
```

</details>

## 🤖 Assistant

U9 has **no `{{vd:}}` tokens** (version-currency confirms nothing version-specific) — clean prose pass, no garble risk. I also spotted an auto-pass artifact at the workflows bullet ("deep onboarding deep onboarding" — the script de-coded a link but left the trailing duplicate word) that I'll clean up.

Group 1 — objectives + TL;DR:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: bug-fix) into a "pure" refactor, and diff-review specifically for behavior that snuck in (`CV`).
- new: bug-fix) into a "pure" refactor, and diff-review specifically for behavior that snuck in (cross-cutting verification, CV).
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: > the heavy version of U2's light explore) and **multi-file refactoring**
- new: > the heavy version of **Explore a codebase**'s light explore) and **multi-file refactoring**
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: > one byte of observable behavior** — including the overdue bug from U7, which you must *not* fix here
- new: > one byte of observable behavior** — including the overdue bug from **Debugging**, which you must *not* fix here
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group 2 — Part headers + Concept refs:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: **Part 1 — deep onboarding (W8, deep).** You met the light version in [Explore a codebase](../02-explore-a-codebase/unit.md):
- new: **Part 1 — deep onboarding.** You met the light version in [Explore a codebase](../02-explore-a-codebase/unit.md):
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: **Part 2 — multi-file refactoring (W5).** A refactor is a **behavior-preserving** change:
- new: **Part 2 — multi-file refactoring.** A refactor is a **behavior-preserving** change:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: is green." (It's the U7 capture reflex — pin behavior so a change is measurable — pointed at a whole
- new: is green." (It's the capture reflex from **Debugging** — pin behavior so a change is measurable — pointed at a whole
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: Plan mode (U5) is the right gate here — get the decomposition plan and approve it *before* Claude
- new: Plan mode (from **Ship a feature**) is the right gate here — get the decomposition plan and approve it *before* Claude
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: ("I'm right here, I'll just fix it") is exactly the scope creep W5 warns about. **Don't.** A refactor
- new: ("I'm right here, I'll just fix it") is exactly the scope creep this workflow warns about. **Don't.** A refactor
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: and its tests via the Bash tool, plan mode from U5). See
- new: and its tests via the Bash tool, plan mode from **Ship a feature**). See
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group 3 — Lab section:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: > refactor **preserved behavior exactly** (the W5 "green before and after," and it fails if you let a
- new: > refactor **preserved behavior exactly** (the "green before and after" rule, and it fails if you let a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: 2. **Onboard deeply (W8).** Ask Claude to map the file: the layers (storage / domain / formatting /
- new: 2. **Onboard deeply.** Ask Claude to map the file: the layers (storage / domain / formatting /
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: 4. **Plan the decomposition, then refactor in increments (W5).** In plan mode, get a module split you
- new: 4. **Plan the decomposition, then refactor in increments.** In plan mode, get a module split you
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: increment for any behavior that moved. Commit the refactor as its own clean history (U8).
- new: increment for any behavior that moved. Commit the refactor as its own clean history (the **Git & PR** habit).
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: **Self-check (objective — R7.AC3):** run `tools/verify-lab u09-lab1`. It passes only if, driving your
- new: **Self-check (objective):** run `tools/verify-lab u09-lab1`. It passes only if, driving your
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group 4 — Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: - **Next:** U10 (spec-driven development) is the other force-multiplier discipline — building the *right*
- new: - **Next:** **Spec-driven dev** is the other force-multiplier discipline — building the *right*
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
- old: objective" / [TDD](../06-tdd/unit.md)'s red-green, scaled from one bug to a whole program — and U7
- new: objective" / [TDD](../06-tdd/unit.md)'s red-green, scaled from one bug to a whole program — and the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/09-onboard-refactor-legacy/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/09-onboard-refactor-legacy
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

Renders clean. Let me eyeball the Going-deeper tail to confirm the workflows bullet and de-dup fix:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/09-onboard-refactor-legacy/unit.md
```

<details><summary>tool result</summary>

```
222	
223	## Going deeper
224	
225	- **Next:** **Spec-driven dev** is the other force-multiplier discipline — building the *right*
226	  thing up front rather than rescuing the wrong thing later; **Code & security review** is how you'd
227	  review a refactor like this one before it merges.
228	- [`meta/workflows.md`](../../../meta/workflows.md#w5--multi-file-refactoring) — generalized multi-file
229	  refactoring, and [deep onboarding](../../../meta/workflows.md#w8--onboarding-to-an-unfamiliarlarge-codebase)
230	  (the heavy version of [Explore a codebase](../02-explore-a-codebase/unit.md)'s light explore).
231	- The characterization-test reflex is [Debugging](../07-debug-a-failure/unit.md)'s "capture it so 'fixed' is
232	  objective" / [TDD](../06-tdd/unit.md)'s red-green, scaled from one bug to a whole program — and the
233	  debugging lab literally foreshadowed this one: the overdue bug hid in three copies *because* of the
234	  duplication you untangle here.
235	- Plan-mode-as-a-gate and diff review come straight from [Ship a feature](../05-ship-a-feature/unit.md); clean
236	  incremental history is [Git & PR](../08-git-and-pr/unit.md).
237	- Stuck? [`course/stuck.md`](../../stuck.md) and the
238	  [progress checklist](../../progress-checklist.md).
239	
```

</details>

## 🤖 Assistant

All clean — the "deep onboarding deep onboarding" duplicate is fixed and the workflows bullet reads naturally. U9 done, `make check` green.

## U9 complete — summary

**`09-onboard-refactor-legacy`** — migrated + de-coded:
- **CV expanded** in objectives.
- **Workflow codes dropped from headers/labels** — `**Part 1 — deep onboarding (W8, deep).**` → `**Part 1 — deep onboarding.**`; `**Part 2 … (W5).**` → drop; lab steps `**Onboard deeply (W8).**`/`**…increments (W5).**` → drop; "the W5 '…'" / "scope creep W5 warns about" → "the '…' rule" / "this workflow warns about".
- **Codes → titles** — U2→**Explore a codebase**, U7→**Debugging** (×2 in body; the Going-deeper self-ref reworded to "the debugging lab … this one" to avoid a third repeat), U5→**Ship a feature** (×2, plan mode), U8→**Git & PR**, U10/U11→**Spec-driven dev**/**Code & security review**; workflows bullet `generalized W5` → "generalized multi-file refactoring".
- **R# breadcrumb dropped** — `(R7.AC3)` on the self-check.
- **Auto-pass artifact fixed** — the workflows bullet had "[deep onboarding](…) **deep onboarding** (the heavy version…)" (script de-coded the `[W8]` link text but left the trailing duplicate word); collapsed to a single "deep onboarding".
- No `{{vd:}}` tokens, so no garble risk.

Files changed (uncommitted): `09-onboard-refactor-legacy/unit.src.md` (new), `unit.md` (regenerated).

**Progress: U1–U9 done; U10–U16 remain.** U9 is uncommitted on the branch (committed checkpoint sits at U8 / `f18ed18`).

Next is **U10 (Spec-driven dev)** — the special one: the grid says **keep** the teaching `R1`/`R2.AC3`/`R1`–`R15` references but strip the breadcrumb cites (`R3.AC2`, `R7.AC3`); plus `W7`, U5/U11 prose, and CV. Want me to continue to U10?

## 🧑 User

continue to U10

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U10
3	title: "Build a feature spec-first: requirements → design → tasks"
4	stage: force-multiplier
5	depth_tier: core
6	use_case: "Build a feature spec-first"
7	can_do: [C11]
8	workflows: [W7]
9	coverage_areas: [15]
10	prerequisites: [U5]
11	reading_time_min: 11
12	lab_time_min: 35
13	---
14	
15	# Build a feature spec-first: requirements → design → tasks
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Run a spec-driven workflow for a feature whose cost-of-wrong is high** — drive Claude through
22	  **requirements → design → tasks** with an explicit approval gate between phases.
23	- **Write requirements that pin behavior, not implementation** — testable acceptance criteria with
24	  stable IDs, so "done" is objective and every later artifact has something to trace back to.
25	- **Hold the phase gates** — review and approve each phase *before* the next begins, rather than
26	  letting Claude race from a one-line prompt straight to code.
27	- **Keep the spec traceable** — every design choice serves a requirement, every task builds a design
28	  element, so you can answer "why does this code exist?" by walking back up the chain (`CV`).
29	
30	## Fast path (TL;DR)
31	
32	> Spec-driven development ([spec-driven development](../../../meta/workflows.md#w7--spec-driven-development)) is the
33	> heavyweight cousin of U5's explore→plan→code: for a feature where building the *wrong* thing is
34	> expensive, you align **before** writing code by producing three reviewed artifacts in order —
35	> **requirements** (the WHAT, as testable criteria), **design** (the HOW), **tasks** (the ordered
36	> build plan) — with an **approval gate** between each. The discipline is *gates and traceability*:
37	> don't start design until requirements are approved, and make every design choice and task trace
38	> back to a requirement. **This course's own [`specs/`](../../../specs/claude-code-mastery/) is the
39	> worked example** — you're reading a thing built this way. The lab has you run a mini spec for one
40	> small `taskflow-api` feature and grade it against a rubric (spec quality is a judgment call, so
… [+177 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/10-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
15:  element, so you can answer "why does this code exist?" by walking back up the chain (`CV`).
20:> heavyweight cousin of U5's explore→plan→code: for a feature where building the *wrong* thing is
40:U5 taught the everyday loop: explore, plan, code, commit. Plan mode there is a *lightweight* gate —
46:**The workflow — W7.** The generalized pattern lives once in
56:requirements describe *observable behavior and constraints*, and they get IDs (`R1`, `R2.AC3`…) so
77:is the U5 loop (explore→plan→code→commit) — but now the plan is largely written and the acceptance
89:U5's plan mode. Reserve the full ceremony for genuinely ambiguous or expensive work; misapplying it to
92:**Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — W7 is a
100:[`specs/claude-code-mastery/`](../../../specs/claude-code-mastery/) is the worked example (R3.AC2):
103:  acceptance criteria with stable IDs (`R1`–`R15`, `R*.AC*`). Notice they describe behavior and
106:  requirement it serves (e.g. *"§3 Workflow methods → `meta/workflows.md` [R3]"*) — that bracketed
122:> or a gate was genuinely held are **judgment calls** no script can grade (R7.AC3) — and the point of
123:> W7 is the reviewed alignment, not a passing test. So the self-check is an objective **rubric** you
124:> apply to your own spec; applying it *is* the skill. (Precedent: U2, U4, U8.)
139:   ID'd (`R1`, `R2`…), describing behavior not implementation, and resolving the ambiguities above.
148:4. **Build against the spec (U5 loop).** Implement following the tasks (explore→plan→code→commit), using
153:**Self-check (objective rubric — R7.AC3):** your spec-driven run is sound when **all** hold:
185:  to resent the process. Match the ceremony to the cost-of-wrong; small/obvious → U5's plan mode.
192:- **Next:** U11 (code & security review) is how a reviewed spec's implementation gets a final
193:  correctness/security pass before merge; together U9–U11 are the Force-Multiplier disciplines —
195:- [`meta/workflows.md`](../../../meta/workflows.md#w7--spec-driven-development) — generalized W7, the
196:  heavyweight cousin of [W1](../05-ship-a-feature/unit.md) (U5's explore→plan→code).
198:  worked example (R3.AC2); start at
```

</details>

## 🤖 Assistant

This is the special unit. I'll **keep** the teaching R-IDs (`R1`, `R2.AC3`, `R1`–`R15`, `R*.AC*`, the `R-whatever` and the illustrative `[R3]` traceability tag — they teach what requirement IDs look like) and **strip only the breadcrumb cites** (`R3.AC2`, `R7.AC3`), plus the usual U#/W#/CV pass. No `{{vd:}}` tokens beyond none here, so no garble risk.

Group A — objectives, TL;DR, Concept open, workflow header:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: element, so you can answer "why does this code exist?" by walking back up the chain (`CV`).
- new: element, so you can answer "why does this code exist?" by walking back up the chain (cross-cutting verification, CV).
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: > heavyweight cousin of U5's explore→plan→code: for a feature where building the *wrong* thing is
- new: > heavyweight cousin of **Ship a feature**'s explore→plan→code: for a feature where building the *wrong* thing is
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: U5 taught the everyday loop: explore, plan, code, commit. Plan mode there is a *lightweight* gate —
- new: **Ship a feature** taught the everyday loop: explore, plan, code, commit. Plan mode there is a *lightweight* gate —
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: **The workflow — W7.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group B — Concept §4, "When NOT", version currency:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: is the U5 loop (explore→plan→code→commit) — but now the plan is largely written and the acceptance
- new: is the **Ship a feature** loop (explore→plan→code→commit) — but now the plan is largely written and the acceptance
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: building the wrong thing is high. A one-line fix or an obvious endpoint doesn't need three phases — use
- new: building the wrong thing is high. A one-line fix or an obvious endpoint doesn't need three phases — use
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: **Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — W7 is a
- new: **Version currency.** Nothing in this unit depends on a version-specific Claude Code surface — spec-driven development is a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group C — breadcrumb cites (R3.AC2, R7.AC3) and the Precedent titles:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: [`specs/claude-code-mastery/`](../../../specs/claude-code-mastery/) is the worked example (R3.AC2):
- new: [`specs/claude-code-mastery/`](../../../specs/claude-code-mastery/) is the worked example:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: > or a gate was genuinely held are **judgment calls** no script can grade (R7.AC3) — and the point of
- new: > or a gate was genuinely held are **judgment calls** no script can grade — and the point of
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group D — lab step 4 + self-check heading:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: 4. **Build against the spec (U5 loop).** Implement following the tasks (explore→plan→code→commit), using
- new: 4. **Build against the spec.** Implement following the tasks with the **Ship a feature** loop
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: **Self-check (objective rubric — R7.AC3):** your spec-driven run is sound when **all** hold:
- new: **Self-check (objective rubric):** your spec-driven run is sound when **all** hold:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group E — pitfall + Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: to resent the process. Match the ceremony to the cost-of-wrong; small/obvious → U5's plan mode.
- new: to resent the process. Match the ceremony to the cost-of-wrong; small/obvious → **Ship a feature**'s plan mode.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md
- old: - **Next:** U11 (code & security review) is how a reviewed spec's implementation gets a final
- new: - **Next:** **Code & security review** is how a reviewed spec's implementation gets a final
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/10-spec-driven-dev/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify — only the *teaching* R-IDs should remain (no U#/W# codes, no breadcrumb cites):

## 🤖 Assistant

**→ Bash**

```
f=course/units/10-spec-driven-dev/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UW][0-9]+\b|`CV`|advances|Advances' || echo "NO U#/W#/CV CODES REMAIN"; echo "--- remaining R-IDs (should be teaching only) ---"; awk 'NR>13' "$f" | grep -nE '\bR[0-9]'
```

<details><summary>tool result</summary>

```
NO U#/W#/CV CODES REMAIN
--- remaining R-IDs (should be teaching only) ---
56:requirements describe *observable behavior and constraints*, and they get IDs (`R1`, `R2.AC3`…) so
103:  acceptance criteria with stable IDs (`R1`–`R15`, `R*.AC*`). Notice they describe behavior and
106:  requirement it serves (e.g. *"§3 Workflow methods → `meta/workflows.md` [R3]"*) — that bracketed
139:   ID'd (`R1`, `R2`…), describing behavior not implementation, and resolving the ambiguities above.
```

</details>

## 🤖 Assistant

The remaining R-IDs are exactly the four teaching uses (the `R1`/`R2.AC3` ID examples and the illustrative `[R3]` traceability tag) — all correctly kept. The breadcrumb cites are gone. Now migrate and render:

## 🤖 Assistant

**→ Bash**

```
d=course/units/10-spec-driven-dev
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

All edits rendered clean. U10 done, `make check` green. The teaching R-IDs (`R1`/`R2.AC3`/`R1`–`R15`/`R*.AC*`/`R-whatever`/`[R3]`) are preserved; breadcrumb cites stripped.

## U10 complete — summary

**`10-spec-driven-dev`** — migrated + de-coded, with the special-case handling:
- **Teaching R-IDs KEPT** — `(\`R1\`, \`R2.AC3\`…)`, `(\`R1\`–\`R15\`, \`R*.AC*\`)`, the lab's `(\`R1\`, \`R2\`…)`, `\`R-whatever\``, and the illustrative `[R3]` traceability-tag example all stay (they teach what requirement IDs and traceability look like — this unit's whole subject).
- **Breadcrumb cites STRIPPED** — `(R3.AC2)` ×2 (worked example + Going deeper) and `(R7.AC3)` ×2 (lab callout + self-check heading).
- **CV expanded** in objectives.
- **`**The workflow — W7.**` → `**The workflow.**`**; `W7` in version-currency and lab callout → "spec-driven development".
- **Codes → titles** — U5→**Ship a feature** (×6: TL;DR, Concept open, §4 loop, "when not", pitfall, lab step 4); U11→**Code & security review**; U9–U11 range → "these three"; workflows bullet `generalized W7` + link text `[W1]` → "generalized spec-driven development" + `[Ship a feature]`; Precedent `U2, U4, U8` → **Explore a codebase**, **Memory & context**, **Git & PR**.
- No `{{vd:}}` tokens — no garble risk.

Files changed (uncommitted): `10-spec-driven-dev/unit.src.md` (new), `unit.md` (regenerated).

**Progress: U1–U10 done; U11–U16 remain.** U9 and U10 are now uncommitted on the branch (last commit is the U5–U8 checkpoint at `f18ed18`).

Next is **U11 (Code & security review)** — grid flags an irregular tail ("advances `C12` and consolidates `CV`"), CV ×3, `W6`, prose refs U3/U5/U6/U10/U12/U16, an `R7.AC3` breadcrumb, plus the `{{vd:review-cmds}}` token. Want me to continue to U11?

## 🧑 User

continue to U11

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U11
3	title: "Review a change for correctness and security — and triage the findings"
4	stage: force-multiplier
5	depth_tier: core
6	use_case: "Review a change for correctness and security"
7	can_do: [C12, CV]
8	workflows: [W6]
9	coverage_areas: [16]
10	prerequisites: [U3, U5]
11	reading_time_min: 11
12	lab_time_min: 35
13	---
14	
15	# Review a change for correctness and security — and triage the findings
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Run a structured review over a diff for both correctness *and* security** — using
22	  `/code-review` and `/security-review` as a first pass, not the last word.
23	- **Triage findings instead of trusting them** — confirm a real bug is real (reproduce it), and
24	  dismiss a confident false positive with a reason — advances `C12` and consolidates `CV`.
25	- **Catch the security issues an AI is prone to introduce** — broken object-level authorization
26	  (IDOR), missing ownership checks, injection, leaked secrets — by reviewing against the codebase's
27	  established pattern, not in the abstract.
28	- **Treat "green tests" as necessary, not sufficient** — a passing suite says nothing about the
29	  vulnerability it never tested; verification means the diff, the review, *and* a test you wrote to
30	  pin the finding (`CV` consolidated).
31	
32	## Fast path (TL;DR)
33	
34	> Before a significant or security-sensitive change merges, run a structured review
35	> ([code & security review](../../../meta/workflows.md#w6--code--security-review)) over the diff — correctness **and**
36	> security. Claude gives you two first-pass tools, {{vd:review-cmds}} — but the workflow's own rule
37	> is **the review is a lead, not a verdict**: it both *misses* real issues and *raises* false
38	> positives, so you cross-check every finding against the code. The lab hands you a feature branch
39	> that adds project archiving to `taskflow-api` and has you review it: it contains a real **security
40	> hole** (an archive endpoint that skips the ownership check — any user can archive anyone's
… [+168 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/11-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances|consolidates'
```

<details><summary>tool result</summary>

```
11:  dismiss a confident false positive with a reason — advances `C12` and consolidates `CV`.
17:  pin the finding (`CV` consolidated).
42:You can now build the right thing (U10), ship it (U5), and operate safely (U3). U11 is the gate
45:running under every lab (`CV`) gets named and consolidated. The core idea: **an AI review is a
49:**The workflow — W6.** The generalized pattern lives once in
63:project mutation goes through `get_project`, which 404s on someone else's project (U5's `CLAUDE.md`).
85:lesson of `CV`: a green suite only proves the things you already tested still work. Real verification
104:warns: while authoring U6 the version-reference check **raised a false positive** (a `vd:` token
108:to "satisfy" the check by mangling a real reference. That is the W6 reflex in miniature — an automated
185:- **Next:** the Autonomy & Scale stage (U12 commands/skills onward) automates the workflows you now run by
186:  hand — and a review gate like this one is what you'd wire into the headless CI of U16 (automate & scale).
187:- [`meta/workflows.md`](../../../meta/workflows.md#w6--code--security-review) — the generalized W6 pattern.
```

</details>

## 🤖 Assistant

U11 uses `{{vd:review-cmds}}` three times. Let me check its rendered value for garble risk:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
print(repr(render_vd('{{vd:review-cmds}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
'`claude ultrareview` runs a cloud multi-agent review of the branch/PR; /code-review and /security-review are in-REPL skills.'
```

</details>

## 🤖 Assistant

`review-cmds` is a full sentence (backtick-leading, semicolon, ends with period). Of its three uses, §1 (L67) renders fine in sentence position (keep), but the TL;DR (L36), version-currency (L107), and Going-deeper (L204) placements garble — I'll fix those. This unit also *consolidates* CV (it's even a declared `can_do`), so I'll expand CV once and de-backtick the rest, and drop the irregular "advances `C12` and consolidates `CV`" tail.

Group A — objectives:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: dismiss a confident false positive with a reason — advances `C12` and consolidates `CV`.
- new: dismiss a confident false positive with a reason.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: pin the finding (`CV` consolidated).
- new: pin the finding — cross-cutting verification (CV) consolidated.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group B — Concept open, workflow header, CV de-backtick:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: You can now build the right thing (U10), ship it (U5), and operate safely (U3). U11 is the gate
- new: You can now build the right thing, ship it, and operate safely. This unit is the gate
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: running under every lab (`CV`) gets named and consolidated. The core idea: **an AI review is a
- new: running under every lab (CV) gets named and consolidated. The core idea: **an AI review is a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: **The workflow — W6.** The generalized pattern lives once in
- new: **The workflow.** The generalized pattern lives once in
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: project mutation goes through `get_project`, which 404s on someone else's project (U5's `CLAUDE.md`).
- new: project mutation goes through `get_project`, which 404s on someone else's project (from **Ship a feature**'s `CLAUDE.md`).
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: lesson of `CV`: a green suite only proves the things you already tested still work. Real verification
- new: lesson of CV: a green suite only proves the things you already tested still work. Real verification
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group C — TL;DR + version-currency review-cmds, worked example codes:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: > security. Claude gives you two first-pass tools, {{vd:review-cmds}} — but the workflow's own rule
- new: > security. Claude gives you two first-pass tools — `/code-review` and `/security-review` — but the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`; the review
- new: **Version currency.** This unit was verified against Claude Code `{{vd:_verified_version}}`. The review
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: warns: while authoring U6 the version-reference check **raised a false positive** (a `vd:` token
- new: warns: while authoring the **TDD** unit the version-reference check **raised a false positive** (a `vd:` token
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: to "satisfy" the check by mangling a real reference. That is the W6 reflex in miniature — an automated
- new: to "satisfy" the check by mangling a real reference. That is the review reflex in miniature — an automated
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Group D — Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: - **Next:** the Autonomy & Scale stage (U12 commands/skills onward) automates the workflows you now run by
- new: - **Next:** the Autonomy & Scale stage (starting with **Commands & skills**) automates the workflows you now run by
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md
- old: - The review commands — {{vd:review-cmds}}; version-specifics in
- new: - The review commands: {{vd:review-cmds}} Version-specifics in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/11-code-and-security-review/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify — no U#/W# codes, no backticked `CV`, no `advances`:

## 🤖 Assistant

**→ Bash**

```
f=course/units/11-code-and-security-review/unit.md
echo "--- U#/W#/advances ---"; awk 'NR>13' "$f" | grep -nE '\b[UW][0-9]+\b|advances|Advances|consolidates' || echo "none"
echo "--- backticked CV ---"; awk 'NR>13' "$f" | grep -nE '`CV`' || echo "none"
echo "--- R-IDs ---"; awk 'NR>13' "$f" | grep -nE '\bR[0-9]' || echo "none"
```

<details><summary>tool result</summary>

```
--- U#/W#/advances ---
none
--- backticked CV ---
none
--- R-IDs ---
none
```

</details>

## 🤖 Assistant

All clear (no R7.AC3 was present — already handled in an earlier pass). Now migrate and render:

## 🤖 Assistant

**→ Bash**

```
d=course/units/11-code-and-security-review
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U11 done, `make check` green. All three `review-cmds` placements render cleanly in sentence position; CV is expanded once and de-backticked throughout (it's the unit that consolidates it).

## U11 complete — summary

**`11-code-and-security-review`** — migrated + de-coded:
- **Irregular tail removed** — `— advances \`C12\` and consolidates \`CV\`` dropped from the objective.
- **CV handled** (central to this unit) — expanded once (`— cross-cutting verification (CV) consolidated`), backticked `` `CV` `` instances de-backticked (Concept, §4); the legitimately bare `(CV)` at the §3/lab/verify headings kept.
- **`**The workflow — W6.**` → `**The workflow.**`**; `W6` in worked-example ("the W6 reflex" → "the review reflex") and Going-deeper bullet ("generalized W6 pattern" → "generalized code-and-security-review pattern").
- **Codes → titles** — Concept opener breadcrumbs `(U10)(U5)(U3)` dropped + `U11 is the gate` → "This unit is the gate"; `U5's CLAUDE.md` → **Ship a feature**'s; worked-example "authoring U6" → "authoring the **TDD** unit"; Going-deeper `U12`/`U16` → **Commands & skills**/**Automate & scale**.
- **Garble fixes (3 of 4 `{{vd:review-cmds}}` uses):** the value is a full backtick-leading sentence with a semicolon. Repositioned the TL;DR (became plain `/code-review` + `/security-review`), version-currency, and Going-deeper placements to sentence position; §1's placement already rendered fine and was kept.

Files changed (uncommitted): `11-code-and-security-review/unit.src.md` (new), `unit.md` (regenerated).

**Progress: U1–U11 done; U12–U16 remain.** U9, U10, U11 uncommitted on the branch (checkpoint at `f18ed18`).

Next is **U12 (Commands & skills)** — note it also carries an **L2 reading-time bump (8→10)**, which means editing `reading_time_min` in the source and running **`make render`** (not just `render-units`) so the navigation index regenerates too. Grid also flags multi-line "Advances\n`C13`" tails the auto-pass couldn't remove, R14/R7.AC3 breadcrumbs, and U13 prose. Want me to continue to U12?

## 🧑 User

continue to U12

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U12
3	title: "Package a repeatable routine as a custom command and a skill"
4	stage: autonomy-scale
5	depth_tier: core
6	use_case: "Eliminate repetitive prompting"
7	can_do: [C13]
8	workflows: []
9	coverage_areas: [17, 18]
10	prerequisites: [U4]
11	reading_time_min: 8
12	lab_time_min: 20
13	---
14	
15	# Package a repeatable routine as a custom command and a skill
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Turn a routine you keep hand-typing into a custom slash command** — a saved, argument-taking
22	  prompt you trigger with `/name` — so the routine is one keystroke instead of a paragraph. Advances
23	  `C13`.
24	- **Package a structured, reusable capability as a skill** — a named `SKILL.md` whose *description*
25	  tells Claude when it applies — so the capability is available across tasks, not retyped per session.
26	 
27	- **Choose correctly between the two** — reach for a command when *you* deliberately trigger a prompt,
28	  and a skill when a multi-step capability is worth naming and letting Claude recognize.
29	- **Scope each one deliberately** — project (`.claude/`, committed, shared) vs. personal (`~/.claude/`),
30	  the same source distinction you met for settings in [Memory & context](../04-memory-and-context/unit.md).
31	
32	## Fast path (TL;DR)
33	
34	> Stop re-typing the same prompt. A **custom slash command** is a saved prompt in a markdown file
35	> under `.claude/commands/` — its filename becomes `/name`, and it can take arguments ({{vd:custom-commands}}).
36	> A **skill** is a packaged capability in `.claude/skills/<name>/SKILL.md` with a `name` + a
37	> `description` that lets Claude pull it in when it fits ({{vd:skills}}). Rule of thumb: a prompt *you*
38	> trigger on demand → command; a structured capability worth naming and reusing across tasks → skill.
39	> This repo ships both as worked examples — `/close-unit` (command) and `prime-context` (skill). The lab has
40	> you build one of each against `taskflow-api`; the self-check is a checklist on the two artifacts.
… [+179 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/12-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
9:  prompt you trigger with `/name` — so the routine is one keystroke instead of a paragraph. Advances
10:  `C13`.
106:`/close-unit 13` the moment U13's prose is done — and it expands into that checklist. It's a *prompt you
108:land every unit in this course — authentic dogfooding, R14.)
121:> the artifacts you produce live in your own `.claude/` (R7.AC3/AC7). So the self-check is an objective
154:**Self-check (objective checklist — R7.AC3):** you're done when **all** hold:
195:- **Next:** the rest of the Autonomy stage extends "package the work." U13 (subagents) delegates a
196:  scoped task to a **subagent**; U14 (hooks) automates enforcement with **hooks** — and this repo's own
197:  `make check` suite is U14's worked example; U16 (automate & scale) runs these packaged routines
```

</details>

## 🤖 Assistant

U12 uses `{{vd:custom-commands}}` and `{{vd:skills}}` repeatedly, plus the L2 reading-time bump (8→10). Let me check those two token values for garble risk:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
for k in ['custom-commands','skills']:
    print(k, '::', repr(render_vd('{{vd:'+k+'}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
custom-commands :: 'Custom slash commands are user-defined skills, invoked as /name; `--disable-slash-commands` turns all skills off.'
skills :: 'Skills resolve via /skill-name; reusable packaged capabilities.'
```

</details>

## 🤖 Assistant

Both values are full sentences (semicolon, trailing period). U12 wedges these tokens into parentheticals and mid-sentence in **eight** spots — most will garble. My plan: keep tokens in sentence position at the authoritative spots (Concept §1/§2, version-currency, Going-deeper) and drop the redundant parenthetical pointers (TL;DR, lab step, pitfall — `claude --help` is already named there). Plus the prose codes, R14/R7 breadcrumbs, the multi-line "Advances `C13`" tail, and the L2 reading-time bump.

Batch 1 — reading time, objective tail, TL;DR token drops:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: reading_time_min: 8
- new: reading_time_min: 10
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: prompt you trigger with `/name` — so the routine is one keystroke instead of a paragraph. Advances
- new: prompt you trigger with `/name` — so the routine is one keystroke instead of a paragraph.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: > under `.claude/commands/` — its filename becomes `/name`, and it can take arguments ({{vd:custom-commands}}).
- new: > under `.claude/commands/` — its filename becomes `/name`, and it can take arguments.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: > `description` that lets Claude pull it in when it fits ({{vd:skills}}). Rule of thumb: a prompt *you*
- new: > `description` that lets Claude pull it in when it fits. Rule of thumb: a prompt *you*
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The reading-time bump (8→10) put the navigation index out of sync — expected for the L2 case, and it'll be regenerated by `make render` at the end. To keep the edit-hook quiet while I finish, let me regenerate the index now (U12 isn't migrated yet, so `render-units` leaves it alone; `render-index` just picks up the new reading time):

## 🤖 Assistant

**→ Bash**

```
tools/render-index >/dev/null && make check >/dev/null 2>&1 && echo "GREEN — index back in sync" || echo "still failing"
```

<details><summary>tool result</summary>

```
GREEN — index back in sync
```

</details>

## 🤖 Assistant

Good. Continuing edits. Batch 2 — Concept §1/§2 token repositions:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: syntax, how to disable them) is the version-specific part: {{vd:custom-commands}}.
- new: syntax, how to disable them) is the version-specific part: {{vd:custom-commands}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: want available across many tasks rather than triggered by one keystroke. The resolution surface is
- new: want available across many tasks rather than triggered by one keystroke. The resolution surface: {{vd:skills}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 3 — version-currency rework:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: exact paths and the invocation/argument syntax against `claude --help` and the docs before relying on a
- new: exact paths and the invocation/argument syntax against `claude --help` and the docs before relying on a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 4 — worked example (U13, R14):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: `/close-unit 13` the moment U13's prose is done — and it expands into that checklist.
- new: `/close-unit 13` the moment that unit's prose is done — and it expands into that checklist.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: land every unit in this course — authentic dogfooding, R14.)
- new: land every unit in this course — authentic dogfooding.)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 5 — lab callout, lab step 3 token drop, self-check heading:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: > the artifacts you produce live in your own `.claude/` (R7.AC3/AC7). So the self-check is an objective
- new: > the artifacts you produce live in your own `.claude/`. So the self-check is an objective
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: invocation format from memory — check the current convention ({{vd:custom-commands}}, {{vd:skills}}).
- new: invocation format from memory — check the current convention against `claude --help`.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: **Self-check (objective checklist — R7.AC3):** you're done when **all** hold:
- new: **Self-check (objective checklist):** you're done when **all** hold:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 6 — pitfall token drop + Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: version-specific surface — copy the working repo artifacts and confirm against `claude --help` rather
- new: version-specific surface — copy the working repo artifacts and confirm against `claude --help` rather
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: - **Next:** the rest of the Autonomy stage extends "package the work." U13 (subagents) delegates a
- new: - **Next:** the rest of the Autonomy stage extends "package the work." **Subagents** delegates a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md
- old: - The invocation, argument, and resolution surfaces — {{vd:custom-commands}} and {{vd:skills}};
- new: - The invocation, argument, and resolution surfaces: {{vd:custom-commands}} {{vd:skills}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/12-commands-and-skills/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/12-commands-and-skills/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

No codes remain. Now migrate and run the **full `make render`** (so the index picks up the reading-time change), then check:

## 🤖 Assistant

**→ Bash**

```
d=course/units/12-commands-and-skills
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
make render >/dev/null 2>&1 && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U12 done, `make render` + `make check` green. Token placements read cleanly in sentence position; reading time is now 10 and the navigation index regenerated to match.

## U12 complete — summary

**`12-commands-and-skills`** — migrated + de-coded:
- **L2 reading-time bump** — `reading_time_min: 8 → 10`; ran full `make render` so `course/units/README.md` index reflects it.
- **Multi-line tail removed** — `Advances\n\`C13\`` (which the auto-pass couldn't catch) dropped from objective 1.
- **CV** — none in this unit.
- **Codes → titles** — worked-example "U13's prose" → "that unit's prose"; Going-deeper `U13`/`U14`/`U16` → **Subagents**/**Hooks**/**Automate & scale** (and "U14's worked example" → "that unit's worked example").
- **R# breadcrumbs dropped** — `R14` (worked example), `R7.AC3/AC7` (lab callout), `R7.AC3` (self-check).
- **Garble fixes — all 8 `{{vd:custom-commands}}`/`{{vd:skills}}` uses:** both values are full sentences (semicolon + trailing period). Kept tokens in clean sentence position at the authoritative spots (Concept §1 colon, §2 colon, version-currency as `Commands: … Skills: …`, Going-deeper); dropped the four redundant parenthetical pointers (TL;DR ×2, lab step 3, pitfall) where `claude --help` is already named.

Files changed (uncommitted): `12-commands-and-skills/unit.src.md` (new), `unit.md` (regenerated), `course/units/README.md` (index, reading-time update).

**Progress: U1–U12 done; U13–U16 remain.** U9–U12 uncommitted on the branch (checkpoint at `f18ed18`).

Next is **U13 (Subagents)** — also an L2 bump (**8→12**), plus "the U12 line" and an `R7.AC3` breadcrumb, and the `{{vd:subagents}}` token. Want me to continue to U13?

## 🧑 User

continue to U13

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U13
3	title: "Delegate a scoped task to a subagent"
4	stage: autonomy-scale
5	depth_tier: core
6	use_case: "Delegate focused / parallel sub-tasks"
7	can_do: [C14]
8	workflows: []
9	coverage_areas: [19]
10	prerequisites: [U12]
11	reading_time_min: 8
12	lab_time_min: 20
13	---
14	
15	# Delegate a scoped task to a subagent
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Hand a self-contained task to a subagent and use the result it returns** — a separate Claude
22	  instance, with its own context window, that does the work and reports back a conclusion rather than
23	  its whole transcript.
24	- **Recognize when delegation pays off** — a context-heavy exploration you don't want polluting your
25	  main thread, two independent tasks worth running in parallel, or work worth fencing to a restricted
26	  toolset.
27	- **Scope a task so a subagent can finish it without you** — a crisp, self-contained brief with a
28	  defined deliverable, distinct from a routine you reuse in your own context (a skill, [Commands & skills](../12-commands-and-skills/unit.md)).
29	- **Verify what comes back** — a subagent returns a conclusion you didn't watch it derive, so you
30	  check the result against the code instead of trusting that an agent ran.
31	
32	## Fast path (TL;DR)
33	
34	> A **subagent** is a second Claude the main session spins up to handle one scoped task. It has its
35	> **own context window** and can be given its **own restricted tools** — it does the work and returns a
36	> *result* (a summary, an answer, a diff), not its entire transcript. You delegate for three reasons:
37	> **context isolation** (its 30-file search stays in *its* context, only the conclusion lands in
38	> yours), **parallelism** (independent tasks run at once), and **fencing** (a read-only explorer can't
39	> write). Define a custom agent inline with `--agents <json>` or as a file under `.claude/agents/`,
40	> each with a `description` that tells the main agent when to reach for it ({{vd:subagents}}). The
… [+214 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/13-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
78:**4 — Subagent vs. skill (the U12 line).** Both package work; they differ in *where the work runs*:
151:> (R7.AC3/AC7). So the self-check is an objective checklist you apply to what you built and to the
183:**Self-check (objective checklist — R7.AC3):** you're done when **all** hold:
228:- **Next in the Autonomy stage:** U14 (hooks) automates *enforcement* — and this repo's own `make check`
229:  suite is its worked example; U15 (MCP & vetting) extends today's trust-delegation lesson to
230:  *third-party* tools you connect and must vet before relying on; U16 (automate & scale) runs delegated
```

</details>

## 🤖 Assistant

U13 is largely de-coded already (links converted). Remaining: "the U12 line", two R7.AC3 breadcrumbs, the Going-deeper Next titles, the L2 bump (8→12), and the `{{vd:subagents}}` token (used in many parenthetical spots). Let me check that token's value:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
print(repr(render_vd('{{vd:subagents}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
'`--agent <agent>` / `--agents <json>` set session agents; the `agents` subcommand manages background agents.'
```

</details>

## 🤖 Assistant

`subagents` is a backtick-leading full sentence with a semicolon and trailing period — the same garble profile. It's used in ~8 mostly-parenthetical spots. I'll keep it in sentence position at the three authoritative spots (Concept §3, version-currency, Going-deeper) and drop the redundant parenthetical pointers. Plus "the U12 line", the R7 breadcrumbs, Going-deeper titles, and the L2 bump (8→12). I'll do body edits first, then the reading-time change.

Batch A — "U12 line", TL;DR + Concept §3 + version-currency tokens:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: **4 — Subagent vs. skill (the U12 line).** Both package work; they differ in *where the work runs*:
- new: **4 — Subagent vs. skill.** Both package work; they differ in *where the work runs*:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: > each with a `description` that tells the main agent when to reach for it ({{vd:subagents}}). The
- new: > each with a `description` that tells the main agent when to reach for it. The
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: with the `agents` subcommand. The version-specific surface — the flags, the subcommand, the on-disk
- new: with the `agents` subcommand. The version-specific surface is the flags, the subcommand, and the on-disk
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: **convention** — confirm the exact path and format against `claude --help` and the docs before relying
- new: **convention** — confirm the exact path and format against `claude --help` and the docs before relying
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch B — worked-example + lab token drops, R7 breadcrumbs:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: **convention** — confirm the path/front-matter against the docs, {{vd:subagents}}), with that
- new: **convention** — confirm the path/front-matter against the docs), with that
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: project. Confirm the path and front-matter format against `claude --help`/the docs rather than
- new: project. Confirm the path and front-matter format against `claude --help`/the docs rather than
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: > result you got back, with the worked example's `explorer` as the reference pattern.
- new: > result you got back, with the worked example's `explorer` as the reference pattern.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

That third edit was a slip — I appended a stray newline instead of doing the breadcrumb edit. Let me re-read the affected regions to get exact current strings and fix it:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
```

<details><summary>tool result</summary>

```
160	## Lab
161	
162	> **This lab has no automated verifier.** The artifact you produce — a subagent definition — lives in
163	> your own `.claude/`, and whether a delegation is *well-scoped* is a judgment call, not a diff
164	> (R7.AC3/AC7). So the self-check is an objective checklist you apply to what you built and to the
165	> result you got back, with the worked example's `explorer` as the reference pattern.
166	
167	
168	**Goal:** define a **scoped, read-only subagent**, delegate a real context-heavy task to it against
169	`taskflow-api`, use the result it returns, and **verify that result** against the code — so you can say
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: > your own `.claude/`, and whether a delegation is *well-scoped* is a judgment call, not a diff
- new: > your own `.claude/`, and whether a delegation is *well-scoped* is a judgment call, not a diff.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the self-check heading + bullet, pitfall, and Going-deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: **Self-check (objective checklist — R7.AC3):** you're done when **all** hold:
- new: **Self-check (objective checklist):** you're done when **all** hold:
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: - [ ] Nothing in the definition **hardcodes a version-specific format from memory** — the path and
- new: - [ ] Nothing in the definition **hardcodes a version-specific format from memory** — the path and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: matter are the version-specific surface — confirm against `claude --help` and the docs rather than
- new: matter are the version-specific surface — confirm against `claude --help` and the docs rather than
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: - **Next in the Autonomy stage:** U14 (hooks) automates *enforcement* — and this repo's own `make check`
- new: - **Next in the Autonomy stage:** **Hooks** automates *enforcement* — and this repo's own `make check`
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: - The flags, `agents` subcommand, and on-disk format — {{vd:subagents}}; version-specifics in
- new: - The flags, `agents` subcommand, and on-disk format: {{vd:subagents}} Version-specifics in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the reading-time bump, verify codes, then migrate + full render:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/13-subagents/unit.md
- old: reading_time_min: 8
- new: reading_time_min: 12
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/13-subagents/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Expected — the reading-time change put the index out of sync. Let me verify codes are clear, then migrate and run full `make render`:

## 🤖 Assistant

**→ Bash**

```
f=course/units/13-subagents/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/13-subagents
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
make render >/dev/null 2>&1 && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U13 done, `make render` + `make check` green. Token placements read cleanly; reading time is 12 and the index regenerated.

## U13 complete — summary

**`13-subagents`** — migrated + de-coded:
- **L2 reading-time bump** — `reading_time_min: 8 → 12`; full `make render` updated the index.
- **"the U12 line" removed** — `**4 — Subagent vs. skill (the U12 line).**` → `**4 — Subagent vs. skill.**`.
- **Codes → titles** — Going-deeper Next `U14`/`U15`/`U16` → **Hooks**/**MCP & vetting**/**Automate & scale**. (Most other cross-refs were already de-coded links.)
- **R# breadcrumbs dropped** — `(R7.AC3/AC7)` (lab callout) and `(R7.AC3)` (self-check); also tidied a double blank line that resulted.
- **Garble fixes — all `{{vd:subagents}}` uses** (backtick-leading full sentence, semicolon + period): kept in sentence position at Concept §3 (colon), version-currency (own sentence), and Going-deeper; dropped the five redundant parenthetical pointers (TL;DR, worked example, lab starting-state, self-check bullet, pitfall) where `claude --help`/docs is already cited.

Files changed (uncommitted): `13-subagents/unit.src.md` (new), `unit.md` (regenerated), `course/units/README.md` (index).

**Progress: U1–U13 done; U14–U16 remain.** U9–U13 uncommitted on the branch (checkpoint at `f18ed18`).

Next is **U14 (Hooks)** — the last L2 bump (**8→11**), plus "the C15 move", R14/R13 breadcrumbs, U15 prose, and the `{{vd:hooks}}` token. Want me to continue to U14?

## 🧑 User

continue to U14

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U14
3	title: "Enforce a standard automatically with a hook"
4	stage: autonomy-scale
5	depth_tier: core
6	use_case: "Enforce my standards automatically"
7	can_do: [C15]
8	workflows: []
9	coverage_areas: [20]
10	prerequisites: [U12]
11	reading_time_min: 8
12	lab_time_min: 22
13	---
14	
15	# Enforce a standard automatically with a hook
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Wire a hook that runs automatically on a lifecycle event** — a command the *harness* fires before
22	  or after a tool call (not something you or Claude choose to invoke), configured in `settings.json`.
23	 
24	- **Use the two moves a hook makes** — **block** an action that violates a standard (a `PreToolUse`
25	  hook that denies it) and **react** to one that already happened (a `PostToolUse` hook that formats,
26	  tests, or checks, and feeds failures back).
27	- **Choose a hook over a command/skill/subagent** — reach for a hook when something **must always** or
28	  **must never** happen, because only a hook is enforced deterministically rather than left to anyone's
29	  judgment.
30	- **Verify a hook actually fires** — drive it with a synthetic event payload and confirm it blocks or
31	  reacts as intended, instead of trusting that a config entry works.
32	
33	## Fast path (TL;DR)
34	
35	> A **hook** is a command Claude Code runs **for you, automatically, on a lifecycle event** —
36	> configured in `settings.json` as `hooks.<Event>: [{ "matcher": "...", "hooks": [{ "type":
37	> "command", "command": "..." }] }]`. The two you'll use most: **`PreToolUse`** (runs before a tool —
38	> can **block** the action) and **`PostToolUse`** (runs after — format, test, or check, and feed
39	> failures back). The hook reads the event as JSON on stdin (`tool_input.file_path`, …) and steers via
40	> its output ({{vd:hooks}}). The thing that makes a hook different from a command/skill/subagent: **the
… [+201 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/14-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
105:**This course enforces its own standards with the very mechanism this unit teaches (R14).** Open this
116:   machinery, R13);
123:  re-implement any rule. The standard lives in one place (R13); the hook is just a new *trigger* for it.
130:That is the C15 move in one artifact: a standard (the checks) that *used to* depend on someone
216:- **Next:** U15 (MCP & vetting) connects external tools and asks how far to trust them; U16 (automate &
```

</details>

## 🤖 Assistant

U14 codes are mostly R13/R14 breadcrumbs, "the C15 move", the Going-deeper titles, the L2 bump (8→11), and the `{{vd:hooks}}` token (used in many parenthetical spots). Let me check the token value:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
print(repr(render_vd('{{vd:hooks}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
'Hooks run a command on a lifecycle event, configured in settings.json as `hooks.<Event>: [{matcher, hooks:[{type:"command", command}]}]`. Common events: PreToolUse (can block), PostToolUse, Stop, SessionStart, PreCompact. `--include-hook-events` streams them; `--bare` skips hooks.'
```

</details>

## 🤖 Assistant

`hooks` is a **long, three-sentence** value (backticks, periods, semicolons) — it garbles badly in every parenthetical. Given its length, I'll keep it in just two authoritative spots in clean sentence position (version-currency and Going-deeper) and drop the seven inline/parenthetical pointers, rewording Concept §1 to plain prose. Plus the R13/R14 breadcrumbs, "the C15 move", Going-deeper titles, and the L2 bump (8→11). Body edits first.

Batch 1 — TL;DR/Concept token drops + R14:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: > its output ({{vd:hooks}}). The thing that makes a hook different from a command/skill/subagent: **the
- new: > its output. The thing that makes a hook different from a command/skill/subagent: **the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: event names and the exact shape are the version-specific surface — {{vd:hooks}}.
- new: event names and the exact shape are the version-specific surface — confirm them against the docs rather than authoring from memory.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: into the conversation so Claude addresses it. (Exact field names and options: {{vd:hooks}}.) A hook
- new: into the conversation so Claude addresses it. A hook
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: **This course enforces its own standards with the very mechanism this unit teaches (R14).** Open this
- new: **This course enforces its own standards with the very mechanism this unit teaches.** Open this
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 2 — R13 breadcrumbs + "C15 move":

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: machinery, R13);
- new: machinery);
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: re-implement any rule. The standard lives in one place (R13); the hook is just a new *trigger* for it.
- new: re-implement any rule. The standard lives in one place; the hook is just a new *trigger* for it.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: That is the C15 move in one artifact: a standard (the checks) that *used to* depend on someone
- new: That is this unit's move in one artifact: a standard (the checks) that *used to* depend on someone
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 3 — version-currency rework:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: **Version currency.** Verified against Claude Code {{vd:_verified_version}}. The hook **event-name
- new: **Version currency.** Verified against Claude Code {{vd:_verified_version}}. The hook **event-name
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 4 — lab / self-check / pitfall token drops:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: event name and structure against the docs / the settings schema rather than memory ({{vd:hooks}}).
- new: event name and structure against the docs / the settings schema rather than memory.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: react). Confirm the event name + the `{matcher, hooks:[{type,command}]}` shape against the docs
- new: react). Confirm the event name + the `{matcher, hooks:[{type,command}]}` shape against the docs
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: - [ ] Nothing about the **event name or schema was authored from memory** — it was confirmed against
- new: - [ ] Nothing about the **event name or schema was authored from memory** — it was confirmed against
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: just never fires. Confirm against the settings schema / docs ({{vd:hooks}}).
- new: just never fires. Confirm against the settings schema / docs.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 5 — Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: - **Next:** U15 (MCP & vetting) connects external tools and asks how far to trust them; U16 (automate &
- new: - **Next:** **MCP & vetting** connects external tools and asks how far to trust them; **Automate &
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: - The event enum, matcher syntax, and output fields — {{vd:hooks}}; version-specifics in
- new: - The event enum, matcher syntax, and output fields: {{vd:hooks}} Version-specifics in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the reading-time bump, verify codes, regen index, then migrate + full render:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/14-hooks/unit.md
- old: reading_time_min: 8
- new: reading_time_min: 11
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/14-hooks/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Expected — reading-time change vs. index. Let me verify codes are clear, then migrate and run full `make render`:

## 🤖 Assistant

**→ Bash**

```
f=course/units/14-hooks/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/14-hooks
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
make render >/dev/null 2>&1 && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U14 done, `make render` + `make check` green. The long `hooks` value now renders as its own clean sentences in the version-currency note; reading time is 11 and the index regenerated.

## U14 complete — summary

**`14-hooks`** — migrated + de-coded:
- **L2 reading-time bump** — `reading_time_min: 8 → 11`; full `make render` updated the index. (This was the last of the three L2 bumps — U12/U13/U14 all done.)
- **"the C15 move" reworded** — → "this unit's move".
- **Codes → titles** — Going-deeper Next `U15`/`U16` → **MCP & vetting**/**Automate & scale**.
- **R# breadcrumbs dropped** — `(R14)` (worked-example lead), `R13` ×2 (worked-example bullets).
- **Garble fixes — all `{{vd:hooks}}` uses:** this value is a *three-sentence* block (backticks, periods, semicolons). Given its length I kept it in only two authoritative sentence-position spots (version-currency, Going-deeper) and dropped the seven inline/parenthetical pointers (TL;DR, Concept §1 → reworded to prose, Concept §3, lab starting-state, lab step 1, self-check bullet, pitfall), each of which already cites the docs/settings schema.

Files changed (uncommitted): `14-hooks/unit.src.md` (new), `unit.md` (regenerated), `course/units/README.md` (index).

**Progress: U1–U14 done; U15–U16 remain.** Six units (U9–U14) are now uncommitted on the branch — the last checkpoint is the U5–U8 commit (`f18ed18`). That's a sizable chunk; a checkpoint commit here would be sensible.

Want me to **commit U9–U14** then continue to **U15 (MCP & vetting)** — or push straight on to U15 first?

## 🧑 User

commit U9–U14 then continue to U15

## 🤖 Assistant

Committing U9–U14 first. Let me stage and confirm green:

## 🤖 Assistant

**→ Bash**

```
git add course/units/09-onboard-refactor-legacy course/units/10-spec-driven-dev course/units/11-code-and-security-review course/units/12-commands-and-skills course/units/13-subagents course/units/14-hooks course/units/README.md
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
M  course/units/09-onboard-refactor-legacy/unit.md
A  course/units/09-onboard-refactor-legacy/unit.src.md
M  course/units/10-spec-driven-dev/unit.md
A  course/units/10-spec-driven-dev/unit.src.md
M  course/units/11-code-and-security-review/unit.md
A  course/units/11-code-and-security-review/unit.src.md
M  course/units/12-commands-and-skills/unit.md
A  course/units/12-commands-and-skills/unit.src.md
M  course/units/13-subagents/unit.md
A  course/units/13-subagents/unit.src.md
M  course/units/14-hooks/unit.md
A  course/units/14-hooks/unit.src.md
M  course/units/README.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
git commit -q -F - <<'MSG'
P7: roll learner-prose remediation through U9–U14 (migrate + de-code)

Continue the Stage-C editorial rollout (tasks/P7-quality-pass.md §7.6). U9–U14
migrated to the committed-rendered pattern and fully de-coded, matching the
U1–U8 precedent:

- Cross-ref codes → titles; "The workflow — W#." headers → "The workflow.";
  CV expanded once per unit (and de-backticked where U11 consolidates it); R#
  breadcrumbs dropped. U10 keeps its *teaching* R-IDs (R1/R2.AC3/R1–R15/[R3])
  and drops only the breadcrumb cites (R3.AC2/R7.AC3).
- L2 reading-time bumps: U12 8→10, U13 8→12, U14 8→11 (index regenerated).
- Render-and-eyeball fixed sentence-valued/backtick-leading version-token
  garbles in U11 (review-cmds), U12 (custom-commands/skills), U13 (subagents),
  U14 (hooks — a 3-sentence value): kept tokens in sentence position at the
  authoritative spots, dropped redundant parenthetical pointers.

make check green. Branch local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (43.5KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bndgtjgn1.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
ed66fe8 P7: roll learner-prose remediation through U9–U14 (migrate + de-code)
---
```

</details>

## 🤖 Assistant

Committed (`ed66fe8`), tree clean. Now **U15 (MCP & vetting)**:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U15
3	title: "Connect an MCP server and vet it before trusting it"
4	stage: autonomy-scale
5	depth_tier: core
6	use_case: "Give Claude access to my tools & data — safely"
7	can_do: [C16]
8	workflows: []
9	coverage_areas: [21, 22]
10	prerequisites: [U3, U13]
11	reading_time_min: 9
12	lab_time_min: 22
13	---
14	
15	# Connect an MCP server and vet it before trusting it
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Connect an MCP server to Claude Code** — a local stdio server (a subprocess) or a remote HTTP one —
22	  so Claude can call tools and read data beyond its built-ins.
23	- **Treat connecting as a trust-delegation decision** — recognize that an MCP server, plugin, or
24	  marketplace item runs code or sees data on your behalf, so installing one grants it trust (the
25	  [Subagents](../13-subagents/unit.md) lesson, now applied to *third-party* code).
26	- **Vet a third-party extension before installing it** — evaluate source, scope/permissions, transport,
27	  and secrets against a checklist, and reach an explicit connect / don't-connect decision (R10.AC5).
28	- **Use the approval gate, and verify the results** — leave a `.mcp.json` server *pending* until you've
29	  vetted it, and check what a connected server returns rather than trusting it because it connected.
30	
31	## Fast path (TL;DR)
32	
33	> **MCP** (Model Context Protocol) lets Claude Code connect to external **servers** that expose tools
34	> and data. Add a local one (runs as a subprocess) with `claude mcp add <name> -- <command>`, or a
35	> remote one with `claude mcp add --transport http <name> <url>`; `claude mcp get`/`list` health-check
36	> them, and a project `.mcp.json` server stays **`⏸ Pending approval`** until you approve it ({{vd:mcp}}).
37	> The catch: connecting a server — or installing a plugin/marketplace item — is a **trust-delegation
38	> decision** (R10.AC5). It runs code or sees data for you, so **vet it first**: source, scope, transport,
39	> secrets ({{vd:plugins}}). This repo ships a real, offline stdio server you connect in the lab
40	> (`codebases/fixtures/taskflow_mcp.py`, verified `✓ Connected`); the other half is vetting a
… [+191 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/15-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
14:  and secrets against a checklist, and reach an explicit connect / don't-connect decision (R10.AC5).
25:> decision** (R10.AC5). It runs code or sees data for you, so **vet it first**: source, scope, transport,
61:**3 — Connecting is a trust-delegation decision.** This is the unit's thesis (R10.AC5). An MCP server,
156:**Part B — vet (the judgment, R10.AC5):** consider a third-party MCP server you're tempted to install —
205:- **Next:** U16 (automate & scale) runs Claude **headlessly** and in parallel — where a connected MCP
```

</details>

## 🤖 Assistant

U15 has no L2 bump. Codes are four `R10.AC5` breadcrumbs, the Going-deeper title, and the `{{vd:mcp}}`/`{{vd:plugins}}` tokens (many spots). Let me check those token values and whether any bare `CV` is present:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
for k in ['mcp','plugins']:
    print(k, '::', repr(render_vd('{{vd:'+k+'}}', vd)[0]))
"
echo "--- bare CV in U15? ---"
grep -nE '\bCV\b' course/units/15-mcp-and-vetting/unit.md || echo "no CV"
```

<details><summary>tool result</summary>

```
mcp :: '`claude mcp add <name> -- <cmd>` adds a local stdio server (subprocess); `--transport http <url>` adds a remote one. `claude mcp get`/`list` health-check connections; a project `.mcp.json` server shows as `⏸ Pending approval` until approved. `--mcp-config <files>` loads per-session; `--strict-mcp-config` ignores others.'
plugins :: '`claude plugin|plugins` manages plugins; `--plugin-dir <path>` / `--plugin-url <url>` load a plugin for one session.'
--- bare CV in U15? ---
no CV
```

</details>

## 🤖 Assistant

`mcp` is a very long four-sentence value and `plugins` a backtick-leading sentence — both garble in parentheticals. No CV and no L2 bump here. I'll keep `mcp` at Concept §2 (its natural teaching spot) + Going-deeper, `plugins` at Concept §4 + version-currency + Going-deeper, and drop the redundant parenthetical pointers (which all cite `claude mcp --help` anyway). Plus the four `R10.AC5` breadcrumbs and the Going-deeper title.

Batch 1 — R10.AC5 breadcrumbs:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: and secrets against a checklist, and reach an explicit connect / don't-connect decision (R10.AC5).
- new: and secrets against a checklist, and reach an explicit connect / don't-connect decision.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: > decision** (R10.AC5). It runs code or sees data for you, so **vet it first**: source, scope, transport,
- new: > decision**. It runs code or sees data for you, so **vet it first**: source, scope, transport,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: **3 — Connecting is a trust-delegation decision.** This is the unit's thesis (R10.AC5). An MCP server,
- new: **3 — Connecting is a trust-delegation decision.** This is the unit's thesis. An MCP server,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: **Part B — vet (the judgment, R10.AC5):** consider a third-party MCP server you're tempted to install —
- new: **Part B — vet (the judgment):** consider a third-party MCP server you're tempted to install —
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 2 — TL;DR token drops + Concept §2/§4 colons:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: > them, and a project `.mcp.json` server stays **`⏸ Pending approval`** until you approve it ({{vd:mcp}}).
- new: > them, and a project `.mcp.json` server stays **`⏸ Pending approval`** until you approve it.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: > secrets ({{vd:plugins}}). This repo ships a real, offline stdio server you connect in the lab
- new: > secrets. This repo ships a real, offline stdio server you connect in the lab
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: **`⏸ Pending approval`** until you approve it. The exact commands and config shape are the
- new: **`⏸ Pending approval`** until you approve it. The exact commands and config shape are the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: not "looks fine." The version-specific surface for plugins/marketplace vetting is {{vd:plugins}}.
- new: not "looks fine." The version-specific surface for plugins/marketplace vetting: {{vd:plugins}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 3 — version-currency:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: Connected`); confirm them against `claude mcp --help` before relying on a detail, and treat the
- new: Connected`); confirm them against `claude mcp --help` before relying on a detail. The
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 4 — lab, self-check, pitfalls:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: Confirm every command against {{vd:mcp}} rather than typing it from memory.
- new: Confirm every command against `claude mcp --help` rather than typing it from memory.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: `⏸ Pending approval` gate ({{vd:mcp}}) lets you hold the decision until you've vetted.
- new: `⏸ Pending approval` gate lets you hold the decision until you've vetted.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: - [ ] No `claude mcp` command or config shape was **authored from memory** — each was confirmed against
- new: - [ ] No `claude mcp` command or config shape was **authored from memory** — each was confirmed against
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: supply-chain attacks land. Confirm the publisher and that it's the genuine package ({{vd:plugins}}).
- new: supply-chain attacks land. Confirm the publisher and that it's the genuine package.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: shape are version-specific — confirm against `claude mcp --help` ({{vd:mcp}}) rather than recall.
- new: shape are version-specific — confirm against `claude mcp --help` rather than recall.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 5 — Going deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: - **Next:** U16 (automate & scale) runs Claude **headlessly** and in parallel — where a connected MCP
- new: - **Next:** **Automate & scale** runs Claude **headlessly** and in parallel — where a connected MCP
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md
- old: - The `mcp` subcommands and extension-vetting surface — {{vd:mcp}} and {{vd:plugins}};
- new: - The `mcp` subcommands and extension-vetting surface: {{vd:mcp}} {{vd:plugins}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/15-mcp-and-vetting/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/15-mcp-and-vetting/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

**→ Bash**

```
d=course/units/15-mcp-and-vetting
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

U15 done, `make check` green. Both long token values render cleanly in sentence position; redundant parenthetical pointers dropped.

## U15 complete — summary

**`15-mcp-and-vetting`** — migrated + de-coded:
- **R# breadcrumbs dropped** — `(R10.AC5)` ×4 (objective, TL;DR, Concept §3 thesis, lab Part B heading).
- **Codes → titles** — Going-deeper Next `U16` → **Automate & scale**. (Other cross-refs were already de-coded links; no CV, no L2 bump.)
- **Garble fixes — all `{{vd:mcp}}`/`{{vd:plugins}}` uses:** `mcp` is a four-sentence value, `plugins` a backtick-leading sentence. Kept `mcp` at Concept §2 (colon, its teaching spot) + Going-deeper; `plugins` at Concept §4 + version-currency + Going-deeper — all in clean sentence position. Dropped the six redundant parenthetical pointers (TL;DR ×2, lab starting-state, lab Part B, self-check, two pitfalls), each of which already cites `claude mcp --help`.

Files changed (uncommitted): `15-mcp-and-vetting/unit.src.md` (new), `unit.md` (regenerated).

**Progress: U1–U15 done; only U16 remains.** U15 uncommitted on the branch (checkpoint at `ed66fe8`).

Next is the **last unit — U16 (Automate & scale)** — grid flags many `(W9)` in prose, R14/R12.AC7/R15 breadcrumbs, U14 prose, and CV. After it, task 7.6 (the U5–U16 rollout) is fully done, and what remains is 7.7 (capstone/stuck sweep), 7.8 (convention docs), and 7.9 (close-out). Want me to continue to U16?

## 🧑 User

continue to U16

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
```

<details><summary>tool result</summary>

```
1	---
2	id: U16
3	title: "Run Claude unattended — headless, in CI, and in parallel"
4	stage: autonomy-scale
5	depth_tier: core
6	use_case: "Run Claude unattended and in parallel"
7	can_do: [C17]
8	workflows: [W9]
9	coverage_areas: [6, 23, 24, 25]
10	prerequisites: [U8, U14]
11	reading_time_min: 9
12	lab_time_min: 25
13	---
14	
15	# Run Claude unattended — headless, in CI, and in parallel
16	
17	## Learning objectives
18	
19	By the end of this unit you can:
20	
21	- **Run Claude headlessly** with `-p`/`--print` and a structured `--output-format`, so it executes a
22	  task non-interactively — scriptable, pipeable, and runnable in automation.
23	- **Run Claude in CI** — wire a headless invocation (or your enforcement suite) into a pipeline that
24	  runs on every push, the way this repo's own checks do.
25	- **Coordinate parallel agents with git worktrees (W9)** — give each independent task its own worktree
26	  so agents don't collide, run them concurrently, and review each diff separately before integrating.
27	 
28	- **Keep unattended runs safe** — apply the guardrails that matter when *no one is at the keyboard to
29	  approve*: deterministic hooks ([Hooks](../14-hooks/unit.md)), bounded blast radius and checkpoints
30	  ([Operate safely](../03-operate-safely/unit.md)), and per-diff review.
31	
32	## Fast path (TL;DR)
33	
34	> Three moves to run Claude without babysitting it. **Headless:** `claude -p "<task>"
35	> --output-format json` runs non-interactively and prints structured output you can pipe or parse
36	> ({{vd:headless}}); cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
37	> every push; this repo's [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) is
38	> the worked example ({{vd:ci}}). **Parallel (W9):** give each independent task its own **git
39	> worktree** (`claude --worktree`, or `git worktree add`), run agents concurrently, and **review each
40	> diff separately** before merging ({{vd:worktrees}}). The catch: unattended means **no interactive
… [+188 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=$(ls course/units/16-*/unit.md); awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances'
```

<details><summary>tool result</summary>

```
12:- **Coordinate parallel agents with git worktrees (W9)** — give each independent task its own worktree
25:> the worked example ({{vd:ci}}). **Parallel (W9):** give each independent task its own **git
60:**3 — Parallel agents via worktrees (W9).** When several **independent** tasks can proceed at once,
64:[W9 pattern](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is: isolate each task
97:**This repo runs its own standards in CI — that workflow is the example (R14).** Open
101:That's the **third and outermost layer** of the defense-in-depth from U14: the hook gives in-session
111:  against the CLI (R12.AC7). Automation isn't only for tests; here it's wired to prompt the very
120:# Parallel via worktrees (W9): two independent tasks, isolated trees, reviewed separately.
132:> path needs no extra service; R15.)
144:2. **Parallel via worktrees (W9).** Pick **two genuinely independent** changes (e.g. add a `GET
153:   trigger, what runs unattended, and how it relates to the U14 hook + pre-commit gate (defense in
168:      W9 verification step.
170:      U14 hook + pre-commit gate.
178:[W9 method](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is the reference for
208:- **W9** parallel-agents pattern: [`meta/workflows.md`](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees).
```

</details>

## 🤖 Assistant

U16 — the final unit. Lots of `(W9)`, U14 refs, R14/R12.AC7/R15 breadcrumbs, and four vd tokens (`headless`, `ci`, `worktrees`, `checkpoint-rewind`). No CV, no L2 bump. Let me check the token values for garble:

## 🤖 Assistant

**→ Bash**

```
python3 -c "
import sys; sys.path.insert(0,'tools')
from _common import load_version_data, render_vd
vd=load_version_data()
for k in ['headless','ci','worktrees','checkpoint-rewind']:
    print(k, '::', repr(render_vd('{{vd:'+k+'}}', vd)[0]))
"
```

<details><summary>tool result</summary>

```
headless :: '`-p`/`--print` runs headlessly; `--output-format text|json|stream-json` shapes the output.'
ci :: 'CI runs use headless `-p` with `--output-format json` (and optionally `--max-budget-usd`); a GitHub Action wraps this. (unverified — see meta/version-record.md)'
worktrees :: '`-w`/`--worktree [name]` creates a git worktree for the session; `--tmux` opens it in a tmux session.'
checkpoint-rewind :: 'In-REPL `/rewind` checkpoints/restores recent changes to undo them; `--no-session-persistence` disables saving sessions.'
```

</details>

## 🤖 Assistant

All four are full sentences (backtick-leading, semicolons, periods) — same garble profile. I'll keep each in sentence position at its Concept teaching spot (and version-currency for the unverified `ci`/`checkpoint-rewind`), keep the Going-deeper pointer, and drop the many parenthetical pointers. Plus the `(W9)` strip throughout, U14→**Hooks**, and the R14/R12.AC7/R15 breadcrumbs. This is the biggest unit — I'll go in careful batches.

Batch 1 — TL;DR (headless, ci + Parallel, worktrees):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: > --output-format json` runs non-interactively and prints structured output you can pipe or parse
- new: > --output-format json` runs non-interactively and prints structured output you can pipe or parse;
```

<details><summary>tool result</summary>

```
<tool_use_error>String to replace not found in file.
String: > --output-format json` runs non-interactively and prints structured output you can pipe or parse
> ({{vd:headless}}); cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
> every push; this repo's [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) is
> the worked example ({{vd:ci}}). **Parallel (W9):** give each independent task its own **git
> worktree** (`claude --worktree`, or `git worktree add`), run agents concurrently, and **review each
> diff separately** before merging ({{vd:worktrees}}). The catch: unattended means **no interactive**
(note: Edit also tried swapping \uXXXX escapes and their characters; neither form matched, so the mismatch is likely elsewhere in old_string. Re-read the file and copy the exact surrounding text.)</tool_use_error>
```

</details>

## 🤖 Assistant

The bold spans a line break at the end. Let me do three smaller, exact edits instead:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: > ({{vd:headless}}); cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
- new: > cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: > the worked example ({{vd:ci}}). **Parallel (W9):** give each independent task its own **git
- new: > the worked example. **Parallel:** give each independent task its own **git
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: > diff separately** before merging ({{vd:worktrees}}). The catch: unattended means **no interactive
- new: > diff separately** before merging. The catch: unattended means **no interactive
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 2 — objective W9, Concept §1 headless, Concept §2 ci:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - **Coordinate parallel agents with git worktrees (W9)** — give each independent task its own worktree
- new: - **Coordinate parallel agents with git worktrees** — give each independent task its own worktree
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: an unattended run. This is the primitive everything else here is built from — Claude as a *command*,
- new: an unattended run. This is the primitive everything else here is built from — Claude as a *command*,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: review a diff — or, as in *this* repo, runs the enforcement suite as a backstop. The official GitHub
- new: review a diff — or, as in *this* repo, runs the enforcement suite as a backstop. The official GitHub
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 3 — Concept §3 (W9 header, worktrees token, W9 link) + §5 checkpoint-rewind:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: **3 — Parallel agents via worktrees (W9).** When several **independent** tasks can proceed at once,
- new: **3 — Parallel agents via worktrees.** When several **independent** tasks can proceed at once,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: one with `--worktree` ({{vd:worktrees}}); or use plain `git worktree add`. The
- new: one with `--worktree`, or use plain `git worktree add`. {{vd:worktrees}} The
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: approval and no one to notice a runaway. ({{vd:checkpoint-rewind}}.)
- new: approval and no one to notice a runaway. {{vd:checkpoint-rewind}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 4 — version-currency rework:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: `--output-format`, `--max-budget-usd`, and `--worktree` are `--help`-verified; the GitHub Action
- new: `--output-format`, `--max-budget-usd`, and `--worktree` are `--help`-verified; the GitHub Action
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 5 — worked example breadcrumbs (R14, U14→Hooks, R12.AC7) + code comment W9:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: **This repo runs its own standards in CI — that workflow is the example (R14).** Open
- new: **This repo runs its own standards in CI — that workflow is the example.** Open
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: That's the **third and outermost layer** of the defense-in-depth from U14: the hook gives in-session
- new: That's the **third and outermost layer** of the defense-in-depth from **Hooks**: the hook gives in-session
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: against the CLI (R12.AC7). Automation isn't only for tests; here it's wired to prompt the very
- new: against the CLI. Automation isn't only for tests; here it's wired to prompt the very
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: # Parallel via worktrees (W9): two independent tasks, isolated trees, reviewed separately.
- new: # Parallel via worktrees: two independent tasks, isolated trees, reviewed separately.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 6 — lab section (R15, step 1 headless, step 2 W9 + worktrees, step 4 U14 + ci):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: > path needs no extra service; R15.)
- new: > path needs no extra service.)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: unattended run ({{vd:headless}}).
- new: unattended run.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: 2. **Parallel via worktrees (W9).** Pick **two genuinely independent** changes (e.g. add a `GET
- new: 2. **Parallel via worktrees.** Pick **two genuinely independent** changes (e.g. add a `GET
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: shows ≥2 trees ({{vd:worktrees}}).
- new: shows ≥2 trees.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: trigger, what runs unattended, and how it relates to the U14 hook + pre-commit gate (defense in
- new: trigger, what runs unattended, and how it relates to the in-session hook + pre-commit gate (defense in
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: a PR ({{vd:ci}}).
- new: a PR.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Batch 7 — self-check, reference link, pitfalls, Going-deeper:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - [ ] You **reviewed each diff separately** before integrating, and integrated only what passed — the
- new: - [ ] You **reviewed each diff separately** before integrating, and integrated only what passed — the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - [ ] You can describe the repo's **CI** trigger and what it runs unattended, and how it layers with the
- new: - [ ] You can describe the repo's **CI** trigger and what it runs unattended, and how it layers with the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - [ ] No flag or integration detail was **authored from memory** — confirmed against {{vd:headless}} /
- new: - [ ] No flag or integration detail was **authored from memory** — confirmed against `claude --help` / the docs.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: [W9 method](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is the reference for
- new: [parallel-agents workflow](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees) is the reference for
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: `--output-format json`/`stream-json` — scraping the human-readable text is brittle ({{vd:headless}}).
- new: `--output-format json`/`stream-json` — scraping the human-readable text is brittle.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: are version-/integration-specific — confirm against `--help` and the docs ({{vd:headless}},
- new: are version-/integration-specific — confirm against `--help` and the docs.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - **W9** parallel-agents pattern: [`meta/workflows.md`](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees).
- new: - The parallel-agents pattern: [`meta/workflows.md`](../../../meta/workflows.md#w9--running-parallel-agents-git-worktrees).
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md
- old: - Headless / CI / worktree surfaces — {{vd:headless}}, {{vd:ci}}, {{vd:worktrees}};
- new: - Headless / CI / worktree surfaces: {{vd:headless}} {{vd:ci}} {{vd:worktrees}}
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
f=course/units/16-automate-and-scale/unit.md; awk 'NR>13' "$f" | grep -nE '\b[UCRW][0-9]+\b|`CV`|advances|Advances' || echo "NO CODES REMAIN"
```

<details><summary>tool result</summary>

```
NO CODES REMAIN
```

</details>

## 🤖 Assistant

All codes clear. Now migrate and render:

## 🤖 Assistant

**→ Bash**

```
d=course/units/16-automate-and-scale
git mv $d/unit.md $d/unit.src.md
tmp=$(mktemp); cat > "$tmp" <<'HDR'
<!-- SOURCE — authored unit. Edit THIS file; the sibling unit.md is generated by
     tools/render-units, which resolves the version-data tokens. Run `make render` after editing. -->
HDR
cat "$d/unit.src.md" >> "$tmp" && mv "$tmp" "$d/unit.src.md"
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

I spot a grammar slip in the rendered TL;DR (L36–37): dropping the headless token left "...pipe or parse" running straight into "cap spend" with no punctuation. Let me fix it in the source:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.src.md
```

<details><summary>tool result</summary>

```
36	> Three moves to run Claude without babysitting it. **Headless:** `claude -p "<task>"
37	> --output-format json` runs non-interactively and prints structured output you can pipe or parse
38	> cap spend with `--max-budget-usd`. **CI:** run that — or your check suite — on
39	> every push; this repo's [`.github/workflows/checks.yml`](../../../.github/workflows/checks.yml) is
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.src.md
- old: > --output-format json` runs non-interactively and prints structured output you can pipe or parse
- new: > --output-format json` runs non-interactively and prints structured output you can pipe or parse;
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/units/16-automate-and-scale/unit.src.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Expected drift — I edited the source. Re-render and check:

## 🤖 Assistant

**→ Bash**

```
tools/render-units >/dev/null && make check >/dev/null 2>&1 && echo GREEN || echo "CHECK FAILED"
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

**→ Bash**

```
grep -n 'pipe or parse' course/units/16-automate-and-scale/unit.md
```

<details><summary>tool result</summary>

```
36:> --output-format json` runs non-interactively and prints structured output you can pipe or parse;
```

</details>

## 🤖 Assistant

U16 done, `make check` green — and that completes **task 7.6 (the U5–U16 rollout)**. The TL;DR now reads cleanly.

## U16 complete — summary

**`16-automate-and-scale`** — migrated + de-coded:
- **`(W9)` stripped throughout** — objective, TL;DR, Concept §3 header, code comment, lab step 2, self-check ("parallel-worktrees verification step"); link texts `[W9 pattern]`/`[W9 method]` → "parallel-worktrees pattern"/"parallel-agents workflow"; Going-deeper "**W9** parallel-agents pattern" → "The parallel-agents pattern".
- **Codes → titles** — `U14`→**Hooks** (worked example) / "in-session hook" (lab + self-check).
- **R# breadcrumbs dropped** — `(R14)`, `(R12.AC7)`, `; R15`.
- **Garble fixes — all four token types** (`headless`/`ci`/`worktrees`/`checkpoint-rewind`, each a backtick-leading multi-clause sentence): kept in sentence position at their Concept teaching spots (§1/§2/§3/§5), the version-currency note (`ci`+`checkpoint-rewind` as the unverified-surface references), and the Going-deeper pointer; dropped the ~12 redundant parenthetical pointers. Caught and fixed a punctuation slip ("pipe or parse cap spend") on the eyeball pass.

Files changed (uncommitted): `16-automate-and-scale/unit.src.md` (new), `unit.md` (regenerated).

## Milestone: task 7.6 is complete 🎉
**All 16 units are now de-coded + migrated to the committed-rendered pattern.** U15 and U16 are uncommitted (last checkpoint `ed66fe8` = U9–U14).

What remains in P7:
- **7.7** — cross-cutting prose sweep: `course/capstone/{README,briefs,rubric,case-study}.md`, `course/stuck.md` (same M1/M2 sweep, keeping load-bearing rubric `[Cn]` tags; maintainer-guide may keep `R#`).
- **7.8** — convention docs for the `unit.src.md` split: `course/maintainer-guide.md`, `meta/templates/unit-*.md`, the `close-unit` skill.
- **7.9** — close-out: strike **L8** in `decisions.md`, mark P7 done in `tasks.md` + `IMPLEMENTATION.md` §3, final commit(s).

Want me to **commit U15–U16** (closing out 7.6) and then start **7.7**?

## 🧑 User

commit U15–U16 then continue to 7.7

## 🤖 Assistant

Committing U15–U16 to close out 7.6:

## 🤖 Assistant

**→ Bash**

```
git add course/units/15-mcp-and-vetting course/units/16-automate-and-scale
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
M  course/units/15-mcp-and-vetting/unit.md
A  course/units/15-mcp-and-vetting/unit.src.md
M  course/units/16-automate-and-scale/unit.md
A  course/units/16-automate-and-scale/unit.src.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
git commit -q -F - <<'MSG'
P7: roll learner-prose remediation through U15–U16 — completes 7.6 (all 16 units)

Final units of the Stage-C editorial rollout (tasks/P7-quality-pass.md §7.6),
migrated to the committed-rendered pattern and fully de-coded:

- U15: R10.AC5 breadcrumbs dropped (×4); mcp/plugins version-token garbles
  fixed (kept in sentence position at Concept §2/§4 + version-currency +
  going-deeper, dropped redundant parenthetical pointers).
- U16: (W9) stripped throughout; U14 → Hooks / "in-session hook"; R14/R12.AC7/
  R15 breadcrumbs dropped; headless/ci/worktrees/checkpoint-rewind tokens
  (multi-clause sentences) repositioned to sentence position.

7.6 is complete: all 16 units (U1–U16) are de-coded + committed-rendered.
Remaining P7: 7.7 cross-cutting sweep, 7.8 convention docs, 7.9 close-out.
make check green. Branch local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (48.8KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bdhnjoced.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
60dfd69 P7: roll learner-prose remediation through U15–U16 — completes 7.6 (all 16 units)
---
```

</details>

## 🤖 Assistant

Committed (`60dfd69`), tree clean — **7.6 done**. Now **task 7.7**, the cross-cutting prose sweep. Let me scope it by scanning the five files for codes, R-IDs, CV, and any `{{vd:}}` tokens:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
for f in course/capstone/README.md course/capstone/briefs.md course/capstone/rubric.md course/capstone/case-study.md course/stuck.md; do
  echo "===== $f ====="
  grep -nE '\b[UW][0-9]+\b|\bR[0-9]+(\.AC[0-9]+)?\b|\bC[0-9]+\b|\bCV\b|\{\{vd:' "$f" || echo "  (none)"
done
```

<details><summary>tool result</summary>

```
===== course/capstone/README.md =====
3:The capstone is the course's **single graded assessment** (R8.AC1) — the one place you prove, end to
10:result. Whichever you choose, the deliverable must show all four (R8.AC1):
19:built with Claude Code — is your worked **exemplar** (R8.AC2).
27:3. **The required verification reflection** (R8.AC6) — structured by these prompts, each with concrete
35:This reflection is not optional polish — it is the core of the cross-cutting [CV] dimension and the
36:thesis the whole course defends: verify, don't trust (R10).
40:Score the work product against the [rubric](./rubric.md). It is **self-applicable** (R8.AC4): for each
44:**Optional AI-assisted self-grade (R8.AC5).** You may have Claude score your capstone against the
50:After the **Daily Driver** stage (through U8), you may take an optional, **ungraded** self-check to
51:surface gaps before the capstone (R8.AC7). It does not change the capstone's status as the sole graded
57:can-dos **C5–C9 and CV** using the [rubric](./rubric.md). If any land at "not yet," revisit that
===== course/capstone/briefs.md =====
4:have room to make it yours while facing the same kind of work the course prepared you for (R8.AC2).
6:Whichever you choose, your capstone must demonstrate all four of these (R8.AC1):
34:- **Workflow:** spec-driven (W7) to pin down requirements → design → tasks, then explore → plan →
35:  code → commit (W1) to build it.
61:- **Workflow:** onboard to the unfamiliar code (W8) to map it, then multi-file refactor (W5),
62:  behavior-preserving. If you fix a bug, do it test-first (W3/W2) *after* the refactor.
92:- **Workflow:** review-and-vet (W6) the extension, then use it; coordinate the run (W9) if you go
===== course/capstone/rubric.md =====
3:This is how you grade your **capstone work product** — not yourself (R8.AC3). It is **self-applicable**:
4:a solo learner can score their own capstone against it with no external evaluator (R8.AC4). The
5:dimensions below collectively cover **every can-do** in the capability map (C1–C17 + the cross-cutting
6:verification habit CV), which is also what
22:your capstone *and* the labs you completed**, with the cross-cutting CV dimension demonstrated *within
28:- **[C1] Working setup, repeatably checked** — demonstrated when your environment is established and you
30:- **[C2] A single, verified change to a real codebase** — demonstrated when at least one change is made
32:- **[C3] Explore and locate** — demonstrated when your write-up shows you used Claude to understand
34:- **[C4] Operate safely** — demonstrated when you chose appropriate permission posture, protected any
36:- **[C5] Steer with memory and context** — demonstrated when you used `CLAUDE.md` and deliberate context
40:- **[C6] Feature end-to-end (explore → plan → code → commit)** — demonstrated when a non-trivial change
42:- **[C7] Test-first** — demonstrated when at least one behavior was driven from a failing test confirmed
44:- **[C8] Diagnose to root cause** — demonstrated when a failure was fixed after confirming the cause
46:- **[C9] Clean commits and a reviewable PR** — demonstrated when the work is staged into coherent
50:- **[C10] Large multi-file refactor, kept green** — demonstrated when a behavior-preserving change spans
52:- **[C11] Spec-driven workflow** — demonstrated when you ran requirements → design → tasks with a real
54:- **[C12] Review for correctness and security** — demonstrated when you reviewed a change (yours or
58:- **[C13] Package repeatable work as commands & skills** — demonstrated when you built at least one
60:- **[C14] Delegate to subagents** — demonstrated when a focused (or parallel) sub-task was delegated to a
… [+32 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

This is a meaningful sweep with judgment calls — especially `rubric.md`, where the `[Cn]`/`[CV]` bracket tags are load-bearing and must stay. Let me read the files to edit accurately. Starting with README and rubric:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/capstone/README.md
```

<details><summary>tool result</summary>

```
1	# Capstone
2	
3	The capstone is the course's **single graded assessment** (R8.AC1) — the one place you prove, end to
4	end, that you can do real work with Claude Code and **verify** it. Units are instructional and labs are
5	ungraded practice; this is the only thing you "grade," and you grade the **work product**, not yourself.
6	
7	## What it asks of you
8	
9	Pick one brief from the [brief menu](./briefs.md) and take it from nothing to a verified, finished
10	result. Whichever you choose, the deliverable must show all four (R8.AC1):
11	
12	- **Context engineering** — deliberate `CLAUDE.md` / context steering.
13	- **At least one custom extension** — a command, subagent, skill, hook, or MCP connection you build
14	  and use.
15	- **A non-trivial workflow** — a real multi-step workflow, not a one-shot prompt.
16	- **Explicit verification** — you check Claude's output, not merely the test bar.
17	
18	You do **not** face a blank page: the [build case study](./case-study.md) — how this course itself was
19	built with Claude Code — is your worked **exemplar** (R8.AC2).
20	
21	## The deliverable
22	
23	1. **The work itself** — committed to a branch (or your own repo), with a short README pointing at
24	   what you built and how to run/verify it.
25	2. **A brief write-up** — which brief, the workflow you followed, the custom extension you built and
26	   why, and how you engineered context.
27	3. **The required verification reflection** (R8.AC6) — structured by these prompts, each with concrete
28	   evidence from your work:
29	   - **One catch** — a place you caught Claude producing something wrong or suboptimal, and what you
30	     did about it.
31	   - **One justified accept** — a place you accepted Claude's output, and the evidence that justified
32	     trusting it (not "the tests passed" alone).
33	   - **One override** — a place you overrode or redirected Claude, and why your judgment won.
34	
35	This reflection is not optional polish — it is the core of the cross-cutting [CV] dimension and the
36	thesis the whole course defends: verify, don't trust (R10).
37	
38	## Grading your own capstone
39	
40	Score the work product against the [rubric](./rubric.md). It is **self-applicable** (R8.AC4): for each
… [+25 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/capstone/rubric.md
```

<details><summary>tool result</summary>

```
1	# Capstone rubric
2	
3	This is how you grade your **capstone work product** — not yourself (R8.AC3). It is **self-applicable**:
4	a solo learner can score their own capstone against it with no external evaluator (R8.AC4). The
5	dimensions below collectively cover **every can-do** in the capability map (C1–C17 + the cross-cutting
6	verification habit CV), which is also what
7	[`progress-checklist.md`](../progress-checklist.md) tracks.
8	
9	## How to score
10	
11	For each dimension, mark the **evidence in your deliverable** at one of three levels — never a label on
12	you:
13	
14	- **Demonstrated** — the work product clearly shows this, with evidence you can point to (a commit, a
15	  diff, a test, a file, a passage in your write-up).
16	- **Partially demonstrated** — some of it is there, but it is incomplete, unverified, or only implied.
17	- **Not yet demonstrated** — the capstone does not show this.
18	
19	**Honest "not yet" is the point.** No single brief exercises all eighteen dimensions equally — that is
20	expected. The rubric is the full capability map so gaps surface; a "not yet" is not a failure, it is a
21	pointer back to the unit that teaches it. Aim to have **every dimension at least "demonstrated" across
22	your capstone *and* the labs you completed**, with the cross-cutting CV dimension demonstrated *within
23	the capstone itself*.
24	
25	## Dimensions
26	
27	### First Wins
28	- **[C1] Working setup, repeatably checked** — demonstrated when your environment is established and you
29	  can re-confirm it (e.g. `tools/doctor` or an equivalent check) rather than assuming it.
30	- **[C2] A single, verified change to a real codebase** — demonstrated when at least one change is made
31	  *and* its effect is confirmed by observation/test, not assumed from the fact that Claude produced it.
32	- **[C3] Explore and locate** — demonstrated when your write-up shows you used Claude to understand
33	  unfamiliar code and pinpoint where the work had to happen (file/symbol level), rather than guessing.
34	- **[C4] Operate safely** — demonstrated when you chose appropriate permission posture, protected any
35	  secrets, and kept blast radius bounded (and can say how) for the work you did.
36	- **[C5] Steer with memory and context** — demonstrated when you used `CLAUDE.md` and deliberate context
37	  selection to shape Claude's behavior, and can point to where it changed an outcome.
38	
39	### Daily Driver
40	- **[C6] Feature end-to-end (explore → plan → code → commit)** — demonstrated when a non-trivial change
… [+43 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
```

<details><summary>tool result</summary>

```
1	# Capstone briefs
2	
3	Pick **one** brief. Each is a realistic, non-trivial, end-to-end job — not a fixed project — so you
4	have room to make it yours while facing the same kind of work the course prepared you for (R8.AC2).
5	
6	Whichever you choose, your capstone must demonstrate all four of these (R8.AC1):
7	
8	1. **Context engineering** — deliberate use of `CLAUDE.md` and context selection to steer Claude.
9	2. **At least one custom extension** — a command, subagent, skill, hook, or MCP connection that you
10	   build and actually use in the work.
11	3. **A non-trivial workflow** — a real multi-step workflow from the course
12	   ([`meta/workflows.md`](../../meta/workflows.md)), not a one-shot prompt.
13	4. **Explicit verification** — you verify Claude's output (read the diff, check the approach,
14	   spot-check edges), not merely trust green tests.
15	
16	You will grade the result against the [rubric](./rubric.md), and the
17	[build case study](./case-study.md) is your worked exemplar so you never start from a blank page.
18	
19	---
20	
21	## Brief A — Ship a substantial feature, spec-first
22	
23	**Substrate:** [`taskflow-api`](../../codebases/primary/taskflow-api) (primary).
24	
25	**Goal.** Add a substantial, multi-layer feature to the API — one big enough to be worth a spec.
26	Good candidates: task **dependencies / blocked-by** (with cycle handling), **recurring tasks**, an
27	**activity/audit log**, or **saved filters/views**. The feature must touch models, services, routes,
28	and tests, and respect the app's ownership/auth rules.
29	
30	**What makes it capstone-worthy.** It is ambiguous enough that jumping straight to code fails — the
31	design decisions (data model, edge cases, error contracts) are the real work.
32	
33	**Shape.**
34	- **Workflow:** spec-driven (W7) to pin down requirements → design → tasks, then explore → plan →
35	  code → commit (W1) to build it.
36	- **Custom extension:** build a **custom command** (or skill) that automates a routine in this
37	  loop — e.g. scaffolding a route + schema + test stub, or running and triaging the test suite.
38	- **Context engineering:** use the project `CLAUDE.md` and targeted context so Claude follows the
39	  app's conventions (services → exceptions → routes).
40	- **Verification:** the suite stays green; you read the diff; and you confirm the **ownership/404
… [+63 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
```

<details><summary>tool result</summary>

```
1	# Case study: how this course was built and is maintained with Claude Code
2	
3	This is the **worked exemplar** for your capstone (R8.AC2) — and it is real. This course was itself
4	built end-to-end with Claude Code, spec-driven, against the same discipline the units teach. Read it
5	before you start your capstone so you have a concrete picture of a non-trivial job done well: context
6	engineered deliberately, custom extensions built and used, a real workflow followed, and Claude's
7	output verified at every step rather than trusted.
8	
9	It is also the course's standing dogfooding record (R14.AC4): if we teach a feature, we point at the
10	real artifact we used, never a prop (R14.AC3).
11	
12	## 1. The job
13	
14	Take a seasoned developer who is new to AI-assisted coding to elite Claude Code practitioner — as a
15	self-paced, hands-on course organized around real use cases, tiered for fast learners, and resilient
16	to a fast-moving CLI. That is a large, ambiguous brief with no single right answer, exactly the kind
17	of work where ad-hoc prompting falls apart and a deliberate process pays for itself.
18	
19	## 2. The workflow: spec-driven, with real gates
20	
21	We ran the [Kiro-style spec workflow](../units/10-spec-driven-dev/unit.md) the course teaches in U10,
22	on the course itself. The artifacts are not illustrations — they are the spec we actually built from:
23	
24	- **Requirements** ([`requirements.md`](../../specs/claude-code-mastery/requirements.md)) — R1–R15 in
25	  EARS form, with stable IDs. Approved turn-by-turn **before** any design work began.
26	- **Design** ([`design.md`](../../specs/claude-code-mastery/design.md)) — architecture, the unit
27	  model, the version-resilience mechanism, the lab/codebase plan, and a traceability table mapping
28	  every requirement to the component that satisfies it. Approved **before** tasks.
29	- **Tasks** ([`tasks.md`](../../specs/claude-code-mastery/tasks.md)) — the ordered build plan, chunked
30	  into phases (scaffold → tooling → codebases → units → finalize) so each could be executed in a
31	  bounded context window.
32	
33	The gates were genuine, not ceremony: requirements were locked before design, design before tasks. A
34	held gate is the difference between a spec and a wish — when a requirement felt arbitrary later, the
35	reasoning was already recorded rather than re-litigated. That "why" lives in
36	[`decisions.md`](../../specs/claude-code-mastery/decisions.md), the build's decision log (R14.AC7),
37	which a fresh session reads to recover context it never had.
38	
39	**Context was engineered, not dumped.** Each unit was authored in its own slice, loading only the
40	relevant requirements, the one design section, and the cross-cutting `meta/` artifacts it referenced —
… [+70 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/stuck.md
```

<details><summary>tool result</summary>

```
1	# When you're stuck
2	
3	You're working through this course **solo** — so getting unstuck without an instructor is a skill
4	in itself. This page is your recovery mechanism (R9.AC4). Work top to bottom; stop as soon as you're
5	moving again.
6	
7	## 1. Re-read the lab's self-check
8	
9	Every lab states an **objective self-check** and (where feasible) a `tools/verify-lab` command. If
10	you're not sure whether you're stuck, run the check — "done" is defined, not a feeling.
11	
12	## 2. Use a hint before the solution
13	
14	Hints are deliberately separated from solutions so you can get a nudge without spoiling the exercise:
15	
16	- **Hint:** read the unit's **Common pitfalls** section — most stuck points are a known pitfall for
17	  *that* task.
18	- **Still stuck:** skim the relevant pattern in [`../meta/workflows.md`](../meta/workflows.md) (the
19	  unit names the workflow it uses).
20	- **Last resort:** inspect the reference solution branch `solution/uNN-labM` (`git diff
21	  start/uNN-labM solution/uNN-labM`). Read it to understand *why*, then redo the lab yourself from a
22	  clean `tools/reset-lab uNN-labM`.
23	
24	## 3. Use Claude Code itself to get unstuck
25	
26	This is the meta-skill the course is teaching — Claude is also your debugger and tutor:
27	
28	- **Explain the failure:** paste the error and ask Claude to explain it *and* point at the file/line.
29	  Then **verify** its explanation against the code (CV) — don't just accept it.
30	- **Ask for the approach, not the answer:** "What are the likely causes of this, in order?" keeps you
31	  in the driver's seat.
32	- **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the W3 debugging
33	  pattern) so "fixed" becomes objective.
34	- **Reset and retry:** if a session has gone sideways, `tools/reset-lab uNN-labM` and start the lab
35	  clean — a fresh context often beats untangling a confused one.
36	
37	## 4. Environment problems
38	
39	- Run [`../tools/doctor`](../tools/doctor) — it checks install, version, auth, and a first command.
40	- If `claude --version` differs from `meta/version-record.md`, some version-specific details may have
… [+13 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Now I have all five files mapped. Note one judgment call I'll make: in `case-study.md` I'll **keep** "R1–R15 in EARS form" (L24) — like U10's teaching R-IDs, it describes the *real* requirements file the learner opens, not a breadcrumb. Everything else (R#.AC# cites) drops.

Editing **README.md** (8 edits):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: The capstone is the course's **single graded assessment** (R8.AC1) — the one place you prove, end to
- new: The capstone is the course's **single graded assessment** — the one place you prove, end to
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: result. Whichever you choose, the deliverable must show all four (R8.AC1):
- new: result. Whichever you choose, the deliverable must show all four:
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: built with Claude Code — is your worked **exemplar** (R8.AC2).
- new: built with Claude Code — is your worked **exemplar**.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: 3. **The required verification reflection** (R8.AC6) — structured by these prompts, each with concrete
- new: 3. **The required verification reflection** — structured by these prompts, each with concrete
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: This reflection is not optional polish — it is the core of the cross-cutting [CV] dimension and the
- new: This reflection is not optional polish — it is the core of the cross-cutting verification (CV) dimension and the
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: Score the work product against the [rubric](./rubric.md). It is **self-applicable** (R8.AC4): for each
- new: Score the work product against the [rubric](./rubric.md). It is **self-applicable**: for each
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: **Optional AI-assisted self-grade (R8.AC5).** You may have Claude score your capstone against the
- new: **Optional AI-assisted self-grade.** You may have Claude score your capstone against the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/README.md
- old: After the **Daily Driver** stage (through U8), you may take an optional, **ungraded** self-check to
- new: After the **Daily Driver** stage (through **Git & PR**), you may take an optional, **ungraded** self-check to
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Editing **rubric.md** (keeping all `[Cn]`/`[CV]` dimension headings):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/rubric.md
- old: This is how you grade your **capstone work product** — not yourself (R8.AC3). It is **self-applicable**:
- new: This is how you grade your **capstone work product** — not yourself. It is **self-applicable**:
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/rubric.md
- old: override. This dimension should be **demonstrated**, not partial: it is the thesis the whole course
- new: override. This dimension should be **demonstrated**, not partial: it is the thesis the whole course
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/rubric.md
- old: ## Optional AI-assisted self-grade (then critique it) — R8.AC5
- new: ## Optional AI-assisted self-grade (then critique it)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/rubric.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/rubric.md
- old: why, with evidence from your deliverable. Accepting an AI grade unexamined is the exact failure mode
- new: why, with evidence from your deliverable. Accepting an AI grade unexamined is the exact failure mode
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/rubric.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/rubric.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/rubric.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Editing **briefs.md** (drop the W# workflow codes in the three Shape sections + two R# cites):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
- old: have room to make it yours while facing the same kind of work the course prepared you for (R8.AC2).
- new: have room to make it yours while facing the same kind of work the course prepared you for.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
- old: Whichever you choose, your capstone must demonstrate all four of these (R8.AC1):
- new: Whichever you choose, your capstone must demonstrate all four of these:
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
- old: - **Workflow:** spec-driven (W7) to pin down requirements → design → tasks, then explore → plan →
- new: - **Workflow:** spec-driven to pin down requirements → design → tasks, then explore → plan →
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/briefs.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
- old: - **Workflow:** onboard to the unfamiliar code (W8) to map it, then multi-file refactor (W5),
- new: - **Workflow:** onboard to the unfamiliar code to map it, then multi-file refactor,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/briefs.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/briefs.md
- old: - **Workflow:** review-and-vet (W6) the extension, then use it; coordinate the run (W9) if you go
- new: - **Workflow:** review-and-vet the extension, then use it; coordinate the run if you go
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/briefs.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/briefs.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/briefs.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Editing **case-study.md** — prose cites, the `U4`/`U10` refs, the table link texts, and the `(CV)` heading:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: This is the **worked exemplar** for your capstone (R8.AC2) — and it is real. This course was itself
- new: This is the **worked exemplar** for your capstone — and it is real. This course was itself
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: It is also the course's standing dogfooding record (R14.AC4): if we teach a feature, we point at the
- new: It is also the course's standing dogfooding record: if we teach a feature, we point at the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: We ran the [Kiro-style spec workflow](../units/10-spec-driven-dev/unit.md) the course teaches in U10,
- new: We ran the [Kiro-style spec workflow](../units/10-spec-driven-dev/unit.md) the course teaches,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: [`decisions.md`](../../specs/claude-code-mastery/decisions.md), the build's decision log (R14.AC7),
- new: [`decisions.md`](../../specs/claude-code-mastery/decisions.md), the build's decision log,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: never the whole spec. Project memory ([`CLAUDE.md`](../../CLAUDE.md), the U4 example) carries the
- new: never the whole spec. Project memory ([`CLAUDE.md`](../../CLAUDE.md), the **Memory & context** example) carries the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: These are authentic — each one earns its place by doing a job in the real build loop (R14.AC1/AC2):
- new: These are authentic — each one earns its place by doing a job in the real build loop:
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: ## 4. Verification was the through-line (CV)
- new: ## 4. Verification was the through-line
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: The course is built to be refreshed, not rewritten, when Claude Code moves (R12.AC7). The process — run
- new: The course is built to be refreshed, not rewritten, when Claude Code moves. The process — run
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: In the spirit of the responsible-output guidance the course itself teaches (R10.AC9): AI-assisted
- new: In the spirit of the responsible-output guidance the course itself teaches: AI-assisted
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the case-study table link texts (U# → titles; `replace_all` for the duplicated U12/U16):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: | [U12](../units/12-commands-and-skills/unit.md) |
- new: | [Commands & skills](../units/12-commands-and-skills/unit.md) |
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: | [U16](../units/16-automate-and-scale/unit.md) |
- new: | [Automate & scale](../units/16-automate-and-scale/unit.md) |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: | [U14](../units/14-hooks/unit.md) |
- new: | [Hooks](../units/14-hooks/unit.md) |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: | [U15](../units/15-mcp-and-vetting/unit.md) |
- new: | [MCP & vetting](../units/15-mcp-and-vetting/unit.md) |
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/capstone/case-study.md
- old: | [U1](../units/01-onboarding-first-win/unit.md) |
- new: | [Onboarding](../units/01-onboarding-first-win/unit.md) |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/capstone/case-study.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Finally **stuck.md** (4 edits):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/stuck.md
- old: in itself. This page is your recovery mechanism (R9.AC4). Work top to bottom; stop as soon as you're
- new: in itself. This page is your recovery mechanism. Work top to bottom; stop as soon as you're
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/stuck.md
- old: Then **verify** its explanation against the code (CV) — don't just accept it.
- new: Then **verify** its explanation against the code — don't just accept it.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/stuck.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/stuck.md
- old: - **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the W3 debugging
- new: - **Reproduce, then narrow:** ask Claude to help you write a minimal failing test (the debugging
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/stuck.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/stuck.md
- old: (the authoritative ordering); the numeric path is just the default (R9.AC2).
- new: (the authoritative ordering); the numeric path is just the default.
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/stuck.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/stuck.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify the sweep — confirm only intended codes remain (rubric `[Cn]`/`[CV]` tags, the kept case-study `R1–R15`, the lab-id `uNN` placeholders, and `{{vd:*}}` literal in stuck.md), then run the checks:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== remaining R#.AC# / bare U#,W# / bare CV (should be only kept ones) ==="
for f in course/capstone/README.md course/capstone/briefs.md course/capstone/rubric.md course/capstone/case-study.md course/stuck.md; do
  hits=$(grep -nE '\bR[0-9]+\.AC[0-9]+|\b[UW][0-9]+\b' "$f")
  [ -n "$hits" ] && echo "--- $f ---" && echo "$hits"
done
echo "(R1–R15 in case-study and uNN-labM placeholders are expected/kept)"
echo "=== make check ==="
make check >/dev/null 2>&1 && echo GREEN || echo "FAILED"
```

<details><summary>tool result</summary>

```
=== remaining R#.AC# / bare U#,W# / bare CV (should be only kept ones) ===
(R1–R15 in case-study and uNN-labM placeholders are expected/kept)
=== make check ===
GREEN
```

</details>

## 🤖 Assistant

No residual breadcrumb codes remain, and `make check` is green. The intended keepers survived: rubric `[Cn]`/`[CV]` dimension tags, the README's `C5–C9 and CV` rubric pointer, case-study's descriptive `R1–R15`, and lab-id `uNN-labM` placeholders.

## 7.7 complete — cross-cutting prose sweep

Swept all five files (edited in place — these aren't units, so no migration):

- **`README.md`** — dropped 8 `R8.AC#`/`R10` breadcrumbs; `[CV]` → "cross-cutting verification (CV)"; `U8` → **Git & PR**. Kept the `C5–C9 and CV` checkpoint pointer (it indexes the rubric's labeled rows).
- **`rubric.md`** — dropped `R8.AC3/AC4/AC5`/`R10` cites and the `C1–C17` code-dump (expanded CV inline); de-bracketed the one *prose* `[CV]` at the end. **All `[Cn]`/`[CV]` dimension headings preserved** (load-bearing for `check-traceability`).
- **`briefs.md`** — dropped `R8.AC1/AC2` and the workflow codes `(W1)(W5)(W6)(W7)(W8)(W9)(W3/W2)` from the three Shape sections (the workflow names are already spelled out).
- **`case-study.md`** — dropped `R8.AC2`, `R14.AC1/AC2/AC3/AC4/AC7`, `R12.AC7`, `R10.AC9`; `U10`/`U4` → titles; the "Taught in" table link texts `U1/U12/U14/U15/U16` → unit titles; dropped `(CV)` from the §4 heading. **Kept** the descriptive `R1–R15` (it names the real requirements file, like U10's teaching IDs).
- **`stuck.md`** — dropped `R9.AC4`/`R9.AC2`, the `(CV)` tag, and `(the W3 debugging pattern)` → "(the debugging workflow)". Left the literal `` `{{vd:*}}` `` callout reference (it documents the token syntax).

Per the 7.7 spec, the **maintainer-guide is left for 7.8** (it may legitimately keep `R#`, and it also needs the `unit.src.md` convention update).

That leaves:
- **7.8** — convention docs for the committed-rendered split: `course/maintainer-guide.md`, `meta/templates/unit-*.md`, the `close-unit` skill (authored file is now `unit.src.md`; `make render` regenerates `unit.md`).
- **7.9** — close-out: strike L8, mark P7 done in `tasks.md` + IMPLEMENTATION §3, final commit.

Want me to **commit 7.7** and continue to **7.8**?

## 🧑 User

commit 7.7 then continue to 7.8

## 🤖 Assistant

Committing 7.7:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add course/capstone/README.md course/capstone/briefs.md course/capstone/rubric.md course/capstone/case-study.md course/stuck.md
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
M  course/capstone/README.md
M  course/capstone/briefs.md
M  course/capstone/case-study.md
M  course/capstone/rubric.md
M  course/stuck.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git commit -q -F - <<'MSG'
P7 (7.7): cross-cutting prose sweep — capstone files + stuck.md

Apply the same learner-prose de-coding to the non-unit course files (edited in
place; these aren't committed-rendered units):

- Dropped R#/R#.AC# breadcrumb cites and bare U#/W# taxonomy codes; converted
  unit cross-refs (incl. the case-study "Taught in" table link texts) to titles;
  expanded/de-bracketed CV in prose.
- Kept the load-bearing rubric [Cn]/[CV] dimension headings (check-traceability),
  the README "C5–C9 and CV" rubric pointer, and case-study's descriptive R1–R15
  (names the real requirements file, like U10's teaching IDs).

maintainer-guide intentionally deferred to 7.8 (may keep R#; also needs the
unit.src.md convention update). make check green. Branch local only.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (48.8KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/btvooo53z.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
cfd04ec P7 (7.7): cross-cutting prose sweep — capstone files + stuck.md
---
```

</details>

## 🤖 Assistant

Committed (`cfd04ec`), clean. Now **7.8** — teach the `unit.src.md`/`unit.md` split in the convention docs. Let me find where these files reference unit authoring:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== templates present ==="; ls meta/templates/
echo "=== unit.md / unit.src.md / render mentions ==="
grep -rnE 'unit\.md|unit\.src\.md|make render|render-units|render-index' course/maintainer-guide.md .claude/commands/close-unit.md meta/templates/ 2>/dev/null
```

<details><summary>tool result</summary>

```
=== templates present ===
unit-awareness.md
unit-core.md
=== unit.md / unit.src.md / render mentions ===
.claude/commands/close-unit.md:6:Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.md`
course/maintainer-guide.md:16:- **Front matter** — every `course/units/NN-slug/unit.md` validates against
course/maintainer-guide.md:44:   `course/units/NN-slug/unit.md`, using a zero-padded `NN` and kebab-case slug
course/maintainer-guide.md:58:7. **Sync state and check.** Run the [`close-unit` command](../.claude/commands/close-unit.md) to
course/maintainer-guide.md:80:4. **Close the unit.** Run [`close-unit`](../.claude/commands/close-unit.md) to sync every state file
meta/templates/unit-core.md:2:TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.md and fill every section.
meta/templates/unit-awareness.md:2:TEMPLATE: awareness-tier unit (reduced — R6.AC2). Copy to course/units/NN-slug/unit.md.
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
```

<details><summary>tool result</summary>

```
1	# Maintainer guide
2	
3	How to add or update a unit — and refresh the course when the CLI changes — **without breaking the
4	catalog, coverage matrix, or capability map** (R13.AC3). The automated checks are your backstop, but
5	they tell you *that* something broke, not *how to avoid* breaking it; this guide is the "how."
6	
7	If you are picking up this repo cold, start by reading
8	[`../specs/claude-code-mastery/IMPLEMENTATION.md`](../specs/claude-code-mastery/IMPLEMENTATION.md) and
9	running the [`prime-context` skill](../.claude/skills/prime-context/SKILL.md) — see the recipe below.
10	
11	## The invariants you must not break
12	
13	Everything cross-cutting lives **once** and is referenced by key (R13.AC2); duplication rots. The
14	[checks](../tools/) enforce these — run `make check` and keep it green:
15	
16	- **Front matter** — every `course/units/NN-slug/unit.md` validates against
17	  [`unit-frontmatter.schema.json`](../meta/unit-frontmatter.schema.json) (`check-frontmatter`).
18	- **Coverage** — every can-do (C1–C17 + CV) is advanced by ≥1 unit, every coverage-matrix area is
19	  covered, and every `advances`/`covered_by` id is real (`check-coverage`).
20	- **Links** — every internal relative link resolves (`check-links`). A link to a not-yet-created file
21	  fails the build, so reference forward targets as plain text until they exist.
22	- **Version references** — every version-data token (the `vd:` references) in `course/**` resolves to
23	  a key in [`version-data.yaml`](../meta/version-data.yaml) (`check-version-refs`).
24	- **Traceability** — every requirement R1–R15 is referenced by a course artifact, and every can-do
25	  traces to ≥1 lab **and** ≥1 capstone-rubric dimension (`check-traceability`).
26	
27	`make check` is the day-to-day guard; `make check-strict` is the release gate (it turns
28	not-yet-authored placeholders into hard failures).
29	
30	## Adding a unit
31	
32	Work in this order — **meta artifacts first, prose second** — so the single sources of truth lead and
33	the checks pass as you go:
34	
35	1. **Decide what it teaches.** If it introduces a genuinely new capability, add the can-do to
36	   [`capability-map.yaml`](../meta/capability-map.yaml) (and regenerate its `.json` twin — never
37	   hand-edit the JSON). Otherwise map the unit to existing can-dos.
38	2. **Register it in the catalog.** Add the unit to
39	   [`use-case-catalog.yaml`](../meta/use-case-catalog.yaml) (`advances:` the can-dos it teaches) and
40	   ensure the [`coverage-matrix.yaml`](../meta/coverage-matrix.yaml) areas it covers point back at it
… [+51 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

The maintainer-guide may keep its `R#` (per the 7.7 note) — my 7.8 job is to teach the `unit.src.md`/`unit.md` split. Let me read close-unit and the template headers first:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md
```

<details><summary>tool result</summary>

```
1	---
2	description: Sync every project state file after a unit's prose is authored, then run the checks
3	argument-hint: <NN>
4	---
5	
6	Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.md`
7	is authored, then verify. Pull specifics from the files, not memory; follow `meta/conventions.md`.
8	
9	Do each step, in order:
10	
11	1. **`specs/claude-code-mastery/IMPLEMENTATION.md` §3** — update the P5 progress marker so U$1 is in the
12	   done list (and the matching `tasks.md` status header if it tracks a count). Keep §3 terse.
13	2. **`specs/claude-code-mastery/tasks.md`** — add or confirm the unit's detail bullet (gist ·
14	   _Lab/refs_ · _Trace & version keys_). **Only check the `[ ] **U$1**` box if the unit is *fully*
15	   done** — prose authored **and** its lab complete: either the mutating lab's `start/`/`solution/`
16	   refs + `verify.sh` exist and pass end-to-end, or it is a no-refs unit (read-only / prose-self-check,
17	   like U2/U8/U12) that needs none. If lab artifacts are still pending, **leave the box unchecked**,
18	   record the prose as authored, and ensure step 3 keeps that lab open in **L7**. A checked box must
19	   never coexist with pending L7 lab refs for the same unit.
20	3. **`specs/claude-code-mastery/decisions.md`** — add the `P5-U$1-*` rationale entries (lab choice, any
21	   built artifacts, vd/L1 status), each with a **Why:** line, and refresh the 🔓 open-loops ledger —
22	   **L7** (per-lab `start/`/`solution/` refs + verifier status) and **L1** (version debt) for this unit.
23	4. **Verify version currency** — any `{{vd:*}}` key the unit introduced must be `unverified: false` in
24	   `meta/version-data.yaml`, verified against the installed CLI (R12.AC3–AC4). Flag any that isn't as
25	   open **L1** debt rather than claiming it's done.
26	5. **Run `make check`** and report the result — it must be green before the unit counts as closed.
27	
28	Then report a short summary of what each file received and the check result. Do not invent status: if a
29	verifier, a `SEEDED.md` §2 row, or a vd key isn't actually done, say so and leave it open in the ledger.
30	
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/templates/unit-core.md
```

<details><summary>tool result</summary>

```
1	<!--
2	TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.md and fill every section.
3	Sections are REQUIRED and must appear IN THIS ORDER (R6.AC1). Front matter must validate
4	against meta/unit-frontmatter.schema.json (R6.AC3). Delete these HTML comments when authoring.
5	Author in CommonMark; no meaning by color/emoji alone (R15.AC6). Reference version-specific
6	values only as {{vd:key}} — never hardcode them (R12.AC2).
7	-->
8	---
9	id: U0
10	title: "<imperative outcome, e.g. Ship a feature in taskflow-api>"
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/meta/templates/unit-awareness.md
```

<details><summary>tool result</summary>

```
1	<!--
2	TEMPLATE: awareness-tier unit (reduced — R6.AC2). Copy to course/units/NN-slug/unit.md.
3	Required sections IN ORDER: front matter; learning objectives; >=1 worked example or mention;
4	going deeper. Fast-path, skip-check, lab, and pitfalls are OPTIONAL at this tier.
5	NOTE: all 16 v1 units are core-tier; awareness tiering is applied at the FEATURE level inside
6	meta/coverage-matrix.yaml, not by demoting whole units (design §6). This template exists so a
7	future awareness-tier unit has a conforming shape. Front matter still validates against
8	meta/unit-frontmatter.schema.json. Delete these comments when authoring.
9	-->
10	---
```

</details>

## 🤖 Assistant

Now I have the full picture. Editing the **two templates** (authored file → `unit.src.md`, note the render step):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/meta/templates/unit-core.md
- old: TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.md and fill every section.
- new: TEMPLATE: core-tier unit. Copy to course/units/NN-slug/unit.src.md and fill every section.
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/meta/templates/unit-awareness.md
- old: TEMPLATE: awareness-tier unit (reduced — R6.AC2). Copy to course/units/NN-slug/unit.md.
- new: TEMPLATE: awareness-tier unit (reduced — R6.AC2). Copy to course/units/NN-slug/unit.src.md
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/meta/templates/unit-core.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/meta/templates/unit-awareness.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now **close-unit.md** (authored file is `unit.src.md`; note `make render` before the check):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md
- old: Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.md`
- new: Close out unit **U$1** — bring every state-tracking file in sync now that `course/units/$1-*/unit.src.md`
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/commands/close-unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/commands/close-unit.md
- old: 5. **Run `make check`** and report the result — it must be green before the unit counts as closed.
- new: 5. **Run `make check`** and report the result — it must be green before the unit counts as closed. If
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/commands/close-unit.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now **maintainer-guide.md** — add a rendered-units invariant and thread `unit.src.md` + `make render` through the add/update/recipe steps:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: - **Front matter** — every `course/units/NN-slug/unit.md` validates against
- new: - **Front matter** — every `course/units/NN-slug/unit.md` (generated from `unit.src.md`) validates
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: 3. **Create the unit from a template.** Copy [`unit-core.md`](../meta/templates/unit-core.md) (or
- new: 3. **Create the unit from a template.** Copy [`unit-core.md`](../meta/templates/unit-core.md) (or
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: Edit the prose, then keep its references honest: if you rename or move anything it links to, fix the
- new: Edit the prose in `unit.src.md` (never the generated `unit.md`), run `make render`, then keep its
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: the whole spec. Draft the meta entries, then the unit and lab, against the invariants above.
- new: the whole spec. Draft the meta entries, then the unit (as `unit.src.md`, then `make render`) and
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The check caught my literal `{{vd:key}}` in the maintainer-guide — `check-version-refs` scans `course/**` and tried to resolve key `key`. (That's why `stuck.md` uses `{{vd:*}}`, which doesn't match the key pattern.) I'll switch my illustrations to the angle-bracket placeholder `{{vd:<key>}}`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:key}}` tokens);
- new: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:<key>}}` version tokens);
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: is what the traceability check reads — and write version-specifics as `{{vd:key}}` tokens. Run
- new: is what the traceability check reads — and write version-specifics as `{{vd:<key>}}` tokens. Run
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Still failing — `{{vd:<key>}}` also matches the checker (it extracted key `key`). The proven-safe form in this repo is `{{vd:*}}` (what `stuck.md` uses). Let me switch to that:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:<key>}}` version tokens);
- new: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:*}}` version tokens);
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: is what the traceability check reads — and write version-specifics as `{{vd:<key>}}` tokens. Run
- new: is what the traceability check reads — and write version-specifics as `{{vd:*}}` tokens. Run
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The hook didn't fire a failure this time. Let me confirm green explicitly:

## 🤖 Assistant

**→ Bash**

```
make check >/dev/null 2>&1 && echo GREEN || { echo "FAILED"; make check 2>&1 | grep -iE 'fail|unresolved'; }
```

<details><summary>tool result</summary>

```
GREEN
```

</details>

## 🤖 Assistant

Green. **7.8 done.** Let me commit it:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add course/maintainer-guide.md meta/templates/unit-core.md meta/templates/unit-awareness.md .claude/commands/close-unit.md
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git status --short
```

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). To tell you how to proceed, the user said:
The asterisk we used in the maintainer-guide is not descriptive enough and could be misleading to the reader. It does not make sense to me why the checker would see {{vd:<key>}} as a tag when the `<` character is not a valid starting character for a keyname, right?
```

</details>

## 🤖 Assistant

Good point — let me look at the actual regex instead of guessing why `<key>` matched. Let me find the token pattern:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
grep -rnE 'vd:|VD_|re\.(compile|finditer|findall|search)' tools/check-version-refs tools/_common.py | grep -iE 'vd|\{\{|pattern|token' 
```

<details><summary>tool result</summary>

```
tools/check-version-refs:2:"""check-version-refs (R13.AC4d): every {{vd:key}} in course prose resolves to a key in
tools/check-version-refs:5:Scope: course/**/*.md only. The {{vd:key}} token is documented (illustratively) in
tools/check-version-refs:25:            rep.fail(f"{rel}: unresolved {{vd:...}} keys: {', '.join(sorted(unresolved))}")
tools/check-version-refs:26:        any_tokens = any_tokens or "{{vd:" in path.read_text(encoding="utf-8")
tools/check-version-refs:29:               + ("" if any_tokens else " (no {{vd:}} tokens authored yet)"))
tools/_common.py:11:- Version-specific values live solely in meta/version-data.yaml and are referenced as {{vd:key}};
tools/_common.py:95:# --- version-data resolution ({{vd:key}}) ----------------------------------------------------
tools/_common.py:97:VD_TOKEN_RE = re.compile(r"\{\{vd:([A-Za-z0-9_-]+)\}\}")
tools/_common.py:104:def resolve_vd(key: str, vd: dict):
tools/_common.py:105:    """Resolve a single {{vd:key}}. Returns (value, unverified) or (None, None) if unknown.
tools/_common.py:119:def render_vd(text: str, vd: dict):
tools/_common.py:120:    """Render every {{vd:key}} in `text`. Returns (rendered_text, unresolved_keys:set).
tools/_common.py:134:    return VD_TOKEN_RE.sub(repl, text), unresolved
```

</details>

## 🤖 Assistant

You're exactly right, and I misdiagnosed it. The regex is `\{\{vd:([A-Za-z0-9_-]+)\}\}` — `<` isn't a valid key char, so `{{vd:<key>}}` genuinely **cannot** match. The "key" failure I saw was actually from the *other* line in that batch: the edit-hook runs after each Edit, and at that moment step 3 still held the un-fixed literal `{{vd:key}}`. So `<key>` was fine all along. Let me switch back to the descriptive `<key>` and prove it:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:*}}` version tokens);
- new: - **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:<key>}}` version tokens);
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/course/maintainer-guide.md
- old: is what the traceability check reads — and write version-specifics as `{{vd:*}}` tokens. Run
- new: is what the traceability check reads — and write version-specifics as `{{vd:<key>}}` tokens. Run
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/course/maintainer-guide.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The edit-hook ran `make check` after both edits with no failure — confirming `{{vd:<key>}}` passes. Let me verify explicitly:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check >/dev/null 2>&1 && echo "GREEN — {{vd:<key>}} resolves clean" || { echo FAILED; make check 2>&1 | grep -iE 'fail|unresolved'; }
echo "--- the two lines ---"; grep -n 'vd:<key>' course/maintainer-guide.md
```

<details><summary>tool result</summary>

```
GREEN — {{vd:<key>}} resolves clean
--- the two lines ---
18:- **Rendered units** — each unit is **authored** as `unit.src.md` (front matter + `{{vd:<key>}}` version tokens);
51:   is what the traceability check reads — and write version-specifics as `{{vd:<key>}}` tokens. Run
```

</details>

## 🤖 Assistant

Green with the descriptive `{{vd:<key>}}` placeholder. Now let me commit 7.8:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add course/maintainer-guide.md meta/templates/unit-core.md meta/templates/unit-awareness.md .claude/commands/close-unit.md
git status --short
```

<details><summary>tool result</summary>

```
M  .claude/commands/close-unit.md
M  course/maintainer-guide.md
M  meta/templates/unit-awareness.md
M  meta/templates/unit-core.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git commit -q -F - <<'MSG'
P7 (7.8): document the unit.src.md / unit.md split in the convention docs

Teach the committed-rendered pattern wherever a maintainer is told how to
author a unit:

- meta/templates/unit-{core,awareness}.md: copy to unit.src.md (not unit.md);
  the committed unit.md is GENERATED by tools/render-units — run `make render`.
- .claude/commands/close-unit.md: authored file is unit.src.md; run `make render`
  before `make check` so the generated unit.md + index are current.
- course/maintainer-guide.md: new "Rendered units" invariant (author unit.src.md,
  never unit.md; render-units/render-index are drift-gated by make check); add-a-unit
  step 3, the update-a-unit step, and the with-Claude recipe all route through
  unit.src.md + make render.

Version tokens illustrated as `{{vd:<key>}}` (the `<` keeps it out of the
check-version-refs key charset [A-Za-z0-9_-], so it's documented, not resolved).
make check green. Branch local only.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (48.9KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/byv00bbyk.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
ecb36f9 P7 (7.8): document the unit.src.md / unit.md split in the convention docs
---
```

</details>

## 🤖 Assistant

7.8 committed (`ecb36f9`), tree clean.

## Where P7 stands
- **7.1–7.5** ✅ (findings, render infra, index, U1 pilot, gate)
- **7.6** ✅ all 16 units de-coded + committed-rendered
- **7.7** ✅ capstone files + stuck.md swept
- **7.8** ✅ convention docs teach the `unit.src.md`/`unit.md` split

Only **7.9 (close-out)** remains. It's pure state-sync — the files you audit — so here's exactly what I'd change before committing:

1. **`decisions.md`** — strike **L8** in the 🔓 ledger (mark it closed: all units + capstone files de-coded, conventions documented), and add a short P7-completion note to the "P7 — Quality pass" section.
2. **`tasks/P7-quality-pass.md`** — flip the status header and tasks 7.6/7.7/7.8/7.9 to done; the per-unit grid to all ✅. (Note: **T2** — the optional unit-dir rename — was explicitly deferred; I'll leave it as a non-blocking open item, not part of P7 close-out.)
3. **`tasks.md`** P7 index + **`IMPLEMENTATION.md` §3** — mark P7 complete.
4. Final `make check`, then a close-out commit.

Want me to do the 7.9 close-out now? And a question on scope:

## 🤖 Assistant

**→ AskUserQuestion**

```
{
  "questions": [
    {
      "question": "How should 7.9 handle the deferred T2 (unit-dir rename, e.g. 01-onboarding-first-win → 01-setup-and-first-change)?",
      "header": "T2 dir rename",
      "multiSelect": false,
      "options": [
        {
          "label": "Leave deferred (Recommended)",
          "description": "Close P7 with T2 noted as an optional, non-blocking follow-up in the ledger. Slugs are short identifiers; the index links by title; meta is slug-agnostic — so it's cosmetic."
        },
        {
          "label": "Do it now as part of P7",
          "description": "Rename the unit dirs + fix every reference (git mv, links, lab ids, tags). Larger, riskier change touching many files; would extend 7.9 well beyond close-out."
        }
      ]
    }
  ]
}
```

<details><summary>tool result</summary>

```
Your questions have been answered: "How should 7.9 handle the deferred T2 (unit-dir rename, e.g. 01-onboarding-first-win → 01-setup-and-first-change)?"="Leave deferred (Recommended)". You can now continue with these answers in mind.
```

</details>

## 🤖 Assistant

T2 stays deferred — sensible. Now the 7.9 close-out. Let me read the current state of the files I need to update:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
376	## P7 — Quality pass & learner-experience remediation (2026-05-31, in progress)
377	
378	A systematic post-v1 quality pass (8 lenses: functional run + content). The product verified
379	mechanically/functionally clean; findings confined to learner-facing prose + one version-token
380	rendering gap. **No new requirements** — every item traces to an existing R-ID; this is remediation,
381	not new scope, so requirements stay frozen and only a **design gate** (before the U2–U16 rollout)
382	applies. Task breakdown + findings + per-unit grid: [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md).
383	
384	_Format: **decision-id** — the decision; **Why:** the rationale._
385	
386	**P7-render ✅ (mechanism)** — Closed M4 (the most material finding: learners read source `unit.md`,
387	which carried 109 raw `{{vd:key}}` tokens — an R15 graceful-degradation miss). Adopted the
388	**committed-rendered pattern**: `unit.src.md` is authored (front matter + tokens), `unit.md` is
389	generated + committed (leading `GENERATED` comment, resolved prose) by new `tools/render-units`; a
390	`--check` drift gate is wired into `make check`/`check-strict`, write-mode into `make render`. Proven
391	on U1.
392	**Why:** finally realizes R12.AC2's "build step" for the *reader*, not just the author, while keeping
393	the single-source + drift guarantees. Mirrors the existing `render-checklist` generated-artifact +
394	drift-gate pattern (idiomatic for this repo). Rejected: humanizing the front matter (breaks the
395	schema/checks — R6); relocating front matter to file-bottom (our parser + GitHub table both require
396	top); a sidecar metadata file (contradicts R6, heavy). All confirmed against the parser + schema.
397	
398	**P7-garble ✅ (content bug the render exposed)** — Backticked *sentence-valued* tokens
399	(`` `{{vd:settings}}` `` / `` `{{vd:memory}}` ``) resolve a whole sentence inside inline-code →
400	garbled output, invisible while un-rendered. Fixed in U1 (those tokens were misused as noun-phrases;
401	U1 only *establishes* the baseline — the settings/memory mechanism belongs to U4). Rollout must
402	**render-and-eyeball** each unit; known sites U3:75/U3:202.
403	**Why:** rendering is what surfaced it — vindicates M4's fix doing double duty as a correctness check.
404	
405	**P7-index ✅** — Closed M5 (navigation). Generated `course/units/README.md` (new `tools/render-index`,
406	drift-gated) — a stage-grouped TOC linking each `unit.md` directly with read/lab times; top README
407	routes through it.
408	**Why:** R9.AC2 (navigable entry); a learner clicks a titled lesson and never browses the
409	`unit.md`/`unit.src.md` pair. Built from front matter so it can't drift (L2 fixes flow through).
410	
411	**P7-prose ✅ (U1 pilot) / ⏳ (rollout)** — Learner-prose ergonomics: strip spec requirement-IDs
412	(`R#`, M1 — no learner key; keep the U10 *teaching* use of `R1`/`R2.AC3`), convert bare taxonomy codes
413	to **title-only** cross-refs (M2), expand `CV` on first use (L3), light density relief (L1), recompute
414	under-declared reading times (L2, U12–U14), and the title fix (T1). Applied to U1; **gated** before
415	U2–U16.
… [+15 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
```

<details><summary>tool result</summary>

```
490	**L8 (in progress, opened 2026-05-30) — learner-prose ergonomics remediation.** Post-v1 quality
491	pass (8 lenses) found the product mechanically/functionally clean (strict gate, all lab verifiers,
492	substrates, version system, authenticity, accessibility all ✅) with findings confined to
493	learner-facing prose: M1 spec requirement-IDs (`R#`) leaking into units; M2 bare taxonomy codes
494	(`U#`/`C#`/`W#`/`CV`) used where titles read better; L1 density in some `Concept` passages; L2
495	under-declared `reading_time_min` on U12–U14; L3 unexpanded `CV`. **Not release-blocking — polish.**
496	Plus **M4 — `{{vd:key}}` tokens rendered raw to learners** (most material; an R15 graceful-degradation
497	miss): fixed with the committed-rendered pattern — authored `unit.src.md` → generated+committed
498	`unit.md` via new `tools/render-units` (drift gate in `make check`), proven on U1. Full tracker +
499	per-unit grid + rollout procedure: [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md) (+ P7
500	rationale section above). _Status (2026-05-31, WIP checkpoint committed on `spec/quality-pass-phase`):_ gate
501	approved; **U1–U4 fully de-coded + migrated**; **U5–U16 have link-anchors + advances-tails
502	auto-de-coded by script but are not migrated and prose codes remain**. `make check` green. _Resolve
503	in:_ the editorial roll-out — **next session starts at `tasks/P7-quality-pass.md` → "Resume state"**
504	(7.6 U5–U16 prose, 7.7 cross-cutting sweep, 7.8 convention docs, 7.9 close-out).
```

</details>

## 🤖 Assistant

Now the close-out edits. Starting with **decisions.md** — strike L8 and mark the P7 section complete:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: ## P7 — Quality pass & learner-experience remediation (2026-05-31, in progress)
- new: ## P7 — Quality pass & learner-experience remediation (2026-05-31, COMPLETE)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **P7-process ✅** — This phase was **retro-fitted into the spec methodology**: the freelance
- new: **P7-process ✅** — This phase was **retro-fitted into the spec methodology**: the freelance
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now strike the **L8 ledger entry**:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **L8 (in progress, opened 2026-05-30) — learner-prose ergonomics remediation.** Post-v1 quality
- new: **~~L8~~ — ✅ CLOSED (P7, 2026-05-31).** Learner-prose ergonomics remediation complete. The post-v1
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the **P7 task file** — let me re-read its status header, task checkboxes, and grid:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
1	# P7 — Quality pass & learner-experience remediation
2	
3	**Goal:** a systematic post-v1 quality pass (8 lenses) and the remediation of what it found. The
4	product was verified **mechanically and functionally clean**; findings are confined to learner-facing
5	prose ergonomics and one version-token rendering gap. **Polish + gap-closure — not release-blocking.**
6	
7	**Status:** 🚧 **IN PROGRESS (2026-05-31).** Gate **approved** (pattern + U1 voice). **U1–U4 fully
8	done** (migrated to `unit.src.md` + rendered; prose de-coded; garbles fixed). **U5–U16: link anchors
9	+ `advances \`C#\`` tails already auto-de-coded by script — do NOT redo; but units are NOT migrated
10	and prose codes remain.** `make check` green. Work is a WIP checkpoint commit on branch
11	`spec/quality-pass-phase`. **NEXT SESSION: start at "## Resume state" below.** No new requirements.
12	
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
70	      (incl. title-only cross-refs; "your first unit" for U1 back-refs). Rollout unblocked.
71	
72	### 7.6 Roll out to U2–U16 [R5/R6/R15] — 🚧 IN PROGRESS (U1–U4 done; U5–U16 partial)
73	Per-unit procedure (render-and-read, not a mechanical `git mv` — see Resume state for the recipe):
74	- [x] **U2** ✅ · **U3** ✅ (settings/permission-modes/checkpoint-rewind garbles fixed) · **U4** ✅
75	- [ ] U5 · U6 · U7 · U8 — prose codes remain (links+advances auto-done)
76	- [ ] U9 · U10 (keep the teaching `R1`/`R2.AC3`/`R1`–`R15`; strip breadcrumb `R3.AC2`/`R7.AC3`) · U11
77	- [ ] U12 (L2 rt 8→10) · U13 (L2 rt 8→12) · U14 (L2 rt 8→11) · U15 · U16
78	
79	### 7.7 Cross-cutting prose sweep — ⏳ PENDING GATE
80	- [ ] `course/capstone/{README,briefs,rubric,case-study}.md`, `course/stuck.md` — same M1/M2 sweep
81	      with judgment (keep load-bearing rubric `[Cn]` tags). Maintainer-guide may legitimately keep `R#`.
82	
83	### 7.8 Convention docs for the unit.src.md split — ⏳ PENDING GATE
84	- [ ] Update `course/maintainer-guide.md`, `meta/templates/unit-*.md`, and the `close-unit` skill:
85	      authored file is `unit.src.md`; `make render` regenerates `unit.md`.
86	
87	### 7.9 Close-out
88	- [ ] `make check` green; reading times recomputed; clean commits on a branch; L8 struck in
89	      `decisions.md`; `tasks.md` P7 + `IMPLEMENTATION.md` §3 marked complete.
90	
91	## Per-unit grid
92	
93	Legend: ✅ done · 🔗 link-anchors+advances auto-de-coded (script) · ⬜ prose codes + migration pending.
94	
95	| Unit | state | notes for the prose pass |
96	|------|-------|--------------------------|
97	| U1 onboarding        | ✅ | pilot |
98	| U2 explore           | ✅ | |
99	| U3 operate-safely    | ✅ | settings/permission-modes/checkpoint-rewind garbles fixed |
100	| U4 memory-context    | ✅ | home unit for memory/settings — tokens taught here (sentence-position) |
101	| U5 ship-feature      | 🔗⬜ | `**The workflow — W1.**`→`**The workflow.**`; CV expand; bare U1/U2/U4/U10 prose refs |
102	| U6 tdd               | 🔗⬜ | `**The workflow — W2.**`; CV; U5/U7 prose refs |
103	| U7 debug             | 🔗⬜ | `**The workflow — W3.**`; CV; U5/U6/U9 prose; "the W2 reflex" |
104	| U8 git-pr            | 🔗⬜ | `**The workflow — W4.**`; CV; U5–U7/U9/U16 prose; R7.AC3/AC7/AC8 breadcrumbs |
105	| U9 legacy-refactor   | 🔗⬜ | W8/W5 in prose; CV; U2/U5/U7/U8 prose; R7.AC3 |
106	| U10 spec-driven      | 🔗⬜ | **KEEP teaching** `R1`/`R2.AC3`/`R1`–`R15`; strip breadcrumb R3.AC2/R7.AC3; W7; U5/U11 prose; CV |
107	| U11 review           | 🔗⬜ | L11 "advances `C12` and consolidates `CV`" (irregular); CV ×3; W6; U3/U5/U6/U10/U12/U16 prose; R7.AC3 |
108	| U12 commands-skills  | 🔗⬜ | L9–10 "Advances\n`C13`" (multi-line, not auto-removed); R14/R7.AC3; U13 prose; **L2 rt 8→10** |
109	| U13 subagents        | 🔗⬜ | "the U12 line"; R7.AC3; **L2 rt 8→12** |
… [+3 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Updating the **P7 task file** — status header, the four task sections, and the grid:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: **Status:** 🚧 **IN PROGRESS (2026-05-31).** Gate **approved** (pattern + U1 voice). **U1–U4 fully
- new: **Status:** ✅ **COMPLETE (2026-05-31).** Gate approved; the full editorial rollout landed. **All 16
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: ### 7.6 Roll out to U2–U16 [R5/R6/R15] — 🚧 IN PROGRESS (U1–U4 done; U5–U16 partial)
- new: ### 7.6 Roll out to U2–U16 [R5/R6/R15] — ✅ DONE (all 16 units)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: ### 7.7 Cross-cutting prose sweep — ⏳ PENDING GATE
- new: ### 7.7 Cross-cutting prose sweep — ✅ DONE
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the **per-unit grid** — flip U5–U16 to ✅:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: | U5 ship-feature      | 🔗⬜ | `**The workflow — W1.**`→`**The workflow.**`; CV expand; bare U1/U2/U4/U10 prose refs |
- new: | U5 ship-feature      | ✅ | workflow header + CV + U1/U2/U4/U10 refs de-coded; `thinking` token garble fixed |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now **tasks.md** P7 index and **IMPLEMENTATION.md §3**. Let me locate the P7 lines:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== tasks.md P7 lines ==="; grep -nE 'P7|quality.pass|🚧' specs/claude-code-mastery/tasks.md | head -20
```

<details><summary>tool result</summary>

```
=== tasks.md P7 lines ===
7:Definition-of-Done mechanical gate (L3) passes. **P7 (Quality pass) 🚧 IN PROGRESS (2026-05-31)** —
126:### P7 — Quality pass & learner-experience remediation 🚧 **IN PROGRESS (2026-05-31)**  → [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md)
127:Post-v1 quality pass (8 lenses). Mechanically/functionally clean; findings confined to learner-facing
129:`decisions.md` → "P7 — Quality pass".
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
5	**Status:** v1 ✅ **COMPLETE (2026-05-30)** — P1 (Design) ✅, P2 (Scaffolding) ✅, P3 (Tooling) ✅,
6	P4 (Codebases) ✅, P5 (Units) ✅, **P6 (Finalization) ✅**. `make check-strict` green — the v1
7	Definition-of-Done mechanical gate (L3) passes. **P7 (Quality pass) 🚧 IN PROGRESS (2026-05-31)** —
8	post-v1 learner-experience remediation; no new requirements. Remaining non-release-blocking (**L1**
9	in-REPL version-key refresh; commit/push + CI). Open loops & deferrals are tracked in `decisions.md`
10	→ "Open loops & deferrals 🔓" (the canonical ledger).
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
126	### P7 — Quality pass & learner-experience remediation 🚧 **IN PROGRESS (2026-05-31)**  → [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md)
127	Post-v1 quality pass (8 lenses). Mechanically/functionally clean; findings confined to learner-facing
128	prose + a version-token rendering gap. **No new requirements** (traces to R5/R6/R9/R12/R15). See
129	`decisions.md` → "P7 — Quality pass".
130	- [x] Findings & triage (8-lens report)
131	- [x] Version-token **committed-rendered** pattern — `tools/render-units` + `{{vd}}` drift gate; U1 migrated [R12.AC2/R15]
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
```

<details><summary>tool result</summary>

```
130	- [x] Findings & triage (8-lens report)
131	- [x] Version-token **committed-rendered** pattern — `tools/render-units` + `{{vd}}` drift gate; U1 migrated [R12.AC2/R15]
132	- [x] Navigation **units index** — `tools/render-index` → `course/units/README.md`; README routes through it [R9.AC2]
133	- [x] U1 **pilot** prose — strip `R#` (M1), title-only cross-refs (M2), expand `CV` (L3), light density (L1), title (T1) [R5/R6]
134	- [ ] **GATE:** user approves pattern + rollout procedure + U1 voice (before U2–U16)
135	- [ ] Roll out U2–U16 (render-migrate + prose; fix `{{vd:settings}}` garble at U3) [R5/R6/R15]
136	- [ ] Cross-cutting prose sweep (capstone, stuck); reading-time recompute (L2, U12–U14) [R5.AC6]
137	- [ ] Convention docs for the `unit.src.md` split (maintainer-guide, templates, `close-unit`); final green + clean commits
138	
```

</details>

## 🤖 Assistant

Now let me update the tasks.md P7 status line, the P7 section header, and the P7 checklist:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: Definition-of-Done mechanical gate (L3) passes. **P7 (Quality pass) 🚧 IN PROGRESS (2026-05-31)** —
- new: Definition-of-Done mechanical gate (L3) passes. **P7 (Quality pass) ✅ COMPLETE (2026-05-31)** —
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: ### P7 — Quality pass & learner-experience remediation 🚧 **IN PROGRESS (2026-05-31)**  → [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md)
- new: ### P7 — Quality pass & learner-experience remediation ✅ **COMPLETE (2026-05-31)**  → [`tasks/P7-quality-pass.md`](./tasks/P7-quality-pass.md)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md
- old: - [ ] **GATE:** user approves pattern + rollout procedure + U1 voice (before U2–U16)
- new: - [x] **GATE:** user approved pattern + rollout procedure + U1 voice (before U2–U16)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Finally **IMPLEMENTATION.md §3** — the live status dashboard. Let me re-read the P7 lines to edit precisely:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
```

<details><summary>tool result</summary>

```
37	| Phase | Status |
38	|---|---|
39	| 1. Requirements (`requirements.md`) | ✅ **APPROVED** (2026-05-29) — turn-by-turn review; gap-free IDs |
40	| 2. Design (`design.md`) | ✅ **APPROVED & merged to `main`** (2026-05-29) — §0–§11; design gate passed |
41	| 3. Tasks (`tasks.md`) | ✅ v1 **COMPLETE** (2026-05-30) — P1–P6 executed; `make check-strict` green. 🚧 **P7 (Quality pass)** in progress (2026-05-31) |
42	| Rationale (`decisions.md`) | ✅ Per-phase decisions + the canonical 🔓 open-loops ledger |
43	
44	**Phase 3 (Tasks) breakdown:** P1 ✅ · P2 ✅ · P3 ✅ · P4 ✅ (both lab codebases built; `SEEDED.md`
45	inventory + offline mock) · **P5 ✅ — all 16 units (U1–U16) authored; every can-do C1–C17+CV practiced
46	by ≥1 lab** · **P6 ✅ — capstone (briefs/exemplar/rubric), build case study + transparency note,
47	maintainer guide, README finalized, `tools/render-checklist` added; `make check-strict` green = the
48	v1 Definition-of-Done mechanical gate (L3) passes.** Current branch: **`main`** (P6 committed).
49	
50	**P7 — Quality pass (post-v1, in progress, 2026-05-31).** A systematic 8-lens quality pass found the
51	product mechanically/functionally clean; remediation is confined to learner-facing prose + a closed
52	version-token rendering gap (new `tools/render-units` committed-rendered pattern + `tools/render-index`
53	navigation). **No new requirements** (traces to R5/R6/R9/R12/R15). Gate approved; **U1–U4 done** (migrated +
54	de-coded); **U5–U16 partially auto-de-coded (links + advances tails), prose + migration pending** —
55	WIP checkpoint committed on branch `spec/quality-pass-phase`. **Next session: `tasks/P7-quality-pass.md` →
56	"Resume state".** See also `decisions.md` → "P7 — Quality pass". Tracked as open loop **L8**.
57	
58	**v1 build is complete.** Remaining is **not release-blocking**: **L1** is now mostly closed — the
59	interactive `/help`+docs pass (2026-05-30) verified 5 of the 7 keys; only `ci` (GitHub Action wrapper)
60	and `managed-settings` (enterprise) stay `unverified`, each blocked by access this environment lacks
61	(Gitea instead of GitHub Actions; no enterprise account). See the 🔓 ledger in `decisions.md`.
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: | 3. Tasks (`tasks.md`) | ✅ v1 **COMPLETE** (2026-05-30) — P1–P6 executed; `make check-strict` green. 🚧 **P7 (Quality pass)** in progress (2026-05-31) |
- new: | 3. Tasks (`tasks.md`) | ✅ v1 **COMPLETE** (2026-05-30) — P1–P6 executed; `make check-strict` green. ✅ **P7 (Quality pass) COMPLETE** (2026-05-31) |
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: **P7 — Quality pass (post-v1, in progress, 2026-05-31).** A systematic 8-lens quality pass found the
- new: **P7 — Quality pass (post-v1, ✅ COMPLETE 2026-05-31).** A systematic 8-lens quality pass found the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

All four state files updated. The P7 task file still has a "Resume state (NEXT SESSION — START HERE)" section that's now stale — let me mark it superseded so it can't mislead a future reader:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
grep -n '## Resume state' specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
126:## Resume state (NEXT SESSION — START HERE)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: ## Resume state (NEXT SESSION — START HERE)
- new: ## Resume state (⚠️ SUPERSEDED — P7 is complete; kept for historical reference)
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify everything's still green and commit the 7.9 close-out:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
echo "--- residual 'in progress' / open L8 in synced files ---"
grep -rniE 'L8.*in progress|P7.*in progress|🚧.*P7' specs/claude-code-mastery/IMPLEMENTATION.md specs/claude-code-mastery/tasks.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks/P7-quality-pass.md || echo "none — all marked complete"
echo "--- git status ---"; git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
--- residual 'in progress' / open L8 in synced files ---
none — all marked complete
--- git status ---
 M specs/claude-code-mastery/IMPLEMENTATION.md
 M specs/claude-code-mastery/decisions.md
 M specs/claude-code-mastery/tasks.md
 M specs/claude-code-mastery/tasks/P7-quality-pass.md
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add specs/claude-code-mastery/IMPLEMENTATION.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md specs/claude-code-mastery/tasks/P7-quality-pass.md
git commit -q -F - <<'MSG'
P7 (7.9): close-out — mark P7 complete, strike L8

State-sync to finish the quality pass:
- decisions.md: P7 section → COMPLETE; new P7-rollout entry; L8 struck in the
  🔓 ledger (all 16 units de-coded + migrated, capstone/stuck swept, convention
  docs updated; kept rubric [Cn]/[CV] tags, U10 teaching R-IDs, case-study R1–R15).
- tasks/P7-quality-pass.md: status → COMPLETE; 7.6–7.9 checked; per-unit grid all
  ✅ (with the garble-fix notes); Resume-state section marked superseded.
- tasks.md: P7 index + top status line → COMPLETE.
- IMPLEMENTATION.md §3: P7 → COMPLETE.

Sole remaining follow-up is T2 (optional unit-dir rename), deferred — non-blocking.
make check green. Branch spec/quality-pass-phase, local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -8 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). To tell you how to proceed, the user said:
before we close out I'd like to revisit the navigation flow in this quality pass. I want to add navigation breadcrumbs in the units that allow you to navigate back to their parent pages all the way to the main readme. Sorry for the churn.
```

</details>

## 🤖 Assistant

No problem at all — better to get the navigation right before closing. Let me look at the current nav structure (root README, units index, a rendered unit head) so I can propose a concrete breadcrumb design:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/course/units/README.md
```

<details><summary>tool result</summary>

```
1	<!-- GENERATED from each unit's front matter by tools/render-index — do not hand-edit. Run `make render`. -->
2	
3	# Course units
4	
5	The 16 units, in the default order. Each is self-contained; skim a unit's **Skip-check** and skip deliberately if you already know it. Track yourself on the [progress checklist](../progress-checklist.md); finish with the [capstone](../capstone/).
6	
7	## First Wins
8	
9	| # | Unit | Read | Lab |
10	|---|------|------|-----|
11	| 1 | [Set up Claude Code and make your first verified change](./01-onboarding-first-win/unit.md) | 8 min | 15 min |
12	| 2 | [Explore and explain an unfamiliar codebase](./02-explore-a-codebase/unit.md) | 8 min | 20 min |
13	| 3 | [Operate safely while letting Claude act on your code](./03-operate-safely/unit.md) | 10 min | 20 min |
14	| 4 | [Steer Claude with project memory and deliberate context](./04-memory-and-context/unit.md) | 9 min | 18 min |
15	
16	## Daily Driver
17	
18	| # | Unit | Read | Lab |
19	|---|------|------|-----|
20	| 5 | [Ship a feature end-to-end with explore → plan → code → commit](./05-ship-a-feature/unit.md) | 10 min | 25 min |
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== root README head ==="; sed -n '1,8p' README.md
echo "=== render-units: how it builds output ==="; sed -n '26,75p' tools/render-units
```

<details><summary>tool result</summary>

```
=== root README head ===
# Claude Code Mastery

A self-paced, hands-on course that takes a **seasoned developer who is new to AI-assisted coding**
to a fluent, elite Claude Code practitioner — someone who picks the right workflow and feature for
each real job, and who **verifies** Claude's output rather than trusting it.

The course is **outcome-driven** (organized around real use cases, not a feature tour), **tiered**
for experienced engineers (it won't teach you Git or the terminal), and **version-resilient** (it
=== render-units: how it builds output ===
)
LEADING_COMMENT_RE = re.compile(r"^<!--.*?-->\s*", re.DOTALL)


def sources():
    if not UNITS.exists():
        return []
    return sorted(UNITS.glob("*/unit.src.md"))


def render_source(src, vd):
    """Return (generated_text, unresolved_keys). Strips any leading source comment and prepends
    the GENERATED header, so editing unit.md directly is always caught as drift."""
    text = LEADING_COMMENT_RE.sub("", src.read_text(encoding="utf-8"), count=1)
    rendered, unresolved = render_vd(text, vd)
    return HEADER + rendered, unresolved


def main(argv):
    check = "--check" in argv
    rep = Reporter("render-units")
    vd = load_version_data()
    srcs = sources()

    if not srcs:
        rep.ok("no unit.src.md sources yet — nothing to render")
        return rep.done()

    for src in srcs:
        out = src.with_name("unit.md")
… [+20 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Clear structure: the chain is **Claude Code Mastery** (root README) › **Course units** (index) › the unit. Since units are committed-rendered, the right move — consistent with how the index itself is generated — is to **inject the breadcrumb in `render-units`** (DRY, drift-gated, automatic for all 16 + any future unit) rather than hand-author it into 16 `unit.src.md` files. Let me confirm `_common` can read the title from front matter:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
grep -nE 'def .*front|front_matter|def parse|title|yaml|---' tools/_common.py | head -25
```

<details><summary>tool result</summary>

```
11:- Version-specific values live solely in meta/version-data.yaml and are referenced as {{vd:key}};
21:import yaml
24:# --- repo layout -----------------------------------------------------------------------------
43:def load_yaml(path: Path):
45:        return yaml.safe_load(fh)
60:    """Yield text-ish files (md/yaml/json/py/sh/toml/yml/cfg/ini) under roots."""
61:    exts = {".md", ".yaml", ".yml", ".json", ".py", ".sh", ".toml", ".cfg", ".ini", ".txt"}
72:# --- unit front matter -----------------------------------------------------------------------
74:FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
77:def parse_frontmatter(path: Path):
85:    return yaml.safe_load(m.group(1))
95:# --- version-data resolution ({{vd:key}}) ----------------------------------------------------
101:    return load_yaml(META / "version-data.yaml")
137:# --- reporting -------------------------------------------------------------------------------
```

</details>

## 🤖 Assistant

`_common` has `parse_frontmatter` + `FRONTMATTER_RE`, so generation is straightforward. The unit breadcrumb will link directly to both parents, so a unit reaches the root README in one click. Before I implement, one visible-format choice:

## 🤖 Assistant

**→ AskUserQuestion**

```
{
  "questions": [
    {
      "question": "Breadcrumb format to generate at the top of each unit (injected by render-units, above the H1)?",
      "header": "Crumb format",
      "multiSelect": false,
      "options": [
        {
          "label": "Ancestors only (Recommended)",
          "description": "Two up-links; the H1 right below is the current page. Cleanest, never wraps awkwardly on long titles.",
          "preview": "[Claude Code Mastery](../../../README.md) › [Course units](../README.md)\n\n# Ship a feature end-to-end with explore → plan → code → commit"
        },
        {
          "label": "Include current page",
          "description": "Full trail ending in the unit's (often long) title as plain text. More explicit but can wrap.",
          "preview": "[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Ship a feature end-to-end with explore → plan → code → commit\n\n# Ship a feature end-to-end with explore → plan → code → commit"
        }
      ]
    },
    {
      "question": "Scope — also add an up-link on the generated units index (course/units/README.md → root README) so the chain is symmetric?",
      "header": "Index up-link",
      "multiSelect": false,
      "options": [
        {
          "label": "Yes, add index up-link (Recommended)",
          "description": "render-index also emits a '‹ Claude Code Mastery' link atop the units index. Completes the up-navigation at every level.",
          "preview": "[‹ Claude Code Mastery](../../README.md)\n\n# Course units"
        },
        {
          "label": "Units only",
          "description": "Just the unit breadcrumbs. The unit already links straight to the root README, so 'all the way up' still works; the index keeps its existing links."
        }
      ]
    }
  ]
}
```

<details><summary>tool result</summary>

```
Your questions have been answered: "Breadcrumb format to generate at the top of each unit (injected by render-units, above the H1)?"="Ancestors only (Recommended)" selected preview:
[Claude Code Mastery](../../../README.md) › [Course units](../README.md)

# Ship a feature end-to-end with explore → plan → code → commit, "Scope — also add an up-link on the generated units index (course/units/README.md → root README) so the chain is symmetric?"="Yes, add index up-link (Recommended)" selected preview:
[‹ Claude Code Mastery](../../README.md)

# Course units. You can now continue with these answers in mind.
```

</details>

## 🤖 Assistant

Both confirmed. Let me implement — first `render-units` to inject the breadcrumb. Let me see its header constants and imports:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/tools/render-units
```

<details><summary>tool result</summary>

```
20	sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
21	from _common import ROOT, UNITS, Reporter, load_version_data, render_vd  # noqa: E402
22	
23	HEADER = (
24	    "<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. "
25	    "Edit unit.src.md, then run `make render`. -->\n"
26	)
27	LEADING_COMMENT_RE = re.compile(r"^<!--.*?-->\s*", re.DOTALL)
28	
29	
30	def sources():
31	    if not UNITS.exists():
32	        return []
33	    return sorted(UNITS.glob("*/unit.src.md"))
34	
35	
36	def render_source(src, vd):
37	    """Return (generated_text, unresolved_keys). Strips any leading source comment and prepends
38	    the GENERATED header, so editing unit.md directly is always caught as drift."""
39	    text = LEADING_COMMENT_RE.sub("", src.read_text(encoding="utf-8"), count=1)
40	    rendered, unresolved = render_vd(text, vd)
41	    return HEADER + rendered, unresolved
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/tools/render-units
- old: sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
- new: sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/tools/render-units has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/tools/render-units
- old: def render_source(src, vd):
- new: def render_source(src, vd):
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/tools/render-units has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now `render-index` — add the index up-link. Let me find where it builds the header:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
grep -nE 'GENERATED|# Course units|HEADER|lines\.append|out\.|"""|def ' tools/render-index | head -30
```

<details><summary>tool result</summary>

```
2:"""render-index: generate course/units/README.md — the learner-facing table of contents.
8:"""
23:HEADER = (
24:    "<!-- GENERATED from each unit's front matter by tools/render-index — do not hand-edit. "
29:def unit_num(uid: str) -> int:
34:def build() -> str:
52:    out = [HEADER, "# Course units\n"]
53:    out.append(
62:        out.append(f"## {stage_label}\n")
63:        out.append("| # | Unit | Read | Lab |")
64:        out.append("|---|------|------|-----|")
66:            out.append(f"| {num} | [{title}](./{slug}/unit.md) | {read} min | {lab} min |")
67:        out.append("")
71:def main(argv):
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/tools/render-index
```

<details><summary>tool result</summary>

```
52	    out = [HEADER, "# Course units\n"]
53	    out.append(
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/tools/render-index
- old: out = [HEADER, "# Course units\n"]
- new: out = [HEADER, "[‹ Claude Code Mastery](../../README.md)\n", "# Course units\n"]
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/tools/render-index has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now regenerate everything and check, then eyeball a unit head and the index head:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make render >/dev/null 2>&1 && make check >/dev/null 2>&1 && echo "GREEN" || { echo FAILED; make check 2>&1 | grep -iE 'fail|unresolved' | head; }
echo "=== U5 head (rendered) ==="; sed -n '1,18p' course/units/05-ship-a-feature/unit.md
echo "=== units index head ==="; sed -n '1,5p' course/units/README.md
```

<details><summary>tool result</summary>

```
GREEN
=== U5 head (rendered) ===
<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U5
title: "Ship a feature end-to-end with explore → plan → code → commit"
stage: daily-driver
depth_tier: core
use_case: "Ship a new feature in taskflow-api"
can_do: [C6]
workflows: [W1]
coverage_areas: [9, 10]
prerequisites: [U2, U4]
reading_time_min: 10
lab_time_min: 25
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md)

# Ship a feature end-to-end with explore → plan → code → commit
=== units index head ===
<!-- GENERATED from each unit's front matter by tools/render-index — do not hand-edit. Run `make render`. -->

[‹ Claude Code Mastery](../../README.md)

# Course units
```

</details>

## 🤖 Assistant

Both render correctly. Let me confirm all 16 units got the breadcrumb and the new link targets resolve:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "units with breadcrumb: $(grep -l '› \[Course units\](../README.md)' course/units/*/unit.md | wc -l) / 16"
echo "index up-link present: $(grep -c '‹ Claude Code Mastery' course/units/README.md)"
echo "--- confirm link-check covered the new targets ---"
make check 2>&1 | grep -E 'README.md -> \.\./(\.\./\.\./)?README.md|check-links: OK' | head
```

<details><summary>tool result</summary>

```
units with breadcrumb: 16 / 16
index up-link present: 1
--- confirm link-check covered the new targets ---
check-links: OK
```

</details>

## 🤖 Assistant

All 16 units carry the breadcrumb, the index has its up-link, and links resolve. Let me record this navigation enhancement in the trackers (it extends M5), then commit. First the P7 task file's navigation task:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
61	      `unit.md`, read/lab times) from front matter; `--check` drift gate in `make check`.
62	- [x] Top README "How it's structured" + "How to start" route through the index.
63	
64	### 7.4 U1 pilot prose [R5/R6/R15] — ✅ DONE
65	- [x] M1 (drop `R#`), M2 (codes→titles, title-only), L3 (`CV` expanded), light L1; title T1 fixed.
66	- [x] Fixed the backticked-`{{vd:settings}}` garble surfaced by rendering.
67	
68	### 7.5 GATE — design approval before rollout — ✅ APPROVED (2026-05-31)
```

</details>

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
```

<details><summary>tool result</summary>

```
59	### 7.3 Navigation index [R9.AC2] — ✅ DONE
60	- [x] `tools/render-index`: generates `course/units/README.md` (stage-grouped TOC linking each
61	      `unit.md`, read/lab times) from front matter; `--check` drift gate in `make check`.
62	- [x] Top README "How it's structured" + "How to start" route through the index.
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: ### 7.3 Navigation index [R9.AC2] — ✅ DONE
- new: ### 7.3 Navigation index + breadcrumbs [R9.AC2] — ✅ DONE
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: **P7-index ✅** — Closed M5 (navigation). Generated `course/units/README.md` (new `tools/render-index`,
- new: **P7-index ✅** — Closed M5 (navigation). Generated `course/units/README.md` (new `tools/render-index`,
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Let me check make check is still green and review what's changed before the two commits:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
echo "--- changed files ---"; git status --short
```

<details><summary>tool result</summary>

```
CHECK GREEN
--- changed files ---
 M course/units/01-onboarding-first-win/unit.md
 M course/units/02-explore-a-codebase/unit.md
 M course/units/03-operate-safely/unit.md
 M course/units/04-memory-and-context/unit.md
 M course/units/05-ship-a-feature/unit.md
 M course/units/06-tdd/unit.md
 M course/units/07-debug-a-failure/unit.md
 M course/units/08-git-and-pr/unit.md
 M course/units/09-onboard-refactor-legacy/unit.md
 M course/units/10-spec-driven-dev/unit.md
 M course/units/11-code-and-security-review/unit.md
 M course/units/12-commands-and-skills/unit.md
 M course/units/13-subagents/unit.md
 M course/units/14-hooks/unit.md
 M course/units/15-mcp-and-vetting/unit.md
 M course/units/16-automate-and-scale/unit.md
 M course/units/README.md
 M specs/claude-code-mastery/IMPLEMENTATION.md
 M specs/claude-code-mastery/decisions.md
 M specs/claude-code-mastery/tasks.md
 M specs/claude-code-mastery/tasks/P7-quality-pass.md
 M tools/render-index
 M tools/render-units
```

</details>

## 🤖 Assistant

Commit 1 — the breadcrumb feature (tools + regenerated units/index):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add tools/render-units tools/render-index course/units
git commit -q -F - <<'MSG'
P7: add up-navigation breadcrumbs (units + index up-link)

Every learner-facing page can now climb back to the course root:
- tools/render-units injects "[Claude Code Mastery](../../../README.md) ›
  [Course units](../README.md)" after the front matter, above each unit's H1.
  Generated (not authored) so all 16 units — and any future one — get it for
  free; the render drift gate in `make check` keeps it consistent.
- tools/render-index adds a matching "[‹ Claude Code Mastery]" up-link atop
  course/units/README.md.

All 16 unit.md + the index regenerated via `make render`. check-links confirms
the new relative targets resolve. make check green.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (51KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bxzpovooa.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -1
```

<details><summary>tool result</summary>

```
965ce81 P7: add up-navigation breadcrumbs (units + index up-link)
```

</details>

## 🤖 Assistant

Commit 2 — the 7.9 close-out (state files, now including the breadcrumb mentions):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add specs/claude-code-mastery/IMPLEMENTATION.md specs/claude-code-mastery/decisions.md specs/claude-code-mastery/tasks.md specs/claude-code-mastery/tasks/P7-quality-pass.md
git commit -q -F - <<'MSG'
P7 (7.9): close-out — mark P7 complete, strike L8

State-sync to finish the quality pass:
- decisions.md: P7 section → COMPLETE; new P7-rollout entry; P7-index extended
  with the up-navigation breadcrumbs; L8 struck in the 🔓 ledger (all 16 units
  de-coded + migrated, capstone/stuck swept, convention docs updated, breadcrumbs
  added; kept rubric [Cn]/[CV] tags, U10 teaching R-IDs, case-study R1–R15).
- tasks/P7-quality-pass.md: status → COMPLETE; 7.3 records breadcrumbs; 7.6–7.9
  checked; per-unit grid all ✅; Resume-state section marked superseded.
- tasks.md: P7 index + top status line → COMPLETE.
- IMPLEMENTATION.md §3: P7 → COMPLETE.

Sole remaining follow-up is T2 (optional unit-dir rename), deferred — non-blocking.
make check green. Branch spec/quality-pass-phase, local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -6 && echo "---" && git status --short
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (51.4KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/b5lzmayzo.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
git log --oneline -6 && echo "---" && git status --short && echo "(clean if nothing listed)"
```

<details><summary>tool result</summary>

```
c9484aa P7 (7.9): close-out — mark P7 complete, strike L8
965ce81 P7: add up-navigation breadcrumbs (units + index up-link)
ecb36f9 P7 (7.8): document the unit.src.md / unit.md split in the convention docs
cfd04ec P7 (7.7): cross-cutting prose sweep — capstone files + stuck.md
60dfd69 P7: roll learner-prose remediation through U15–U16 — completes 7.6 (all 16 units)
ed66fe8 P7: roll learner-prose remediation through U9–U14 (migrate + de-code)
---
(clean if nothing listed)
```

</details>

## 🤖 Assistant

Done — **P7 is complete.** Both commits landed and the tree is clean.

## P7 — Quality pass: closed out ✅

**This session** took P7 from "U1–U4 done" to fully complete:
- **7.6** — de-coded + migrated **all of U5–U16** to the committed-rendered pattern (the per-unit render-and-eyeball caught the predicted multi-clause `{{vd:*}}` garbles — `test-run`, `git-pr`, `subagents`, `hooks`, `mcp`/`plugins`, `headless`/`ci`/`worktrees` — each repositioned to sentence position; L2 reading-time bumps on U12/U13/U14).
- **7.7** — swept the capstone files + `stuck.md` (kept the load-bearing rubric `[Cn]`/`[CV]` tags, U10's teaching R-IDs, and case-study's descriptive `R1–R15`).
- **7.8** — taught the `unit.src.md`/`unit.md` split in the maintainer-guide, both templates, and `close-unit`.
- **Navigation breadcrumbs** (your add) — `render-units` now injects `Claude Code Mastery › Course units` above every unit's H1, and `render-index` adds a matching `‹ Claude Code Mastery` up-link atop the index. Generated, so it's DRY, drift-gated, and free for future units.
- **7.9** — struck **L8**; marked P7 complete in `decisions.md`, `tasks.md`, `IMPLEMENTATION.md §3`, and the P7 task file.

`make check` green throughout. Commits this session: U5–U8, U9–U14, U15–U16, 7.7, 7.8, breadcrumbs, 7.9 close-out — all on `spec/quality-pass-phase`.

## State of play
- **Branch `spec/quality-pass-phase` is local only — not pushed/merged.** Per your standing rule I won't push without a go-ahead. When you're ready, the options are: push the branch, or merge it to `main` (it's a clean, self-contained P7).
- **Remaining, non-blocking:** **T2** (optional unit-dir rename, deliberately deferred) and **L1** (the `ci`/`managed-settings` version keys that need GitHub-Actions/enterprise access this env lacks).

Want me to push the branch (or open a PR / merge to `main`), or leave it local?

## 🧑 User

Push to the branch only

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== remotes ==="; git remote -v
echo "=== current branch + upstream ==="; git rev-parse --abbrev-ref HEAD; git rev-parse --abbrev-ref --symbolic-full-name '@{u}' 2>/dev/null || echo "(no upstream set)"
echo "=== unpushed commits ==="; git log --oneline @{u}..HEAD 2>/dev/null || git log --oneline -10
```

<details><summary>tool result</summary>

```
=== remotes ===
origin	git@gitea.marlow.home:marlow/claude-training.git (fetch)
origin	git@gitea.marlow.home:marlow/claude-training.git (push)
=== current branch + upstream ===
spec/quality-pass-phase
(no upstream set)
=== unpushed commits ===
c9484aa P7 (7.9): close-out — mark P7 complete, strike L8
965ce81 P7: add up-navigation breadcrumbs (units + index up-link)
ecb36f9 P7 (7.8): document the unit.src.md / unit.md split in the convention docs
cfd04ec P7 (7.7): cross-cutting prose sweep — capstone files + stuck.md
60dfd69 P7: roll learner-prose remediation through U15–U16 — completes 7.6 (all 16 units)
ed66fe8 P7: roll learner-prose remediation through U9–U14 (migrate + de-code)
f18ed18 P7: roll learner-prose remediation through U5–U8 (migrate + de-code)
8e9f477 Add quality-pass-session-1 log
0d35846 P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
79ba027 P7: committed-rendered units + navigation index (U1 pilot)
```

</details>

## 🤖 Assistant

Remote is `origin` (Gitea), no upstream set yet. Pushing the branch and setting upstream:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git push -u origin spec/quality-pass-phase 2>&1
```

<details><summary>tool result</summary>

```
remote: 
remote: Create a new pull request for 'spec/quality-pass-phase':        
remote:   https://gitea.marlow.home/marlow/claude-training/pulls/new/spec/quality-pass-phase        
remote: 
remote: . Processing 1 references        
remote: Processed 1 references in total        
To gitea.marlow.home:marlow/claude-training.git
   8e9f477..c9484aa  spec/quality-pass-phase -> spec/quality-pass-phase
branch 'spec/quality-pass-phase' set up to track 'origin/spec/quality-pass-phase'.
```

</details>

## 🤖 Assistant

Pushed. `spec/quality-pass-phase` is now on `origin` (Gitea) and tracking it.

- **Pushed:** `8e9f477..c9484aa` — all of this session's P7 work (U5–U8, U9–U14, U15–U16, 7.7, 7.8, breadcrumbs, 7.9 close-out).
- **Upstream set:** the branch now tracks `origin/spec/quality-pass-phase`, so future `git push` from it is a bare push.
- Gitea offers a PR link if you want it later: `https://gitea.marlow.home/marlow/claude-training/pulls/new/spec/quality-pass-phase` — but I've **only pushed the branch**, no PR opened and nothing merged to `main`, as asked.

P7 is complete and now backed up on the remote. Remaining non-blocking items whenever you want them: merging this branch to `main`, **T2** (deferred dir-rename), and **L1** (`ci`/`managed-settings` version keys).

## 🧑 User

<local-command-caveat>Caveat: The messages below were generated by the user while running local commands. DO NOT respond to these messages or otherwise consider them in your response unless the user explicitly asks you to.</local-command-caveat>

## 🧑 User

<command-name>/export</command-name>
            <command-message>export</command-message>
            <command-args>quality-pass-session-2</command-args>

## 🧑 User

<local-command-stdout>Conversation exported to: /home/jj/dev/claude-training/quality-pass-session-2.txt</local-command-stdout>

## 🧑 User

## Context Usage

**Model:** claude-opus-4-8  
**Tokens:** 626.3k / 1m (63%)

### Estimated usage by category

| Category | Tokens | Percentage |
|----------|--------|------------|
| System prompt | 2.7k | 0.3% |
| System tools | 6.8k | 0.7% |
| MCP tools (deferred) | 1.5k | 0.1% |
| System tools (deferred) | 11.4k | 1.1% |
| Memory files | 1.6k | 0.2% |
| Skills | 1.5k | 0.1% |
| Messages | 615.2k | 61.5% |
| Free space | 372.3k | 37.2% |

### MCP Tools

| Tool | Server | Tokens |
|------|--------|--------|
| mcp__claude_ai_Gmail__authenticate | claude_ai_Gmail | 207 |
| mcp__claude_ai_Gmail__complete_authentication | claude_ai_Gmail | 268 |
| mcp__claude_ai_Google_Calendar__authenticate | claude_ai_Google_Calendar | 218 |
| mcp__claude_ai_Google_Calendar__complete_authentication | claude_ai_Google_Calendar | 283 |
| mcp__claude_ai_Google_Drive__authenticate | claude_ai_Google_Drive | 212 |
| mcp__claude_ai_Google_Drive__complete_authentication | claude_ai_Google_Drive | 277 |

### Memory Files

| Type | Path | Tokens |
|------|------|--------|
| Project | /home/jj/dev/claude-training/CLAUDE.md | 1.1k |
| AutoMem | /home/jj/.claude/projects/-home-jj-dev-claude-training/memory/MEMORY.md | 498 |

### Skills

| Skill | Source | Tokens |
|-------|--------|--------|
| prime-context | Project | ~100 |
| close-unit | Project | ~30 |
| update-config | Built-in | ~240 |
| keybindings-help | Built-in | ~80 |
| verify | Built-in | ~90 |
| code-review | Built-in | ~130 |
| simplify | Built-in | ~60 |
| fewer-permission-prompts | Built-in | ~60 |
| loop | Built-in | ~110 |
| schedule | Built-in | ~130 |
| claude-api | Built-in | ~250 |
| run | Built-in | ~120 |
| init | Built-in | ~20 |
| review | Built-in | < 20 |
| security-review | Built-in | ~30 |

## 🧑 User

Most of the prompts I gave you or questions I gave you stopped showing in my terminal after my first push-back in the context. They're not in the "/export" log either. I'm using this log as a training source and would like all my commands captured so my interactions with you and decisions are captured. How do I ensure that my prompts and answers are always displayed in the claude REPL?

## 🤖 Assistant

Good question — and since you're using this as a training record, let me actually verify what's captured where rather than guess. Let me check the `/export` file you just made and the raw session transcript on disk:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== export file: do your short prompts appear? ==="
for p in "continue to U6" "continue to U7" "commit U5–U8 then continue to U9" "Push to the branch only" "before we close out" "The asterisk we used"; do
  n=$(grep -cF "$p" quality-pass-session-2.txt 2>/dev/null || echo 0)
  echo "  [$n] $p"
done
echo "=== export size ==="; wc -l quality-pass-session-2.txt
```

<details><summary>tool result</summary>

```
Exit code 1
=== export file: do your short prompts appear? ===
  [] continue to U6
  [] continue to U7
  [] commit U5–U8 then continue to U9
  [] Push to the branch only
  [] before we close out
  [] The asterisk we used
=== export size ===
wc: quality-pass-session-2.txt: No such file or directory
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== find the export ==="; ls -la quality-pass-session-2.txt 2>&1; find . -maxdepth 2 -name 'quality-pass-session*' 2>/dev/null; ls -la ~/quality-pass-session-2.txt 2>&1 | head -1
echo "=== session transcripts on disk ==="
ls -lat ~/.claude/projects/-home-jj-dev-claude-training/*.jsonl 2>/dev/null | head -5
```

<details><summary>tool result</summary>

```
=== find the export ===
ls: cannot access 'quality-pass-session-2.txt': No such file or directory
./log/quality-pass-session-2.txt
./log/quality-pass-session-1.txt
ls: cannot access '/home/jj/quality-pass-session-2.txt': No such file or directory
=== session transcripts on disk ===
-rw------- 1 jj jj 4110820 May 31 10:21 /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
-rw------- 1 jj jj 2989019 May 31 01:50 /home/jj/.claude/projects/-home-jj-dev-claude-training/44c5e90c-2f12-47b1-bd76-79b471a323de.jsonl
-rw------- 1 jj jj    9055 May 30 23:42 /home/jj/.claude/projects/-home-jj-dev-claude-training/fe65bf55-b4be-47c6-8d0f-5055f442f09d.jsonl
-rw------- 1 jj jj  602791 May 30 23:21 /home/jj/.claude/projects/-home-jj-dev-claude-training/d85e1257-8e4f-4e6b-80c7-fae34ff2447f.jsonl
-rw------- 1 jj jj    8428 May 30 21:23 /home/jj/.claude/projects/-home-jj-dev-claude-training/0a29df3c-9ffd-442d-8d05-a26a00807871.jsonl
```

</details>

## 🤖 Assistant

Found them — export is at `log/quality-pass-session-2.txt`, and the live session transcript is `18010791-….jsonl`. Let me check whether your prompts are in each:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
JSONL=~/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
for p in "continue to U6" "Push to the branch only" "before we close out" "The asterisk we used"; do
  e=$(grep -cF "$p" log/quality-pass-session-2.txt); j=$(grep -cF "$p" "$JSONL")
  printf "  export:%s  jsonl:%s  | %s\n" "$e" "$j" "$p"
done
echo "=== how user turns are encoded in the jsonl (type:user count) ==="
grep -o '"type":"user"' "$JSONL" | wc -l
echo "=== AskUserQuestion answers present in jsonl? ==="
grep -cF "Ancestors only" "$JSONL"; grep -cF "Leave deferred" "$JSONL"
```

<details><summary>tool result</summary>

```
  export:0  jsonl:2  | continue to U6
  export:1  jsonl:4  | Push to the branch only
  export:0  jsonl:3  | before we close out
  export:0  jsonl:3  | The asterisk we used
=== how user turns are encoded in the jsonl (type:user count) ===
419
=== AskUserQuestion answers present in jsonl? ===
2
2
```

</details>

## 🤖 Assistant

Here's what the evidence shows — and it's good news for your training-source goal.

## The raw transcript already has everything
The authoritative record is the per-session JSONL on disk, and I verified it's **complete**:

```
~/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
```

| your prompt | in `/export` | in raw `.jsonl` |
|---|---|---|
| "continue to U6" | 0 | ✅ 2 |
| "before we close out…" | 0 | ✅ 3 |
| "The asterisk we used…" | 0 | ✅ 3 |
| "Push to the branch only" | 1 | ✅ 4 |

It has **419 user-turn entries**, and even your *picker* answers are recorded verbatim ("Ancestors only", "Leave deferred"). So nothing you said or decided was lost — `/export` and the terminal scrollback are the lossy views, not the underlying log.

## Why the REPL/`/export` drop them
- **`/export` and the visible scrollback reflect a trimmed/collapsed view**, not the full event log. The TUI condenses older turns as a session grows (and terminal scrollback is finite regardless), so a long session like this one exports only part of it. There isn't a reliable "keep every turn fully expanded forever" toggle — so the REPL display itself isn't a dependable capture mechanism.
- **Interactive questions are the other gap.** When I use the `AskUserQuestion` picker (the T2 deferral, the breadcrumb-format choices), your answer is recorded as a selection chip, not as a typed line — so it won't *look* like one of your prompts in the terminal even though it's in the `.jsonl`.

## How to ensure full capture
1. **Use the `.jsonl` as your training source, not `/export`.** It's append-only and complete. One JSON event per line; your turns are `{"type":"user", ...}`.
2. **If you want decisions captured as normal typed prompts** (visible + cleaner to read), tell me to **pose choices as plain-text questions you answer by typing**, rather than via the interactive picker. I'll avoid `AskUserQuestion` for this session if you say so.
3. Bump your terminal emulator's scrollback if you also want more visible history live — but that's cosmetic; the `.jsonl` is the real record.

Since the export is lossy, the most useful thing I can do for your training corpus is extract a clean, ordered transcript of **just the human turns** (your typed prompts + your picker answers) straight from the `.jsonl`. Want me to write that to `log/quality-pass-session-2.usermsgs.md` (and, if useful, a full human-readable user+assistant transcript alongside it)?

## 🧑 User

I have more to add before we start next steps. As you can see in log/ I've been capturing the session output using the "/export" feature. My workflow has been at the very end of every session, as the very last act of the clean session, I export the conversation, move it to the log directory, and then commit and push to that directory. I was at the point where I was about to commit and push. Knowing now that the export is lossy puts me in a bad place. I likely have missing info in those old logs as well. I want to capture the full transcript .jsonl file directly for completeness and machine parseability, but I also want a human to be able to read it. I'm considering creating a skill that can capture the .jsonl of the current conversation, place it in the repo, and also somehow provide a re-rendered human-readable version? I'm open for suggestions, this is only my first design thought.

## 🤖 Assistant

Before next steps — first, a reassurance that changes your situation: **you're not in a bad place. Every past session's raw `.jsonl` is still on disk**, so the complete record for your older (lossy-exported) logs is recoverable; we can back-fill them. Let me ground the design in the actual data before I propose:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
D=~/.claude/projects/-home-jj-dev-claude-training
echo "=== all session jsonls (date / size / lines) ==="
for f in "$D"/*.jsonl; do printf "%s  %6sKB  %5s lines  %s\n" "$(date -r "$f" +%Y-%m-%d_%H:%M)" "$(( $(stat -c%s "$f")/1024 ))" "$(wc -l <"$f")" "$(basename "$f")"; done
echo "=== existing committed logs ==="; ls -1 log/ 2>/dev/null
echo "=== jq available? ==="; command -v jq >/dev/null && echo yes || echo no
echo "=== event 'type' distribution in current session jsonl ==="
JSONL="$D/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl"
grep -oE '"type":"[a-z_]+"' "$JSONL" | sort | uniq -c | sort -rn | head
```

<details><summary>tool result</summary>

```
=== all session jsonls (date / size / lines) ===
2026-05-30_13:14     968KB    442 lines  03472b7e-9e1a-45d6-8373-d70188648cfd.jsonl
2026-05-30_09:32      12KB     19 lines  03e50ade-9257-4754-85c7-8911965a87b4.jsonl
2026-05-30_21:23       8KB      8 lines  0a29df3c-9ffd-442d-8d05-a26a00807871.jsonl
2026-05-30_15:56    2384KB    812 lines  16a51be7-4778-46a4-8e2d-7f5ba3f55ee1.jsonl
2026-05-31_10:33    4047KB   1560 lines  18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
2026-05-31_01:50    2918KB   1032 lines  44c5e90c-2f12-47b1-bd76-79b471a323de.jsonl
2026-05-30_09:42      11KB     14 lines  502765fc-efd3-4f43-939f-ae2ec3c9acc6.jsonl
2026-05-30_09:31    1384KB    571 lines  60da1c88-1049-436f-b19d-64dfecc96d3a.jsonl
2026-05-30_18:02    1666KB    603 lines  68d16797-e225-4ea9-8ba6-3ac257e6927e.jsonl
2026-05-30_08:47    1197KB    541 lines  752dc658-6df5-43ad-84ae-dcb38329eeab.jsonl
2026-05-30_17:18      10KB      7 lines  77031a53-8f39-484a-ae83-8c620a662121.jsonl
2026-05-30_08:11    1404KB    613 lines  7b80c621-d0b2-4c18-8155-cae8bb3e270c.jsonl
2026-05-30_20:04    1013KB    355 lines  7cd46d5f-dec2-4836-ac29-2bb7eccdbab5.jsonl
2026-05-30_10:39    1639KB    706 lines  a2724d32-ece9-4efe-a3e3-0736c86604dd.jsonl
2026-05-30_17:02    1158KB    542 lines  a3523ae6-5ee4-497a-ba5b-546ea4e8af0b.jsonl
2026-05-30_09:31      20KB     28 lines  b657b709-75e8-447b-92e0-e7f8db09f004.jsonl
2026-05-30_09:33     982KB    347 lines  cc3dd161-853d-4864-a339-da1a8ad14d66.jsonl
2026-05-30_23:21     588KB    196 lines  d85e1257-8e4f-4e6b-80c7-fae34ff2447f.jsonl
2026-05-30_09:27     935KB    413 lines  e841cbb1-089b-4114-8712-31998d589e19.jsonl
2026-05-30_14:13    1651KB    743 lines  e8c2a669-1cfc-48f5-8981-dff3db943624.jsonl
2026-05-30_07:25      16KB     16 lines  ebb78c30-b61b-4273-83be-06b46593765d.jsonl
2026-05-30_09:41      11KB     14 lines  f155bb78-c02b-493a-b6d0-9e4309d1ec0c.jsonl
2026-05-30_23:42       8KB      9 lines  fe65bf55-b4be-47c6-8d0f-5055f442f09d.jsonl
=== existing committed logs ===
implementation-session-1.txt
implementation-session-10.txt
implementation-session-11.txt
implementation-session-2.txt
implementation-session-3.txt
implementation-session-4.txt
implementation-session-5.txt
implementation-session-6.txt
implementation-session-7.txt
implementation-session-8.txt
implementation-session-9.txt
quality-pass-session-1.txt
quality-pass-session-2.txt
spec-creation-session-1.txt
spec-creation-session-2.txt
… [+13 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Grounded now. The inventory is reassuring and clarifying:

- **~23 session `.jsonl` files** exist (2026‑05‑30 → 05‑31); ~13 are substantial work sessions (>300 lines), the rest are tiny/aborted. **All recoverable.**
- **15 committed `.txt` logs** in `log/` (11 implementation + 2 quality-pass + 2 spec-creation) — all from lossy `/export`.
- `jq` is available; event types in a session are `user`, `assistant`, `text`, `thinking`, `tool_use`, `tool_result`, `attachment`, etc.

So: the raw record for every past session is intact on disk — the lossy `.txt` logs can be regenerated complete. You're in a recoverable spot, not a bad one.

## Recommended architecture (matches this repo's idiom)
Keep logic in a committed tool; make the skill a thin orchestrator — exactly like `render-units`/`render-index`/`render-checklist`:

1. **`tools/render-transcript`** (committed Python) — pure function: takes a `.jsonl` path → emits readable `.md`. Tolerant of unknown event types (so a future Claude Code schema bump degrades gracefully, not crashes). Because it's just `jsonl → md`, the *same* tool serves both the current session **and** back-filling old ones.
2. **A skill (e.g. `capture-session`)** — orchestration only: find the current session's `.jsonl` → copy the raw `.jsonl` into `log/` → run `tools/render-transcript` → report what it wrote. You run it as your end-of-session ritual (replacing the `/export` step), eyeball the result, then commit/push.

Both raw `.jsonl` (complete, machine-parseable) and rendered `.md` (human-readable) land in `log/`. That satisfies both your goals from one capture.

*(Alternative for full automation: a `SessionEnd` hook gets the exact `transcript_path` handed to it — no heuristic, no remembering. But it fires on every session including throwaways, and — per this repo's own R12.AC3 rule — the exact event name/payload must be verified against the CLI before wiring. I'd keep the manual skill as the primary and treat a hook as later hardening.)*

## Design forks I'd want your call on (please answer in text, not a picker — so it's captured)
1. **Mechanism:** manual skill now (fits your ritual, lets you review before committing), or go straight to a `SessionEnd` hook, or both?
2. **Finding the current `.jsonl`:** the pragmatic way from inside a running session is "newest `.jsonl` in the project dir" (it's the one being appended to). Two honest limits: it can't capture its *own* trailing lines (you can't log the act of logging), and it'd misfire if two Claude sessions run in the same repo at once. Acceptable?
3. **Rendering fidelity** (the big one — readability vs completeness):
   - User + assistant text: always in.
   - **Thinking blocks** (106 in this session): include, omit, or collapse? They're verbose and are *my* internal reasoning, not your decisions — I'd lean omit-by-default for the readable `.md` (they're still in the raw `.jsonl`).
   - **Tool calls / results:** big outputs (e.g. the full `make check` dumps) — include verbatim, truncate, or wrap in collapsible `<details>`? I'd lean: show tool *name + key args* and **truncate** long results in the `.md`, full fidelity preserved in the `.jsonl`.
4. **Repo hygiene:** keep the lossy `.txt` exports, replace them, or leave them and add `.jsonl`+`.md` going forward? And confirm you're OK committing raw `.jsonl` (~1–4 MB each; ~20 MB for a back-fill of all 13).
5. **Back-fill:** want me to regenerate complete logs for the ~13 past sessions too? That needs a small matching pass (jsonl ↔ your `session-N` names by date/content), since names don't map 1:1.

## Two caveats worth stating up front
- **Secrets/PII:** the `.jsonl` is *more* complete than the export — it contains everything typed and every file excerpt read. Since you push `log/` to Gitea, the raw transcript publishes more than the `.txt` did. Worth a conscious "yes, that's fine for this repo."
- **Schema drift:** the `.jsonl` shape is Claude Code's internal format and can change across versions — another reason the renderer must skip unknown event types rather than assume a fixed schema.

Tell me your calls on the five forks (and the two caveats) and I'll draft the tool + skill. Which would you like to nail down first?

## 🧑 User

Skill now; collapse thinking, truncate tool output; wait to back-fill all 13 until we've confirmed the rendering and content are appropriate together. Assume the skill can be triggered multiple times in the session and it will update to the latest possible point in the current session each tigger. I understand that the act of logging can't itself be logged for the active session. Assume also that multiple sessions could be active for the same repo, so the mechanism to specify which .jsonl to capture must be robust.

## 🤖 Assistant

Good, clear calls. The one genuinely hard requirement is #6 — **robustly** picking the right `.jsonl` when sessions can run concurrently (mtime "newest" is not safe then). That decides the whole mechanism, so let me investigate what reliable session identity is actually available rather than guess:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== env vars that could identify the session ==="
env | grep -iE 'claude|session|transcript|anthropic' | sed 's/=.*/=<redacted>/' || echo "(none)"
echo "=== fields on a jsonl event (current session, first + a middle line) ==="
JSONL=~/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
jq -rc 'keys' "$JSONL" | sort | uniq -c
echo "=== sample identifying fields ==="
jq -rc '{sessionId, cwd, gitBranch, version, type}' "$JSONL" 2>/dev/null | head -3
```

<details><summary>tool result</summary>

```
=== env vars that could identify the session ===
AI_AGENT=<redacted>
WT_SESSION=<redacted>
CLAUDE_CODE_SESSION_ID=<redacted>
CLAUDE_EFFORT=<redacted>
PWD=<redacted>
TMPPREFIX=<redacted>
CLAUDECODE=<redacted>
TMPDIR=<redacted>
CLAUDE_CODE_TMPDIR=<redacted>
CLAUDE_CODE_ENTRYPOINT=<redacted>
WSLENV=<redacted>
CLAUDE_CODE_EXECPATH=<redacted>
DBUS_SESSION_BUS_ADDRESS=<redacted>
OLDPWD=<redacted>
=== fields on a jsonl event (current session, first + a middle line) ===
     81 ["aiTitle","sessionId","type"]
     22 ["attachment","cwd","entrypoint","gitBranch","isSidechain","parentUuid","sessionId","slug","timestamp","type","userType","uuid","version"]
     59 ["attachment","cwd","entrypoint","gitBranch","isSidechain","parentUuid","sessionId","timestamp","type","userType","uuid","version"]
     11 ["attributionSkill","cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","requestId","sessionId","timestamp","type","userType","uuid","version"]
      2 ["content","cwd","entrypoint","gitBranch","isMeta","isSidechain","level","parentUuid","sessionId","slug","subtype","timestamp","type","userType","uuid","version"]
      5 ["cwd","durationMs","entrypoint","gitBranch","isMeta","isSidechain","messageCount","parentUuid","sessionId","slug","subtype","timestamp","type","userType","uuid","version"]
     13 ["cwd","durationMs","entrypoint","gitBranch","isMeta","isSidechain","messageCount","parentUuid","sessionId","subtype","timestamp","type","userType","uuid","version"]
      2 ["cwd","entrypoint","gitBranch","isMeta","isSidechain","message","parentUuid","promptId","sessionId","slug","timestamp","type","userType","uuid","version"]
      1 ["cwd","entrypoint","gitBranch","isMeta","isSidechain","message","parentUuid","promptId","sessionId","timestamp","type","userType","uuid","version"]
      5 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","permissionMode","promptId","sessionId","slug","timestamp","type","userType","uuid","version"]
     14 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","permissionMode","promptId","sessionId","timestamp","type","userType","uuid","version"]
    125 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","promptId","sessionId","slug","sourceToolAssistantUUID","timestamp","toolUseResult","type","userType","uuid","version"]
      2 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","promptId","sessionId","slug","timestamp","type","userType","uuid","version"]
    272 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","promptId","sessionId","sourceToolAssistantUUID","timestamp","toolUseResult","type","userType","uuid","version"]
      2 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","promptId","sessionId","timestamp","type","userType","uuid","version"]
    225 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","requestId","sessionId","slug","timestamp","type","userType","uuid","version"]
    434 ["cwd","entrypoint","gitBranch","isSidechain","message","parentUuid","requestId","sessionId","timestamp","type","userType","uuid","version"]
     51 ["isSnapshotUpdate","messageId","snapshot","type"]
     80 ["lastPrompt","leafUuid","sessionId","type"]
      2 ["leafUuid","sessionId","type"]
     83 ["mode","sessionId","type"]
     83 ["permissionMode","sessionId","type"]
=== sample identifying fields ===
{"sessionId":"18010791-8af3-4a98-aaba-9b5373df76eb","cwd":null,"gitBranch":null,"version":null,"type":"mode"}
… [+2 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

That settles it cleanly. Two robust signals exist:

- **`CLAUDE_CODE_SESSION_ID`** is set in the session's environment — the current session's UUID, direct and per-session (concurrent sessions each carry their own).
- **Every `.jsonl` event has a `sessionId` field** equal to the filename UUID.

So no mtime guessing and no sentinel hack needed. Let me verify the env var maps to the file:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "session id == current jsonl name?"
[ "$CLAUDE_CODE_SESSION_ID" = "18010791-8af3-4a98-aaba-9b5373df76eb" ] && echo "  YES — env matches this session's jsonl" || echo "  (differs: $CLAUDE_CODE_SESSION_ID)"
echo "resolve transcript by id (works regardless of cwd-encoding):"
find ~/.claude/projects -name "$CLAUDE_CODE_SESSION_ID.jsonl" 2>/dev/null
echo "and its events' sessionId is internally consistent:"
f=$(find ~/.claude/projects -name "$CLAUDE_CODE_SESSION_ID.jsonl"); jq -r 'select(.sessionId!=null).sessionId' "$f" | sort -u | head
```

<details><summary>tool result</summary>

```
session id == current jsonl name?
  YES — env matches this session's jsonl
resolve transcript by id (works regardless of cwd-encoding):
/home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb.jsonl
and its events' sessionId is internally consistent:
18010791-8af3-4a98-aaba-9b5373df76eb
```

</details>

## 🤖 Assistant

Verified and bulletproof: `find ~/.claude/projects -name "$CLAUDE_CODE_SESSION_ID.jsonl"` resolves the **exact** current transcript — robust to concurrent sessions and independent of cwd-path encoding. No mtime guessing, no sentinel hack.

The design is fully settled, so I'll build it and exercise it on *this* session (which is `quality-pass-session-2`) — that gives you the real rendered output to judge before we back-fill, exactly as you asked. Defaults I'm choosing (call them out if you want them changed): skill takes a name arg → writes `log/<name>.jsonl` + `log/<name>.md`, idempotent overwrite; tool output truncated to 40 lines; thinking folded into `<details>`; system/meta + sidechain events omitted from the `.md` (always intact in the `.jsonl`).

First, the committed renderer (`jsonl → md`, defensive about unknown event types):

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/tools/render-transcript  (write 7277 chars, 168 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/tools/render-transcript (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
chmod +x tools/render-transcript
# Exercise it on THIS session to produce the real session-2 log (raw + rendered).
id="$CLAUDE_CODE_SESSION_ID"
src=$(find ~/.claude/projects -name "$id.jsonl")
cp "$src" log/quality-pass-session-2.jsonl
tools/render-transcript log/quality-pass-session-2.jsonl --out log/quality-pass-session-2.md
echo "--- sizes ---"
wc -l log/quality-pass-session-2.jsonl log/quality-pass-session-2.md
echo "--- human turns captured in the rendered md (should be many, vs /export's near-zero) ---"
grep -c '^## 🧑 User' log/quality-pass-session-2.md
```

<details><summary>tool result</summary>

```
render-transcript: wrote log/quality-pass-session-2.md (1595 events)
--- sizes ---
   1595 log/quality-pass-session-2.jsonl
  11466 log/quality-pass-session-2.md
  13061 total
--- human turns captured in the rendered md (should be many, vs /export's near-zero) ---
26
```

</details>

## 🤖 Assistant

26 human turns captured (the lossy `/export` had ~0). Let me show you representative slices so you can judge the rendering — the header + opening exchange, and a middle chunk with a tool call + collapsed thinking + truncated result:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "================ HEAD (header + first exchange) ================"
sed -n '1,40p' log/quality-pass-session-2.md
echo
echo "================ a 'thinking' (collapsed) + tool call + result sample ================"
awk '/<details><summary>thinking<\/summary>/{f=1} f{print} /tool result<\/summary>/{c++} c>=1 && /<\/details>/{print "---(end sample)---"; exit}' log/quality-pass-session-2.md | head -45
```

<details><summary>tool result</summary>

```
================ HEAD (header + first exchange) ================
# Session transcript

- **Session:** `18010791-8af3-4a98-aaba-9b5373df76eb`
- **Title:** Editorial pass on U5 with reference diffs
- **Source:** rendered from the raw `.jsonl` by `tools/render-transcript` (thinking collapsed; tool output truncated to 40 lines). The sibling `.jsonl` is the complete, machine-parseable record.

---

## 🧑 User

<command-message>prime-context</command-message>
<command-name>/prime-context</command-name>

## 🧑 User

Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/prime-context

# Prime context

Bring a fresh session up to speed on this repo before doing anything else. The spec is the source of
truth; the auto-loaded project memory is only a pointer — trust the files for specifics.

Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state surfaced):

1. **Read `specs/claude-code-mastery/IMPLEMENTATION.md`** — the orientation hub. Note §2 (read order)
   and especially **§3 (live phase/unit status)** — the single most important "where are we."
2. **Read `specs/claude-code-mastery/decisions.md`** — focus on the canonical **🔓 open-loops ledger**
   (deferred work; per-lab status **L7**; version debt **L1**) and the most recent `P5-*` entries.
3. **Skim as the task needs:** `requirements.md` (the WHAT, R1–R15, EARS), `design.md` (the HOW +
   traceability), `tasks.md` (ordered build plan; the P5 unit table).
4. **Check git state:** current branch and what's uncommitted — `git status` and `git log --oneline -5`.

Then report a tight summary, not a full audit:

- **Where we are** — current phase + unit from §3 (e.g. "P5: U1–U12 done, U13 next").
- **Open loops** — anything live in the 🔓 ledger that bears on the next step.
- **Working state** — branch, uncommitted changes, anything mid-flight.
- **Next action** — the obvious next task, framed so the user can confirm or redirect.

… [+4 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

The header and prompt capture look right. Let me show a clean assistant-with-tool-call + truncated-result + collapsed-thinking sample:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== first assistant tool call + its truncated result ==="
n=$(grep -n '^\*\*→ Bash\*\*' log/quality-pass-session-2.md | head -1 | cut -d: -f1)
sed -n "$((n-2)),$((n+18))p" log/quality-pass-session-2.md
echo
echo "=== a collapsed thinking block (first occurrence, ~12 lines) ==="
t=$(grep -n 'summary>thinking' log/quality-pass-session-2.md | head -1 | cut -d: -f1)
sed -n "${t},$((t+10))p" log/quality-pass-session-2.md
```

<details><summary>tool result</summary>

```
=== first assistant tool call + its truncated result ===
## 🤖 Assistant

**→ Bash**

```
git status && echo "---LOG---" && git log --oneline -5
```

<details><summary>tool result</summary>

```
On branch spec/quality-pass-phase
nothing to commit, working tree clean
---LOG---
8e9f477 Add quality-pass-session-1 log
0d35846 P7 (WIP): roll learner-prose remediation through U2–U4; auto-de-code U5–U16
79ba027 P7: committed-rendered units + navigation index (U1 pilot)
f12e692 P7: add quality-pass spec (findings, design, tasks)
179cd30 Add implementation-session-11 log
```


=== a collapsed thinking block (first occurrence, ~12 lines) ===
  "content": "#!/usr/bin/env python3\n\"\"\"render-transcript: turn a Claude Code session `.jsonl` into a human-readable Markdown\ntranscript. Pure function of the input file — works for the current session and for back-fill.\n\nUsage:\n  tools/render-transcript <session.jsonl> [--out FILE] [--max-tool-lines N]\n                          [--thinking collapsed|full|omit]\n\nThe raw `.jsonl` is the complete, machine-parseable record; this `.md` is the readable view:\nuser prompts and assistant prose in full, tool calls summarized, long tool output truncated\n(with a pointer back to the `.jsonl`), and the assistant's internal *thinking* folded away.\n\nDesign notes\n- The `.jsonl` schema is Claude Code's internal format and may shift across versions, so this\n  reader is deliberately tolerant: unknown event types and missing fields are skipped, never fatal.\n- System/meta bookkeeping (mode, permission-mode, snapshots, titles, summaries) and subagent\n  sidechains are omitted from the `.md` for readability — all of it remains in the `.jsonl`.\n\"\"\"\nimport argparse\nimport json\nimport sys\n\n\ndef _text_blocks(content):\n    \"\"\"Normalize a message `content` (str or list of blocks) into a list of blocks.\"\"\"\n    if isinstance(content, str):\n        return [{\"type\": \"text\", \"text\": content}]\n    if isinstance(content, list):\n        return content\n    return []\n\n\ndef _result_to_text(content):\n    \"\"\"A tool_result's `content` is a str or a list of {type:text,text:...} blocks.\"\"\"\n    if isinstance(content, str):\n        return content\n    if isinstance(content, list):\n        out = []\n        for b in content:\n            if isinstance(b, dict) and b.get(\"type\") == \"text\":\n                out.append(b.get(\"text\", \"\"))\n            elif isinstance(b, str):\n                out.append(b)\n        return \"\\n\".join(out)\n    return \"\" if content is None else str(content)\n\n\ndef _truncate(text, max_lines):\n    text = (text or \"\").rstrip(\"\\n\")\n    if max_lines <= 0:\n        return text\n    lines = text.split(\"\\n\")\n    if len(lines) <= max_lines:\n        return text\n    kept = \"\\n\".join(lines[:max_lines])\n    return f\"{kept}\\n… [+{len(lines) - max_lines} more lines — full output in the .jsonl]\"\n\n\ndef _tool_input_summary(name, tool_input, max_lines):\n    \"\"\"One-liner-ish for the call; Bash shows its command, others show compact JSON.\"\"\"\n    if not isinstance(tool_input, dict):\n        return _truncate(str(tool_input), max_lines)\n    if name == \"Bash\" and \"command\" in tool_input:\n        return _truncate(tool_input[\"command\"], max_lines)\n    if name in (\"Read\", \"Glob\", \"Grep\") and (tool_input.get(\"file_path\") or tool_input.get(\"pattern\")):\n        return tool_input.get(\"file_path\") or tool_input.get(\"pattern\")\n    try:\n        return _truncate(json.dumps(tool_input, indent=2, ensure_ascii=False), max_lines)\n    except (TypeError, ValueError):\n        return _truncate(str(tool_input), max_lines)\n\n\ndef render(events, max_tool_lines=40, thinking=\"collapsed\"):\n    out = []\n    for ev in events:\n        if not isinstance(ev, dict):\n            continue\n        if ev.get(\"isSidechain\"):  # subagent traffic — omit from the readable view\n            continue\n        msg = ev.get(\"message\")\n        if not isinstance(msg, dict):\n            continue  # mode / permission-mode / snapshot / title / summary — skip in .md\n        role = msg.get(\"role\")\n        blocks = _text_blocks(msg.get(\"content\"))\n\n        if role == \"user\":\n            # A user turn is either a human prompt (text) or tool_result(s) feeding a prior call.\n            texts = [b.get(\"text\", \"\") for b in blocks if isinstance(b, dict) and b.get(\"type\") == \"text\"]\n            results = [b for b in blocks if isinstance(b, dict) and b.get(\"type\") == \"tool_result\"]\n            human = \"\\n\".join(t for t in texts if t.strip())\n            if human.strip():\n                out.append(f\"## 🧑 User\\n\\n{human.strip()}\\n\")\n            for r in results:\n                body = _truncate(_result_to_text(r.get(\"content\")), max_tool_lines)\n                if body.strip():\n                    out.append(f\"<details><summary>tool result</summary>\\n\\n```\\n{body}\\n```\\n\\n</details>\\n\")\n        elif role == \"assistant\":\n            chunks = []\n            for b in blocks:\n                if not isinstance(b, dict):\n                    continue\n                t = b.get(\"type\")\n                if t == \"text\" and b.get(\"text\", \"\").strip():\n                    chunks.append(b[\"text\"].rstrip())\n                elif t == \"thinking\" and thinking != \"omit\":\n                    think = (b.get(\"thinking\") or \"\").strip()\n                    if not think:\n                        continue\n                    if thinking == \"full\":\n                        chunks.append(f\"> _thinking_\\n>\\n\" + \"\\n\".join(f\"> {ln}\" for ln in think.split(\"\\n\")))\n                    else:  # collapsed\n                        chunks.append(f\"<details><summary>thinking</summary>\\n\\n{think}\\n\\n</details>\")\n                elif t == \"tool_use\":\n                    summary = _tool_input_summary(b.get(\"name\", \"?\"), b.get(\"input\"), max_tool_lines)\n                    chunks.append(f\"**→ {b.get('name', '?')}**\\n\\n```\\n{summary}\\n```\")\n            if chunks:\n                out.append(\"## 🤖 Assistant\\n\\n\" + \"\\n\\n\".join(chunks) + \"\\n\")\n    return \"\\n\".join(out).rstrip() + \"\\n\"\n\n\ndef load_events(path):\n    events = []\n    with open(path, encoding=\"utf-8\") as fh:\n        for line in fh:\n            line = line.strip()\n            if not line:\n                continue\n            try:\n                events.append(json.loads(line))\n            except json.JSONDecodeError:\n                continue  # tolerate a partial trailing line on a live session\n    return events\n\n\ndef main(argv):\n    ap = argparse.ArgumentParser(description=\"Render a Claude Code session .jsonl as readable Markdown.\")\n    ap.add_argument(\"jsonl\", help=\"path to the session .jsonl\")\n    ap.add_argument(\"--out\", help=\"output .md path (default: stdout)\")\n    ap.add_argument(\"--max-tool-lines\", type=int, default=40, help=\"truncate tool I/O to N lines (0 = no limit)\")\n    ap.add_argument(\"--thinking\", choices=[\"collapsed\", \"full\", \"omit\"], default=\"collapsed\")\n    args = ap.parse_args(argv)\n\n    events = load_events(args.jsonl)\n    title = next((e.get(\"aiTitle\") for e in events if isinstance(e, dict) and e.get(\"aiTitle\")), None)\n    sid = next((e.get(\"sessionId\") for e in events if isinstance(e, dict) and e.get(\"sessionId\")), \"unknown\")\n    header = (\n        f\"# Session transcript\\n\\n\"\n        f\"- **Session:** `{sid}`\\n\"\n        + (f\"- **Title:** {title}\\n\" if title else \"\")\n        + f\"- **Source:** rendered from the raw `.jsonl` by `tools/render-transcript` \"\n        f\"(thinking {args.thinking}; tool output truncated to {args.max_tool_lines} lines). \"\n        f\"The sibling `.jsonl` is the complete, machine-parseable record.\\n\\n---\\n\\n\"\n    )\n    body = render(events, max_tool_lines=args.max_tool_lines, thinking=args.thinking)\n
… [+572 more chars — full content in the .jsonl]
```

</details>

## 🤖 Assistant

Good — the tool-call + collapsed-result rendering is exactly right. But that sample exposed a real bug: my last grep matched the **`Write` tool's input**, which dumped the *entire* file content as one giant escaped line (line-truncation doesn't help when it's all on one logical line). Every `Write`/`Edit` would bloat the `.md`. Let me make the input summary field-aware (show path + size, not the whole blob) and add a character cap as a backstop:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/tools/render-transcript
- old: def _truncate(text, max_lines):
- new: def _clip(text, max_chars):
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/tools/render-transcript has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
tools/render-transcript log/quality-pass-session-2.jsonl --out log/quality-pass-session-2.md
echo "--- size now (was 11466 lines) ---"; wc -l log/quality-pass-session-2.md
echo "--- a Write call now renders as path+size (not a file dump): ---"
grep -n '→ Write' log/quality-pass-session-2.md | head -2
n=$(grep -n '→ Write' log/quality-pass-session-2.md | head -1 | cut -d: -f1); sed -n "${n},$((n+4))p" log/quality-pass-session-2.md
echo "--- real collapsed thinking blocks present (section-start lines): ---"
grep -c '^<details><summary>thinking</summary>' log/quality-pass-session-2.md
```

## 🧑 User

but after I'd like to pause to consider all security concerns before we continue much further.

<details><summary>tool result</summary>

```
render-transcript: wrote log/quality-pass-session-2.md (1595 events)
--- size now (was 11466 lines) ---
10719 log/quality-pass-session-2.md
--- a Write call now renders as path+size (not a file dump): ---
10707:**→ Write**
**→ Write**

```
/home/jj/dev/claude-training/tools/render-transcript  (write 7277 chars, 168 lines)
```
--- real collapsed thinking blocks present (section-start lines): ---
0
```

</details>

## 🤖 Assistant

Good call — and the right moment for it, since the very next steps (committing + pushing raw transcripts) are the ones with exposure. Let me hold here. (Noting one **non-security** loose end to return to later: real `thinking` blocks rendered 0 — they aren't being emitted; a fidelity bug to fix after the security pass.)

First, let me make the review evidence-based with a **count-only** scan (I'll deliberately print no matching content, so I don't re-leak anything into *this* transcript):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "Scanning for sensitive patterns — COUNTS ONLY, no content printed."
scan() {
  local f="$1"
  [ -f "$f" ] || return
  printf "  %-40s " "$(basename "$f")"
  printf "email:%s " "$(grep -aoEc '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f" 2>/dev/null | paste -sd+ | bc 2>/dev/null || grep -aoE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$f" | wc -l)"
  printf "apikey-ish:%s " "$(grep -aiEc 'api[_-]?key|sk-ant|secret|password|bearer |authorization:' "$f" | tr -d ' ')"
  printf "privkey:%s " "$(grep -ac 'BEGIN .*PRIVATE KEY' "$f" | tr -d ' ')"
  printf "aws:%s " "$(grep -aoEc 'AKIA[0-9A-Z]{16}' "$f" | tr -d ' ')"
  printf "userEmail-line:%s\n" "$(grep -ac 'userEmail' "$f" | tr -d ' ')"
}
echo "=== NEW raw jsonl (candidate to commit) ==="; scan log/quality-pass-session-2.jsonl
echo "=== NEW rendered md ==="; scan log/quality-pass-session-2.md
echo "=== ALREADY-COMMITTED .txt logs (sample) ==="
for f in log/quality-pass-session-1.txt log/implementation-session-11.txt log/spec-creation-session-1.txt; do scan "$f"; done
```

## 🧑 User

but I also want to better understand the full contents of the .jsonl file and ensure no secrets are there by convention. I understand the user could always leak secrets and we can't avoid that.

<details><summary>tool result</summary>

```
Scanning for sensitive patterns — COUNTS ONLY, no content printed.
=== NEW raw jsonl (candidate to commit) ===
  quality-pass-session-2.jsonl             email:24 apikey-ish:26 privkey:0 aws:0 userEmail-line:0
=== NEW rendered md ===
  quality-pass-session-2.md                email:16 apikey-ish:10 privkey:0 aws:0 userEmail-line:0
=== ALREADY-COMMITTED .txt logs (sample) ===
  quality-pass-session-1.txt               email:0 apikey-ish:4 privkey:0 aws:0 userEmail-line:0
  implementation-session-11.txt            email:0 apikey-ish:0 privkey:0 aws:0 userEmail-line:0
  spec-creation-session-1.txt              email:1 apikey-ish:16 privkey:0 aws:0 userEmail-line:0
```

</details>

## 🤖 Assistant

Right — let's anatomize the `.jsonl` so you can reason about it structurally, separating what the **format puts there by convention** from what enters via **your actions** (typing, files read, command output). Still count-only / structure-only so I don't re-leak.

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
f=log/quality-pass-session-2.jsonl
echo "=== 1. top-level event types (the record's anatomy) ==="
jq -r '.type' "$f" | sort | uniq -c | sort -rn
echo
echo "=== 2. message roles present (is the SYSTEM PROMPT stored?) ==="
jq -r 'select(.message!=null) | .message.role' "$f" | sort | uniq -c
echo 'literal "role":"system" occurrences:' "$(grep -ac '"role":"system"' "$f")"
echo
echo "=== 3. content-block types inside messages ==="
jq -r 'select((.message.content|type)=="array") | .message.content[].type' "$f" 2>/dev/null | sort | uniq -c | sort -rn
echo
echo "=== 4. structural env disclosure (always present, by convention) ==="
echo "distinct cwd values:"; jq -r 'select(.cwd!=null) | .cwd' "$f" | sort -u
echo "distinct gitBranch values:"; jq -r 'select(.gitBranch!=null) | .gitBranch' "$f" | sort -u
echo "distinct version values:"; jq -r 'select(.version!=null) | .version' "$f" | sort -u
```

<details><summary>tool result</summary>

```
=== 1. top-level event types (the record's anatomy) ===
    679 assistant
    426 user
     85 permission-mode
     85 mode
     84 last-prompt
     83 ai-title
     81 attachment
     52 file-history-snapshot
     20 system

=== 2. message roles present (is the SYSTEM PROMPT stored?) ===
    679 assistant
    426 user
literal "role":"system" occurrences: 0

=== 3. content-block types inside messages ===
    400 tool_use
    400 tool_result
    170 text
    111 thinking

=== 4. structural env disclosure (always present, by convention) ===
distinct cwd values:
/home/jj/dev/claude-training
distinct gitBranch values:
spec/quality-pass-phase
distinct version values:
2.1.158
```

</details>

## 🤖 Assistant

Two convention-level capture surfaces beyond plain messages stand out and I want to characterize them before judging: **`file-history-snapshot`** (52 — Claude Code's checkpoint feature, which may embed file *contents* by design) and **`attachment`** (81). Also confirming whether **thinking plaintext** is actually stored. Structure/lengths only — no values:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
f=log/quality-pass-session-2.jsonl
echo "=== file-history-snapshot: top-level keys of .snapshot (does it hold file CONTENT?) ==="
jq -rc 'select(.type=="file-history-snapshot") | .snapshot | if type=="object" then keys else type end' "$f" 2>/dev/null | sort | uniq -c
echo "  does any snapshot contain a 'content'/'text' scalar key path?"
jq -rc 'select(.type=="file-history-snapshot") | [paths(scalars)|join(".")]' "$f" 2>/dev/null | tr ',' '\n' | grep -iE 'content|text|snippet' | sort | uniq -c | head
echo
echo "=== attachment: shape ==="
jq -rc 'select(.type=="attachment") | .attachment | if type=="object" then (keys|join(",")) else type end' "$f" 2>/dev/null | sort | uniq -c | head
echo
echo "=== system events: subtypes ==="
jq -r 'select(.type=="system") | .subtype // .level // "?"' "$f" 2>/dev/null | sort | uniq -c
echo
echo "=== thinking: is PLAINTEXT stored? (block lengths, no content) ==="
jq -r 'select((.message.content|type)=="array") | .message.content[] | select(.type=="thinking") | (.thinking|length)' "$f" 2>/dev/null | awk '{n++; s+=$1; if($1>m)m=$1} END{print "  blocks:",n,"| total chars:",s,"| max block chars:",m}'
```

<details><summary>tool result</summary>

```
=== file-history-snapshot: top-level keys of .snapshot (does it hold file CONTENT?) ===
     52 ["messageId","timestamp","trackedFileBackups"]
  does any snapshot contain a 'content'/'text' scalar key path?

=== attachment: shape ===
      1 addedLines,addedNames,pendingMcpServers,readdedNames,removedNames,type
      1 allowedTools,type
     15 blockingError,hookEvent,hookName,toolUseID,type
      1 content,isInitial,names,skillCount,type
     50 content,itemCount,type
     12 filename,snippet,type
      1 planExists,planFilePath,type

=== system events: subtypes ===
      2 local_command
     18 turn_duration

=== thinking: is PLAINTEXT stored? (block lengths, no content) ===
  blocks: 111 | total chars: 0 | max block chars:
```

</details>

## 🤖 Assistant

Two important convention-level findings from that:

- **`file-history-snapshot` stores backup *references*, not file bodies** (`{messageId, timestamp, trackedFileBackups}`; no content/text/snippet scalar) — the checkpoint feature doesn't inline file contents into the transcript. Good.
- **Thinking is stored redacted** — 111 thinking blocks, **0 characters** of plaintext. So the model's chain-of-thought is *not* persisted (which also explains why my renderer emitted none — that was correct, not a bug). Worth knowing for your training goal: **CoT won't be in the corpus.**
- But **attachments do carry content by convention**: `filename,snippet` ×12 and `content,itemCount` ×50 — auto-attached context/file snippets can land in the transcript even without an explicit Read. And hook outputs (`blockingError` ×15) capture our `make check` dumps.

One more evidence pass — scanning for **real credential patterns** (not the English words "api key/secret", which appear in the U3 course prose) across the new jsonl and the already-pushed logs, count-only:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
realscan() {
  local f="$1"; [ -f "$f" ] || return
  local hits=0 t
  for pat in 'sk-ant-[A-Za-z0-9_-]{20}' 'sk-[A-Za-z0-9]{32}' 'gh[posru]_[A-Za-z0-9]{36}' 'AKIA[0-9A-Z]{16}' 'xox[baprs]-[A-Za-z0-9-]{10}' 'eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.' ; do
    t=$(grep -aoEc "$pat" "$f" 2>/dev/null); hits=$((hits + t))
  done
  local pk; pk=$(grep -ac 'BEGIN .*PRIVATE KEY' "$f" 2>/dev/null)
  local assign; assign=$(grep -aoEic "(password|secret|api[_-]?key|token)[\"' ]*[:=][\"' ]*[A-Za-z0-9/_+-]{12}" "$f" 2>/dev/null)
  printf "  %-38s real-key-patterns:%s  private-keys:%s  quoted-secret-assignments:%s\n" "$(basename "$f")" "$hits" "$pk" "$assign"
}
echo "=== NEW (candidate to commit) ==="; realscan log/quality-pass-session-2.jsonl
echo "=== ALREADY PUSHED (.txt logs) ==="; for f in log/*.txt; do realscan "$f"; done
```

<details><summary>tool result</summary>

```
=== NEW (candidate to commit) ===
  quality-pass-session-2.jsonl           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
=== ALREADY PUSHED (.txt logs) ===
  implementation-session-1.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-10.txt          real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-11.txt          real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-2.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:1
  implementation-session-3.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-4.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-5.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-6.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-7.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-8.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  implementation-session-9.txt           real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  quality-pass-session-1.txt             real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  quality-pass-session-2.txt             real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  spec-creation-session-1.txt            real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
  spec-creation-session-2.txt            real-key-patterns:0  private-keys:0  quoted-secret-assignments:0
```

</details>

## 🤖 Assistant

Clean. **Zero** real credential patterns and zero private keys across the new transcript *and* all 15 already-pushed logs. (One `quoted-secret-assignment` flagged in `implementation-session-2.txt` — almost certainly prose like a `password:` example; worth a 10-second eyeball, but not a key.) The earlier "apikey-ish" hits were the English words in the U3 *course content* ("keep API keys out of context", the `ANTHROPIC_API_KEY` variable *name*), not secrets.

## Security review of the transcript-capture workflow

### What the `.jsonl` contains — by convention vs by your actions
**Structural / bookkeeping (the format adds these; no secrets by design):**
- IDs (`sessionId`, `uuid`, `requestId`, …), timestamps, `version` (`2.1.158`), `userType`, `permissionMode`.
- `cwd` + `gitBranch` on every event → **discloses `/home/jj/...` and your branch names** (low-severity environment leak).
- `mode` / `ai-title` / `last-prompt` / `turn_duration` bookkeeping.
- `file-history-snapshot` → **backup references only, not file bodies.** ✓
- **No system prompt** stored (`role:system` = 0). ✓
- **Thinking redacted** (111 blocks, 0 chars) — model reasoning isn't persisted. ✓ (and so it won't be in your training corpus.)

**Content surfaces — the only places secrets can enter, all driven by the session, not the format:**
- **Your typed prompts** (the unavoidable vector you named).
- **Assistant text.**
- **`tool_use` inputs** — commands, args, Write/Edit payloads.
- **`tool_result` outputs — the biggest vector**: full command output and full file contents from `Read` (e.g., `cat .env`, `env`, a `curl` with a token).
- **Attachments** — auto-attached **file snippets** (`filename,snippet` ×12) and bulk context (`content,itemCount` ×50): repo/file content can appear even without an explicit `Read`.
- **Hook output** (`blockingError` ×15) — captured our `make check` dumps verbatim.

### Verdict on "no secrets by convention"
**The format itself injects no credential material** — confirmed: no system prompt, no env dump, snapshots are references, thinking is redacted, structural fields are IDs/paths/branch/version. Secrets can *only* arrive through session content. And empirically, **this transcript and every already-pushed log scanned clean** of real keys. So the residual risk is entirely content-driven (what you type / read / run), which is exactly the part you said we can't fully prevent — but **can** gate.

### What I'd put in place (a convention, not a hope)
1. **A secret-scan gate** — bake a real-credential scan (the count-only pattern set above, ideally `gitleaks` if you'll install it) into the capture skill *and* the pre-commit hook, run over the `.jsonl` **and** `.md`. On any hit → block the commit and report the location. Heuristic, not a guarantee (false negatives exist), but it raises the floor a lot and matches this repo's existing `tools/` + pre-commit pattern.
2. **An operational convention** (documented in the skill): in sessions you intend to publish, avoid `cat`-ing secret files or printing `env`; the scan is the backstop.
3. **Git-history discipline:** prevention-first, because once a secret is pushed, cleanup means history rewrite + force-push + **credential rotation** — far costlier than blocking it pre-commit.

### Decisions I need from you before building further
1. **The gating fact I can't check myself:** is `marlow/claude-training` a **private** repo, and is the Gitea instance internet-reachable? Severity of all of the above hinges on this.
2. **`.jsonl`-in-repo policy:** commit the **raw** `.jsonl` (complete/parseable) behind the scan gate — or commit only the rendered/truncated `.md` and keep raw transcripts local/gitignored? (You wanted raw; I'd say raw-behind-gate *if* the repo is private.)
3. **Build the secret-scan gate** into the skill + pre-commit? (I'd recommend yes regardless of #1/#2.)
4. Want me to surface the one `quoted-secret-assignment` line in `implementation-session-2.txt` so you can confirm it's benign?

I'll hold here — no skill finalization, no committing the new `.jsonl`/`.md`, and no back-fill — until you've weighed these.

## 🧑 User

The remote is a private repo, and the gitea instance is not internet-reachable. Commit the raw .jsonl after a secret-scan security gate. That gate should come in the form, at least in part, of a prompt from you for the user to check a specific line in the .jsonl file. Do that for the quoted-secret-assignment offense now.

## 🤖 Assistant

Understood — private + air-gapped Gitea lowers the severity, and the gate will be **scan + a human-in-the-loop prompt**: when the scanner flags a line, I surface that exact location for you to confirm benign-or-abort before any commit. Let me run that gate step now on the one flagged offense.

Since the real-key scan already returned **0** for this file, displaying this heuristic match is low-risk — and verifying it is the whole point of the gate:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
f=log/implementation-session-2.txt
echo "GATE: secret-scan flagged 1 'quoted-secret-assignment' in $f"
echo "Showing the exact match line(s) + context for your verification:"
echo "------------------------------------------------------------"
grep -niE "(password|secret|api[_-]?key|token)[\"' ]*[:=][\"' ]*[A-Za-z0-9/_+-]{12}" "$f" | while IFS=: read -r ln rest; do
  echo ">>> line $ln:"
  sed -n "$((ln>1?ln-1:1)),$((ln+1))p" "$f"
  echo "------------------------------------------------------------"
done
```

<details><summary>tool result</summary>

```
GATE: secret-scan flagged 1 'quoted-secret-assignment' in log/implementation-session-2.txt
Showing the exact match line(s) + context for your verification:
------------------------------------------------------------
>>> line 394:
      36 +        )                                                      
      37      return Token(access_token=create_access_token(user.id))
      38  
------------------------------------------------------------
```

</details>

## 🤖 Assistant

**Assessment: benign — clear it.** The match on line 394 is application code from a diff in that log:

```
return Token(access_token=create_access_token(user.id))
```

The heuristic fired on `token=create_access...` — but that's `taskflow-api`'s JWT auth code (a function *call* that mints a token from `user.id`), **not a credential value**. No secret, nothing to rotate. This is exactly the false-positive class the human-check step exists to clear. (And it's in an already-pushed `.txt`, so there'd be no action even if it mattered.)

That completes the gate's check on the one offense — and it demonstrates the pattern we'll bake in: **scan → surface each flagged line with location + context → you confirm benign or abort → commit only if cleared.**

Two quick confirmations before I build it:

1. **Do you clear line 394 as benign?** (My read: yes.)
2. **Scope of the gate's human prompt:** always pause for *every* heuristic hit (what we just did), or only pause for the higher-confidence patterns (real key prefixes, `BEGIN PRIVATE KEY`, etc.) and just *report* the low-confidence "quoted-assignment / word-adjacent" hits without blocking? The first is safest (nothing slips silently); the second is less noisy on logs full of auth *code* like this repo. I lean **pause-on-everything** for now since these logs are code-heavy and you're publishing them — we can relax later.

On your confirmation I'll build the gate (a `tools/scan-secrets` the capture skill and pre-commit both call) + finish the `capture-session` skill, then run the full gated flow to commit this session's raw `.jsonl` + rendered `.md`.

## 🧑 User

Yes, clear it; pause on everything

## 🤖 Assistant

Cleared — line 394 is benign (auth code, not a secret). And **pause-on-everything** it is. Let me build the gate.

First, `tools/scan-secrets` — scans given files, reports each hit as `file:line` with a tight context **window** (not the whole giant jsonl line), tagged by confidence; exits non-zero if anything matches:

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/tools/scan-secrets  (write 4159 chars, 89 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/tools/scan-secrets (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now make both tools executable and write the `capture-session` skill that orchestrates capture → render → **gate** → commit:

## 🤖 Assistant

**→ Bash**

```
chmod +x tools/scan-secrets tools/render-transcript && mkdir -p .claude/skills/capture-session && echo "ready"
```

<details><summary>tool result</summary>

```
ready
```

</details>

## 🤖 Assistant

**→ Write**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md  (write 2770 chars, 59 lines)
```

<details><summary>tool result</summary>

```
File created successfully at: /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now exercise the gate end-to-end: re-capture this session to its latest point, render, and run the scan. This both refreshes the candidate files and shows the gate's pause behavior:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
id="$CLAUDE_CODE_SESSION_ID"; src=$(find ~/.claude/projects -name "$id.jsonl")
echo "resolved files for session: $(echo "$src" | wc -l)"
cp "$src" log/quality-pass-session-2.jsonl
tools/render-transcript log/quality-pass-session-2.jsonl --out log/quality-pass-session-2.md >/dev/null
echo "=== GATE OUTPUT ==="
tools/scan-secrets log/quality-pass-session-2.jsonl log/quality-pass-session-2.md
echo "=== exit: $? (1 = hits need review) ==="
```

<details><summary>tool result</summary>

```
resolved files for session: 1
=== GATE OUTPUT ===
scan-secrets: ⚠ 9 match(es) need human review (0 high-confidence). Verify each line is benign (code/prose) or ABORT.

  · log/quality-pass-session-2.jsonl:1654:597  [secret-assignment]
      …                        \n      37      return Token(access_token=create_access_token(user.id))\n      38  \n------------------------------------…
  · log/quality-pass-session-2.jsonl:1654:1184  [secret-assignment]
      …                        \n      37      return Token(access_token=create_access_token(user.id))\n      38  \n------------------------------------…
  · log/quality-pass-session-2.jsonl:1656:346  [secret-assignment]
      …n code from a diff in that log:\n\n```\nreturn Token(access_token=create_access_token(user.id))\n```\n\nThe heuristic fired on `token=create_acce…
  · log/quality-pass-session-2.jsonl:1656:414  [secret-assignment]
      …eate_access_token(user.id))\n```\n\nThe heuristic fired on `token=create_access...` — but that's `taskflow-api`'s JWT auth code (a function…
  · log/quality-pass-session-2.jsonl:1667:819  [secret-assignment]
      …son can confirm it's benign\n(e.g. auth *code* like `access_token=create_access_token(...)`, or course prose about API keys)\nor abort. Exit code…
  · log/quality-pass-session-2.jsonl:1668:1063  [secret-assignment]
      …son can confirm it's benign\n(e.g. auth *code* like `access_token=create_access_token(...)`, or course prose about API keys)\nor abort. Exit code…
  · log/quality-pass-session-2.md:11223:34  [secret-assignment]
            37      return Token(access_token=create_access_token(user.id))
  · log/quality-pass-session-2.md:11235:20  [secret-assignment]
      return Token(access_token=create_access_token(user.id))
  · log/quality-pass-session-2.md:11238:24  [secret-assignment]
      The heuristic fired on `token=create_access...` — but that's `taskflow-api`'s JWT auth code (a function…

Nothing is committed until a human clears every line above.
=== exit: 1 (1 = hits need review) ===
```

</details>

## 🤖 Assistant

The gate works exactly as designed. **9 matches, 0 high-confidence** — and on inspection all 9 are the *same* benign string we already cleared: `access_token=create_access_token(user.id)` (taskflow-api's JWT auth — a function call, not a credential). It now echoes through this session's transcript because we *discussed* that false positive and I used it as the canonical benign example in `scan-secrets`'s own docstring. So:

- jsonl:1654/1656/1667/1668 → the diff I showed + our discussion + the scanner's docstring example
- md:11223/11235/11238 → rendered copies of the same

**Recommend: clear all 9.** They're one harmless pattern (auth code) reflected several times.

One honest note this surfaces: that heuristic (`name = …`) will *keep* firing on `access_token=create_access_token(...)`-style **code** in any transcript — it's self-perpetuating now that it's even in the scanner's docstring. Two ways to live with it, your call:
- **Keep the scanner "dumb"** and clear these few benign hits each time (safest; pause-on-everything as you chose), or
- **Refine the heuristic** to skip values that are obviously a function call (`…=word(`) rather than an opaque token — cuts this noise, with a small risk of suppressing a real `token=somesecret(` (rare).

I lean keep-it-dumb for now.

## Where this leaves us — your calls
The tooling is built and the **`capture-session` skill is registered** (it shows in the skill list now). Two things to decide before I commit anything:

1. **Clear the 9 hits?** (my read: yes — all benign auth code.)
2. **Sequencing.** Three uncommitted pieces:
   - **The capture tooling** — `tools/scan-secrets`, `tools/render-transcript`, `.claude/skills/capture-session/SKILL.md` (new infrastructure, unrelated to P7).
   - **This session's log** — `log/quality-pass-session-2.{jsonl,md}` (currently a *partial* snapshot; capturing now misses everything from this turn onward).

   Since the transcript is best captured as your **last act** (so it's complete), I'd suggest: **commit the tooling now**, and when you're done, run `/capture-session quality-pass-session-2` as the final step to produce + gate + commit the complete log. Or, if you'd rather, I can also commit the partial log checkpoint now and you re-run the skill later (it's idempotent).

   Also: we're on `spec/quality-pass-phase`. Want this capture tooling committed here, or on its own branch (it's repo infra, not P7 content)?

Tell me (1) clear or not, and (2) how you want the tooling vs. log committed and on which branch — and I'll proceed. Holding for your go.

## 🧑 User

Clear them; keep the scanner dumb; commit tooling in it's own branch then rebase back on the spec/quality-pass-phase branch when you're done. Consider the tooling a feature enhancement in terms of branch name and commit language.

## 🤖 Assistant

Clearing all 9 (benign auth code), scanner stays dumb. Now the branch dance — let me first confirm exactly what's uncommitted so I stage only the tooling (not the partial log snapshot):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== current branch ==="; git rev-parse --abbrev-ref HEAD
echo "=== status ==="; git status --short
echo "=== make check (pre-commit will run it) ==="; make check >/dev/null 2>&1 && echo GREEN || echo FAILED
```

<details><summary>tool result</summary>

```
=== current branch ===
spec/quality-pass-phase
=== status ===
?? .claude/skills/capture-session/
?? log/quality-pass-session-2.jsonl
?? log/quality-pass-session-2.md
?? log/quality-pass-session-2.txt
?? tools/render-transcript
?? tools/scan-secrets
=== make check (pre-commit will run it) ===
GREEN
```

</details>

## 🤖 Assistant

Confirmed — I'll commit only the three tooling items; all `log/*` stay untracked for the end-of-session capture. Creating the feature branch and committing the tooling there:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git checkout -b feat/session-transcript-capture
git add tools/render-transcript tools/scan-secrets .claude/skills/capture-session/SKILL.md
git commit -q -F - <<'MSG'
feat: capture full session transcripts behind a secret-scan gate

Replace the lossy /export logs (which drop most user turns on long sessions)
with a complete + readable session-archival workflow:

- tools/render-transcript: render a session .jsonl → readable Markdown (user +
  assistant turns in full, tool calls summarized, long tool output truncated,
  thinking folded; tolerant of unknown event types so a schema bump degrades
  gracefully).
- tools/scan-secrets: credential scanner — high-confidence key patterns
  (sk-ant-/AKIA/ghp_/JWT/PRIVATE KEY/…) plus heuristic assignment/word-adjacent
  patterns — reporting each hit as file:line + a context window and exiting
  non-zero. A human-reviewed gate, not an auto-redactor.
- .claude/skills/capture-session: orchestrates capture as the last act of a
  session — resolves THIS session's transcript via $CLAUDE_CODE_SESSION_ID
  (robust to concurrent sessions, not mtime), copies the raw .jsonl + renders
  the .md, runs the scan gate (pausing for human clearance of every hit), then
  commits (never pushes).

The raw .jsonl is the complete, machine-parseable record; the .md is the
human-readable view. Thinking is stored redacted by Claude Code, so none renders.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
echo "--- feature branch state ---"; git log --oneline -1; git status --short
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (51.2KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bxxc2rt6t.txt

Preview (first 2KB):
Switched to a new branch 'feat/session-transcript-capture'
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

The tooling commit landed on the feature branch (pre-commit's `make check` passed). Now integrate it back onto `spec/quality-pass-phase` as a linear fast-forward (rebase-equivalent, since the feature branched cleanly off it), and clean up:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== feat branch tip ==="; git log --oneline -1
git checkout spec/quality-pass-phase
echo "=== integrate (linear ff = rebased-back) ==="
git merge --ff-only feat/session-transcript-capture
git branch -d feat/session-transcript-capture
echo "=== result ==="
git log --oneline -3
echo "--- origin delta (local ahead; not pushed) ---"
git rev-list --count origin/spec/quality-pass-phase..HEAD 2>/dev/null
echo "--- working tree (log/* still untracked, for end-of-session capture) ---"
git status --short
```

<details><summary>tool result</summary>

```
=== feat branch tip ===
53ae9ef feat: capture full session transcripts behind a secret-scan gate
Switched to branch 'spec/quality-pass-phase'
Your branch is up to date with 'origin/spec/quality-pass-phase'.
=== integrate (linear ff = rebased-back) ===
Updating c9484aa..53ae9ef
Fast-forward
 .claude/skills/capture-session/SKILL.md |  58 ++++++++++
 tools/render-transcript                 | 184 ++++++++++++++++++++++++++++++++
 tools/scan-secrets                      |  88 +++++++++++++++
 3 files changed, 330 insertions(+)
 create mode 100644 .claude/skills/capture-session/SKILL.md
 create mode 100755 tools/render-transcript
 create mode 100755 tools/scan-secrets
Deleted branch feat/session-transcript-capture (was 53ae9ef).
=== result ===
53ae9ef feat: capture full session transcripts behind a secret-scan gate
c9484aa P7 (7.9): close-out — mark P7 complete, strike L8
965ce81 P7: add up-navigation breadcrumbs (units + index up-link)
--- origin delta (local ahead; not pushed) ---
1
--- working tree (log/* still untracked, for end-of-session capture) ---
?? log/quality-pass-session-2.jsonl
?? log/quality-pass-session-2.md
?? log/quality-pass-session-2.txt
```

</details>

## 🤖 Assistant

Done. The capture tooling is integrated cleanly:

- **`53ae9ef`** `feat: capture full session transcripts behind a secret-scan gate` now sits on `spec/quality-pass-phase` — committed on `feat/session-transcript-capture`, fast-forwarded back (linear, rebase-equivalent), and the feature branch deleted.
- Files: `tools/render-transcript`, `tools/scan-secrets`, `.claude/skills/capture-session/SKILL.md` (330 lines).
- Gate verified working: 9 hits, 0 high-confidence, all the benign `create_access_token` auth code — cleared; scanner kept dumb.
- Working tree has only the untracked `log/quality-pass-session-2.*` (left for the proper end-of-session capture).

Also closing the earlier loose end honestly: the "thinking rendered 0" wasn't a bug — Claude Code **stores thinking redacted** (111 blocks, 0 chars), so there's genuinely nothing to render. The `--thinking` flag is a no-op against current transcripts; I left it in for forward-compatibility.

## State & open choices (nothing pushed — holding per ask-before-push)
- **`spec/quality-pass-phase` is 1 commit ahead of origin** (the tooling). Say the word and I'll push.
- **Complete session log:** the `log/quality-pass-session-2.*` on disk are a *partial* snapshot. The right move is to run **`/capture-session quality-pass-session-2`** as your genuine last act — it'll re-capture to the latest point, re-run the gate (same benign hits to clear), and commit the complete `.jsonl` + `.md`. Want me to also remove the now-superseded lossy `log/quality-pass-session-2.txt` at that point?
- **Back-fill:** you wanted to wait until the rendering looked right together — it does now. Whenever you're ready, I can render complete `.md` (+ copy raw `.jsonl`) for the ~13 substantial past sessions, matching them to your `session-N` names, each behind the gate.
- **Still deferred from P7 (unrelated):** T2 dir-rename, and L1 (`ci`/`managed-settings` keys).

How would you like to proceed — push the tooling, run the final capture, start the back-fill, or stop here?

## 🧑 User

start the back-fill

## 🤖 Assistant

On it. The critical first step is the **mapping** — which `.jsonl` is which named session — and I must not guess and produce mislabeled training data. The strongest signal is your own workflow: you exported + committed each log at session end, so each committed `.txt`'s **add-date ≈ that session's end ≈ the jsonl's mtime**. Let me gather that evidence (plus each jsonl's title + first prompt as a cross-check) and propose a mapping for you to confirm before I render anything.

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== committed .txt logs: first-add commit date (≈ session end) ==="
for t in $(git ls-files log/*.txt | sort); do
  d=$(git log --diff-filter=A --format='%ad' --date=format:'%Y-%m-%d %H:%M' -- "$t" | tail -1)
  printf "  %-36s  added: %s\n" "$(basename "$t")" "$d"
done
echo
echo "=== substantial jsonls: mtime | lines | aiTitle | first human prompt (cross-check) ==="
D=~/.claude/projects/-home-jj-dev-claude-training
for f in "$D"/*.jsonl; do
  lines=$(wc -l <"$f"); [ "$lines" -lt 80 ] && continue
  mt=$(date -r "$f" +'%Y-%m-%d %H:%M')
  title=$(jq -r 'select(.aiTitle!=null)|.aiTitle' "$f" 2>/dev/null | head -1)
  fp=$(jq -r 'select(.type=="user") | (.message.content) | if type=="array" then ([.[]|select(.type=="text")|.text]|join(" ")) else (.|tostring) end' "$f" 2>/dev/null | grep -vE '^\s*$|command-name|command-message|local-command' | head -1 | tr '\n' ' ' | cut -c1-70)
  printf "  %s | %4s | %-42s | %s\n" "$mt" "$lines" "${title:0:42}" "$fp"
done | sort
```

<details><summary>tool result</summary>

```
=== committed .txt logs: first-add commit date (≈ session end) ===
  implementation-session-1.txt          added: 2026-05-30 08:13
  implementation-session-10.txt         added: 2026-05-30 20:04
  implementation-session-11.txt         added: 2026-05-30 23:19
  implementation-session-2.txt          added: 2026-05-30 08:48
  implementation-session-3.txt          added: 2026-05-30 09:34
  implementation-session-4.txt          added: 2026-05-30 10:40
  implementation-session-5.txt          added: 2026-05-30 13:15
  implementation-session-6.txt          added: 2026-05-30 14:13
  implementation-session-7.txt          added: 2026-05-30 15:56
  implementation-session-8.txt          added: 2026-05-30 17:02
  implementation-session-9.txt          added: 2026-05-30 18:02
  quality-pass-session-1.txt            added: 2026-05-31 02:04
  spec-creation-session-1.txt           added: 2026-05-30 09:34
  spec-creation-session-2.txt           added: 2026-05-30 09:34

=== substantial jsonls: mtime | lines | aiTitle | first human prompt (cross-check) ===
  2026-05-30 08:11 |  613 | Approve design and merge to main           | chat 
  2026-05-30 08:47 |  541 | Implement commit P4 on spec/tasks-phase    | chat 
  2026-05-30 09:27 |  413 | Review next steps in documentation         | chat 
  2026-05-30 09:31 |  571 | Design Claude Code expert training course  | chat 
  2026-05-30 09:33 |  347 | Continue with next phase                   | chat 
  2026-05-30 10:39 |  706 | Review implementation and next steps       | chat 
  2026-05-30 13:14 |  442 | Continue with next unit                    | chat 
  2026-05-30 14:13 |  743 | Audit the open loops                       | chat 
  2026-05-30 15:56 |  812 | Continue with next step in plan            | chat 
  2026-05-30 17:02 |  542 | Check implementation status section 3      | chat 
  2026-05-30 18:02 |  603 | Proceed with U13 implementation            | chat 
  2026-05-30 20:04 |  355 | Start plan for P6                          | chat 
  2026-05-30 23:21 |  196 | Prepare L1 verification checklist          | chat 
  2026-05-31 01:50 | 1032 | Comprehensive quality assurance review     | chat 
  2026-05-31 11:35 | 1720 | Editorial pass on U5 with reference diffs  | Base directory for this skill: /home/jj/dev/claude-training/.claude/sk
```

</details>

## 🤖 Assistant

Starting the back-fill surfaced a real problem I won't paper over: **I can't reliably auto-map jsonl → `session-N` names**, and guessing would produce a mislabeled training corpus — the opposite of the goal. Two concrete anomalies from the evidence:

1. **Add-dates cluster** — `spec-creation-session-1`, `spec-creation-session-2`, and `implementation-session-3` were all first committed at the same `09:34` (a batch commit), so "commit date = session end" breaks for those.
2. **mtimes don't order by phase** — a jsonl titled *"Design Claude Code expert training course"* has mtime `09:31`, *after* ones titled *"Implement P4"* (`08:47`) and *"Approve design and merge to main"* (`08:11`). Spec-creation can't post-date implementation, so mtime ≠ original chronology (resumes/file-touches scrambled it).

So neither add-date, mtime, nor aiTitle gives a trustworthy 1:1 to your `session-N` scheme — for the **mid/late implementation sessions the match is clean**, but the **early ones (spec-creation 1/2, impl 1–3) are ambiguous**.

The clean tight matches (high confidence, by add-date↔mtime):

| `.txt` log | jsonl (mtime, title) |
|---|---|
| implementation-session-4 | 10:39 "Review implementation and next steps" |
| implementation-session-5 | 13:14 "Continue with next unit" |
| implementation-session-6 | 14:13 "Audit the open loops" |
| implementation-session-7 | 15:56 "Continue with next step in plan" |
| implementation-session-8 | 17:02 "Check implementation status §3" |
| implementation-session-9 | 18:02 "Proceed with U13 implementation" |
| implementation-session-10 | 20:04 "Start plan for P6" |
| implementation-session-11 | 23:21 "Prepare L1 verification checklist" |
| quality-pass-session-1 | 05-31 01:50 "Comprehensive quality assurance review" |

…but the early cluster (08:11 / 08:47 / 09:27 / 09:31 / 09:33) I can't confidently assign to spec-creation-1/2 + impl-1/2/3.

**Two ways forward — your call:**

- **(A, recommended — zero mapping risk, I start now):** back-fill with **self-describing names**, e.g. `log/transcripts/2026-05-30_1413-audit-the-open-loops.{jsonl,md}` (date + aiTitle). Each file is faithfully identified by its own metadata; no guessing. Your `session-N` `.txt` logs stay as-is, and you can rename later if you want.
- **(B) Confirmed `session-N` mapping:** you resolve the early cluster (open the 5 early jsonls or tell me the order), I use your `session-N` names exactly.

Two more decisions regardless of A/B:
- **Gate batching:** for ~14 files, instead of pausing per file I'll run the gate across all of them and give you **one consolidated hit review** to clear, then commit — still reviewing every hit, just not 14 separate pauses. OK?
- **Branch:** same pattern as the tooling — do the back-fill on its own branch and fast-forward back onto `spec/quality-pass-phase`?

Which naming path (A or B), and OK to batch the gate + use a feature branch?

## 🧑 User

A, and ensure the self describing names best fit the content of the session, not just the first query; Gate batching; do the backfill on this quality pass branch and log it as part of the quality pass closeout ammendment.

## 🤖 Assistant

Got it: **A** with content-fit names (using each session's *arc*, not just its first line), **batched gate**, and on **`spec/quality-pass-phase`** as a quality-pass closeout amendment.

To name each session by what it actually *did*, let me pull each substantial session's title + the sequence of your prompts (the arc):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
D=~/.claude/projects/-home-jj-dev-claude-training
cur="$CLAUDE_CODE_SESSION_ID"
for f in "$D"/*.jsonl; do
  lines=$(wc -l <"$f"); [ "$lines" -lt 100 ] && continue
  base=$(basename "$f" .jsonl); [ "$base" = "$cur" ] && continue   # current session captured separately
  mt=$(date -r "$f" +'%m-%d_%H:%M')
  title=$(jq -r 'select(.aiTitle!=null)|.aiTitle' "$f" 2>/dev/null | head -1)
  echo "### $mt | ${lines}L | $title | ${base:0:8}"
  jq -r 'select(.type=="user" and (.message.role=="user")) | .message.content | if type=="array" then ([.[]|select(.type=="text")|.text]|join(" ")) else tostring end' "$f" 2>/dev/null \
    | grep -vE '^\s*$|command-name|command-message|local-command|system-reminder|<command|^chat$' \
    | sed 's/^[[:space:]]*//' | head -5 | cut -c1-78 | sed 's/^/    • /'
done | sort
```

<details><summary>tool result</summary>

```
    • # Prime context
    • # Prime context
    • # Prime context
    • # Prime context
    • ## Context Usage
    • **Model:** claude-opus-4-8  
    • **Tokens:** 180.6k / 1m (18%)
    • 1.
    • A venv is already active with pyyaml installed. If you need to install a pytho
    • Added 1 line, removed 1 line
    • Approve as-is.
    • Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/pri
    • Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/pri
    • Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/pri
    • Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/pri
    • Bring a fresh session up to speed on this repo before doing anything else. The
    • Bring a fresh session up to speed on this repo before doing anything else. The
    • Bring a fresh session up to speed on this repo before doing anything else. The
    • Bring a fresh session up to speed on this repo before doing anything else. The
    • Continue but wait to commit to git until this session that is meant to complet
    • Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state sur
    • Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state sur
    • Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state sur
    • Do this in order (this is `IMPLEMENTATION.md` §2's read order, with state sur
    • I
    • I have forgot to activate the proper venv prior to starting this session. Plea
    • I like these plans. Do you think it's overboard to also create a skill for the
    • I saw many errors in the console when you were trying to update files. Are you
    • I would like to use spec-driven development to create a training course that c
    • I'd like to approve the design and merge to main
    • I've added a git remote and uploaded the main branch and the previous commit o
    • Let's do the next step in the plan
    • Let's push the spec/tasks-phase branch as well
    • Pull the Security unit forward. Don't assume a fix limit of 12 units but rathe
    • Start a spec/tasks-phase branch and lets start the tasks phase
    • The intention is to use this session for both the requirements and design phas
    • Yes, let's continue to P3.
    • [Request interrupted by user for tool use]
    • [Request interrupted by user for tool use]
    • [Request interrupted by user]
… [+41 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

The trailing `sort` scrambled the per-session grouping. Let me re-run grouped (oldest-first), so each session's arc stays together — that's what I need to name by content:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
D=~/.claude/projects/-home-jj-dev-claude-training
cur="$CLAUDE_CODE_SESSION_ID"
for f in $(ls -tr "$D"/*.jsonl); do
  lines=$(wc -l <"$f"); [ "$lines" -lt 100 ] && continue
  base=$(basename "$f" .jsonl); [ "$base" = "$cur" ] && continue
  mt=$(date -r "$f" +'%m-%d_%H:%M')
  title=$(jq -r 'select(.aiTitle!=null)|.aiTitle' "$f" 2>/dev/null | head -1)
  echo "### $mt | ${lines}L | $title | ${base:0:8}"
  jq -r 'select(.type=="user" and (.message.role=="user")) | .message.content | if type=="array" then ([.[]|select(.type=="text")|.text]|join(" ")) else tostring end' "$f" 2>/dev/null \
    | grep -vE '^\s*$|command-name|command-message|local-command|system-reminder|<command|Prime context|prime-context|Base directory|Bring a fresh|Do this in order|trust the files|auto-loaded|^chat$|^I$|Request interrupted|Context Usage|Tokens:|Model:' \
    | sed 's/^[[:space:]]*//' | awk 'length>8' | head -6 | cut -c1-78 | sed 's/^/    • /'
done
```

<details><summary>tool result</summary>

```
### 05-30_08:11 | 613L | Approve design and merge to main | 7b80c621
    • I'd like to approve the design and merge to main
    • Start a spec/tasks-phase branch and lets start the tasks phase
    • A venv is already active with pyyaml installed. If you need to install a pytho
    • Yes, let's continue to P3.
    • Are we effectively tracking diversions and deferrals for session-to-session co
    • Yes, make those updates now.
### 05-30_08:47 | 541L | Implement commit P4 on spec/tasks-phase | 752dc658
    • commit P4 on spec/tasks-phase
### 05-30_09:27 | 413L | Review next steps in documentation | e841cbb1
    • what's next according to the docs?
    • commit U1 and create the lab refs
    • I've added a git remote and uploaded the main branch and the previous commit o
    • I'd like to conclude this session. Let's review our work one last time, ensure
### 05-30_09:31 | 571L | Design Claude Code expert training course spec | 60da1c88
    • I would like to use spec-driven development to create a training course that c
    • using industry tested best practices for a variety of workflows, targeting the
    • The intention is to use this session for both the requirements and design phas
    • I declined on accident. I meant to ask a question about the options. Please de
    • For Q1 I would like Option A - Markdown curriculum + hands-on labs. For Q2 I w
    • Let's discuss each requirement in turn and some alternatives that we may choos
### 05-30_09:33 | 347L | Continue with next phase | cc3dd161
    • continue with the next phase
    • Pull the Security unit forward. Don't assume a fix limit of 12 units but rathe
    • Approve as-is.
    • Continue but wait to commit to git until this session that is meant to complet
    • Please commit the changes
### 05-30_10:39 | 706L | Review implementation and next steps | a2724d32
    • check IMPLEMENTATION.md and what's next
    • start authoring U3
    • I saw many errors in the console when you were trying to update files. Are you
    • Added 1 line, removed 1 line
    • |---|---|---|
    • | 1. Requirements | `requirements.md` | ✅ **APPROVED** (2026-05-29) — revi
### 05-30_13:14 | 442L | Continue with next unit | 03472b7e
    • continue with the next unit
    • I have forgot to activate the proper venv prior to starting this session. Plea
    • add the .vscode directory into .gitignore please, then commit and push. Be sur
    • push start/u01-lab1 too to match
### 05-30_14:13 | 743L | Audit the open loops | e8c2a669
… [+48 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Clear arcs now. Per A, I'll name each by its content (using the session's whole arc, not the opening line), with a faithful `date_time` prefix for grouping, under `log/transcripts/`. Generating the raw `.jsonl` + rendered `.md` for all 14 past substantial sessions:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
D=~/.claude/projects/-home-jj-dev-claude-training
mkdir -p log/transcripts
declare -A SLUG=(
  [7b80c621]="design-approval-and-tasks-kickoff"
  [752dc658]="p4-sample-codebases"
  [e841cbb1]="u1-onboarding-labs-and-git-remote"
  [60da1c88]="requirements-and-design-spec-creation"
  [cc3dd161]="catalog-approval-and-scaffolding"
  [a2724d32]="u3-operate-safely-authoring"
  [03472b7e]="unit-authoring-and-lab-ref-pushes"
  [e8c2a669]="open-loops-audit-and-u6"
  [16a51be7]="unit-authoring-through-u10"
  [a3523ae6]="u12-commands-and-skills-dogfooding"
  [68d16797]="u13-subagents-authoring"
  [7cd46d5f]="p6-capstone-finalization"
  [d85e1257]="l1-version-key-verification"
  [44c5e90c]="quality-pass-8-lens-review-and-p7-start"
)
for id in "${!SLUG[@]}"; do
  src=$(find "$D" -name "$id*.jsonl"); [ -f "$src" ] || { echo "MISSING $id"; continue; }
  dt=$(date -r "$src" +'%Y-%m-%d_%H%M')
  name="${dt}-${SLUG[$id]}"
  cp "$src" "log/transcripts/$name.jsonl"
  tools/render-transcript "log/transcripts/$name.jsonl" --out "log/transcripts/$name.md" >/dev/null
done
echo "=== generated (sorted = roughly chronological) ==="
ls -1 log/transcripts/*.md | sed 's:.*/::; s/\.md$//'
echo "count: $(ls log/transcripts/*.jsonl | wc -l) jsonl + $(ls log/transcripts/*.md | wc -l) md"
```

<details><summary>tool result</summary>

```
=== generated (sorted = roughly chronological) ===
2026-05-30_0811-design-approval-and-tasks-kickoff
2026-05-30_0847-p4-sample-codebases
2026-05-30_0927-u1-onboarding-labs-and-git-remote
2026-05-30_0931-requirements-and-design-spec-creation
2026-05-30_0933-catalog-approval-and-scaffolding
2026-05-30_1039-u3-operate-safely-authoring
2026-05-30_1314-unit-authoring-and-lab-ref-pushes
2026-05-30_1413-open-loops-audit-and-u6
2026-05-30_1556-unit-authoring-through-u10
2026-05-30_1702-u12-commands-and-skills-dogfooding
2026-05-30_1802-u13-subagents-authoring
2026-05-30_2004-p6-capstone-finalization
2026-05-30_2321-l1-version-key-verification
2026-05-31_0150-quality-pass-8-lens-review-and-p7-start
count: 14 jsonl + 14 md
```

</details>

## 🤖 Assistant

All 14 generated. Now the **batched gate** — scanning all 28 files at once for a single consolidated review:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
out=$(tools/scan-secrets log/transcripts/*.jsonl log/transcripts/*.md); ec=$?
echo "$out" | head -1
echo
echo "=== HIGH-confidence hits (each must be verified/aborted) ==="
echo "$out" | grep -A1 '‼ HIGH' || true
echo "  -> high-confidence count: $(echo "$out" | grep -c '‼ HIGH')"
echo
echo "=== heuristic hits per file ==="
echo "$out" | grep -E '^\s+·' | grep -oE 'log/transcripts/[^:]+\.(jsonl|md)' | sort | uniq -c
echo
echo "=== heuristic hits by pattern label ==="
echo "$out" | grep -oE '\[[a-z-]+\]' | sort | uniq -c
echo "gate exit: $ec"
```

<details><summary>tool result</summary>

```
scan-secrets: ⚠ 37 match(es) need human review (0 high-confidence). Verify each line is benign (code/prose) or ABORT.

=== HIGH-confidence hits (each must be verified/aborted) ===
  -> high-confidence count: 0

=== heuristic hits per file ===
     25 log/transcripts/2026-05-30_0847-p4-sample-codebases.jsonl
      4 log/transcripts/2026-05-30_1314-unit-authoring-and-lab-ref-pushes.jsonl
      8 log/transcripts/2026-05-30_1556-unit-authoring-through-u10.jsonl

=== heuristic hits by pattern label ===
     37 [secret-assignment]
gate exit: 1
```

</details>

## 🤖 Assistant

37 heuristic hits, **0 high-confidence**, all `secret-assignment`, clustered in 3 sessions — and notably the **P4 session (25)**, which is exactly where real risk could hide since it *built taskflow-api's JWT auth*. Per the gate, here are the **distinct** matched strings (deduped, with counts) for you to verify — especially watching for any hardcoded signing secret vs. a dev placeholder:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
for f in 2026-05-30_0847-p4-sample-codebases \
         2026-05-30_1314-unit-authoring-and-lab-ref-pushes \
         2026-05-30_1556-unit-authoring-through-u10; do
  echo "===== $f.jsonl — distinct matches (count × snippet) ====="
  tools/scan-secrets "log/transcripts/$f.jsonl" --window 38 2>/dev/null \
    | grep -E '^\s{6}\S' | sed 's/^ *//' | sort | uniq -c | sort -rn
  echo
done
```

<details><summary>tool result</summary>

```
===== 2026-05-30_0847-p4-sample-codebases.jsonl — distinct matches (count × snippet) =====
      4 … password\")\n    return Token(access_token=create_access_token(user.id))\n\n\n@router.get(\"/me\", r…
      2 …st_tampered_token_is_rejected():\n    token = create_access_token(7)\n    assert decode_access_token(to…
      2 …rd\" in updates:\n        user.hashed_password = hash_password(updates.pop(\"password\"))\n    for f…
      2 …me_returns_current_user(client):\n    token = register_and_login(client, email=\"me@taskflow.test\")\n…
      2 …me=\"Demo User\",\n            hashed_password=hash_password(DEMO_PASSWORD),\n        )\n        s…
      2 …mail, full_name=\"Test User\", hashed_password=hash_password(password))\n    session.add(user)\n  …
      2 …est_expired_token_is_rejected():\n    token = create_access_token(7, expires_delta=timedelta(seconds=-1…
      2 …_name=data.full_name,\n        hashed_password=hash_password(data.password),\n    )\n    session.a…
      2 …\n\ndef test_token_round_trip():\n    token = create_access_token(42)\n    assert decode_access_token(t…
      1 …,\n        )\n    return Token(access_token=create_access_token(user.id))"},"caller":{"type":"direct"…
      1 …,\n        )\n    return Token(access_token=create_access_token(user.id))","originalFile":"\"\"\"Auth…
      1 …+        )","     return Token(access_token=create_access_token(user.id))"," "," "]}],"userModified":…
      1 … password\")\n    return Token(access_token=create_access_token(user.id))","new_string":"    user = u…
      1 … password\")\n    return Token(access_token=create_access_token(user.id))","newString":"    user = us…

===== 2026-05-30_1314-unit-authoring-and-lab-ref-pushes.jsonl — distinct matches (count × snippet) =====
      2 …mail, full_name=\"Test User\", hashed_password=hash_password(password))\n    session.add(user)\n  …
      2 …,\n        )\n    return Token(access_token=create_access_token(user.id))\n\n\n@router.get(\"/me\", r…

===== 2026-05-30_1556-unit-authoring-through-u10.jsonl — distinct matches (count × snippet) =====
      2 …st_tampered_token_is_rejected():\n    token = create_access_token(7)\n    assert decode_access_token(to…
      2 …mail, full_name=\"Test User\", hashed_password=hash_password(password))\n    session.add(user)\n  …
      2 …est_expired_token_is_rejected():\n    token = create_access_token(7, expires_delta=timedelta(seconds=-1…
      2 …\n\ndef test_token_round_trip():\n    token = create_access_token(42)\n    assert decode_access_token(t…
```

</details>

## 🤖 Assistant

All 37 are unmistakably taskflow-api **auth code** — `create_access_token(user.id)` (JWT minting), `hash_password(...)` (hashing), and token round-trip *tests*. No credential *values*, and — directly to your concern — **no hardcoded signing secret was flagged**. Let me confirm how the sample app handles its key (this is committed repo code, so no re-leak):

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
echo "=== how taskflow-api sources its JWT signing secret ==="
grep -rniE 'secret_key|jwt.*secret|getenv|environ' codebases/primary/taskflow-api/app 2>/dev/null | grep -iE 'secret|key' | head
```

<details><summary>tool result</summary>

```
=== how taskflow-api sources its JWT signing secret ===
codebases/primary/taskflow-api/app/core/config.py:4:runs out of the box for local development and tests. In a real deployment ``TASKFLOW_SECRET_KEY``
codebases/primary/taskflow-api/app/core/config.py:23:    secret_key: str = "dev-secret-change-me-in-production-0123456789"
codebases/primary/taskflow-api/app/core/security.py:42:    return jwt.encode(payload, settings.secret_key, algorithm=settings.algorithm)
codebases/primary/taskflow-api/app/core/security.py:48:        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
```

</details>

## 🤖 Assistant

**Verdict: clear all 37.** Every one is taskflow-api auth *code* — token minting (`create_access_token`), password *hashing* (`hash_password`), and round-trip *tests* — with no credential values. And the only secret-shaped string in the app is a **deliberate, self-documenting dev placeholder**:

```
app/core/config.py:  secret_key: str = "dev-secret-change-me-in-production-0123456789"   # overridable via TASKFLOW_SECRET_KEY
```

That's intentionally a non-secret default, already committed in the repo, overridable by env — not a real credential. (Worth noting the heuristic *didn't* even flag it — `secret_key` has `_key` between the word and the `=`, so it slips the pattern; a reminder the scan has false negatives. Benign here regardless.)

So: **0 high-confidence, 37 benign, no real signing secret anywhere.** Per pause-on-everything, this is your call.

**On your clearance, I'll (all on `spec/quality-pass-phase`):**
1. Commit the 28 back-fill files in `log/transcripts/`.
2. Align the `capture-session` skill to also write to `log/transcripts/` (so every complete transcript — back-fill and future — lives in one place; the legacy `.txt` exports stay in `log/`).
3. Record it as the **quality-pass closeout amendment** — a short note in `decisions.md` (P7 section), `tasks/P7-quality-pass.md`, and `IMPLEMENTATION.md` §3 that, post-close, P7 gained the session-transcript capture tooling + the historical corpus back-fill behind the secret-scan gate.
4. Stop before pushing and check with you.

Clear the 37 and say go, and I'll do 1–4.

## 🧑 User

Clear them; go

## 🤖 Assistant

Cleared — executing 1–4 on `spec/quality-pass-phase`. First, align the `capture-session` skill to write into `log/transcripts/`:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: log/<name>.jsonl
- new: log/transcripts/<name>.jsonl
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: log/<name>.md
- new: log/transcripts/<name>.md
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Add a defensive `mkdir -p` to the skill's copy step:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: ```bash
- new: ```bash
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now the closeout-amendment notes. **decisions.md** (P7 section):

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: ## Open loops & deferrals 🔓 (canonical ledger)
- new: **P7-amendment ✅ (post-close, 2026-05-31) — session-transcript corpus.** After P7 closed, added a
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**tasks/P7-quality-pass.md** (a 7.10 amendment) and **IMPLEMENTATION.md §3**:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: ## Per-unit grid
- new: ### 7.10 Closeout amendment — session-transcript corpus ✅ (post-close, 2026-05-31)
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: Committed in slices on branch **`spec/quality-pass-phase`** (not yet merged/pushed). **L8 struck**; the
- new: Committed in slices on branch **`spec/quality-pass-phase`** (not yet merged/pushed). **L8 struck**; the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify green, stage the back-fill + skill + amendment docs (leaving the current session's partial files untracked), and commit:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git add log/transcripts .claude/skills/capture-session/SKILL.md \
        specs/claude-code-mastery/decisions.md \
        specs/claude-code-mastery/tasks/P7-quality-pass.md \
        specs/claude-code-mastery/IMPLEMENTATION.md
echo "=== staged (count) ==="; git diff --cached --name-only | wc -l
echo "=== left untracked (current session, captured at end) ==="; git status --short | grep -v '^A'
```

<details><summary>tool result</summary>

```
The user doesn't want to proceed with this tool use. The tool use was rejected (eg. if it was a file edit, the new_string was NOT written to the file). To tell you how to proceed, the user said:
there is still some file cleanup we need to do before committing. We need to remove all the logs captured with "/export". I also think the rendered transcripts and and raw .jsonl files should live in separate directories. Let's update the skill if needed. All can be added to this phase and branch.
```

</details>

## 🤖 Assistant

Good cleanup instincts — the complete corpus supersedes the lossy `.txt`, and splitting raw/rendered is cleaner. All on this branch. Let me reorganize and purge first:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
# 1. Split raw vs rendered into separate dirs
mkdir -p log/transcripts/raw log/transcripts/rendered
mv log/transcripts/*.jsonl log/transcripts/raw/ 2>/dev/null
mv log/transcripts/*.md   log/transcripts/rendered/ 2>/dev/null
# 2. Remove the lossy /export logs (14 tracked + 1 untracked) and the stale flat partial captures
git rm -q --ignore-unmatch log/*.txt
rm -f log/*.txt log/quality-pass-session-2.jsonl log/quality-pass-session-2.md
echo "=== log/ tree now ==="; find log -type f | sort
echo "counts -> raw: $(ls log/transcripts/raw/*.jsonl 2>/dev/null | wc -l)  rendered: $(ls log/transcripts/rendered/*.md 2>/dev/null | wc -l)"
```

<details><summary>tool result</summary>

```
=== log/ tree now ===
log/transcripts/raw/2026-05-30_0811-design-approval-and-tasks-kickoff.jsonl
log/transcripts/raw/2026-05-30_0847-p4-sample-codebases.jsonl
log/transcripts/raw/2026-05-30_0927-u1-onboarding-labs-and-git-remote.jsonl
log/transcripts/raw/2026-05-30_0931-requirements-and-design-spec-creation.jsonl
log/transcripts/raw/2026-05-30_0933-catalog-approval-and-scaffolding.jsonl
log/transcripts/raw/2026-05-30_1039-u3-operate-safely-authoring.jsonl
log/transcripts/raw/2026-05-30_1314-unit-authoring-and-lab-ref-pushes.jsonl
log/transcripts/raw/2026-05-30_1413-open-loops-audit-and-u6.jsonl
log/transcripts/raw/2026-05-30_1556-unit-authoring-through-u10.jsonl
log/transcripts/raw/2026-05-30_1702-u12-commands-and-skills-dogfooding.jsonl
log/transcripts/raw/2026-05-30_1802-u13-subagents-authoring.jsonl
log/transcripts/raw/2026-05-30_2004-p6-capstone-finalization.jsonl
log/transcripts/raw/2026-05-30_2321-l1-version-key-verification.jsonl
log/transcripts/raw/2026-05-31_0150-quality-pass-8-lens-review-and-p7-start.jsonl
log/transcripts/rendered/2026-05-30_0811-design-approval-and-tasks-kickoff.md
log/transcripts/rendered/2026-05-30_0847-p4-sample-codebases.md
log/transcripts/rendered/2026-05-30_0927-u1-onboarding-labs-and-git-remote.md
log/transcripts/rendered/2026-05-30_0931-requirements-and-design-spec-creation.md
log/transcripts/rendered/2026-05-30_0933-catalog-approval-and-scaffolding.md
log/transcripts/rendered/2026-05-30_1039-u3-operate-safely-authoring.md
log/transcripts/rendered/2026-05-30_1314-unit-authoring-and-lab-ref-pushes.md
log/transcripts/rendered/2026-05-30_1413-open-loops-audit-and-u6.md
log/transcripts/rendered/2026-05-30_1556-unit-authoring-through-u10.md
log/transcripts/rendered/2026-05-30_1702-u12-commands-and-skills-dogfooding.md
log/transcripts/rendered/2026-05-30_1802-u13-subagents-authoring.md
log/transcripts/rendered/2026-05-30_2004-p6-capstone-finalization.md
log/transcripts/rendered/2026-05-30_2321-l1-version-key-verification.md
log/transcripts/rendered/2026-05-31_0150-quality-pass-8-lens-review-and-p7-start.md
counts -> raw: 14  rendered: 14
```

</details>

## 🤖 Assistant

Now update the skill to the split layout:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: log/transcripts/<name>.jsonl
- new: log/transcripts/raw/<name>.jsonl
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: log/transcripts/<name>.md
- new: log/transcripts/rendered/<name>.md
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: mkdir -p log/transcripts
- new: mkdir -p log/transcripts/raw log/transcripts/rendered
```

## 🧑 User

and also make sure that the raw transcripts are not removed if running from a session that does not have the raw .jsonl file, as is the case if I were to work on this repo from a different command-line on a different machine.

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated. All occurrences were successfully replaced. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Important robustness point — on a different machine, `$CLAUDE_CODE_SESSION_ID` resolves to a session whose `.jsonl` isn't local, and the committed corpus must never be clobbered or pruned. Let me read the current skill and harden it:

## 🤖 Assistant

**→ Read**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
```

<details><summary>tool result</summary>

```
1	---
2	name: capture-session
3	description: >
4	  Capture the CURRENT Claude Code session's full transcript into this repo's log/ — copy the raw
5	  .jsonl (complete, machine-parseable), render a human-readable .md, run the secret-scan gate
6	  (pausing for human review of every flagged line), and commit on clearance. Use as the last act
7	  of a session; it replaces the lossy /export workflow. Invoke as: /capture-session <name>
8	---
9	
10	# Capture session transcript
11	
12	Archive this session into `log/` — **complete** (raw `.jsonl`) and **readable** (`.md`) — behind a
13	secret-scan gate. Do the steps in order. **Never skip or auto-pass the gate (step 4).**
14	
15	## 1. Resolve THIS session's transcript (robust to concurrent sessions)
16	Identify the file by session id from the environment — never by mtime (another session in this repo
17	could be newer):
18	```bash
19	id="$CLAUDE_CODE_SESSION_ID"
20	src=$(find ~/.claude/projects -name "$id.jsonl")
21	```
22	If `$id` is empty, or `find` returns anything other than exactly one path, **STOP and report** — do
23	not guess which file is ours.
24	
25	## 2. Name the outputs
26	Use the argument `$1` as `<name>` (e.g. `quality-pass-session-3`). If absent, default to
27	`<YYYY-MM-DD>-<short-slug>` derived from the session's `aiTitle` (fall back to the id prefix).
28	Targets: `log/transcripts/raw/<name>.jsonl` (raw) and `log/transcripts/rendered/<name>.md` (rendered). Re-running **overwrites** both —
29	it's idempotent and captures up to the latest flushed point. (The act of capturing can't capture its
30	own trailing lines; that's expected.)
31	
32	## 3. Copy raw + render readable
33	```bash
34	mkdir -p log/transcripts/raw log/transcripts/rendered
35	cp "$src" "log/transcripts/raw/<name>.jsonl"
36	tools/render-transcript "log/transcripts/raw/<name>.jsonl" --out "log/transcripts/rendered/<name>.md"
37	```
38	The raw `.jsonl` is the complete record; the `.md` folds thinking and truncates long tool output for
39	readability (Claude Code stores thinking redacted, so the `.md` shows none).
40	
… [+20 more lines — full output in the .jsonl]
```

</details>

## 🤖 Assistant

Now harden it against the cross-machine clobber. Three changes: an explicit non-destructive contract, a clean STOP when the local source is absent, and a no-clobber guard that refuses to overwrite a file belonging to a *different* session.

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: Archive this session into `log/` — **complete** (raw `.jsonl`) and **readable** (`.md`) — behind a
- new: Archive this session into `log/transcripts/` — **complete** (raw `.jsonl` in `raw/`) and **readable**
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: If `$id` is empty, or `find` returns anything other than exactly one path, **STOP and report** — do
- new: If `$id` is empty, or `find` returns anything other than exactly one path — e.g. you're on a different
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: Targets: `log/transcripts/raw/<name>.jsonl` (raw) and `log/transcripts/rendered/<name>.md` (rendered). Re-running **overwrites** both —
- new: Targets: `log/transcripts/raw/<name>.jsonl` and `log/transcripts/rendered/<name>.md`. Re-running for the
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: ```bash
- new: ```bash
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

The amendment notes I drafted now say the wrong thing (flat dir; ".txt remain"). Let me correct them to the split layout + `.txt` removed. **decisions.md**:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md
- old: concurrent sessions — copies the raw `.jsonl` + renders the `.md` into `log/transcripts/`, runs the
- new: concurrent sessions — copies the raw `.jsonl` into `log/transcripts/raw/` + renders the `.md` into
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/decisions.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**tasks/P7-quality-pass.md** and **IMPLEMENTATION.md §3**:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md
- old: `capture-session` skill) and **back-filled the 14 substantial historical sessions** into
- new: `capture-session` skill — non-destructive, robust to multi-machine/concurrent sessions) and
```

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md
- old: (`tools/render-transcript`, `tools/scan-secrets`, the `capture-session` skill) and back-filled the 14
- new: (`tools/render-transcript`, `tools/scan-secrets`, the `capture-session` skill) and back-filled the 14
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/tasks/P7-quality-pass.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/specs/claude-code-mastery/IMPLEMENTATION.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

Now verify, stage everything (new transcripts, `.txt` deletions, skill, amendment docs), and commit:

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
make check >/dev/null 2>&1 && echo "CHECK GREEN" || echo "CHECK FAILED"
git add -A log/ .claude/skills/capture-session/SKILL.md \
        specs/claude-code-mastery/decisions.md \
        specs/claude-code-mastery/tasks/P7-quality-pass.md \
        specs/claude-code-mastery/IMPLEMENTATION.md
echo "=== staged summary ==="
git diff --cached --stat | tail -3
echo "added:$(git diff --cached --name-status | grep -c '^A')  deleted:$(git diff --cached --name-status | grep -c '^D')  modified:$(git diff --cached --name-status | grep -c '^M')"
echo "=== any stray untracked left? ==="; git status --short | grep -vE '^[AMD] ' || echo "(none — clean staging)"
```

<details><summary>tool result</summary>

```
CHECK GREEN
=== staged summary ===
 specs/claude-code-mastery/decisions.md             |   19 +
 specs/claude-code-mastery/tasks/P7-quality-pass.md |    9 +
 46 files changed, 67284 insertions(+), 32960 deletions(-)
added:28  deleted:14  modified:4
=== any stray untracked left? ===
(none — clean staging)
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git commit -q -F - <<'MSG'
P7 closeout amendment: session-transcript corpus (back-fill + capture workflow)

Archive the build's sessions completely, replacing the lossy /export logs:

- Back-filled the 14 substantial historical sessions into log/transcripts/,
  split by form: raw/ (complete .jsonl) and rendered/ (readable .md), with
  self-describing date+content names. Each passed the secret-scan gate
  (0 high-confidence hits; the 37 heuristic flags were all taskflow-api auth
  code + the documented dev `secret_key` placeholder — no real credentials).
- Removed the 14 superseded /export .txt logs.
- Hardened the capture-session skill: writes raw→log/transcripts/raw,
  rendered→log/transcripts/rendered; non-destructive (only adds/refreshes the
  current session's own pair, never prunes the corpus); resolves the session via
  $CLAUDE_CODE_SESSION_ID and STOPS cleanly if the source .jsonl isn't local
  (e.g. a different machine); refuses to overwrite a different session's file on
  a name collision — so cross-machine captures can't clobber the corpus.
- Recorded as the P7 closeout amendment in decisions.md (P7-amendment),
  tasks/P7-quality-pass.md (7.10), and IMPLEMENTATION.md §3. Does not reopen L8.

make check green. Branch spec/quality-pass-phase, local only (not pushed).

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -5 && echo "---" && git status --short && echo "(clean if empty)"
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (51.3KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bl54cam7p.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git log --oneline -4
echo "---"; git status --short && echo "(working tree clean if nothing above)"
echo "--- local ahead of origin by ---"; git rev-list --count origin/spec/quality-pass-phase..HEAD
```

<details><summary>tool result</summary>

```
1c20389 P7 closeout amendment: session-transcript corpus (back-fill + capture workflow)
53ae9ef feat: capture full session transcripts behind a secret-scan gate
c9484aa P7 (7.9): close-out — mark P7 complete, strike L8
965ce81 P7: add up-navigation breadcrumbs (units + index up-link)
---
(working tree clean if nothing above)
--- local ahead of origin by ---
2
```

</details>

## 🤖 Assistant

Done — `1c20389` landed, working tree clean.

## Back-fill complete
- **`log/transcripts/`** now holds the corpus, split by form: **`raw/`** (14 `.jsonl`, complete) + **`rendered/`** (14 `.md`, readable), all self-describing date+content names.
- **14 lossy `.txt` exports removed**; the stale flat partials too.
- **`capture-session` skill hardened** — writes to `raw/`+`rendered/`; **non-destructive** (only adds/refreshes the current session's own pair, never prunes); **STOPs cleanly if the source `.jsonl` isn't local** (e.g. a different machine); and **refuses to overwrite a different session's file on a name collision** — so a capture from another clone can't clobber the corpus.
- Recorded as the **P7 closeout amendment** in `decisions.md` (P7-amendment), `tasks/P7-quality-pass.md` (7.10), and `IMPLEMENTATION.md` §3. L8 stays closed.
- `make check` green throughout.

**`spec/quality-pass-phase` is now 2 commits ahead of origin** (the capture tooling `53ae9ef` + this amendment `1c20389`) — not pushed.

## What's left
- **This session's own log:** the back-fill captured the *prior* quality-pass session (the `01:50` one). **This** session isn't archived yet — run **`/capture-session <name>`** as your genuine last act. One naming note: since we've moved to self-describing names, I'd suggest something like `…-p7-rollout-and-transcript-capture-tooling` rather than the legacy `quality-pass-session-2`, to match the back-fill scheme. The skill will gate it (expect the same benign `create_access_token` hits to clear) and commit it.
- **Push** the 2 ahead commits — whenever you give the go.
- **Still deferred (unrelated):** T2 dir-rename, L1 (`ci`/`managed-settings` keys).

Want me to run the final `/capture-session` for this session now, push, or stop here?

## 🧑 User

For the "/capture" skill, will it be clear to you that if no name is given as an argument to the skill, the name should be the session arc similar to what we've done to the backfilled logs in this session?

## 🤖 Assistant

Honestly — **no, as written it wouldn't reliably make me do that.** Step 2 currently says the default is *"derived from the session's `aiTitle`"* and even examples `quality-pass-session-3` (the legacy scheme). The back-fill did something better: for vague aiTitles like *"Continue with next unit"* I derived the slug from the **whole session arc** (→ `unit-authoring-through-u10`). The current wording points at the wrong source and the wrong example, so future-me might just slugify a vague aiTitle. Let me fix it to be explicit:

## 🤖 Assistant

**→ Edit**

```
/home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md
- old: Use the argument `$1` as `<name>` (e.g. `quality-pass-session-3`). If absent, default to
- new: If the argument `$1` is given, use it verbatim as `<name>`. **If absent, derive a self-describing name
```

<details><summary>tool result</summary>

```
The file /home/jj/dev/claude-training/.claude/skills/capture-session/SKILL.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training
git add .claude/skills/capture-session/SKILL.md
git commit -q -F - <<'MSG'
capture-session: derive the default name from the session arc, not just aiTitle

When no name arg is given, the skill now instructs deriving a self-describing
<YYYY-MM-DD_HHMM>-<slug> where the slug summarizes what the whole session did
(matching the back-fill style: p4-sample-codebases, unit-authoring-through-u10,
…) — explicitly not the raw aiTitle (often vague) or just the first prompt.

Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
MSG
git log --oneline -1; git status --short && echo "(clean)"
```

<details><summary>tool result</summary>

```
<persisted-output>
Output too large (51KB). Full output saved to: /home/jj/.claude/projects/-home-jj-dev-claude-training/18010791-8af3-4a98-aaba-9b5373df76eb/tool-results/bx1q60va3.txt

Preview (first 2KB):
pre-commit: running make check…
  PASS  course/units/01-onboarding-first-win/unit.md: front matter valid (U1)
  PASS  course/units/02-explore-a-codebase/unit.md: front matter valid (U2)
  PASS  course/units/03-operate-safely/unit.md: front matter valid (U3)
  PASS  course/units/04-memory-and-context/unit.md: front matter valid (U4)
  PASS  course/units/05-ship-a-feature/unit.md: front matter valid (U5)
  PASS  course/units/06-tdd/unit.md: front matter valid (U6)
  PASS  course/units/07-debug-a-failure/unit.md: front matter valid (U7)
  PASS  course/units/08-git-and-pr/unit.md: front matter valid (U8)
  PASS  course/units/09-onboard-refactor-legacy/unit.md: front matter valid (U9)
  PASS  course/units/10-spec-driven-dev/unit.md: front matter valid (U10)
  PASS  course/units/11-code-and-security-review/unit.md: front matter valid (U11)
  PASS  course/units/12-commands-and-skills/unit.md: front matter valid (U12)
  PASS  course/units/13-subagents/unit.md: front matter valid (U13)
  PASS  course/units/14-hooks/unit.md: front matter valid (U14)
  PASS  course/units/15-mcp-and-vetting/unit.md: front matter valid (U15)
  PASS  course/units/16-automate-and-scale/unit.md: front matter valid (U16)
check-frontmatter: OK
  PASS  every capability home_unit resolves to a unit
  PASS  every can-do is advanced by >=1 catalog unit
  PASS  every catalog 'advances' id is a real can-do
  PASS  every coverage 'covered_by' references a real unit
  PASS  every unit covers >=1 coverage area
  PASS  all nine workflows (W1–W9) are mapped to a unit
  PASS  16 authored unit(s) consistent with catalog declarations
check-coverage: OK
render-checklist: progress-checklist.md is in sync with the capability map
  PASS  course/units/01-onboarding-first-win/unit.md: in sync with unit.src.md
  PASS  course/units/02-explore-a-codebase/unit.md: in sync with unit.src.md
  PASS  course/units/03-operate-safely/unit.md: in sync with unit.src.md
...
</persisted-output>
```

</details>

## 🤖 Assistant

**→ Bash**

```
cd /home/jj/dev/claude-training; git log --oneline -1; git status --short && echo "(clean)"
```

<details><summary>tool result</summary>

```
135b4a9 capture-session: derive the default name from the session arc, not just aiTitle
(clean)
```

</details>

## 🤖 Assistant

Fixed and committed (`135b4a9`). Now it's unambiguous: with **no name arg**, the skill tells me to derive `<YYYY-MM-DD_HHMM>-<slug>` where the **slug summarizes the whole session's arc** — explicitly *not* the raw `aiTitle` (flagged as often-vague, with "Continue with next unit" as the cautionary example) and *not* just the first prompt — and it anchors me with the actual back-fill names (`p4-sample-codebases`, `unit-authoring-through-u10`, …) as the target style. So a future me (or a fresh session) will reproduce the back-fill naming convention rather than slugifying a vague title.

`spec/quality-pass-phase` is now **3 commits ahead of origin** (`53ae9ef` tooling, `1c20389` back-fill amendment, `135b4a9` naming fix), tree clean.

Open, on your word:
- **Final capture of this session** — `/capture-session` with no arg now would auto-name it from the arc (something like `2026-05-31_HHMM-p7-rollout-transcript-capture-tooling`); or pass a name explicitly.
- **Push** the 3 ahead commits.
- Deferred: T2, L1.

## 🧑 User

<command-message>capture-session</command-message>
<command-name>/capture-session</command-name>

## 🧑 User

Base directory for this skill: /home/jj/dev/claude-training/.claude/skills/capture-session

# Capture session transcript

Archive this session into `log/transcripts/` — **complete** (raw `.jsonl` in `raw/`) and **readable**
(`.md` in `rendered/`) — behind a secret-scan gate. Do the steps in order. **Never skip or auto-pass
the gate (step 4).**

**Non-destructive contract:** this skill only ever **adds or refreshes the current session's own
pair**. It must **never delete, prune, or "reconcile"** anything else under `log/transcripts/` — the
corpus includes sessions captured on *other machines*, whose source `.jsonl` is not present here.

## 1. Resolve THIS session's transcript (robust to concurrent sessions)
Identify the file by session id from the environment — never by mtime (another session in this repo
could be newer):
```bash
id="$CLAUDE_CODE_SESSION_ID"
src=$(find ~/.claude/projects -name "$id.jsonl")
```
If `$id` is empty, or `find` returns anything other than exactly one path — e.g. you're on a different
machine/clone that never ran this session, so its `.jsonl` isn't local — **STOP and report, making no
changes.** Do not guess which file is ours, and do not touch the existing corpus.

## 2. Name the outputs
If the argument `` is given, use it verbatim as `<name>`. **If absent, derive a self-describing name
yourself**: `<YYYY-MM-DD_HHMM>-<slug>`, where the date/time comes from the transcript
(`date -r "$src" +'%Y-%m-%d_%H%M'`) and the **slug summarizes what the session actually *did* across
its whole arc** — not just the first prompt, and *not* the raw `aiTitle` (often vague, e.g. "Continue
with next unit"). Skim the session's prompt sequence and the work done, then write a concise
lowercase-kebab slug in the style of the back-filled logs — e.g. `p4-sample-codebases`,
`open-loops-audit-and-u6`, `unit-authoring-through-u10`, `u13-subagents-authoring`. Treat `aiTitle`
as a hint only.
Targets: `log/transcripts/raw/<name>.jsonl` and `log/transcripts/rendered/<name>.md`. Re-running for the
**same** session overwrites its own pair (idempotent — captures up to the latest flushed point; the act
of capturing can't capture its own trailing lines). Step 3 **refuses** to overwrite a file that belongs
to a *different* session (a name collision), so a capture from another machine can't clobber the corpus.

## 3. Copy raw + render readable
```bash
mkdir -p log/transcripts/raw log/transcripts/rendered
dst="log/transcripts/raw/<name>.jsonl"
# No-clobber: only write if the target is absent or already belongs to THIS session.
if [ -f "$dst" ] && ! grep -q "\"sessionId\":\"$id\"" "$dst"; then
  echo "REFUSING: $dst exists for a different session — choose a different <name>."; exit 1
fi
cp "$src" "$dst"
tools/render-transcript "$dst" --out "log/transcripts/rendered/<name>.md"
```
The raw `.jsonl` is the complete record; the `.md` folds thinking and truncates long tool output for
readability (Claude Code stores thinking redacted, so the `.md` shows none).

## 4. SECRET-SCAN GATE — pause on everything
```bash
tools/scan-secrets "log/transcripts/raw/<name>.jsonl" "log/transcripts/rendered/<name>.md"
```
- **Exit 0 (clean):** proceed to step 5.
- **Exit 1 (hits):** **STOP — do not commit.** Surface *every* reported `file:line` + context window
  to the user and ask them to confirm each is benign (auth *code*, course prose about secrets, etc.)
  or to abort. Treat any **HIGH**-confidence hit as a presumed-real credential until the user clears
  it — and if it is real, the fix is abort + rotate, not commit. Continue only after the user
  explicitly clears **all** hits. The gate is heuristic (false negatives possible); the human review
  is the real control.

## 5. Commit (do NOT push)
After clean or fully cleared:
```bash
git add "log/transcripts/raw/<name>.jsonl" "log/transcripts/rendered/<name>.md"
git commit -m "Add <name> session log (raw transcript + rendered)"
```
Report what was written and committed. **Ask before pushing** (repo rule: confirm before any push).
