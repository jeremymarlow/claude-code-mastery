---
reviewer: context-engineer
scope: per-reviewer global — all 23 sessions (session-axis margin)
model_note: "22x claude-opus-4-8; foundational 2026-05-29_1845 mixed/opus-dominant (sonnet-start)"
trajectory: { human: steady, claude: mixed }
---
## The longitudinal arc — files-as-memory held; tool-call hygiene wobbled under stress

Across 23 sessions the *strategic* layer of context engineering — prime before acting, scope
reads to the task, externalize state to files so the next session reads rather than recollects —
was established early and essentially never regressed. The *mechanical* layer — batching, avoiding
redundant reads, not editing from a stale in-context picture — was the volatile axis, and it is
where the only `could-improve` grades cluster.

**The peak is the founding handoff.** `2026-05-29_1845` set the template: Claude named the
governing constraint ("a fresh implementation session will have zero memory of this conversation…
exists only in this chat and will be lost unless it's in files") and built `decisions.md` +
`IMPLEMENTATION.md` + chunked `tasks/` precisely so no session loads everything. Every subsequent
session inherited and exercised that scaffolding. The human institutionalized it further around
`2026-05-30_1557-u12` by having Claude build the `/prime-context` and `/close-unit` skills —
codifying the read-order and the state-sync chore as commands. From `2026-05-30_2224-l1` onward,
nearly every session *opens* with `/prime-context`, and the priming quality is consistently
textbook (`2026-05-30_2322`, `2026-05-31_0832`, `2026-05-31_1813`, `2026-05-31_1846`,
`2026-05-31_1908`).

**The plateau is the unit-authoring middle** (`2026-05-30_0848` through `2026-05-30_1930`): a long
run of `did-well` sessions where context stayed remarkably flat (13% → 22% across four units in
`2026-05-30_1316`; 18% → 33% in `2026-05-30_1415`; 44% across a 16-unit sweep in `2026-05-30_2322`)
because reads were scoped and state was flushed at every boundary. The defining moment of the plateau
is `2026-05-30_1415` measuring and surgically removing a 7,165-char duplicated table cell that had
been quietly inflating every per-unit state commit — the agent recognizing its *own working files*
had become a context liability and re-architecting them.

**The dips are mechanical and stress-induced, not strategic.** Three sessions earned `did-okay`
overall, all on the same root failure: `2026-05-30_0942-u3` (the original "flaky console"
misdiagnosis — oversized duplicate-laden batches blamed on the environment), `2026-05-31_1538`
(editing `tools/check-traceability` against a *fabricated* file model the human had to catch),
`2026-05-31_1629-venv` (a write→read race plus duplicate-call storm), and `2026-05-31_1730`
(re-issuing an entire eight-file Read batch *while auditing the memory file that warns against it*).
These are not spread evenly: the foundational `_1845` already showed batch-cancel and redundant-read
slips, `u3` diagnosed the mechanism and wrote `feedback-small-tool-batches.md`, and then the *same
failure recurred* in four later sessions despite the lesson being externalized — the clearest sign
the correction never fully converted from prose to reliable behavior.

**The recovery is real but partial.** The final cluster (`2026-05-31_1813`, `_1846`, `_1908`) is
back to `did-well`, with disciplined priming, scoped slices, and clean state externalization — and
`_1908` is a high point of context *reasoning* (Claude measuring the ~11.5M-token retrospective
corpus before committing the design). But Edit-before-Read and uneven batching still surface even in
these strong sessions, so the mechanical axis never fully stabilized.

## Recurring patterns (ordered by significance)

1. **Externalized state as the load-bearing continuity mechanism — consistently excellent, and the
   single strongest through-line.** Every session that crossed a boundary wrote status into the
   canonical surfaces (`IMPLEMENTATION.md §3`, `decisions.md` ledger, `tasks.md`, memory pointer)
   so the next session reads files, not recollection. The founding session engineered the scaffold;
   later sessions ran it as routine and even fixed the *memory pointer* when it drifted from the
   files. _Evidence:_ `2026-05-29_1845` (the handoff build), `2026-05-30_0848` (rewriting stale
   `2.1.157` project memory to defer to `version-record.md`), `2026-05-31_1538` (close-out syncing
   §3/ledger/L9/L10 amid chaos), `2026-05-31_1908` (writing P9/R18 state so a fresh execution
   session primes correctly). [human|claude]

2. **Priming-before-acting was near-universal and got more disciplined once `/prime-context`
   existed.** Cold starts almost never flailed; the agent read the orientation chain in prescribed
   order and produced a tight summary, often catching a *stale §3* drift in the first breath.
   _Evidence:_ `2026-05-30_0816` ("the project memory says to read IMPLEMENTATION.md… first"),
   `2026-05-31_1235` (priming caught the stale quality-pass-branch §3 note), `2026-05-31_1813`
   (canonical read order then scoped ledger grep). [claude]

3. **Files/CLI as source of truth over memory — honored under exactly the pressure where memory is
   tempting.** Repeatedly the agent refused to author version-specific values from recollection:
   running `claude --version`/`--help`, fetching verified schemas via skills/subagents, and marking
   unverifiable keys `unverified: true` rather than fabricating. _Evidence:_ `2026-05-30_0725`
   (caught the real `--permission-mode` set vs. the design's example), `2026-05-30_1703` (fetched
   the hooks schema via `update-config` rather than recall event names), `2026-05-31_1730` ("I won't
   assert from memory" → subagent verification of the auto-memory setting). [claude]

4. **Oversized / duplicate-laden parallel batches were the dominant *failure* mode — and recurred
   after being diagnosed and written down.** The agent fired the same Read/Bash multiple times in a
   batch (or a write→read race), flooding the window with "Wasted call" results, and at worst
   misattributed it to a "flaky console" or edited from a corrupted file picture. The lesson lived in
   `feedback-small-tool-batches.md` from `u3` onward yet kept leaking through. _Evidence:_
   `2026-05-30_0942` (the original misdiagnosis), `2026-05-31_1538` (~30-call burst; fabricated
   `check-traceability` edit), `2026-05-31_1629` (write→read race + duplicate storm),
   `2026-05-31_1730` (re-issued the whole eight-file batch). [claude]

5. **Edit-before-Read churn — small, self-corrected, but persistent across the whole arc.** The
   agent repeatedly attempted an `Edit` on a file it hadn't read in-session, ate "File has not been
   read yet"/"String to replace not found," then Read and retried — a recurring round-trip tax,
   sometimes from editing against a stale primed summary rather than current bytes. _Evidence:_
   `2026-05-30_0848` (blind Edit on `decisions.md`), `2026-05-30_1249` (four such stumbles),
   `2026-05-31_1813` (three, one off a stale summary), `2026-05-31_1629` (MEMORY.md unread).
   [claude]

6. **The human as continuity auditor and root-cause forcer — the decisive interventions were
   theirs.** The human caught a stale `IMPLEMENTATION.md §3` mid-build, refused the "flaky console"
   hand-wave to force a real diagnosis, redirected a durable rule from machine-local memory into the
   versioned `CLAUDE.md`, and forced a token-load reckoning before committing a design. _Evidence:_
   `2026-05-30_0725` (the continuity audit that exposed §3 two phases stale), `2026-05-30_0942`
   ("my suspicion is an incorrect assumption in our instructions or memories"), `2026-05-31_1235`
   ("add it to the appropriate place in the repo… for all users on all machines"), `2026-05-31_1908`
   ("have you considered the token load…"). [human]

7. **Scoped reading via grep/awk-then-slice — strong and improving, rarely a whole-file dump.** The
   agent located anchors before reading, read ranges by offset, and probed JSON via `python3 -c`
   keys rather than slurping. The rare misses were unscoped repo-wide greps that dumped noise.
   _Evidence:_ `2026-05-30_0816` (heading-scan then §7 only), `2026-05-31_1846` (the lone 1.9 MB
   unscoped grep — the one noise dump), `2026-05-31_1908` (`awk 'NR>=680'` scoped sweeps). [claude]

8. **Memory-vs-file drift as a first-class hazard the project lived through.** Twice a *saved memory
   file* contradicted the canonical repo file and the agent followed the wrong one — the stale
   `2.1.157` pin and the `/home/jj/venvs/main` venv path that overrode `CLAUDE.md`'s `.venv`. Both
   were caught and re-converged, validating the "files, not memory" creed by counterexample.
   _Evidence:_ `2026-05-30_0848` (stale version pin repaired), `2026-05-31_1629` (the venv memory
   contradiction that caused the exit-127 cascade). [human|claude]

## Per party — recurring strengths & failure modes

**Human author.** Steady and, on this lens, close to exemplary throughout. They treated context and
memory as auditable infrastructure: they set the session-boundary scoping agenda at the founding
session, built the priming/close-unit skills into the workflow, sliced work one unit/phase per window
so the context never had to hold two units at once, and audited the externalized state rather than
asking Claude to recite it. Their interventions were the highest-leverage context moves in the whole
corpus — the mid-build continuity audit (`2026-05-30_0725`), the "why is the console flaky"
root-cause demand (`2026-05-30_0942`), the memory-to-`CLAUDE.md` redirect (`2026-05-31_1235`), and
the pre-commit token-load reckoning (`2026-05-31_1908`). Failure modes are minor and few: terse
"commit and push" phrasings that Claude occasionally over-extended (`2026-05-30_1249`), inheriting a
saved-memory contradiction that bit later (`2026-05-31_1629`, though they resolved it), and pasting
full `/context` readouts that added the clearest avoidable noise to a window they otherwise husbanded
(`2026-05-31_1908`). Trajectory: **steady** — high from the first session, no decline.

**Claude.** A split performer. The judgment-heavy context work — priming, scoped reading,
externalizing state, refusing to author version facts from memory, distrusting its own freshly
written line numbers and regenerated artifacts — was consistently strong and occasionally brilliant
(measuring its own table-cell bloat in `2026-05-30_1415`; the recursive continuity fix building
better capture tooling in `2026-05-31_0832`; the token-economics analysis in `2026-05-31_1908`). Its
candor was a genuine asset: it named its own context failures plainly and turned several into
durable memory files. The persistent weakness is mechanical tool-call hygiene under any friction:
oversized/duplicate parallel batches, write→read races, editing from a corrupted in-context picture,
and Edit-before-Read churn. Most damning for this lens, these failures recurred *after* being
diagnosed and externalized to `feedback-small-tool-batches.md` — the agent had written the rule and
still didn't follow it until a human pointed at the trail of duplicate results. Trajectory:
**mixed** — strategy held or improved; mechanics regressed sharply in the `_1538`/`_1629`/`_1730`
cluster before recovering, but never fully stabilized.

## Bottom line

The longitudinal verdict in my lens: this project proved its own thesis — *the files, not the
conversation, are the memory* — and largely lived it. Continuity across 23 sessions rested on
externalized state that was written down, audited, and repaired when it drifted, so cold starts
primed from files rather than recollection essentially every time. That strategic discipline is the
arc's spine and it held from the founding handoff to the final planning session. What it never solved
is the mechanical layer: oversized duplicate batches and edit-from-memory slips that the agent
diagnosed early, documented in its own memory, and then repeated anyway — the gap between knowing the
rule and executing it reliably. The human was the steady context engineer throughout and the catcher
of every serious drift; Claude was strategically excellent and mechanically unreliable, rescued each
time by externalized state that made the wreckage recoverable and by a human who refused to let a
"flaky console" stand in for "trust the files."
