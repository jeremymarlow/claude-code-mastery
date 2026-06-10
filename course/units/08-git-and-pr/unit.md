<!-- GENERATED from unit.src.md by tools/render-units — do not hand-edit. Edit unit.src.md, then run `make render`. -->
---
id: U8
title: "Turn a body of work into clean commits and a reviewable PR"
stage: daily-driver
depth_tier: core
use_case: "Turn my work into a clean, reviewable PR"
can_do: [C9]
workflows: [W4]
coverage_areas: [13]
prerequisites: [U5]
reading_time_min: 9
lab_time_min: 25
---

[Claude Code Mastery](../../../README.md) › [Course units](../README.md) › Turn a body of work into clean commits and a reviewable PR

# Turn a body of work into clean commits and a reviewable PR

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

**Version currency.** This unit was verified against Claude Code `2.1.159`. The
version-specific surface is the `gh` integration and the `--from-pr` flag: `--from-pr` session resume; PR creation via `gh` in the Bash tool Confirm with
`claude --help` and see [`meta/version-record.md`](../../../meta/version-record.md) if your version
differs. `git` and `gh` themselves are external tools Claude drives through the Bash tool.

## Worked example

This repository is built exactly this way, and its history is the worked example. The design phase
landed on `main` through a single reviewed merge once the design gate passed (not a trickle of
unreviewed commits to `main`); each unit since lands as a focused commit whose message names the unit
and explains the *why*, with the reference solution kept on its own `solution/uNN-labM` branch rather
than mixed into the teaching commit. Run `git log --oneline` in this repo and you'll see the pattern
the lab asks you to produce: one logical change per commit, messages you can read a year later, and
work separated into branches a reviewer can take in at a glance. (That separation — teaching commit
vs. solution branch — is itself a "stage deliberately" decision: the two are unrelated audiences, so
they don't share a commit.)

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
