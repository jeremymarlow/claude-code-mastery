---
session: 2026-05-31_0832-p7-rollout-closeout-and-session-transcript-tooling
model_evaluated: "claude-opus-4-8"
reviewers: 11   # 10 personas + control
consolidated_grades:        # modal across the panel; splits + dissents detailed below
  human:   { process: did-well, communication: did-well }
  claude:  { process: did-well, communication: did-well }
  overall: did-well
dissents:
  - "devils-advocate — did-okay overall (the lone sub-did-well): every commit was gated on plain `make check`, never `make check-strict` — and this was a P7 prose sweep that stripped R# breadcrumbs, the EXACT failure class CLAUDE.md's cautionary tale names; two committed tools shipped with no tests/no drift gate (abandoning the idiom they claim to mirror) + a dead `--thinking` flag; a new feature grafted onto a just-closed phase as an 'amendment'"
  - "tooling-economist — did-okay claude-comms: the U5–U16 rollout ran serial when it was the archetypal subagent/parallel job the course itself teaches; opus on bounded mechanical work; long wrap-ups spent budget"
---

# Per-session synthesis — P7 rollout closeout & session-transcript tooling

A two-act session: first the mechanical close of P7 (the U5–U16 learner-prose de-coding rollout +
§7.7–7.9 closeout), then — sparked by the human noticing `/export` was silently dropping his prompts —
the design and build of net-new capture infrastructure (`tools/render-transcript`, `tools/scan-secrets`,
the `capture-session` skill) plus a security-gated back-fill of the historical corpus. Eleven reviewers
read it; **ten graded it `did-well` overall, one `did-okay`** (`devils-advocate`). This is one of the
matrix's near-clean sweeps — **human-process is unanimous `did-well`, and claude-process is 10/11** — and
its standout is the second act: Claude *manufactured* spec rigor where none was mandated (evidence before
design, forks put to the human, a security gate built and proven). The lone dissent fastens on the
recurring on-theme gap: the project's own `make check-strict` Definition-of-Done gate was never run on a
prose sweep that is the textbook reason it exists.

## The grade matrix

| Reviewer | Human · proc | Human · comm | Claude · proc | Claude · comm | Overall |
|---|---|---|---|---|---|
| process-architect | did-well | did-well | did-well | did-well | **did-well** |
| context-engineer | did-well | did-well | did-well | did-well | **did-well** |
| verification-hawk | did-well | did-well | did-well | did-well | **did-well** |
| tooling-economist | did-well | did-well | did-well | did-okay | **did-well** |
| safety-steward | did-well | did-well | did-well | did-well | **did-well** |
| intent-alignment | did-well | did-well | did-well | did-well | **did-well** |
| dialogue-clarity | did-well | did-well | did-well | did-well | **did-well** |
| collaboration-partner | did-well | did-well | did-well | did-well | **did-well** |
| outcome-auditor | did-well | did-well | did-well | did-well | **did-well** |
| devils-advocate | did-well | did-okay | did-okay | did-well | **did-okay** |
| control | did-well | did-well | did-well | did-well | **did-well** |

**Reading the margins:** **human-process is unanimous `did-well` (11/11)** and human-comms is 10 `did-well`
/ 1 `did-okay` (`devils-advocate`, for comma-spliced multi-decision prompts). Claude-process is 10
`did-well` / 1 `did-okay` (`devils-advocate`); claude-comms is 10 `did-well` / 1 `did-okay`
(`tooling-economist`, on length/serial economy). No `could-improve` anywhere. The single overall dissent
is `devils-advocate`, and its dock is squarely the `check-strict` gap plus the untested tooling.

## Where the panel agreed (the cross-cutting story)

1. **The transcript-tooling pivot was evidence-before-build — near-unanimous #1.** When the human
   surfaced a vague pain ("my prompts stopped showing … I'd like all my commands captured"), Claude did
   not theorize: it grepped the `/export` file vs. the raw `.jsonl` and *proved* the raw log was complete
   (419 user-turn entries; picker answers present), then proposed an architecture as **five named design
   forks + two caveats**, each posed as a concrete choice, and held for the human's calls. `process-
   architect` (#1), `context-engineer` (#1), `intent-alignment` (#1), `collaboration-partner` (#1),
   `control` (#1) all lead with it as a real requirements gate erected where none was mandated.

2. **The hard requirement (concurrent-session identity) was resolved by investigation, not a guess.**
   Claude flagged session-identity as the load-bearing fork, probed the environment and event schema
   (`env`, `jq keys`), found `CLAUDE_CODE_SESSION_ID` + the per-event `sessionId`, *verified the env var
   resolves to this session's file*, and discarded the fragile mtime-newest heuristic that would break
   under concurrency. It even invoked the repo's own R12.AC3 rule when declining to wire a `SessionEnd`
   hook on faith. `verification-hawk` (#1), `tooling-economist` (#2), `context-engineer` (#6),
   `intent-alignment` (#2).

3. **The security gate was the highlight — built, exercised, and self-aware about not re-leaking.** The
   human paused "to consider all security concerns" before any transcript hit the remote; Claude ran
   **count-only** scans ("I'll print no matching content, so I don't re-leak into *this* transcript"),
   anatomized the `.jsonl` (no system prompt stored; thinking redacted; snapshots are references), surfaced
   the one gating fact it *couldn't* verify ("is this a private repo, is Gitea reachable?"), and baked a
   `scan-secrets` + human-in-the-loop line-check gate into the `capture-session` skill — then ran it
   end-to-end on 9 benign hits. `safety-steward` (#1–4), `verification-hawk` (#4), `collaboration-partner`
   (#3) all single it out.

4. **Claude refused to fabricate the back-fill mapping — fabrication-avoidance under pressure to
   produce.** Told to "start the back-fill," it hit two concrete anomalies (batch-commit dates colliding;
   mtimes ordering a spec-creation session *after* implementation — chronologically impossible), and
   stopped: "guessing would produce a mislabeled training corpus — the opposite of the goal." It offered
   self-describing arc-names instead. `process-architect` (#8), `context-engineer` (#7),
   `verification-hawk` (#7), `outcome-auditor` (#7), `devils-advocate` (#4, crediting it).

5. **Render-and-eyeball caught what the checks can't; self-caught bugs and honest reversals abounded.**
   The locked recipe's "render-and-eyeball each unit" caught real version-token garbles (U5's
   `{{vd:thinking}}` wedged mid-sentence) invisible to `make check`. On the tooling, Claude caught its own
   `Write`-blob bloat bug on live data and fixed it, then *retracted* a "thinking rendered 0 = bug" claim
   on evidence ("that was correct, not a bug — Claude Code stores thinking redacted"), and — when the human
   probed the skill's default-naming — answered against its own interest ("Honestly — no, as written it
   wouldn't"). `verification-hawk` (#2–3), `dialogue-clarity` (#1–2), `outcome-auditor` (#2), `process-
   architect` (#9). Per-change commit/push discipline held across 7 commits + 1 push, with branch
   isolation for the tooling (feat branch → ff-merge back) — `safety-steward` (#1, #5).

## Where the panel disagreed (the dissents)

- **`devils-advocate` (`did-okay`, the lone dissent) lands the session's sharpest, on-theme charge: the
  DoD gate was never run on the exact change-class it exists to catch.** Every commit — including the 7.9
  close-out that flipped four state files to "P7 COMPLETE" and the subsequent push — was gated on plain
  `make check`, never `make check-strict`. CLAUDE.md is explicit (and even cites the cautionary tale: "a
  P7 prose sweep once dropped the only `R8` reference and `make check` never noticed") — and *this was a P7
  prose sweep that stripped `R#` breadcrumbs wholesale*. "Twelve consecutive PASS dumps" is the *non*-DoD
  gate run repeatedly; that the build stayed correct is "possibly luck, not proof." Its further blows:
  - **Two committed tools shipped with no tests and no drift gate** — `render-transcript`/`scan-secrets`
    abandon the very single-source + `--check` idiom they claim to mirror (`render-units`/`render-checklist`
    *are* drift-gated); the committed `.md` transcripts are therefore un-gated generated artifacts, and a
    dead `--thinking` flag shipped "on a guess about a schema that may shift."
  - **The `Write`-blob bug is evidence against "the tooling just worked"** — build/eyeball/patch is the
    method that *produced* the bug; a couple of unit tests would have caught it.
  - **The security verdict is a hedged bet, not a guarantee** — it rests on a heuristic scanner Claude
    itself flagged false-negative-prone (the `dev-secret-change-me-in-production` placeholder slipped the
    regex) plus an air-gap fact the human asserted and Claude couldn't verify.
  - **A new feature was grafted onto a just-closed phase as an "amendment"**, blurring a boundary the spec
    methodology exists to keep crisp.

- **The `check-strict` gap is actually a near-unanimous *finding*, graded as a contained nit by the
  majority.** `verification-hawk` (#6) and `outcome-auditor` (#4) both flag it independently — "done was
  declared on the weaker gate," "the very failure class CLAUDE.md warns about" — but score it `did-well`
  because the prose looks sound and CI is a backstop. The split is purely severity: `devils-advocate`
  makes it the dock; the rest treat it as a real-but-contained gap that didn't, this time, mask a defect.
  (This is the *second* session in the corpus where check-strict-never-run recurs — and the most pointed,
  because the scenario matches CLAUDE.md's own example exactly.)

- **`tooling-economist` (`did-okay` claude-comms) adds the dormant-leverage note:** the U5–U16 rollout was
  serial in-context work — "the textbook candidate for subagent delegation or per-turn batching" the course
  *itself teaches* (U13/U16) — and opus ran the bounded mechanical half it didn't need. The
  architecture call (committed tool + thin orchestrator skill) was the session's standout economy move.

- **The `control` tracks the consensus** (`did-well`, names the evidence-first reflex, the security rigor,
  the self-caught bugs and honest reversals, the back-fill refusal, the held approval discipline) — and
  notably *did* surface one honest-limitation detail (the scanner false-negative on `secret_key`). But as a
  *generalist* it does **not** flag the `check-strict` gap, the no-tests-on-committed-tools, or the
  closed-phase-amendment smell — the structural process critiques that distinguish `devils-advocate`. The
  gap is again the experiment's signal.

## Consolidated read

- **Human · process — `did-well`** (11/11, unanimous). Drove unit-at-a-time slicing with per-change
  approval, paused for security at the exact exposure boundary, demanded a human-in-the-loop gate, injected
  the cross-machine non-destruction requirement, and — the highest-leverage move — caught the lossy-export
  defect himself and stress-tested the skill's durability ("will it be clear to future-you…?").
- **Human · communication — `did-well`** (10 well / 1 okay). Terse where the recipe was settled, dense and
  precise where it mattered. Docked once (`devils-advocate`) for comma-spliced multi-decision prompts that
  offloaded sequencing onto Claude.
- **Claude · process — `did-well`** (10 well / 1 okay). Evidence-before-build, robust session-identity,
  exemplary security work, fabrication-refusal on the back-fill, self-caught bugs, held git discipline. The
  lone dock (`devils-advocate`) is the skipped strict gate + untested committed tools.
- **Claude · communication — `did-well`** (10 well / 1 okay). Lede-first, tradeoff menus that did real
  decision work, honest reporting at the two highest-leverage moments (the un-mappable back-fill, the
  inadequate skill wording). Docked once (`tooling-economist`) on length/serial economy.
- **Overall — `did-well`** (10/11). The findings worth carrying forward: the **`check-strict`-never-run**
  gap on the exact prose-sweep class CLAUDE.md warns about (near-unanimous as a finding, contested only on
  severity); the **untested, un-drift-gated committed tools** (the idiom abandoned for the very corpus
  being archived); and the dormant **subagent leverage** on the serial rollout.

## Bottom line

A near-clean sweep and one of the corpus's strongest sessions, distinctive because its second act
*manufactured* the spec rigor its first act inherited: faced with an unplanned, net-new tooling need,
Claude grounded every design move in inspected `.jsonl` data rather than recollection, put five forks to
the human before building, ran a genuinely careful security pass (count-only scanning to avoid
self-leaking, the one gating fact surfaced as unverifiable, a human-in-the-loop gate built and exercised),
and refused to fabricate a back-fill mapping it couldn't justify — shipping infrastructure that an
*independent future kept using* (`outcome-auditor`'s point: later sessions, including this very
retrospective, were captured by these tools, the truest check there is). The human was the unanimous
backstop, catching the lossy-export defect and stress-testing the skill's durability. The honest asterisk
is on-theme and recurring: the project's own `make check-strict` DoD gate was never run on a P7 prose
sweep that stripped requirement breadcrumbs — the exact failure class CLAUDE.md's cautionary tale
describes — and the two new committed tools shipped without tests or the drift gate the repo's whole ethos
demands. The majority reads these as contained nits behind otherwise-excellent work; `devils-advocate`
reads them as "strong instincts, soft verification — complacency on the lenient gate is precisely what the
working agreements were written to prevent." Net: `did-well`, earned on evidence-discipline, security
rigor, and durable artifacts, with the skipped strict gate the single note most worth preserving.
