#!/usr/bin/env python3
# Characterization tests for taskflow-cli.
#
# These were written BEFORE the refactor (U9): they pin what the program does *today* so the
# restructuring could be proven behaviour-preserving. They characterize behaviour as-is, INCLUDING
# the seeded bugs (overdue never flagged; `--limit N` shows N-1 rows) -- a refactor must keep them
# green, because a refactor preserves behaviour. Fixing a bug is a separate change that would
# (correctly) turn the relevant test red.
#
# Stdlib only (the CLI has no third-party deps): run with `python -m unittest test_characterization`.
import os
import subprocess
import sys
import tempfile
import unittest
from datetime import date, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))


class CharacterizationTests(unittest.TestCase):
    def setUp(self):
        self.db = tempfile.mktemp(suffix=".json")
        self.env = {**os.environ, "TASKFLOW_DB": self.db}

    def tearDown(self):
        for p in (self.db, self.db + ".archive"):
            if os.path.exists(p):
                os.unlink(p)

    def run_cli(self, *args, expect=0):
        r = subprocess.run([sys.executable, "taskflow.py", *args],
                           cwd=HERE, env=self.env, capture_output=True, text=True)
        self.assertEqual(r.returncode, expect, f"`taskflow {' '.join(args)}` -> {r.returncode}: {r.stderr}")
        return r.stdout

    def test_add_and_list_roundtrip(self):
        self.run_cli("add", "Write report", "--priority", "high", "--project", "work")
        out = self.run_cli("list")
        self.assertIn("Write report", out)
        self.assertIn("!!", out)  # high-priority marker
        self.assertIn("work", out)

    def test_done_hidden_by_default_shown_with_all(self):
        self.run_cli("add", "Task one")
        self.run_cli("done", "1")
        self.assertNotIn("Task one", self.run_cli("list"))
        self.assertIn("Task one", self.run_cli("list", "--all"))

    def test_overdue_is_never_flagged_BUG_D1(self):
        # Pins the CURRENT (buggy) behaviour: a long-past due date is NOT flagged overdue.
        past = (date.today() - timedelta(days=365)).isoformat()
        self.run_cli("add", "Old thing", "--due", past)
        self.assertIn("(no matching tasks)", self.run_cli("list", "--overdue"))
        self.assertIn("overdue:     0", self.run_cli("stats"))

    def test_limit_is_off_by_one_BUG_D2(self):
        # Pins the CURRENT (buggy) behaviour: `--limit 3` prints only two rows.
        for i in range(5):
            self.run_cli("add", f"T{i}")
        rows = [ln for ln in self.run_cli("list", "--limit", "3").splitlines() if ln.strip()]
        self.assertEqual(len(rows), 2)

    def test_stats_counts(self):
        self.run_cli("add", "A")
        self.run_cli("add", "B")
        self.run_cli("done", "1")
        out = self.run_cli("stats")
        self.assertIn("total tasks: 2", out)
        self.assertIn("done   1", out)


if __name__ == "__main__":
    unittest.main()
