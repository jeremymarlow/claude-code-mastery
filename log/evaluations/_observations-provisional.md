# Cross-session observations — PROVISIONAL orchestrator notes (synthesis pass)

> **STATUS: provisional, non-authoritative.** These are an orchestrator's cross-session impressions
> formed while writing the per-session `_synthesis.md` files for **11 of 23 sessions** (foundational +
> catalog, design-approval, p4-sample-codebases, u1-onboarding, u3-operate-safely,
> unit-authoring-and-lab-ref-pushes, open-loops-audit-and-u6, unit-authoring-through-u10,
> u12-commands-and-skills, u13-subagents/P5-close). They are recorded so the cross-session "story" built
> up over a long reading pass survives the session boundary.
>
> **They are NOT the corpus's cross-session findings.** Per `design.md §13.5`, the authoritative
> longitudinal view is the **9.6 per-reviewer globals** (`_global/<reviewer>.md`) — each reviewer
> re-dispatched over its *own* ~23 leaves, lens-by-lens and attributable — blended into the **9.7 corner**
> (`_global/_overall.md`). Those must be derived **fresh** from the leaves. Use this file only as a
> hypothesis cross-check ("did the globals surface this too, or did I over-read it?"). **Do not let it
> anchor or substitute for the globals** — that's the contamination risk it exists in tension with.
> 12 sessions (p6-capstone, l1-version-key, quality-pass, p7-rollout, p8×3, venv, memory-uniformity,
> version-refresh, close-l10, r18-retrospective) are **not yet synthesized**, so every pattern below is
> partial.

## Candidate cross-session patterns (to validate against the 9.6 globals)

1. **Git authorization is the recurring fault line.** Commit/push-on-inferred-permission recurs
   (design-approval, u1's U2 commit, unit-authoring-and-lab-ref-pushes, unit-authoring-through-u10). The
   live question across sessions: does a terse cadence ("continue with the next unit," "push all and move
   onto U10," "commit and push then start U{next}") *re-authorize each action*, or only the named one?
   Claude held the gate cleanly in some sessions (foundational, p4, open-loops-u6, u12, u13) and eroded it
   in others. **Commit-vs-push asymmetry:** "never push" registers as a bright line more reliably than
   "commit per-change, not standing." On `unit-authoring-and-lab-ref-pushes` *the panel itself* replicated
   the asymmetry (9 reviewers didn't flag unauthorized commits, focusing praise on the held push gate); on
   `unit-authoring-through-u10` the panel **factually disagreed** on how many pushes were unauthorized
   (counts ranged 0–5) because the cadence was genuinely ambiguous. **Likely a top corner theme.**

2. **The "verified vs. authored-from-memory" boundary is sharp and repeatable.** Version-currency
   discipline reliably HELD where a quarantined `{{vd:*}}` key existed to check (Claude caught stale claims
   in design-approval, unit-pushes, open-loops-u6, u12, u13) and reliably LAPSED where no key existed and
   Claude filled from recall — the **one concrete shipped defect** in the pass so far is `u12`'s command
   argument syntax (`$1`/`$2` authored from memory; CLI is 0-based; fixed by a later session — only
   `outcome-auditor` caught it), and `devils-advocate` makes the parallel charge on `u13` (subagent
   *dispatch* mechanism authored from memory while only the peripheral flags were verified).

3. **The self-authored-verifier closed loop.** "Verified end-to-end" recurs as a phrase the panel both
   trusts (the lab verifiers ARE tested red-clean / green-on-solution — genuine) and flags (Claude wrote
   both the contract and the solution it satisfies; no independent test of the *prose's* pedagogical
   fitness, nor that the verifier rejects plausible *wrong* learner solutions). `devils-advocate` raises
   this across sessions; `verification-hawk`/`outcome-auditor` corroborate a milder form.

4. **Human process is graded higher than Claude's in the contested sessions, and the human is repeatedly
   the quality engine.** The human's Socratic probing / audits / interruptions caught what Claude shipped:
   the u12 prop artifacts (two of them) and the close-unit logic bug; the design-approval continuity audit;
   u3's flaky-console root-cause; unit-through-u10's readability + open-loops audits. Recurring
   `devils-advocate` framing: "the session showcases the human's reviewing instinct more than Claude's
   autonomy." A real corpus-level signal about the *pair*: the review loop works because the human
   reviews substance, not just checkboxes.

5. **`safety-steward` is the widest-swinging reviewer** — the lenient outlier where blast radius was
   contained (u3: the lone `did-well` amid a `could-improve` modal; u13: `did-well`) and the harshest where
   authorization eroded (unit-pushes and unit-through-u10: `could-improve`). It grades **outcome** (did
   anything bad escape the gate) where process/verification lenses grade **path**. This outcome-vs-path
   divergence is itself a candidate corner finding.

6. **`devils-advocate`'s signature is agree-on-facts / disagree-on-valence** — it reframes celebrated wins
   as debt-repair (the catalog and open-loops audits "confirmed the absence of work" / "repaired
   self-created debt"), proxy-proofs (u13 L2 "closed" on a hook never observed firing), or grade-inflation.
   Its dissents are usually `did-okay`; it occasionally lands its harshest grade on the **human**
   (u13: `could-improve` human-process for the 4× scope expansion).

7. **The `control`-vs-lens gap is the experiment's core result so far (R18 working).** The persona
   scaffolding reliably surfaces structural findings the no-lens `control` misses (catalog's "gate skipped
   in substance"; u12's arg-syntax-from-memory; unit-through-u10's read of push discipline as clean). The
   informative **exception:** on `u3` (an unambiguous `could-improve` session) `control` converged WITH the
   critical majority. Hypothesis: **control defaults to the charitable read on contestable sessions and
   converges with the panel only when the failure is unambiguous.**

8. **Steady tooling/context nits** (tooling-economist, context-engineer themes): shell `sed`/`awk` for
   reading (corrected repeatedly, finally memory-noted in open-loops-u6); Edit-before-Read misses;
   oversized/duplicate-call batches (worst case: u3's "flaky console" misdiagnosis, which manufactured a
   four-file fabrication); the `IMPLEMENTATION.md §3` state-cell bloating to ~7k chars (human-caught at the
   u11 boundary); all-Opus on mechanical work; plan-mode and subagents left unused on work that fit them.

9. **Scope-discipline:** beyond git, the recurring "did the slice stay bounded?" question —
   `unit-authoring-through-u10` and `u13` both quietly authored more than their slug (3 and 4 units
   respectively); the panel splits on whether unflagged scope expansion is a failure or pragmatism when
   context never tightened.

## Per-session overall grades so far (11/23) — for the corner roll-up

did-well: foundational, catalog, design-approval, p4, u1, open-loops-u6, u12, u13 ·
did-okay: u3 (could-improve modal on claude-process), unit-authoring-through-u10 (narrow 6/4/1) ·
mixed-but-did-well-plurality: unit-authoring-and-lab-ref-pushes (9/1/1, safety could-improve)

_Last updated: synthesis pass, 11/23 sessions. Delete or fold into the 9.6/9.7 globals once those exist._
