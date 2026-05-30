#!/usr/bin/env python3
# taskflow.py
#
# TaskFlow CLI -- the original command line task tracker.
#
# History (read this before you judge): this started life in 2019 as a ~80 line script that
# appended lines to a text file. Then we needed priorities. Then due dates. Then projects, then
# tags, then "can you make it export to CSV for the spreadsheet", then assignees because two of us
# were using the same file on a shared box. It all went into this one file because "we'll split it
# up later". We did not split it up later. The REST API (taskflow-api) eventually replaced this,
# but the CLI is still floating around on a few machines and the JSON files it produced are still
# out there, so it needs to keep working.
#
# There are no tests. There has never been a test. Be careful.
#
# Storage: a single JSON file (default ~/.taskflow/tasks.json, override with $TASKFLOW_DB).

import argparse
import csv
import datetime
import json
import os
import sys

VERSION = "0.9.3"
DB_PATH = os.environ.get("TASKFLOW_DB", os.path.expanduser("~/.taskflow/tasks.json"))

PRIORITIES = ["low", "normal", "high", "urgent"]
PRIORITY_ORDER = {"low": 0, "normal": 1, "high": 2, "urgent": 3}
STATUSES = ["todo", "doing", "done"]
DEFAULT_PRIORITY = "normal"
DEFAULT_STATUS = "todo"

# ---------------------------------------------------------------------------
# Global mutable state. Yes, all of it. The whole program reads and writes
# these directly; almost nothing is passed as an argument. (This is the single
# biggest thing a refactor would untangle.)
# ---------------------------------------------------------------------------
TASKS = []          # list of task dicts
CONFIG = {}         # loaded config blob (default project, etc.)
_loaded = False     # have we read the db yet this process?
_dirty = False      # is there anything to save?
current_project = None   # "active" project selection, set by --project on some commands


# ===========================================================================
# storage
# ===========================================================================
def loadTasks():
    # camelCase here, snake_case three functions down. Nobody agreed on a convention.
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
    # SEEDED BUG D3 (swallowed exception): any failure to write -- bad path, permission
    # error, a value that won't serialize -- is silently swallowed, so the caller prints
    # "added/updated" and the user believes it was saved when it was not. See codebases/SEEDED.md.
    global _dirty
    try:
        d = os.path.dirname(DB_PATH)
        if d and not os.path.exists(d):
            os.makedirs(d)
        f = open(DB_PATH, "w")
        json.dump({"tasks": TASKS, "config": CONFIG}, f, indent=2)
        f.close()
        _dirty = False
    except Exception:
        pass


def _guess_next_id(tasks):
    mx = 0
    for t in tasks:
        if t.get("id", 0) > mx:
            mx = t["id"]
    return mx + 1


def nextId():
    # duplicated id logic: this and _guess_next_id both "figure out the next id" but differently.
    global CONFIG
    n = CONFIG.get("next_id", 1)
    CONFIG["next_id"] = n + 1
    return n


# ===========================================================================
# lookups
# ===========================================================================
def getTask(tid):
    for t in TASKS:
        if t["id"] == tid:
            return t
    return None


def find_task_by_id(tid):
    # this is getTask again, written a second time by someone who didn't grep first.
    for t in TASKS:
        if t.get("id") == tid:
            return t
    return None


# ===========================================================================
# dates
# ===========================================================================
def parse_due_input(s):
    # Accepts a few shapes. Stores ISO (YYYY-MM-DD). Note that we DON'T validate hard --
    # whatever survives gets written, which is part of why is_overdue is such a mess.
    if not s:
        return None
    s = s.strip()
    if s.lower() == "today":
        return datetime.date.today().isoformat()
    if s.lower() == "tomorrow":
        return (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
    # try ISO first
    try:
        return datetime.datetime.strptime(s, "%Y-%m-%d").date().isoformat()
    except ValueError:
        pass
    # then US-style, because the spreadsheet exports came in that way
    try:
        return datetime.datetime.strptime(s, "%m/%d/%Y").date().isoformat()
    except ValueError:
        return s  # give up, store the raw string -- a latent landmine


def is_overdue(t):
    # SEEDED BUG D1 (naive date handling): this compares the stored due date (ISO,
    # "YYYY-MM-DD") against *today formatted a different way* ("MM-DD-YYYY"), as plain
    # strings. The lexicographic compare is meaningless across the two formats, so overdue
    # tasks are essentially never flagged. See codebases/SEEDED.md.
    due = t.get("due")
    if not due:
        return False
    if t.get("status") == "done":
        return False
    today = datetime.datetime.now().strftime("%m-%d-%Y")
    return due < today


def fmt_due(t):
    due = t.get("due")
    if not due:
        return ""
    # duplicated overdue check, inline, with the SAME bug as is_overdue but spelled differently
    try:
        today = datetime.datetime.now().strftime("%m-%d-%Y")
        if due < today and t.get("status") != "done":
            return due + " (OVERDUE)"
    except Exception:
        pass
    return due


# ===========================================================================
# formatting (priority + rows). duplicated in three places, of course.
# ===========================================================================
def priority_label(p):
    if p == "urgent":
        return "!!!"
    if p == "high":
        return "!! "
    if p == "normal":
        return " . "
    return "   "


def format_row(t):
    # used by `list`
    box = "[x]" if t.get("status") == "done" else "[ ]"
    pl = priority_label(t.get("priority", "normal"))
    proj = t.get("project") or "-"
    due = fmt_due(t)
    line = "%4d %s %s %-30s  %-10s  %s" % (
        t.get("id", 0), box, pl, (t.get("title", "")[:30]), proj, due
    )
    tags = t.get("tags") or []
    if tags:
        line = line + "  #" + " #".join(tags)
    return line


def print_task_full(t):
    # used by `show` -- re-implements most of format_row instead of reusing it
    print("id:        %s" % t.get("id"))
    print("title:     %s" % t.get("title"))
    print("status:    %s" % t.get("status"))
    print("priority:  %s" % t.get("priority"))
    print("project:   %s" % (t.get("project") or "-"))
    print("assignee:  %s" % (t.get("assignee") or "-"))
    due = t.get("due")
    if due:
        # third copy of the overdue logic, third slightly different spelling
        flag = ""
        try:
            if t.get("status") != "done" and due < datetime.datetime.now().strftime("%m-%d-%Y"):
                flag = "  <-- overdue"
        except Exception:
            pass
        print("due:       %s%s" % (due, flag))
    else:
        print("due:       -")
    tags = t.get("tags") or []
    print("tags:      %s" % (", ".join(tags) if tags else "-"))
    if t.get("notes"):
        print("notes:")
        print("  " + t.get("notes"))
    print("created:   %s" % t.get("created", "?"))
    print("updated:   %s" % t.get("updated", "?"))


# ===========================================================================
# commands
# ===========================================================================
def cmd_add(args):
    loadTasks()
    title = " ".join(args.title).strip()
    if not title:
        print("error: a task needs a title", file=sys.stderr)
        return 2
    pr = args.priority or DEFAULT_PRIORITY
    if pr not in PRIORITIES:
        print("error: unknown priority %r (use one of %s)" % (pr, ", ".join(PRIORITIES)), file=sys.stderr)
        return 2
    proj = args.project or CONFIG.get("default_project")
    t = {
        "id": nextId(),
        "title": title,
        "status": DEFAULT_STATUS,
        "priority": pr,
        "project": proj,
        "assignee": args.assignee,
        "tags": list(args.tag) if args.tag else [],
        "due": parse_due_input(args.due),
        "notes": args.notes,
        "created": datetime.datetime.now().isoformat(timespec="seconds"),
        "updated": datetime.datetime.now().isoformat(timespec="seconds"),
    }
    TASKS.append(t)
    save_tasks()
    print("added #%d: %s" % (t["id"], t["title"]))
    return 0


def cmd_list(args):
    loadTasks()
    rows = list(TASKS)

    # filters
    if not args.all:
        rows = [t for t in rows if t.get("status") != "done"]
    if args.project:
        rows = [t for t in rows if t.get("project") == args.project]
    if args.status:
        rows = [t for t in rows if t.get("status") == args.status]
    if args.priority:
        rows = [t for t in rows if t.get("priority") == args.priority]
    if args.tag:
        rows = [t for t in rows if args.tag in (t.get("tags") or [])]
    if args.assignee:
        rows = [t for t in rows if t.get("assignee") == args.assignee]
    if args.overdue:
        rows = [t for t in rows if is_overdue(t)]

    # sorting
    if args.sort == "priority":
        rows.sort(key=lambda t: PRIORITY_ORDER.get(t.get("priority", "normal"), 1), reverse=True)
    elif args.sort == "due":
        rows.sort(key=lambda t: (t.get("due") is None, t.get("due") or ""))
    elif args.sort == "created":
        rows.sort(key=lambda t: t.get("created", ""))
    else:
        rows.sort(key=lambda t: t.get("id", 0))

    # SEEDED BUG D2 (off-by-one in listing): --limit N shows only N-1 tasks because of the
    # `-1`. Someone added it thinking they had to leave room for the header row. They did not.
    # See codebases/SEEDED.md.
    if args.limit is not None:
        rows = rows[: args.limit - 1]

    if not rows:
        print("(no matching tasks)")
        return 0
    for t in rows:
        print(format_row(t))
    return 0


def cmd_show(args):
    loadTasks()
    t = getTask(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    print_task_full(t)
    return 0


def cmd_done(args):
    loadTasks()
    t = getTask(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "done"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    save_tasks()
    print("completed #%d" % t["id"])
    return 0


def cmd_start(args):
    loadTasks()
    t = find_task_by_id(args.id)   # note: the *other* lookup function, for no reason
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "doing"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    save_tasks()
    print("started #%d" % t["id"])
    return 0


def cmd_reopen(args):
    loadTasks()
    t = getTask(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["status"] = "todo"
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    save_tasks()
    print("reopened #%d" % t["id"])
    return 0


def cmd_rm(args):
    loadTasks()
    global TASKS
    before = len(TASKS)
    TASKS = [t for t in TASKS if t.get("id") != args.id]
    if len(TASKS) == before:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    save_tasks()
    print("removed #%d" % args.id)
    return 0


def cmd_edit(args):
    loadTasks()
    t = getTask(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    if args.title:
        t["title"] = " ".join(args.title).strip()
    if args.priority:
        if args.priority not in PRIORITIES:
            print("error: unknown priority %r" % args.priority, file=sys.stderr)
            return 2
        t["priority"] = args.priority
    if args.project is not None:
        t["project"] = args.project or None
    if args.assignee is not None:
        t["assignee"] = args.assignee or None
    if args.due is not None:
        t["due"] = parse_due_input(args.due)
    if args.notes is not None:
        t["notes"] = args.notes
    if args.tag:
        t["tags"] = list(args.tag)
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    save_tasks()
    print("updated #%d" % t["id"])
    return 0


def cmd_assign(args):
    loadTasks()
    t = getTask(args.id)
    if not t:
        print("error: no task #%d" % args.id, file=sys.stderr)
        return 1
    t["assignee"] = args.who
    t["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
    save_tasks()
    print("assigned #%d to %s" % (t["id"], args.who))
    return 0


def cmd_search(args):
    loadTasks()
    q = args.query.lower()
    hits = []
    for t in TASKS:
        hay = " ".join([
            str(t.get("title", "")),
            str(t.get("notes", "") or ""),
            " ".join(t.get("tags") or []),
            str(t.get("project") or ""),
        ]).lower()
        if q in hay:
            hits.append(t)
    if not hits:
        print("(no matches)")
        return 0
    for t in hits:
        print(format_row(t))
    return 0


def cmd_projects(args):
    loadTasks()
    projs = {}
    for t in TASKS:
        p = t.get("project") or "(none)"
        if p not in projs:
            projs[p] = {"total": 0, "open": 0}
        projs[p]["total"] += 1
        if t.get("status") != "done":
            projs[p]["open"] += 1
    for name in sorted(projs.keys()):
        s = projs[name]
        print("%-20s  %d open / %d total" % (name, s["open"], s["total"]))
    return 0


def cmd_tags(args):
    loadTasks()
    counts = {}
    for t in TASKS:
        for tag in (t.get("tags") or []):
            counts[tag] = counts.get(tag, 0) + 1
    for tag in sorted(counts.keys()):
        print("#%-15s %d" % (tag, counts[tag]))
    return 0


def cmd_stats(args):
    loadTasks()
    total = len(TASKS)
    by_status = {}
    by_priority = {}
    overdue = 0
    for t in TASKS:
        st = t.get("status", "todo")
        by_status[st] = by_status.get(st, 0) + 1
        pr = t.get("priority", "normal")
        by_priority[pr] = by_priority.get(pr, 0) + 1
        if is_overdue(t):
            overdue += 1
    print("total tasks: %d" % total)
    print("by status:")
    for st in STATUSES:
        print("  %-6s %d" % (st, by_status.get(st, 0)))
    print("by priority:")
    for pr in PRIORITIES:
        print("  %-7s %d" % (pr, by_priority.get(pr, 0)))
    print("overdue:     %d" % overdue)
    return 0


def cmd_export(args):
    loadTasks()
    if args.format == "json":
        json.dump(TASKS, sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    elif args.format == "csv":
        w = csv.writer(sys.stdout)
        w.writerow(["id", "title", "status", "priority", "project", "assignee", "due", "tags"])
        for t in TASKS:
            w.writerow([
                t.get("id"), t.get("title"), t.get("status"), t.get("priority"),
                t.get("project"), t.get("assignee"), t.get("due"),
                " ".join(t.get("tags") or []),
            ])
        return 0
    else:
        print("error: unknown export format %r" % args.format, file=sys.stderr)
        return 2


def cmd_import(args):
    loadTasks()
    global TASKS
    f = open(args.path, "r")
    incoming = json.load(f)
    f.close()
    n = 0
    for t in incoming:
        # naive merge: just append and renumber. duplicate detection? someday.
        t["id"] = nextId()
        TASKS.append(t)
        n += 1
    save_tasks()
    print("imported %d tasks" % n)
    return 0


def cmd_archive(args):
    # move done tasks out to an archive file. only half-built; the restore side never got written.
    loadTasks()
    global TASKS
    done = [t for t in TASKS if t.get("status") == "done"]
    if not done:
        print("nothing to archive")
        return 0
    archive_path = DB_PATH + ".archive"
    existing = []
    if os.path.exists(archive_path):
        af = open(archive_path, "r")
        existing = json.load(af)
        af.close()
    existing.extend(done)
    af = open(archive_path, "w")
    json.dump(existing, af, indent=2)
    af.close()
    TASKS = [t for t in TASKS if t.get("status") != "done"]
    save_tasks()
    print("archived %d done task(s) to %s" % (len(done), archive_path))
    return 0


def cmd_config(args):
    loadTasks()
    if args.action == "get":
        print(json.dumps(CONFIG, indent=2))
    elif args.action == "set-default-project":
        CONFIG["default_project"] = args.value or None
        save_tasks()
        print("default project = %s" % CONFIG["default_project"])
    else:
        print("error: unknown config action", file=sys.stderr)
        return 2
    return 0


# ===========================================================================
# DEAD CODE BELOW. None of this is wired into the argument parser. It has been
# "about to be used" for years. Left here exactly as found.
# ===========================================================================
USE_LEGACY_FORMAT = False   # never read anywhere


def export_xml(tasks):
    # we were going to support XML for some integration that never happened.
    out = ["<tasks>"]
    for t in tasks:
        out.append("  <task id='%s'>%s</task>" % (t.get("id"), t.get("title")))
    out.append("</tasks>")
    return "\n".join(out)


def migrate_v1_to_v2(tasks):
    # one-time migration that was already run on every file we care about.
    for t in tasks:
        if "priority" not in t:
            t["priority"] = "normal"
        if "tags" not in t:
            t["tags"] = []
    return tasks


def recalc_next_id():
    # superseded by nextId()/_guess_next_id, kept "just in case".
    global CONFIG
    CONFIG["next_id"] = _guess_next_id(TASKS)


# def cmd_notify(args):
#     # email reminders for overdue tasks. needs is_overdue to actually work first.
#     for t in TASKS:
#         if is_overdue(t):
#             send_email(t)   # send_email never existed


# ===========================================================================
# argument parsing / entry point
# ===========================================================================
def build_parser():
    p = argparse.ArgumentParser(prog="taskflow", description="TaskFlow CLI (%s)" % VERSION)
    p.add_argument("--version", action="version", version="taskflow " + VERSION)
    sub = p.add_subparsers(dest="cmd")

    a = sub.add_parser("add", help="add a task")
    a.add_argument("title", nargs="+")
    a.add_argument("--due")
    a.add_argument("--priority", "-p")
    a.add_argument("--project")
    a.add_argument("--assignee")
    a.add_argument("--tag", action="append")
    a.add_argument("--notes")
    a.set_defaults(func=cmd_add)

    ls = sub.add_parser("list", help="list tasks")
    ls.add_argument("--all", action="store_true", help="include done tasks")
    ls.add_argument("--project")
    ls.add_argument("--status", choices=STATUSES)
    ls.add_argument("--priority", choices=PRIORITIES)
    ls.add_argument("--tag")
    ls.add_argument("--assignee")
    ls.add_argument("--overdue", action="store_true")
    ls.add_argument("--sort", choices=["id", "priority", "due", "created"], default="id")
    ls.add_argument("--limit", type=int)
    ls.set_defaults(func=cmd_list)

    sh = sub.add_parser("show", help="show one task")
    sh.add_argument("id", type=int)
    sh.set_defaults(func=cmd_show)

    dn = sub.add_parser("done", help="mark a task done")
    dn.add_argument("id", type=int)
    dn.set_defaults(func=cmd_done)

    st = sub.add_parser("start", help="mark a task in progress")
    st.add_argument("id", type=int)
    st.set_defaults(func=cmd_start)

    ro = sub.add_parser("reopen", help="reopen a task")
    ro.add_argument("id", type=int)
    ro.set_defaults(func=cmd_reopen)

    rm = sub.add_parser("rm", help="remove a task")
    rm.add_argument("id", type=int)
    rm.set_defaults(func=cmd_rm)

    ed = sub.add_parser("edit", help="edit a task")
    ed.add_argument("id", type=int)
    ed.add_argument("--title", nargs="+")
    ed.add_argument("--due")
    ed.add_argument("--priority")
    ed.add_argument("--project")
    ed.add_argument("--assignee")
    ed.add_argument("--tag", action="append")
    ed.add_argument("--notes")
    ed.set_defaults(func=cmd_edit)

    asg = sub.add_parser("assign", help="assign a task to someone")
    asg.add_argument("id", type=int)
    asg.add_argument("who")
    asg.set_defaults(func=cmd_assign)

    se = sub.add_parser("search", help="search tasks")
    se.add_argument("query")
    se.set_defaults(func=cmd_search)

    pr = sub.add_parser("projects", help="list projects with counts")
    pr.set_defaults(func=cmd_projects)

    tg = sub.add_parser("tags", help="list tags with counts")
    tg.set_defaults(func=cmd_tags)

    stt = sub.add_parser("stats", help="summary statistics")
    stt.set_defaults(func=cmd_stats)

    ex = sub.add_parser("export", help="export tasks")
    ex.add_argument("--format", choices=["json", "csv"], default="json")
    ex.set_defaults(func=cmd_export)

    im = sub.add_parser("import", help="import tasks from a json file")
    im.add_argument("path")
    im.set_defaults(func=cmd_import)

    ar = sub.add_parser("archive", help="archive done tasks")
    ar.set_defaults(func=cmd_archive)

    cf = sub.add_parser("config", help="get/set config")
    cf.add_argument("action", choices=["get", "set-default-project"])
    cf.add_argument("value", nargs="?")
    cf.set_defaults(func=cmd_config)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "cmd", None):
        parser.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
