# Argument parsing and entry point. Wiring only -- the work lives in commands.py.
import argparse

from . import VERSION
from . import commands
from .constants import PRIORITIES, STATUSES


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
    a.set_defaults(func=commands.cmd_add)

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
    ls.set_defaults(func=commands.cmd_list)

    sh = sub.add_parser("show", help="show one task")
    sh.add_argument("id", type=int)
    sh.set_defaults(func=commands.cmd_show)

    dn = sub.add_parser("done", help="mark a task done")
    dn.add_argument("id", type=int)
    dn.set_defaults(func=commands.cmd_done)

    st = sub.add_parser("start", help="mark a task in progress")
    st.add_argument("id", type=int)
    st.set_defaults(func=commands.cmd_start)

    ro = sub.add_parser("reopen", help="reopen a task")
    ro.add_argument("id", type=int)
    ro.set_defaults(func=commands.cmd_reopen)

    rm = sub.add_parser("rm", help="remove a task")
    rm.add_argument("id", type=int)
    rm.set_defaults(func=commands.cmd_rm)

    ed = sub.add_parser("edit", help="edit a task")
    ed.add_argument("id", type=int)
    ed.add_argument("--title", nargs="+")
    ed.add_argument("--due")
    ed.add_argument("--priority")
    ed.add_argument("--project")
    ed.add_argument("--assignee")
    ed.add_argument("--tag", action="append")
    ed.add_argument("--notes")
    ed.set_defaults(func=commands.cmd_edit)

    asg = sub.add_parser("assign", help="assign a task to someone")
    asg.add_argument("id", type=int)
    asg.add_argument("who")
    asg.set_defaults(func=commands.cmd_assign)

    se = sub.add_parser("search", help="search tasks")
    se.add_argument("query")
    se.set_defaults(func=commands.cmd_search)

    pr = sub.add_parser("projects", help="list projects with counts")
    pr.set_defaults(func=commands.cmd_projects)

    tg = sub.add_parser("tags", help="list tags with counts")
    tg.set_defaults(func=commands.cmd_tags)

    stt = sub.add_parser("stats", help="summary statistics")
    stt.set_defaults(func=commands.cmd_stats)

    ex = sub.add_parser("export", help="export tasks")
    ex.add_argument("--format", choices=["json", "csv"], default="json")
    ex.set_defaults(func=commands.cmd_export)

    im = sub.add_parser("import", help="import tasks from a json file")
    im.add_argument("path")
    im.set_defaults(func=commands.cmd_import)

    ar = sub.add_parser("archive", help="archive done tasks")
    ar.set_defaults(func=commands.cmd_archive)

    cf = sub.add_parser("config", help="get/set config")
    cf.add_argument("action", choices=["get", "set-default-project"])
    cf.add_argument("value", nargs="?")
    cf.set_defaults(func=commands.cmd_config)

    return p


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "cmd", None):
        parser.print_help()
        return 0
    return args.func(args)
