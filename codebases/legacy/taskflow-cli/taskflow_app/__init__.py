# taskflow_app -- the TaskFlow CLI, refactored out of the original single-file taskflow.py.
#
# Layout (one responsibility per module):
#   constants   -- the small enumerations (priorities, statuses, defaults)
#   storage     -- the JSON db: load/save + the process-wide TASKS/CONFIG state + id allocation
#   domain      -- date parsing and the (single) overdue rule
#   lookups     -- find a task by id
#   formatting  -- how a task is rendered for `list` / `show`
#   commands    -- one cmd_* per subcommand
#   cli         -- argparse wiring + entry point
#
# Behaviour is identical to the old monolith on purpose (see taskflow.py).
VERSION = "0.9.3"
