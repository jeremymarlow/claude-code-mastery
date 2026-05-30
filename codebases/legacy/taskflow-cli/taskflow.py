#!/usr/bin/env python3
# taskflow.py -- entry point.
#
# This used to be the whole program: one ~700-line god-module. It was split into the `taskflow_app`
# package (a behaviour-preserving refactor -- U9). This file is now just the entry point so that
# `python taskflow.py ...` keeps working exactly as it always did.
#
# NOTE: the refactor deliberately preserved behaviour, bugs and all. The seeded landmines (overdue
# never flagged, `--limit N` showing N-1 rows, save errors swallowed) are still here, unchanged --
# fixing them is a *separate* change, not part of restructuring.
import sys

from taskflow_app.cli import main

if __name__ == "__main__":
    sys.exit(main())
