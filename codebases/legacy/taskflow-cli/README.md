# TaskFlow CLI (legacy)

The **original** TaskFlow: a single-file argparse command-line task tracker that stores everything
in one JSON file. It predates `taskflow-api` and was eventually replaced by it, but the script (and
the JSON files it produced) are still around.

This codebase is the course's **legacy substrate** — the messy, untested code you practise
*understanding*, *debugging*, and *refactoring* on (units U7 and U9). It is intentionally **not**
clean: one ~700-line god-module, global mutable state, duplicated logic, inconsistent naming, dead
code, and **no tests**. It also contains a few **real, seeded bugs**. Do not "fix it up" on `main` —
the mess is the point. (Maintainers: the seeded defects are inventoried in
[`../../SEEDED.md`](../../SEEDED.md).)

## Run it

No dependencies beyond the Python standard library (Python ≥ 3.9):

```bash
export TASKFLOW_DB=/tmp/taskflow.json     # where to store tasks (default: ~/.taskflow/tasks.json)
python taskflow.py add "Write the report" --priority high --project work --due 2026-06-15
python taskflow.py list
python taskflow.py list --overdue
python taskflow.py done 1
python taskflow.py stats
python taskflow.py --help
```

Commands: `add`, `list`, `show`, `done`, `start`, `reopen`, `rm`, `edit`, `assign`, `search`,
`projects`, `tags`, `stats`, `export`, `import`, `archive`, `config`.

## Known weirdness

It mostly works, but some things are subtly wrong — that is deliberate. Finding out *what* and
*why* is the exercise. Point `$TASKFLOW_DB` at a throwaway file and experiment freely.
