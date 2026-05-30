# Persistence + the process-wide task state.
#
# The original program kept TASKS / CONFIG in module globals that every function read and wrote
# directly. The refactor keeps that single shared store (behaviour-preserving) but in one place:
# other modules import `storage` and reference `storage.TASKS` / `storage.CONFIG` rather than
# re-declaring globals all over. (The dead `current_project` / `_dirty` flags were removed -- they
# were never read.)
import json
import os

DB_PATH = os.environ.get("TASKFLOW_DB", os.path.expanduser("~/.taskflow/tasks.json"))

TASKS = []          # list of task dicts
CONFIG = {}         # loaded config blob (default project, next id)
_loaded = False     # have we read the db yet this process?


def load_tasks():
    global TASKS, CONFIG, _loaded
    if _loaded:
        return
    if not os.path.exists(DB_PATH):
        TASKS = []
        CONFIG = {"default_project": None, "next_id": 1}
        _loaded = True
        return
    f = open(DB_PATH, "r")
    blob = json.load(f)
    f.close()
    # old files were just a bare list; new ones are {"tasks": [...], "config": {...}}
    if isinstance(blob, list):
        TASKS = blob
        CONFIG = {"default_project": None, "next_id": _guess_next_id(blob)}
    else:
        TASKS = blob.get("tasks", [])
        CONFIG = blob.get("config", {"default_project": None, "next_id": _guess_next_id(blob.get("tasks", []))})
    _loaded = True


def save_tasks():
    # Behaviour preserved verbatim, INCLUDING seeded bug D3: any write failure is silently
    # swallowed, so the caller prints "added/updated" even when nothing was persisted. Fixing this
    # is a separate change -- not part of the refactor. See codebases/SEEDED.md.
    try:
        d = os.path.dirname(DB_PATH)
        if d and not os.path.exists(d):
            os.makedirs(d)
        f = open(DB_PATH, "w")
        json.dump({"tasks": TASKS, "config": CONFIG}, f, indent=2)
        f.close()
    except Exception:
        pass


def _guess_next_id(tasks):
    # used at load time to initialise next_id for old/bare db files.
    mx = 0
    for t in tasks:
        if t.get("id", 0) > mx:
            mx = t["id"]
    return mx + 1


def next_id():
    # allocate and reserve the next id (distinct from _guess_next_id, which only *reads* a max).
    global CONFIG
    n = CONFIG.get("next_id", 1)
    CONFIG["next_id"] = n + 1
    return n
