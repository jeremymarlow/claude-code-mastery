---
description: Dispatch the 11-reviewer panel over one build session; each reviewer writes its own leaf evaluation
argument-hint: <session-slug>
---

Run the R18 collaboration-retrospective **leaf pass** for one session: dispatch all eleven reviewers
over the session transcript and persist their evaluations as the matrix's leaf cells. Authoritative
spec: `specs/claude-code-mastery/design.md` §13; layout: `meta/conventions.md` →
"Collaboration-retrospective evaluations"; corpus orientation + grade vocabulary + leaf schema:
`log/evaluations/README.md`.

**Session:** `$ARGUMENTS` (the transcript filename stem).

Do each step, in order:

1. **Preconditions.**
   - Confirm the rendered transcript exists at `log/transcripts/rendered/$ARGUMENTS.md`. If not, stop — `$ARGUMENTS`
     must be a stem present in `log/transcripts/rendered/` (the discoverable corpus).
   - Confirm the reviewer panel is loaded (the eleven `.claude/agents/*.md`). On-disk agents load at
     **session start**, so if they were just authored, reload (`/agents`) or restart first — otherwise
     the dispatch can't find them.
   - If `log/evaluations/$ARGUMENTS/` already holds leaves, they are **cached and immutable** — do **not**
     overwrite. Report which exist and only fill the missing reviewers. (A deliberate re-run of a
     reviewer is a new, dated file, never an overwrite.)

2. **Verify the model attribution (R18.AC7 — never assume).** Read the model(s) that produced Claude's
   side of this session from the raw record, not from memory:

   ```
   jq -rc 'select(.message.model)|.message.model' log/transcripts/raw/$ARGUMENTS.jsonl \
     | grep -v '<synthetic>' | sort | uniq -c
   ```

   Resolve to a single attribution string to hand each reviewer — e.g. `claude-opus-4-8`, or for a
   mixed session note it (e.g. `claude-opus-4-8 (mixed: claude-sonnet-4-6 for the first 2 turns)`).
   Cross-check against the recorded map in `log/evaluations/README.md`; if the file disagrees with the
   map, trust the file and flag the discrepancy.

3. **Dispatch the panel in parallel.** In a **single message**, dispatch **all eleven** reviewers — one
   Agent call each, run concurrently (U16) for wall-clock savings:

   `process-architect`, `context-engineer`, `verification-hawk`, `tooling-economist`, `safety-steward`,
   `intent-alignment`, `dialogue-clarity`, `collaboration-partner`, `outcome-auditor`, `devils-advocate`,
   and `control`.

   Give each reviewer the **same** brief (they each carry their own lens, mandate, and output contract):

   > Evaluate build session **`$ARGUMENTS`**. Rendered transcript: `log/transcripts/rendered/$ARGUMENTS.md` — your
   > primary source; consult `log/transcripts/raw/$ARGUMENTS.jsonl` only for a specific turn if the render is
   > insufficient. The model that produced Claude's side of this session: **\<attribution from step 2>**.
   > **Write** your leaf evaluation to `log/evaluations/$ARGUMENTS/<your-reviewer-name>.md`, exactly per your
   > output contract (begin at the `---` line; no preamble or ``` fence). Then **return only a short receipt** —
   > the path you wrote, your `overall` grade, and one sentence — **not** the document itself.

   `mkdir -p log/evaluations/$ARGUMENTS/` first so the writes land. The reviewers run **least-privilege**
   (`Read, Grep, Glob, Write`): each **writes its own leaf** to the path above and returns only a receipt — the
   full document never round-trips through the orchestrator (the token + latency fix; see decision
   **P9-leaf-write**). Dispatch the `control` with the identical brief — its different behavior must come from
   its own (lens-less, mandate-less) definition, not from a different prompt.

4. **Validate the written leaves (no re-emission — the point of the redesign).** Each reviewer wrote its own
   file; you never reproduce its prose. Lint `log/evaluations/$ARGUMENTS/*.md`:
   - **first line is `---`** — if a preamble or surrounding ``` fence leaked in above it, strip everything
     before the first `---` with a quick `sed`/`awk` (a mechanical fix, not a rewrite);
   - front matter well-formed: `session: $ARGUMENTS`, `reviewer:` equals the filename stem, `model_evaluated:`
     equals the step-2 attribution **and is quoted** (a colon in a mixed-model value breaks unquoted YAML),
     and the `grades` block uses **only** `did-well` / `did-okay` / `could-improve`;
   - the body is verbose and **evidence-cited** (insights with `_Evidence:_` locators), covers **both
     parties**, and is not a grade dump.
   For anything **substantive** — a missing file, a thin/one-sided body, wrong attribution, malformed grades —
   **re-dispatch that one reviewer** (never hand-author a reviewer's prose).

5. **Progress + safety (no commit here).** Run `tools/scan-secrets log/evaluations/$ARGUMENTS/*.md` (it takes
   file arguments, not a directory) and
   human-review any flag before this batch is committed (R18.AC10). Then run `tools/check-evaluations`
   (or `make check`) for the matrix progress readout. **Do not commit** — committing the session's batch
   is the maintainer's call per `CLAUDE.md`; report the batch as ready for review.

Then report: the model attribution used, which of the eleven leaves were written (and any skipped as
already-cached), any reviewer you re-dispatched and why, and the `check-evaluations` progress line. The
per-session `_synthesis.md` is the **next** step (the 9.5 per-session synthesis) — not part of this
command.
