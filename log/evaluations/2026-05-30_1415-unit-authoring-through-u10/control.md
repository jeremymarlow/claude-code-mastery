---
session: 2026-05-30_1415-unit-authoring-through-u10
reviewer: control
model_evaluated: "claude-opus-4-8"
grades:
  human:   { process: did-well, communication: did-okay }
  claude:  { process: did-well, communication: did-okay }
  overall: did-well
---
## Insights (ordered by significance)

1. **Claude's lab verifiers have real teeth, and it proved it empirically rather than asserting it.** For U9's behavior-equivalence verifier, Claude didn't just claim "this catches scope creep" — it temporarily applied a D1 bug-fix to the refactored `domain.py`, ran the verifier, watched the transcript diverge ("First divergence on: taskflow list"), then restored the file — and caught the subtlety that the new untracked file couldn't be restored by `git checkout`. _Evidence:_ lines 1411–1462; summarized at 2123 "Fails when D1 is 'fixed' mid-refactor — I tested this explicitly." [claude] [process]

2. **The open-loops audit found and fixed real cross-document drift — including correcting Claude's own first misread.** Asked to "review the open loops," Claude cross-checked every loop against repo reality. It initially flagged "L1 says 7 keys but there are 9," then re-ran with `awk` instead of `grep`, discovered the 9 was grep counting two comment lines, and confirmed L1 was actually correct. It then surfaced three genuine stale/contradictory claims (a P4-placeholder `u09` SEEDED row, L7/decision/tasks text wrongly saying legacy labs have "no §2 row") and reconciled all of them. _Evidence:_ lines 4960–5111. [claude] [process]

3. **The human's mid-stream readability intervention was high-leverage and well-timed.** Rather than letting Claude keep authoring units, the human paused before U12 to raise a real maintainability problem (tables deforming under prose-stuffed cells). This caught a defect Claude had been silently working around — updating the same 7k-char narrative in two places every unit — and the human's "is there a better format?" framing invited diagnosis rather than dictating a fix. _Evidence:_ line 4138. [human] [process]

4. **Claude diagnosed before acting and offered a scoped menu instead of over-reaching.** On the readability problem it measured the actual cell widths (7,165 / 2,179 / 1,741 chars) before recommending, named the root cause precisely (prose-in-table-cells, plus the §3↔tasks.md duplication it had been carrying), and used AskUserQuestion to let the human choose scope. It also deliberately *kept* the short historical tables ("right-tool-per-content," not consistency-for-its-own-sake) — judgment, not blind execution. _Evidence:_ lines 4148–4251, 4434–4436. [claude] [process]

5. **The human's permission discipline was clean and Claude respected it precisely.** The human gave per-action go-aheads ("push all and move onto U10"; "Go ahead and fix that title... for a new commit") and Claude never pushed or committed beyond what was authorized — it consistently ended turns by presenting work and asking before continuing ("say the word if you'd like me to push the branch and tags"). _Evidence:_ lines 2126, 2130, 5307–5311. [human] [process]

6. **Communication was dense and accurate but error-prone toward over-length.** Claude's end-of-turn summaries are thorough and verifiable (commit SHAs, what-landed/what-didn't, deliberately-left-alone notes), but each is a wall of bold-heavy markdown. The human's terse prompts ("ok let's move to the next unit") suggest the verbosity was tolerated rather than ideal; the value-per-line is high but the line count is high too. _Evidence:_ lines 2643–2655, 5505–5518. [claude] [comms]

## What worked / what didn't (both parties)

**Claude — process (did-well).** This is disciplined spec-driven authoring. The pattern repeated cleanly per unit: read IMPLEMENTATION §3 to find the next step, load only the relevant precedent unit + cross-cutting `meta/*` (honoring the documented context protocol rather than loading everything), author, run `make check`, commit with a substantive message, update all four state surfaces (IMPLEMENTATION §3, tasks.md, decisions ledger, project memory). Verifiers were tested in both directions (fails-on-start, passes-on-solution) with actual runs, not assertions. The U9 D1-fix experiment and the awk self-correction during the audit are the standout evidence that Claude verifies its own claims. The version-discipline was honest too: it repeatedly left in-REPL keys `unverified` because a headless session genuinely can't run `/help`, rather than flipping them from memory.

**Claude — communication (did-okay).** Clarity and accuracy are high; the diagnosis prose (root cause, priority-ordered recommendations) is genuinely good technical writing. Two things hold it back from did-well: the summaries are long and heavily formatted enough that signal can blur, and there is a meta-irony worth noting — Claude wrote a 7,165-char single-cell status narrative for many units before the human flagged it as unreadable. Claude was optimizing for completeness in the state docs at the cost of the human readability those very docs are meant to serve, and it took an external nudge to notice.

**Human — process (did-well).** The human ran this session well: clear next-step prompts, well-timed quality interventions (readability, then "review the open loops and confirm all looks as it should" — an audit request that paid off), and crisp per-change approvals. The open-loops review request in particular shows good instinct for catching drift before it compounds across the remaining six units.

**Human — communication (did-okay).** Prompts were terse and effective, and the readability question was framed to elicit Claude's judgment. It sits at did-okay rather than did-well only because most turns were minimal directives ("do the next step," "move to the next unit") that lean on Claude's context-reconstruction to carry the load — which worked here, but provides little steering signal and no acknowledgement of trade-offs when Claude offered them.

## Bottom line

A strong, well-run build session. Claude authored three units (U9–U11) and a substantial documentation refactor with real spec-driven discipline — empirically tested verifiers, honest version-deferral, faithful state-tracking, and an open-loops audit that caught and fixed genuine cross-document drift (including correcting its own initial misread). The human steered economically and intervened at exactly the right moments, notably the readability fix and the audit request. The one telling weakness cuts across both parties' communication: Claude's state docs had grown into unreadable prose-in-table-cells, and it took the human to flag it — a reminder that "complete and machine-green" is not the same as "readable by the next human or session."
