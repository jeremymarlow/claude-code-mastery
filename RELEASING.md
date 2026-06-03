# Releasing & versioning

How this repository is branched, merged, versioned, and released. This is **repo process** (like a
`CONTRIBUTING` doc), not course content — it is deliberately not a spec requirement. For *course
maintenance* (adding/updating units, refreshing the CLI target) see
[`course/maintainer-guide.md`](./course/maintainer-guide.md).

## Branching — trunk-based

- **`main` is the trunk:** the single long-lived branch, kept releasable. Most work lands here directly.
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
3. **Tag** (annotated, on `main`):
   ```
   git tag -a vX.Y.Z -m "vX.Y.Z — <one-line summary>"
   ```
4. **Push** the commit and the tag (a push is a separate, explicit step):
   ```
   git push origin main --follow-tags
   ```

## Tag lineage

The release history was **backfilled** from the build's phase checkpoints (annotated tags, each dated to
its commit). `v1.0.0` is the first release — the point where the v1 Definition of Done was met (P6). See
[`CHANGELOG.md`](./CHANGELOG.md) for what each version contains.

| Tag | Checkpoint |
|---|---|
| `v0.1.0`–`v0.5.0` | Pre-release development: design gate → scaffolding → tooling → codebases → all 16 units. |
| **`v1.0.0`** | **First release** — v1 build complete (capstone, case study, finalization). |
| `v1.0.1` | Quality/learner-experience pass (committed-rendered units, breadcrumbs, transcript-capture tooling). |
| `v1.1.0` | CLI reference + version-change digest (new requirements R16/R17) and version-resilience maintenance. |
| `v1.2.0` | Collaboration retrospective (new requirement R18) + conflict-of-interest disclosure (R14.AC8). |
