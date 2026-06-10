<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Turn a body of work into clean commits and a reviewable PR

# Turn a body of work into clean commits and a reviewable PR

*Reading: ~12 min · Lab: ~25 min · Prerequisites: [Ship a feature end-to-end with explore → plan → code → commit](../05-ship-a-feature/unit.md)*

## Learning objectives

By the end of this unit you can:

- **Turn a pile of work into clean, logically atomic commits** with messages that explain *why*, and
  a PR whose description matches the actual diff.
- **Stage deliberately** — decide what belongs in each commit rather than `git add -A`-ing everything,
  and keep unrelated changes out of a feature's history.
- **Self-review the PR as if you were the reviewer** before requesting one — reading the full diff and
  confirming the description makes no claims the code doesn't back up — cross-cutting verification (CV) applied to shareable work.
- **Use Claude to draft the history and the PR, then verify it** — drive `git` and `gh` through the
  Bash tool, but own the final shape of the commits and the description.

## Fast path (TL;DR)

> The Git/PR workflow is [the Git/PR workflow](../../../meta/workflows.md#w4--git--pr-workflow): turn work into history
> someone can *review*. **Stage deliberately** (each commit is one logical change), **write messages
> that explain why** (not "fix stuff"), **open a PR whose description matches the diff**, and
> **self-review it first** — read the whole diff as the reviewer would. Claude can draft all of this —
> the commit splits, the messages, the PR body (PR creation runs `gh` through the Bash tool) — but
> *you* confirm the description claims only what the code does. The lab has you take a real change in `taskflow-api` and make it
> review-ready; the self-check is a reviewer's checklist you apply to your own diff.

## Skip-check

**Skip this unit if you can already:** take a body of uncommitted (or messily committed) work and turn
it into a reviewable PR — commits that are individually atomic and explain *why*, a description that
matches the diff with no aspirational claims, and a self-review pass you do *before* asking anyone else
— rather than dumping everything into one `git commit -am "updates"` and a PR titled "changes."

## Concept

You can ship a verified change. This unit is about the last mile: making that change **reviewable** —
because on any real team, work that can't be reviewed efficiently doesn't land. The unit of review
isn't the file, it's the **commit** and the **PR**, and both are artifacts you *author*, not exhaust
the tool produces.

**The workflow.** The generalized pattern lives once in
[`meta/workflows.md`](../../../meta/workflows.md#w4--git--pr-workflow); read it there. The short
version: **stage deliberately → commit with intent → open a PR whose description matches the diff →
self-review before requesting review.** The rest of this section is what's specific to *applying* it
with Claude.

**1 — Stage deliberately; one logical change per commit.** The fastest way to make a diff
un-reviewable is to bundle unrelated changes — a feature, a drive-by rename, and a formatting sweep —
into one commit. Decide what each commit *is* and stage only that (`git add -p` exists for exactly
this). When a feature needs a preparatory tidy (extract a helper, rename a symbol), that prep is its
**own** commit, landed first — so the reviewer reads "here's the cleanup, now here's the feature
riding on it," not a 400-line blob where the two are tangled.

**2 — Write the message for the reader six months from now.** A good commit message says *why* the
change exists, not just *what* the diff already shows. "Add `archived` flag to projects" restates the
diff; "Let users hide finished projects from the default list without deleting them" explains the
decision. Claude will happily generate either — ask it for the *why*, and reject "update code" /
"fix bug" boilerplate.

**3 — Open a PR whose description matches the diff.** PR creation is `gh` through the Bash tool;
Claude can draft the title and body for you. The description should tell the reviewer
**what changed and why, how to verify it, and what you deliberately left out** — and every claim in it
must be true of the actual diff. The most common defect here is the *aspirational* description: a PR
body that describes the feature you intended, including the test you meant to write but didn't. Drafted
by an AI from your prompt rather than from the diff, that gap is easy to introduce — which is exactly
why step 4 exists.

**4 — Self-review before you request review (CV).** Read the full diff yourself, as the reviewer
would — `git diff main...HEAD`, top to bottom. Does every hunk belong? Did a debug print or a stray
file sneak in? Does the description match what you're actually seeing? Catching your own loose ends
here is faster and cheaper than a review round-trip, and it's the same verification reflex from the
previous units pointed at the artifact you're about to ask a human to spend attention on. (There's also
a way to come back to an open PR later: `--from-pr [value]` resumes a session linked to a PR by number/URL; PR creation uses the `gh` CLI via the Bash tool.)

> **Claude drafts; you sign.** Commit messages and PR descriptions are *claims about your code* with
> your name on them. Let Claude write the first draft of all of it — then read the diff and make the
> words match the code. An unread AI-drafted PR description is how false claims get your sign-off.

**Version currency.** This unit was verified against Claude Code `2.1.170`. The
version-specific surface is the `gh` integration and the `--from-pr` flag: `--from-pr` session resume; PR creation via `gh` in the Bash tool Confirm with
`claude --help` and see [`meta/version-record.md`](../../../meta/version-record.md) if your version
differs. `git` and `gh` themselves are external tools Claude drives through the Bash tool.

## Worked example

Two artifacts: a real commit series, and the catch the self-review step exists for.

**The history.** This repository is built the way the unit teaches, and you can read it directly.
One of its features (breadcrumb navigation) landed as this series:

**Captured** — `git log --oneline` in this repo (one feature's slices, oldest last):

```text
abf2f38 P10 10.5 — close-out: R19 breadcrumb navigation COMPLETE; strike L12 [R19]
3cc08b8 P10 10.4 — wire check-breadcrumbs into check/check-strict + record the convention [...]
038dc33 P10 10.3 — hand-authored docs carry the canonical trail [R19.AC1/AC2]
017bdb3 P10 10.2 — generators emit the canonical trail via the shared helper [R19.AC5]
```

Each commit is one reviewable step (the generator change, then the hand-authored docs, then the
enforcement wiring), and each message says what the slice *accomplished* — a reviewer or a future
maintainer can navigate this without opening a single diff. That's the shape the lab asks of you.

**The catch.** Now the failure mode this unit's step 4 exists for — the aspirational description:

**Illustrative** — your session will differ in wording; verify behavior and diffs, not phrasing.

> **Claude (draft PR body):** Adds an `archived` flag to projects with an `include_archived` list
> filter (default: excluded). Includes model + schema changes, the filter, and **tests covering the
> default-exclusion contract**.
>
> **You** *(reading `git diff main...HEAD` next to the draft)*: The diff has the model, schema, and
> filter — but there's no test in it. The body claims a test I never wrote. Either I add the test
> or the description stops claiming it.

The draft wasn't malicious; it was generated from your *intent* (the prompt) rather than the *diff*.
Reading the two side by side is the whole self-review move — and it's why the lab has Claude draft
the body from `git diff main...HEAD`, never from memory of what you asked for.

## Lab

> **This lab has no automated verifier.** Commit and PR *quality* is a judgment call, and a real PR
> needs a remote and `gh` that this course can't assume. So the self-check below is an
> objective **reviewer's checklist** you apply to your own work — applying it *is* the skill this
> workflow teaches. An optional stretch uses real `gh` on your own remote.

**Goal:** take a real change in `taskflow-api` and make it **review-ready** — clean commits, accurate
PR description, self-reviewed — without bundling unrelated work or over-claiming in the description.

**Starting state:** the clean primary codebase on a fresh branch. Work in your own clone:
`cd codebases/primary/taskflow-api`, then `git switch -c u08-archived-projects` (your branch, in your
clone — nothing here gets pushed for you).

**The change (your work to make reviewable):** add an **`archived`** flag to projects.

- Add `archived: bool` (default `False`) to the `Project` model and its read/update schemas.
- Add an `?include_archived=` filter to the project list (default **excludes** archived projects),
  mirroring the existing task-list filters.
- If doing this cleanly needs a small preparatory tidy (e.g. extracting or renaming a filter helper),
  **make that a separate commit, landed first.**

**Steps:**

1. Drive the change with the loop you already know (explore → plan → code, from **Ship a feature**; lean on tests, from **TDD**).
   Don't commit yet — let the work accumulate in the working tree.
2. **Stage deliberately.** Split the work into logical commits: any preparatory tidy first, then the
   feature. Use `git add -p` to keep each commit to one change. Ask Claude to propose the split and the
   messages, then edit them so each message says *why*.
3. **Draft the PR description** (have Claude draft it *from the diff* — `git diff main...HEAD` — not from
   your original prompt): what changed, why, how to verify (`pytest`), and anything deliberately out of
   scope.
4. **Self-review.** Read the full diff top to bottom as the reviewer. Fix anything that doesn't belong;
   make the description match the diff exactly.
5. *(Optional stretch — BYO, non-verifiable):* on your **own** fork/remote, push the branch and
   `gh pr create` for real, then read the rendered PR. Never push to a remote you don't own.

**Self-check (objective checklist):** your work is review-ready when **all** hold:

- [ ] `pytest` is green, and **every** commit builds on its own (no commit leaves the suite broken).
- [ ] Each commit is **one logical change** — no feature bundled with an unrelated rename/format sweep;
      the prep tidy (if any) is its own commit, ordered before the feature.
- [ ] Every commit **message explains why**, not just what — none is "update", "fix", or "wip".
- [ ] The PR description's claims are **all true of `git diff main...HEAD`** — no described-but-absent
      test, no feature you didn't actually build.
- [ ] The diff contains **only** the change — no debug prints, commented-out code, or stray files.
- [ ] `include_archived` defaults to **excluding** archived projects (the contract above), and a test
      pins it.

**Reference:** there's no `solution/` branch for this lab — the artifact is *your* history and PR, and
the checklist above is the rubric. Compare your commit series and description against it directly.

**On your own repo (transfer — optional, bring-your-own, not verifiable by this course's tooling):**
take work currently in flight in your real codebase — the messier the better — and apply exactly this
lab's moves: split it into atomic commits with why-messages, have Claude draft the PR body *from the
diff*, and self-review with the checklist above before you request review from a human.

## Common pitfalls

- **`git commit -am "updates"`.** One giant commit with a contentless message is the default failure.
  The reviewer can't review it and neither can future-you. Split and explain.
- **Bundling unrelated changes.** A feature plus a drive-by rename plus a format sweep in one commit
  triples the review cost. Keep them separate; land prep first.
- **The aspirational PR description.** Describing what you *meant* to do — including the test you
  skipped. Draft the body from the diff, not the plan, and self-review catches the gap.
- **`git add -A` then trusting it.** Staging everything sweeps in debug prints, scratch files, and
  unrelated edits. Stage deliberately (`git add -p`) and read what you staged.
- **Letting Claude's draft message/description ship unread.** It's a claim with your name on it. Read
  the diff and make the words true before you commit or open the PR.
- **Skipping self-review.** "The reviewer will catch it" wastes a round-trip on things you'd have seen
  in thirty seconds reading your own diff.

## Stage checkpoint — Daily Driver

You've finished the Daily Driver stage (**Ship a feature**, **TDD**, **Debugging**, and this unit).
Before moving on, answer these from memory — then check yourself against the unit named in
parentheses. Ungraded; the capstone remains the course's only graded instrument. If one draws a
blank, skim that unit's fast path before continuing.

1. What four things does a working brief carry, and what do you revise when a plan disappoints?
   (**Ship a feature**)
2. What are the two verification gates in the daily loop, and what does each one catch that the other
   can't? (**Ship a feature**)
3. What distinguishes a red that counts from a red that doesn't, and why does the distinction matter?
   (**TDD**)
4. Your fix made the symptom disappear. What two things must still be true before "fixed" is honest?
   (**Debugging**)
5. What's the defining defect of an AI-drafted PR description, and what's the mechanical habit that
   catches it? (this unit)

## Going deeper

- **Next:** the Force-Multiplier stage (**Refactor legacy**, **Spec-driven dev**, **Code & security
  review**) all assume you can produce reviewable history — and **Code & security review** is the other
  side of this coin: *being* the reviewer. **Automate & scale** drives PRs headlessly in CI.
- [`meta/workflows.md`](../../../meta/workflows.md#w4--git--pr-workflow) — the generalized Git/PR pattern.
- The `gh` integration and `--from-pr`: `--from-pr` session resume; PR creation via `gh` in the Bash tool Version-specifics in
  [`meta/version-record.md`](../../../meta/version-record.md).
- The verify-before-you-ship reflex traces straight back to [Ship a feature](../05-ship-a-feature/unit.md)'s diff
  review and [Debugging](../07-debug-a-failure/unit.md)'s "don't claim it's fixed until it's proven."
- Stuck? [`course/stuck.md`](../../stuck.md) and the
  [progress checklist](../../progress-checklist.md).
