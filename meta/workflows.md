# Workflow methods (W1–W9)

The nine named, reusable methods the course teaches **inside** their use cases, then
generalizes (R3.AC4). No workflow is a free-floating lesson — each maps to ≥1 exercising unit
(R3.AC5). Units **reference** this file for the generalized pattern rather than re-explaining
it (R5.AC5). Stage tags match `meta/capability-map.yaml` and `design.md` §3.

Source of truth: `design.md` §3. **[R3, R5.AC5]**

## Summary table

| # | Workflow | Stage | When to choose it | Expected verification (CV) | Unit(s) |
|---|---|---|---|---|---|
| W1 | explore → plan → code → commit | daily-driver | Default for any non-trivial change | Review the **plan** before coding; read the diff + run tests before commit | U5 |
| W2 | test-driven development | daily-driver | Behavior is specifiable as a test; regression-prone or bug-fix work | Confirm the test fails first **for the right reason** (red), then green; review the impl | U6 |
| W3 | debugging an unfamiliar failure | daily-driver | Something is broken and the cause is unknown | Reproduce first; capture the bug in a failing test; confirm root cause, then that the fix doesn't regress | U7 |
| W4 | Git / PR workflow | daily-driver | Turning work into shareable history/review | Review the staged diff; ensure message matches change; self-review the PR | U8 |
| W5 | multi-file refactoring | force-multiplier | Cross-cutting change touching many files; rename/restructure | Behavior-preserving: full suite green **before and after**; diff-review for scope creep | U9 |
| W6 | code & security review | force-multiplier | Before merging a significant or security-sensitive change | The workflow *is* verification — but cross-check findings, don't trust the review blindly | U11 |
| W7 | spec-driven development | force-multiplier | Large/ambiguous feature where upfront alignment pays off | Each phase gate reviewed/approved before the next; trace requirements→design→tasks | U10 |
| W8 | onboarding to an unfamiliar/large codebase | first-wins *(light)* → force-multiplier *(deep)* | Entering code you don't know | Validate Claude's architecture summary against the actual code (spot-check claims) | U2 (light), U9 (deep) |
| W9 | running parallel agents (git worktrees) | autonomy-scale | Multiple independent tasks that can run concurrently | Isolate each in a worktree; review each agent's diff independently before integrating | U16 |

**Reconciliation notes (R3.AC2/AC6):**
- W7 / U10 uses **this very `specs/claude-code-mastery/`** spec as its worked example (R3.AC2).
- W8 is intentionally two-tiered — light exploration (U2, primary repo) vs deep
  onboarding-for-refactor (U9, legacy repo); see `meta/use-case-catalog.yaml`.
- Every workflow has ≥1 exercising unit; no catalog row is better expressed as a workflow.

---

## Generalized patterns

Each pattern below is the durable, version-independent method. Units link here and add only the
unit-specific application (the concrete prompts and the lab).

### W1 — explore → plan → code → commit
**The pattern.** Resist jumping straight to code. (1) **Explore**: have Claude read the relevant
code and restate the task and constraints. (2) **Plan**: get an explicit plan you can review
*before* any edit (use plan mode so nothing is written yet). (3) **Code**: implement against the
approved plan in small steps. (4) **Commit**: read the diff, run the tests, then commit.
**Choose it when:** any change big enough that a wrong turn costs more than the planning does —
the default for non-trivial work. **Verify (CV):** the gate is the *plan*; reject or redirect a
bad plan before code exists. Then read the diff and run tests before committing.

### W2 — test-driven development
**The pattern.** Write (or have Claude write) a test that pins the desired behavior, run it, and
**confirm it fails for the right reason** (not a typo/import error). Then implement just enough to
go green. Refactor with the test as a safety net. **Choose it when:** the behavior is
specifiable as a test, or the work is regression-prone or a bug fix. **Verify (CV):** red-then-
green is the verification — but read the implementation, since a test can be satisfied the wrong
way (e.g., hard-coded return).

### W3 — debugging an unfamiliar failure
**The pattern.** Be a scientist, not a guesser. (1) **Reproduce** the failure deterministically.
(2) Capture it in a **failing test** so "fixed" is objective. (3) Form hypotheses, instrument,
and **confirm the root cause** before changing anything. (4) Fix, then confirm the test passes
**and** nothing else regressed. **Choose it when:** something is broken and the cause is unknown.
**Verify (CV):** a passing test you wrote from the repro, plus a green full suite — never a fix
justified only by "it looks right."

### W4 — Git / PR workflow
**The pattern.** Turn a pile of work into reviewable history: stage deliberately, write commits
that explain *why*, and open a PR whose description matches the actual diff. Self-review the PR as
if you were the reviewer before requesting one. **Choose it when:** sharing work for review or
preserving history. **Verify (CV):** read the staged diff; confirm the message/PR description
matches what changed (no aspirational claims); self-review surfaces issues before others do.

### W5 — multi-file refactoring
**The pattern.** A behavior-preserving change across many files. Establish a green baseline,
make the structural change in reviewable increments, and keep the suite green throughout.
Watch for scope creep — refactor and behavior change should not mix in one diff. **Choose it
when:** a cross-cutting rename/restructure touches many files. **Verify (CV):** full suite green
**before and after**; diff-review specifically for behavior changes that snuck into a "pure"
refactor.

### W6 — code & security review
**The pattern.** Before merging a significant or security-sensitive change, run a structured
review (correctness *and* security) over the diff. Treat findings as leads, triage them, and
fix or justify each. **Choose it when:** a change is significant or touches security-sensitive
surface (auth, input handling, secrets, untrusted content). **Verify (CV):** the review *is* a
verification step — but cross-check its findings against the code; an automated review both
misses real issues and raises false positives, so don't accept or dismiss blindly.

### W7 — spec-driven development
**The pattern.** For a large/ambiguous feature, align *before* building: write **requirements**,
then **design**, then **tasks**, with an explicit approval gate between phases. Trace each later
artifact back to the requirement it serves. **Choose it when:** the cost of building the wrong
thing is high and upfront alignment pays off. **Verify (CV):** each phase gate is reviewed and
approved before the next begins; requirements→design→tasks traceability is checkable.
**Worked example:** this course's own `specs/claude-code-mastery/` (R3.AC2).

### W8 — onboarding to an unfamiliar/large codebase
**The pattern.** Before changing code you don't know, build a map: have Claude summarize the
architecture, entry points, and data flow, then **validate that summary against the actual code**
before trusting it. *Light* onboarding (enough to locate a change site) vs *deep* onboarding
(enough to safely refactor) differ in depth, not method. **Choose it when:** entering code you
don't know. **Verify (CV):** spot-check Claude's architecture claims against the source — an
onboarding summary is a hypothesis until checked.

### W9 — running parallel agents (git worktrees)
**The pattern.** When independent tasks can run concurrently, give each its own **git worktree**
so agents don't collide on the working tree, run them in parallel, then review and integrate each
diff separately. **Choose it when:** multiple independent tasks can proceed at once and isolation
is worth the setup. **Verify (CV):** review each agent's diff independently before integrating;
isolation makes a bad result containable rather than entangled.
