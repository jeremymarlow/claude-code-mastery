# Content review — examples-critic
Reviewer: examples-critic — show-vs-tell audit of demonstration density
Date: 2026-06-09
Scope read: all 16 rendered units + requirements §1 + workflows.md + learner docs

## Headline

The course tells far more than it shows, and it shows least exactly where the stakes are highest. Across ~3,300 lines of unit prose there are **6 fenced code blocks, 1 demonstration table, 1 simulated Claude reply, ~20 quoted sample prompts, ~6 inline bad-vs-good contrast pairs, 0 diagrams, 0 annotated transcripts, and 0 diffs** — in a course whose single load-bearing habit is "read the diff." The four Daily Driver workflow units (U5–U8), the flagship of the curriculum, contain **zero** code blocks, zero sample tool output, and worked examples that are narrations about the course's own build rather than walked instances of the taught skill. By contrast the Autonomy units (U13–U16) demonstrate genuinely well — inline artifacts, real output, drive-it-yourself verification — which proves the authors know how to do this and simply didn't apply it to the workflow units. For an audience defined as "skeptical of AI output and wants to learn to *verify*, not merely *trust*" (requirements.md:31), assertion without instance is exactly the writing this persona discounts.

## Demonstration inventory

Forms found across all 16 units (Worked example + Concept + Pitfalls prose; lab steps counted only where they embed a demonstration):

| Form | Count | Where |
|---|---|---|
| Fenced code blocks | 6 | U1 (doctor commands), U3 (one `claude --permission-mode plan` line), U13 (`--agents` JSON), U14 (hook `settings.json`), U15 (mcp add/get/remove + output), U16 (headless + worktree commands) |
| Simulated Claude/tool output | 3 | U2 (architecture-summary blockquote — the only simulated Claude *reply* in the course), U13 (one inline sample report line), U15 (`✓ Connected`) |
| Demonstration tables | 1 | U3 task→posture→why table (unit.md:131–136) |
| Quoted sample prompts the learner could type | ~20 | concentrated in U1 (2), U2 (6), U4 (4), U13 (4); U7, U8, U9, U12, U14 have **none** |
| Inline bad-vs-good contrast pairs | ~6 | U2 ×2 (question phrasing), U8 ×1 (commit message), U10 ×2 (requirement wording), U12 ×1 (skill description) |
| Annotated real artifacts walked in prose | ~7 | U4 (root CLAUDE.md), U12 (close-unit/prime-context), U14 (check-on-edit), U15 (taskflow_mcp.py), U10 (specs/ tree), U9 (_common.py), U16 (checks.yml) |
| Diffs shown | **0** | — |
| Example plan-mode plans | **0** | one parenthetical sketch in U5:104–105 |
| Sample test/failure output | **0** | — |
| Annotated transcripts / dialogues | **0** | — |
| Diagrams | **0** | — |

Per-unit distribution (code blocks / sample prompts / simulated output / contrast pairs):

| U1 | U2 | U3 | U4 | U5 | U6 | U7 | U8 | U9 | U10 | U11 | U12 | U13 | U14 | U15 | U16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1/2/0/0 | 0/6/1/2 | 1/2/0/0 | 0/4/0/0 | 0/1/0/0 | 0/2/0/0 | 0/0/0/0 | 0/0/0/1 | 0/0/0/0 | 0/1/0/2 | 0/1/0/0 | 0/0/0/1 | 1/4/1/0 | 1/0/0/0 | 1/1/1/0 | 1/1/0/0 |

U7 and U9 — the two longest-lab, highest-difficulty Daily Driver/Force Multiplier units — contain **zero** of every demonstration form except prose description.

## Cross-cutting findings

**F1 — The course never shows a single diff, while "read the diff" is its stated number-one skill.** Evidence: U1 claims "This 30-second habit — not the passing check — is the actual skill this unit teaches" (01-onboarding-first-win/unit.md:143), and grep confirms zero diff blocks in any unit. The learner is told what to check in a diff (U1:140–143 gives criteria a/b/c) but never shown one — not even the one-line `/health` diff the criteria describe, and never a realistic 30-line diff with a smuggled extra change to practice spotting. For a skeptical senior engineer, a habit asserted 16 times but never once demonstrated reads as a slogan. Severity: **high**.

**F2 — Plan mode, "the unit's central tool" (U5), is never shown: no plan, good or bad, appears anywhere.** Evidence: U5 says "Make Claude show you: which files it will touch, what the new behavior is, and how it'll be tested. **Then actually review it.**" (05-ship-a-feature/unit.md:70–71) — but the only plan in the entire course is a one-line parenthetical sketch ("*new `ProjectStats` schema, a `project_task_stats` service function, one route…*", U5:104–105). The pitfall "Rubber-stamping the plan" (U5:165) and the skill "reject or redirect a bad plan" (U5:26–28) are pure assertion: the learner has never seen what a vague plan looks like, what a wrong-layer plan looks like, or what a redirect message says. The learner reaches the lab's step 3 ("Review it against the contract") with no model of what they're reviewing for. Severity: **high**.

**F3 — The "Worked example" sections of U5–U9 and U11 are course-build anecdotes or artifact pointers, not walked instances of the skill.** Inventory of all 16 worked examples: genuinely walked — U2 (sample summary + which claim to verify), U13 (full agent JSON + brief + returned report + spot-check), U14 (hook config + wrapper walk), U15 (commands + output + trust contrast), U16 (CI walk + command block), U12 (annotated real artifacts), U3 (posture table), U4 (annotated CLAUDE.md). Not walked — U5 ("This repository is itself a worked example… when this course's maintainers add an endpoint, they have Claude read… propose a plan… then implement and verify", 05:99–106 — a description of a process, no artifact of it); U6 (a *hypothetical*: "The way to add such a check is to first write the failing case", 06:108–110 — no test code, no red output); U7 (a war story about `check-version-refs`, 07:101–110 — narrative with no transcript, command, or line of code); U8 ("Run `git log --oneline` in this repo and you'll see the pattern", 08:106 — homework, not an example; not even five lines of the log are excerpted); U11 (another war story about the same `vd:` false positive as U7, 11:117–125); U1 (demonstrates `doctor`, not the unit's actual skill of verifying a change); U9 (points at `_common.py` with explanation but no before/after). Six of sixteen "Worked example" headers do not contain a worked example. Severity: **high**.

**F4 — TDD's defining skill — "red for the right reason" — is taught without ever showing a red.** Evidence: U6 devotes its name, an objective, a concept section (06-tdd/unit.md:72–79), a lab step, and a pitfall to distinguishing "an *assertion* failure — 'expected 2 overdue tasks, got 5'" from "a typo, a bad import… a test that errors during collection" — but no pytest output of either kind appears. One quoted fragment is the entire demonstration. A senior engineer knows pytest; what they need shown is which *features of the output* to key on with an AI in the loop, side by side. The same gap repeats in U7: the root-cause line ("compares the stored date (ISO `YYYY-MM-DD`) against today rendered as `MM-DD-YYYY`, as plain strings", 07:78–80) is described but the actual buggy line of code is never excerpted — in a unit about finding a specific line. Severity: **high**.

**F5 — Common pitfalls are ~95% asserted, almost never instantiated.** Across 16 units there are ~85 pitfall bullets; nearly all name a failure abstractly ("Rubber-stamping the plan", "The aspirational PR description", "An unscoped brief") without one concrete instance. The honourable exceptions prove the value: U11's false positive is fully concrete (`Project.archived == False` / E712 / why `is False` breaks the query — 11:92–94) and is the most memorable pitfall in the course; U12's "$1 is the SECOND arg" gotcha is concrete. Compare U8's "aspirational PR description… including the test you meant to write but didn't" (08:79–82): no example PR body, bad or good, is shown anywhere — a four-line pair would nail it. Severity: **medium** (broad but individually cheap to fix).

**F6 — workflows.md promises that units carry the concrete prompts, and most units don't.** Evidence: meta/workflows.md:34–35 — "Units link here and add only the unit-specific application (the concrete prompts and the lab)." The nine W-patterns themselves are pure assertion (correct for a generalized reference), but the deferral contract is only honored by U2 and U13. U7 (W3), U8 (W4), U9 (W5/W8) add *zero* quoted prompts; the learner gets the abstract pattern twice (workflows.md + unit Concept restating it) and the instance zero times. Severity: **medium**.

**F7 — The dogfooding worked examples demonstrate the wrong instance: the course's build, not the learner's task.** U5, U6, U7, U8, U10, U11 all reach for "this repo itself" as the example. That's a defensible authenticity move for U10 (the spec tree genuinely is the artifact being taught) and U14 (the hook is directly imitable), but for the workflow units it substitutes *provenance* for *demonstration*: "we debugged a checker this way once" (U7) gives the learner nothing to imitate on `taskflow-cli`. It also makes several worked examples unreadable without leaving the unit (U8's `git log`, U9's `_common.py`, U10's whole spec tree) — the unit page itself shows nothing. Notably, U10's lab asks for a *miniature* spec, but the only exemplar is a 15-requirement production spec; no scaled-down sample requirement set for "task dependencies" is shown, so the learner can't calibrate size. Severity: **medium**.

**F8 — Zero diagrams in a course full of spatial/structural claims.** The agentic loop (U1), context-window composition (U4), the three-layer defense in depth (U14/U16), subagent-vs-main-context isolation (U13), and the W1 loop with its two gates are all shape-shaped ideas delivered as paragraphs. Even one ASCII diagram per stage would help, and CommonMark permits it (R15 forbids meaning by color/emoji, not diagrams). Severity: **low** (prose is competent; this is leverage, not a defect).

## Per-unit notes

- **U1** — Shows doctor commands; the worked example demonstrates *doctor*, not the verified-change skill. The diff-read criteria (143) are concrete but the diff itself is never shown. Half-demonstrates.
- **U2** — **Demonstrates well**: simulated Claude summary (74–90), six typeable prompts, two question contrast pairs, and a named load-bearing claim to verify. The model the other prose units should have followed.
- **U3** — The posture table (131–136) is a real demonstration and the injection text is quoted; but "recognize prompt injection" never shows an actual embedded payload in the prose (deferred entirely to the lab fixture).
- **U4** — Good annotated specimen (root CLAUDE.md) and a concrete convention line to add (150–152); never shows a *bad* CLAUDE.md or the before/after answer pair the lab promises ("note how specific the answer is" — no sample answer given).
- **U5** — Worst show/tell ratio relative to importance: flagship workflow, zero code blocks, no plan ever shown, worked example is a process description of the maintainers' habits (99–106).
- **U6** — All assertion: hypothetical worked example, no test code, no red output, no cheat-implementation snippet (the `<=` off-by-one is described, never shown).
- **U7** — Zero demonstrations of any form. The buggy comparison, the repro session, the "convince me" exchange — all described, none shown.
- **U8** — One good inline commit-message pair (72–74); otherwise pointers ("run `git log`") and asserted pitfalls; no sample PR description despite it being the central artifact.
- **U9** — Zero prompts, zero code. Characterization testing — the unit's novel concept — is never instantiated; the learner has never seen one before being asked to write a battery of them.
- **U10** — Strong artifact tour of `specs/`, two good requirement contrast pairs; but no mini-spec excerpt sized to the lab, so the exemplar is two orders of magnitude larger than the deliverable.
- **U11** — Mixed: worked example is a recycled war story (same incident as U7), no sample `/code-review` output is shown (the learner doesn't know what findings look like), but the answer key (164–174) is genuinely concrete and the E712 false positive is the best-demonstrated pitfall in the course.
- **U12** — Good annotated walk of two real artifacts with quoted trigger descriptions and an honest borderline-classification discussion; would be better with the actual file contents excerpted inline (front matter shown, not linked).
- **U13** — **Best in course**: inline fenced agent JSON, a crisp brief, a sample returned report line, the verification spot-check, and a real 11-agent panel with a nuanced fencing lesson (167–177). This is what showing looks like.
- **U14** — **Demonstrates well**: config block shown, real wrapper walked step-by-step, synthetic-payload pipe test with literal `echo '{"tool_name":"Edit"…}'` command (187).
- **U15** — **Demonstrates well**: real commands with real output (`✓ Connected`), and the local-vs-`tasktracker-pro` trust contrast is an effective paired example.
- **U16** — Demonstrates adequately: CI file walked, headless + worktree commands shown; the parallel half is commands-only (no sample of two diverging diffs being reviewed).

## Top 5 enhancement recommendations

1. **U5 — show a plan, twice.** Add to the Worked example: (a) a realistic plan-mode plan for the lab's `GET /projects/{id}/stats` feature (files touched, response shape, test list — ~12 lines, blockquoted as Claude output), annotated with *why it passes review*; (b) next to it, a vague/wrong plan (counting logic in the router, 404 case missing), annotated with what's wrong; (c) the literal one-sentence redirect the learner types ("Move the counting into a service function and route ownership through `get_project`; the router stays thin. Re-plan."). This single addition fixes F2 and gives U5–U10 a reviewing template.

2. **U1 — show the diff.** Render the actual one-line `/health` diff as a fenced ```diff block in the Worked example, with the three verify criteria (a/b/c from line 140–143) annotated against it. Then, in U5 or U11, show a ~25-line diff containing one smuggled out-of-scope hunk and ask the reader to find it before the annotation reveals it. The course's #1 habit acquires its first instance.

3. **U6 — paired pytest output.** Two short fenced blocks side by side: a right-reason red (`AssertionError: expected 2 overdue tasks, got 5` in context) vs. a wrong-reason red (`ImportError while importing test module…` / a collection error), each annotated with the one line to look at. Add a third 4-line snippet of a cheating implementation (`due_date <= today`, no status check) so "satisfied the wrong way" is seen, not asserted.

4. **U9 — one characterization test, verbatim.** A ~10-line excerpt: run `taskflow.py list --overdue` against a seeded temp DB, assert the *current buggy* output (empty), with a comment "# yes, this pins the bug — that's the point." This is the unit's novel artifact and currently has zero instances; it also concretely demonstrates "preserve behavior, bugs and all." Secondary: show the actual three-line buggy date comparison in U7 (before) and its fix (after) as a ```diff.

5. **U8 — a bad-vs-good history and PR body.** Fenced block one: `git log --oneline` of a bad series (`updates`, `fix`, `wip`) vs. the good two-commit series (prep tidy + feature, why-phrased). Fenced block two: a 5-line aspirational PR description (claims a test that doesn't exist) next to the accurate one, with the false claim highlighted. The pitfalls section currently asserts both failures; ten lines would demonstrate them. (Honourable mention if there's budget for a sixth: U11 should show ~6 lines of what `/code-review` output actually looks like, so "triage the findings" has a visible input.)

## Out-of-scope flags

- **Missing learner outcome, not demonstration:** the persona "wants to learn to *verify*, not merely *trust*" — but no unit teaches *calibration* (when Claude is likely wrong: long context, off-distribution APIs, plausible-but-stale knowledge). That's a content gap for another reviewer, though it would also be the natural home for transcript-based examples.
- **Labs/capstone (not read, per scope):** much of the demonstration burden appears to be deliberately delegated to labs and `solution/` branches ("attempt unaided, then diff against it"). That is a defensible pedagogy, but it means a learner who reads before doing — or skims a unit via Skip-check — gets prose with no instances. Flagging the design tension, not solving it.
- **`course/README.md` does not exist** (units/README.md breadcrumbs point to the repo root README instead). The prescribed orientation read was impossible; possibly a docs-structure issue for another reviewer.
- **meta/workflows.md** is assertion-only by design; the issue is the broken deferral contract (F6), but whether workflows.md itself *should* carry one canonical example per pattern is an information-architecture call above this review's pay grade.
- **Reading-time front matter** (8–13 min) may be calibrated to current prose; adding demonstrations will lengthen units, and the time budget per R-something may need revisiting — flagged for the maintainer.
