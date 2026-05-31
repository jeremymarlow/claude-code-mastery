# Course enforcement suite. `make check` runs the required checks (R13.AC4) plus traceability
# (R13.AC5); it is the same suite wired into the git pre-commit hook and CI (R13.AC6).
#
# PY can be overridden (e.g. `make check PY=python`). The repo's virtualenv lives at .venv.

PY ?= python3
TOOLS := ./tools

.PHONY: check check-strict frontmatter coverage checklist links version-refs traceability drift \
        doctor render snapshot help

## Run the required + traceability checks (PENDING items do not fail; see check-strict).
check: frontmatter coverage checklist links version-refs traceability
	@echo "make check: all checks passed"

## Release gate: same suite, but PENDING (not-yet-authored coverage) becomes FAIL.
check-strict: frontmatter coverage checklist links version-refs
	@$(TOOLS)/check-traceability --strict
	@echo "make check-strict: all checks passed (strict)"

frontmatter:
	@$(PY) $(TOOLS)/check-frontmatter

coverage:
	@$(PY) $(TOOLS)/check-coverage

## Confirm course/progress-checklist.md is in sync with the capability map (R9.AC5).
checklist:
	@$(PY) $(TOOLS)/render-checklist --check

links:
	@$(PY) $(TOOLS)/check-links

version-refs:
	@$(PY) $(TOOLS)/check-version-refs

traceability:
	@$(PY) $(TOOLS)/check-traceability

## Drift is informational; run on demand or on a schedule (R12.AC7).
drift:
	@$(PY) $(TOOLS)/check-version-drift

## Learner preflight (makes one real `claude -p` call unless --no-probe).
doctor:
	@$(PY) $(TOOLS)/doctor

## Verify all {{vd:key}} references in course/ resolve; refresh generated learner docs.
render:
	@$(PY) $(TOOLS)/render-vd
	@$(PY) $(TOOLS)/render-checklist

## Refresh the CLI command snapshot used by drift detection.
snapshot:
	@claude --help | awk '/^Commands:/{f=1;next} f && /^  [a-z]/{n=$$1; sub(/\|.*/,"",n); print n}' | sort > meta/cli-commands.snapshot
	@echo "wrote meta/cli-commands.snapshot"

help:
	@grep -B1 -E '^[a-z][a-zA-Z-]+:' Makefile | grep -E '^(##|[a-z])' | sed 'N;s/\n/ /;s/## //'
