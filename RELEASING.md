# Releasing & versioning

How this repository is branched, merged, versioned, and released. This is **repo process** (like a
`CONTRIBUTING` doc), not course content — it is deliberately not a spec requirement. For *course
maintenance* (adding/updating units, refreshing the CLI target) see
[`course/maintainer-guide.md`](./course/maintainer-guide.md).

## Branching — trunk-based

- **`main` is the trunk:** the primary long-lived branch, kept releasable. Most work lands here directly.
- **`release/<minor>` maintenance branches** are the one sanctioned **long-lived exception** — one per
  supported minor line (e.g. `release/1.0`, `release/1.1`), cut at that minor's release point so it can
  take patches independently of `main`. See **Maintenance & backports** below.
- **Short-lived branches for non-trivial work,** named by intent — `feat/…` (new capability/requirement),
  `fix/…` (bug/regression), `spec/…` (requirements/design/tasks gate), `chore/…` (tooling/process). Keep
  them short; rebase and land them quickly, then delete.
- **Lab tags are a separate namespace.** `start/<lab>` and `solution/<lab>` tags/branches are course lab
  substrate (see the maintainer guide); they never collide with release tags (`v*`).

## Merge strategy — rebase + fast-forward

Linear history, no merge commits:

```
git fetch origin
git rebase origin/main        # replay your branch on top of latest main
# … resolve, re-run `make check` …
git switch main && git merge --ff-only <branch>   # fast-forward only
git push origin main
git branch -d <branch>
```

A merge that cannot fast-forward means the branch wasn't rebased — rebase, don't create a merge commit.
(One historical exception predates this policy: the design-phase merge commit `d182fbe`.)

## Maintenance & backports

Trunk-based development is optimized for one moving line, but supporting an older release means shipping a
fix to a version that is no longer the tip of `main`. That is what the `release/<minor>` branches are for:
**one long-lived branch per supported minor**, cut at that minor's latest release. A freshly cut
maintenance branch is an **ancestor of `main`** — a pointer marking where the line ended; it diverges only
once a patch lands on it.

**To patch a line** — say a security fix needed in both the current line and an older `1.0.x`:

1. **Land the fix on `main` first** (a `fix/…` branch, rebase + fast-forward) so the next release can't
   regress.
2. **Cherry-pick the isolated fix commit** onto each affected `release/<minor>` — never merge or rebase a
   published maintenance branch; cherry-pick keeps each line linear and merge-commit-free:
   ```
   git switch release/1.0
   git cherry-pick -x <fix-sha>        # -x records the original commit
   git tag -a v1.0.2 -m "v1.0.2 — <fix>"
   git push origin release/1.0 --follow-tags
   ```
3. **Tag the patch on that branch's tip** (`vX.Y.(Z+1)`), not on `main`.

Author the fix where it applies most cleanly (usually newest-first, then backport down); if an old line's
code has diverged, adapt the patch by hand. EOL a line by simply ceasing to patch it — its branch and tags
preserve the history regardless.

## Versioning — semantic versioning

Releases are tagged `vMAJOR.MINOR.PATCH`. The version describes **the course as a learner-facing
product**. It is **independent of the Claude Code CLI version** the course targets (that lives in
[`meta/version-record.md`](./meta/version-record.md) with its own provenance).

| Bump | Meaning for this course | Examples |
|---|---|---|
| **MAJOR** | A breaking change to the learner's path or structure — something that would disrupt a learner mid-course. | Dropping or renumbering units; restructuring the stages; re-targeting a new CLI **major** that invalidates existing labs. |
| **MINOR** | Additive, backward-compatible growth. | A new unit; a new requirement added via the post-v1 enhancement playbook (R16/R17, R18); new labs, tools, or capabilities. |
| **PATCH** | Fixes and refreshes that don't change scope. | A prose/quality pass; a CLI **version-data refresh** that only updates `meta/version-data.*`; link/typo fixes; a clarifying acceptance criterion (e.g. R14.AC8). |

A CLI refresh (R12.AC7) that only re-verifies version-specifics and bumps `version-record.md` is a
**PATCH** — the course's scope is unchanged.

## Cutting a release

1. **Gate.** `make check` is green, **and** `make check-strict` is green *except* for requirements that
   are **explicitly deferred in the open-loops ledger** (`specs/claude-code-mastery/decisions.md`). A
   release may proceed with a ledgered deferral, called out in the changelog.
   - *Current state:* `make check-strict` fails **only** on **R19** (breadcrumb navigation, design
     deferred — ledger **L12**). That is the documented release-readiness state, not a blocker.
2. **Record.** Add the release section to [`CHANGELOG.md`](./CHANGELOG.md).
3. **Tag** (annotated, on `main`). The tag message **is** the in-repo release note (`git show`, the
   Releases UI), so write it **from** the version's [`CHANGELOG.md`](./CHANGELOG.md) section — one
   authored source, the tag a derived snapshot. Use an editor (no one-line `-m`); sign with `-s` if
   signing is in use:
   ```
   git tag -a vX.Y.Z        # editor opens — paste & adapt the CHANGELOG section
   ```
   - **Subject:** `vX.Y.Z — <concise title>` (≤72 chars).
   - **Body:** the summary + grouped highlights (Added/Changed/Fixed/…), with breaking changes and
     upgrade notes called out, wrapped ~72 cols; close with `See CHANGELOG.md for the full entry.`
4. **Push** the commit and the tag (a push is a separate, explicit step):
   ```
   git push origin main --follow-tags
   ```

## Tag lineage

The release history was **backfilled** from the build's phase checkpoints (annotated tags, each dated to
its commit). `v1.0.0` is the first release — the point where the v1 Definition of Done was met (P6). The
table below is an **illustrative snapshot** of how the scheme maps to the build phases;
[`CHANGELOG.md`](./CHANGELOG.md) is the authoritative record of what each version contains.

| Tag | Checkpoint |
|---|---|
| `v0.1.0`–`v0.5.0` | Pre-release development: design gate → scaffolding → tooling → codebases → all 16 units. |
| **`v1.0.0`** | **First release** — v1 build complete (capstone, case study, finalization). |
| `v1.0.1` | Quality/learner-experience pass (committed-rendered units, breadcrumbs, transcript-capture tooling). |
| `v1.1.0` | CLI reference + version-change digest (new requirements R16/R17) and version-resilience maintenance. |
| `v1.2.0` | Collaboration retrospective (new requirement R18) + conflict-of-interest disclosure (R14.AC8). |
| `v1.3.0` | Content enhancement — demonstrations + operator craft (new requirements R20/R21), breadcrumb navigation (R19), CLI refresh to 2.1.170. |
