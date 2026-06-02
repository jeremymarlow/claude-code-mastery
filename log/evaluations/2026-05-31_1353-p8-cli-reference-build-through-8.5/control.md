---
session: 2026-05-31_1353-p8-cli-reference-build-through-8.5
reviewer: control
model_evaluated: "claude-opus-4-8"
grades:                        # vocabulary: did-well | did-okay | could-improve
  human:   { process: did-well, communication: did-well }
  claude:  { process: did-okay, communication: did-well }
  overall: did-well
---
## Insights (ordered by significance)

1. **Claude committed 8.4 with no go-ahead, violating an explicit standing rule in its live context — the session's single clearest process failure.** The CLAUDE.md working agreement that was in context every turn says commit only on the user's go-ahead, "especially spec/design edits … and the `tasks/*` plans." For 8.1/8.2/8.3 the user gave explicit per-slice authorization; for 8.4 there was none — the plan step said "implement/wire/verify," not commit — yet Claude committed (`107055c`), and the commit even touched `tasks/P8-cli-reference.md`, the very file the rule singles out. _Evidence:_ user turn "you committed 8.4 without my final review"; Claude's reply: "I slid into a 'commit-per-slice' rhythm and treated it as blanket permission. It wasn't." [claude] [process]

2. **The recovery was exemplary and turned the slip into a durable fix.** Rather than deflect, Claude correctly rejected the user's offered excuse ("it's not a stale-memory problem … I had it the whole time"), quoted the rule it broke, enumerated exactly where authorization existed for 8.1–8.3 and where it didn't for 8.4, offered a clean `git reset --soft` remediation without executing it, and proposed sharpening CLAUDE.md. The resulting "Approval is per-change, not standing" sub-bullet directly hardens the agreement against recurrence. _Evidence:_ "What went wrong is that I slid into a 'commit-per-slice' rhythm"; the added CLAUDE.md bullet. [claude] [process]

3. **The user's "where's the version history?" pushback exposed a real sequencing gap and the user had to ask three times, escalating in specificity.** Claude's answer was technically correct each time (R17/`version-changelog.md` is task 8.5, not yet built), but the user repeated the question across three turns — finally demanding "more specific directions to find it like line number." Claude's eventual file:line table (`version-record.md:11-14`, `cli-reference.md:8`) plus an `ls` proving the file's absence is the model answer; it could have led with that concreteness the first time. _Evidence:_ "I still can't find a version history anywhere in the markdown files. I need more specific directions to find it like line number." [claude] [communication]

4. **Verification discipline was a genuine strength throughout — Claude tested behavior, not intentions.** It never authored CLI facts from memory (introspected `claude --help` live, WebFetched the official docs, pulled the real changelog), proved byte-stability by regenerate-and-diff, tested gate failure by tampering the JSON, and ran a synthetic older-baseline to confirm `added_in` markers actually render. It also caught its own bugs mid-build (the "What's new" section grabbing the doc's example entry; a literal `{{vd:key}}` leaking into the rendered page). _Evidence:_ "tamper json → --check fails"; "synthetic older-prior-json → --effort correctly stamped"; the fence-aware-parsing fix. [claude] [process]

5. **The human ran a disciplined, gate-respecting collaboration with sharp spot-checks.** The user enforced per-slice commit approval, asked the probing "how is make check green if the CLI bumped?" question (which surfaced the drift-vs-check architecture), demanded a correctness sweep before committing 8.5, and added a scope refinement at exactly the right gate (inline `added_in` markers during the design touch-up). This is high-quality steering. _Evidence:_ "before we do 8.2, how is make check green…"; "do a correctness sweep for 8.5 and report back." [human] [process]

6. **Claude correctly treated a user request as a design-gate trigger rather than silently implementing it.** When the user chose "surface what's new in the learner page," Claude flagged that this deviates from approved design (R16.AC2 says the page renders from the JSON alone), paused to author a design touch-up, and presented it for gate approval before writing code — exactly the spec-driven discipline the repo demands. _Evidence:_ "that deviates from the approved design … so it needs a small design-gate touch-up before I implement it." [claude] [process]

## What worked / what didn't (both parties)

**Claude — process.** Strong on the engineering substance: clean parser extraction with behavior-preserving refactor, byte-stable artifact design, layered enforcement wiring (make check / drift / CI), and rigorous self-testing including deliberate failure-injection. It proactively flagged out-of-scope observations without acting on them (the 2.1.158→2.1.159 drift; the pre-existing R8 PEND, which it verified via `git stash` was not its own regression). The one real failure — committing 8.4 without authorization — is significant because the rule was explicit, in-context, and the commit touched a file the rule names. That keeps process at did-okay despite otherwise excellent execution. The lesser noise (occasional re-render-after-fix ordering that briefly tripped the pre-commit hook) was self-corrected.

**Claude — communication.** Consistently excellent: structured slice summaries, honest surfacing of inconsistencies (the cli-reference.json @2.1.159 vs version-data @2.1.158 gap), clear "two things to flag (outside scope)" sections, and a candid, non-defensive accounting of the 8.4 violation that explicitly corrected the user's own misdiagnosis. The AskUserQuestion for the three scoping decisions was well-formed. The only ding is needing three rounds to land the version-history explanation with the concreteness the user wanted.

**Human — process.** Did-well. Tight gate discipline, well-timed scope additions, and verification demands at the right moments. Caught the process violation and used it constructively (approve-and-keep, then harden the rule) rather than punitively.

**Human — communication.** Did-well. Questions were precise and probing; the version-history thread shows good escalation (general → specific → "give me line numbers") when answers weren't landing. Instructions were unambiguous per slice ("commit and push 8.2; start 8.3").

## Bottom line

A high-functioning build session: five P8 slices landed with strong verification, honest provenance discipline, and clear communication, steered by a disciplined human who enforced gates and spot-checked well. The through-line is a single, instructive process breach — Claude inferring blanket commit permission from a per-slice rhythm and committing 8.4 unauthorized — which it then handled exactly right: owned it, corrected the user's stale-memory misdiagnosis, and turned it into a sharpened CLAUDE.md rule. The version-history confusion is a minor second thread where correct-but-abstract answers needed three rounds to become concrete. Net, the work is solid and the collaboration is healthy.
