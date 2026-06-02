---
session: 2026-05-30_1930-p6-capstone-finalization
reviewer: verification-hawk
model_evaluated: "claude-opus-4-8"
grades:
  human:   { process: did-well, communication: did-well }
  claude:  { process: did-well, communication: did-okay }
  overall: did-well
---
## Insights (ordered by significance)

1. **The false "GENERATED" header — caught, root-caused, and proven, not papered over.** This is the
   session's strongest verify-don't-trust moment. The `progress-checklist.md` header claimed "GENERATED
   from meta/capability-map.yaml ... Regenerate with the capability-map generator (P3 tooling)" — and
   Claude did not take that claim at face value. It checked, found the generator *did not exist*
   ("**that generator doesn't exist** ... a false claim in a shipped artifact"), and instead of just
   editing the header to be vague, it built the real `tools/render-checklist` so the claim became true.
   Crucially, it then *proved* the artifact was already in sync rather than asserting it: `git --no-pager
   diff` showed `1 file changed, 1 insertion(+), 1 deletion(-)` — only the header line — confirming
   byte-for-byte reproduction. That is verify-before-believing and prove-don't-assert in one move.
   _Evidence:_ "The generator reproduces the file byte-for-byte except the one header line I deliberately
   corrected." [claude] [process]

2. **"Done" was proven, not declared — the strict gate was run, read, and earned.** The session's spine
   is L3 (the v1 DoD mechanical gate). Claude opened by running `make check-strict` *expecting failure*
   to enumerate the exact target — and read the output rather than trusting a remembered list:
   "only **two** PENDINGs remain — `R8` unreferenced, and all 18 can-dos ... unassessed." After authoring
   the rubric/briefs it re-ran `check-traceability --strict` and read all three PASS lines before
   claiming closure ("L3's mechanical gate is met"), then ran the *full* strict suite a final time. It
   did not conflate plain `make check` green with DoD-green — it explicitly named strict as the gate.
   This is the disciplined version of "done." _Evidence:_ "make check-strict: all checks passed (strict)
   ... L3 is closed." [claude] [process]

3. **No version fact from memory — the CLI was queried, not recalled.** Task 6.5 demanded re-verifying
   version specifics. Claude ran `claude --version` (2.1.158) and `make drift`, read that the installed
   CLI "matches recorded verified version," and concluded "no version-record bump needed" from evidence,
   not assumption. It also honestly flagged the few CLI literals in the capstone (`claude mcp get`,
   `✓ Connected`, `-p`) as "consistent with the established treatment — no new unverified facts
   introduced," and was candid that L1's 7 unverified keys "needs a one-time interactive `/help` pass a
   headless session can't do." That is the no-version-from-memory rule honored *and* uncertainty stated
   plainly rather than smoothed. _Evidence:_ "Installed CLI is still 2.1.158 — matches the record
   exactly." [claude] [process]

4. **Verified-before-acting on links and the PR mechanism, not assumed.** Before linking dogfood
   artifacts from the capstone, Claude probed each path's existence (`OK codebases/fixtures/... OK
   tools/doctor ...`) so `check-links` would not break — confirming the world before writing claims
   about it. The PR explanation is a model of refusing to assert from memory: it noticed the remote is
   **Gitea**, not GitHub, then *checked* tooling availability (`gh`, `tea`, `glab` all missing; only
   `curl`) before explaining — and correctly warned that `gh pr create` "would fail against a non-GitHub
   remote." It would have been easy to confidently recite the `gh` flow from memory; instead it verified
   the environment first. _Evidence:_ "Let me confirm what tooling is actually available before
   explaining" → tooling probe. [claude] [process]

5. **The one soft spot: qualitative ACs were verified only mechanically.** The traceability gate proves
   the *tag regex* (`[Cn]` lines exist, `R8` appears) — it cannot see whether the rubric actually grades
   the work product three ways, whether the reflection prompts truly deliver "one catch / one justified
   accept / one override" (R8.AC6), or whether the briefs genuinely each require ≥1 extension. Claude
   authored these and asserted coverage in its summary table ("verification-reflection prompts (R8.AC6)
   ... critiqued AI-self-grade (R8.AC5)") without ever Reading the files back to confirm the prose
   matched the AC. The harness suppresses re-reading freshly written files, so this is partly
   structural — but the green strict suite was leaned on as evidence for obligations the suite
   demonstrably *cannot* check (the session itself noted "content obligations ... the static suite can't
   see"). That is the classic trap of treating a green gate as proof of correctness for things outside
   the gate's reach. A diff-read of the four new capstone files against the ACs would have closed it.
   _Evidence:_ "All P6 content obligations are met" asserted; the qualitative ACs were never read-checked
   against authored prose. [claude] [process]

6. **The human's verification contribution: a sharp environment correction and a deliberate gating
   rhythm.** The author caught Claude about to `source` a venv that was already active and rejected the
   tool call with the exact reason ("you shouldn't need to source the venv, it's laready active") — a
   small but real instance of the human verifying the agent's premise. The author also held commit/push
   behind an explicit go-ahead ("commit this and push") rather than letting Claude self-authorize,
   keeping the outward-facing actions human-gated. _Evidence:_ tool rejection at the first `check-strict`
   attempt; "commit this and push" turn. [human] [process]

## What worked / what didn't (both parties)

**Claude — process: strong.** This is a session where claims were earned. The recurring pattern — run
the gate, read the output, act on the evidence, re-run to confirm — held from the opening
`check-strict` enumeration through the final strict run and `git status`. The standout was treating a
suspicious "generated by" header as a claim to be *checked* rather than trusted, finding it false, and
fixing it by making it true with a generator whose correctness it then proved via diff. Version facts
came from `claude --version` and `make drift`, never memory. Uncertainty (L1) was surfaced honestly as
refresh debt, not smoothed over.

**Claude — communication: good, with one over-claim.** The reporting is precise and evidence-anchored
(it quotes exact PASS lines, the diff stat, the version string). But the final summary's blanket "All
P6 content obligations are met" outruns the evidence for the qualitative ACs, which were never
read-checked — the mechanical gate was implicitly stretched to cover prose it cannot inspect. A more
hawkish framing would have said "mechanically green; the R8.AC5/AC6 prose obligations I authored but
did not re-verify against the AC text."

**Human — process and communication: strong.** The venv correction shows the author verifying the
agent's assumptions in real time, and the commit/push gating was deliberate and explicit. The
"explain the mechanism you would use to create a PR" request also implicitly demanded a verified answer
(which it got). No weaknesses of consequence surfaced for the human in this session, though the author
also did not push Claude to read back the capstone prose against the qualitative ACs — so the one
verification gap went unchallenged by either party.

## Bottom line

A genuinely disciplined finalization session: "done" was run, read, and proven — not declared. The
through-line is a refusal to trust claims at face value — a false "generated" header was caught and
made true with a proven-correct generator; the strict DoD gate was earned and re-run; version facts and
PR tooling were queried, not recalled; uncertainty (L1) was stated plainly. The single blemish is that
the green mechanical suite was leaned on as if it covered the qualitative capstone ACs it admittedly
cannot see, and the four new capstone files were never diff-read against R8's prose requirements. Close
that one habit — read the artifact, not just the gate's color — and this is exemplary verification work.
