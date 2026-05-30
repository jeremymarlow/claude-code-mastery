# Finding a task by id. The original had this written twice (`getTask` and `find_task_by_id`,
# byte-for-byte the same job); the refactor keeps one.
from . import storage


def get_task(tid):
    for t in storage.TASKS:
        if t.get("id") == tid:
            return t
    return None
