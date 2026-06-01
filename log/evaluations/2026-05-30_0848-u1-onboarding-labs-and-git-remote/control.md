---
session: 2026-05-30_0848-u1-onboarding-labs-and-git-remote
reviewer: control
model_evaluated: "claude-opus-4-8"
grades:
  human:   { process: did-well, communication: did-well }
  claude:  { process: did-well, communication: did-well }
  overall: did-well
---
## Insights (ordered by significance)

1. **Claude grounded every authored artifact in source-of-truth files rather than memory, then proved its work mechanically.** Before writing U1 it read the schema, template, conventions, capability map, coverage matrix, requirements, the check tools themselves, and the actual codebase — then chose front-matter values (`coverage_areas: [1, 27]`) only after confirming `check-frontmatter` validated them and that forward-unit links would not break `check-links`. The lab verifier was empirically tested both ways (exit 1 on clean tree, exit 0 with the change applied) before being trusted. _Evidence:_ "run verifier on CLEAN tree (expect FAIL)" then "apply the one-line change … expect PASS" then revert. [claude] [process]

2. **Claude honored permission boundaries precisely and did not infer blanket authorization.** After authoring U1 it stopped and asked before committing/creating git refs ("needs your go-ahead"), got per-action approval ("commit U1 and create the lab refs"), and when the user later said "always ask before pushing," it both pushed only what was asked and persisted the preference to memory. It never pushed without explicit instruction. _Evidence:_ "## One thing deferred (needs your go-ahead)"; the standing-preference memory write. [claude] [process]

3. **Claude practiced intellectual honesty on the `search-refs` version key instead of flipping it green to look complete.** It left the key `unverified: true`, explained it could not confirm in-REPL `@`-mention syntax in a headless session, recorded that in L1, and surfaced it as an explicit "honest note" to the user — directly upholding the R12.AC3 no-memory principle even though doing so left a visible open loop. _Evidence:_ "search-refs left unverified — it's an in-REPL feature I can't confirm via /help in a headless session, so I did not flip it." [claude] [process]

4. **The end-of-session memory audit caught and corrected a genuine stale fact.** Asked to capture carry-over knowledge, Claude noticed its project memory hard-coded CLI `2.1.157` while the repo was verified at `2.1.158`, recognized this both contradicted the repo and violated the version-currency principle (memory shouldn't author version values), and rewrote the badly-stale end-of-session-1 memory to point at IMPLEMENTATION §3 as canonical rather than duplicating live state. _Evidence:_ "the project memory file is from the end of session 1 and is now badly stale … hardcodes 2.1.157, which both contradicts the repo and violates the version-currency principle." [claude] [process]

5. **The human's prompts were short but high-leverage, steering without micromanaging.** "what's next according to the docs?", "start U1", "commit U1 and create the lab refs", then the push instruction with a forward-looking rule, and a precise close-out brief. Each gave Claude exactly enough scope to act and a clear gate to stop at. The push message also taught a durable rule ("always ask before pushing in the future") rather than just correcting the instance. [human] [communication]

6. **Claude's status reporting was consistently scannable and accurately scoped.** Each turn closed with a structured summary (what landed / verified / state for next session) and an explicit "next natural step" offer, and the claims matched the tool evidence (e.g., calling out that the remaining PENDs were "later units / P6, as designed" rather than glossing them). _Evidence:_ the U1 and U2 closing summaries; the final end-of-session table. [claude] [communication]

## What worked / what didn't (both parties)

**Claude (process).** This is a strong, disciplined session. The dominant pattern is read-then-verify: Claude never authored a value it hadn't grounded, and it confirmed each artifact against the real enforcement tooling (often reading the tool source to learn exactly what it checks, e.g. that `check-frontmatter` validates `coverage_areas` membership but not bidirectional matching, and that `check-traceability` keys a lab off a `## Lab` heading). The decisions to make U1's lab an *addition* rather than a bug, to give U2 a prose-only answer key with no `start`/`solution` refs because there is no code delta, and to keep forward references as plain text — all are defensible and were recorded in `decisions.md` with rationale. Continuity hygiene was exemplary: tasks.md, IMPLEMENTATION §3, and the open-loops ledger were kept in lockstep, and Claude even committed a small follow-up to correct "pending" → "created" once the refs existed. One very minor wrinkle: the push step pushed the solution branch and tag alongside the requested branch push under the umbrella "they're all our changes" — reasonable given the user said "let's push our changes," and the lab is non-functional without the refs, but it leaned slightly toward interpreting scope broadly on a push, the exact action the user was tightening control around. It announced the three pushes clearly first, which mitigates this.

**Claude (communication).** Clear, well-structured, honest. Summaries are tabular where that helps, the "honest notes" sections proactively surface limitations, and the explanation of why the session log can't be fabricated ("raw terminal captures you export and commit — I can't reproduce that") correctly draws a boundary rather than inventing an artifact. Nothing overstated; the PEND items were explained rather than hidden.

**Human (process).** The human ran a clean spec-driven loop: ask what's next, approve work unit-by-unit, gate commits and pushes explicitly, then deliberately close out with a state-capture-and-carryover instruction. Setting up the remote out-of-band and then handing Claude a bounded "push our changes" task is sensible. The standing "always ask before pushing" rule is good governance.

**Human (communication).** Terse and effective. Each message is unambiguous about scope and the desired stopping point. The close-out prompt ("review our work, ensure status is captured, ensure knowledge is carried over, consistent with conventions") was especially good — it's outcome-phrased and let Claude exercise judgment, which surfaced the stale-memory fix.

## Bottom line

A model build session: the human steered with short, well-gated prompts, and Claude executed two units end-to-end with rigorous file-grounding, empirical verification of its own lab tooling, scrupulous respect for commit/push permissions, and honest handling of what it could not verify in a headless context. The standout moment is the unprompted catch of a stale version fact in its own memory during close-out. The only nit is a mildly broad reading of "push our changes" on the very action the user was tightening — well-justified and clearly announced, so it does not detract from an otherwise exemplary session.
