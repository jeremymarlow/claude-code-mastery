"""Task domain logic: ownership-scoped CRUD plus filtering, sorting and pagination.

Tasks are reached only through projects the acting user owns. Listing supports filtering by
project, status, assignee and due-date window, with a small allow-list of sort fields.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Optional

from sqlmodel import Session, func, select

from app.models import Project, Task, TaskCreate, TaskStatus, TaskUpdate, User
from app.services.exceptions import NotFoundError
from app.services.projects import get_project

# Sort fields the API will honour, mapped to model columns. Anything else falls back to created_at.
_SORT_FIELDS = {
    "created_at": Task.created_at,
    "due_date": Task.due_date,
    "status": Task.status,
    "title": Task.title,
}


@dataclass
class TaskFilters:
    project_id: Optional[int] = None
    status: Optional[TaskStatus] = None
    assignee_id: Optional[int] = None
    due_before: Optional[date] = None
    due_after: Optional[date] = None
    sort: str = "created_at"
    descending: bool = True


def _owned_project_ids(session: Session, owner: User):
    return select(Project.id).where(Project.owner_id == owner.id)


def _validate_assignee(session: Session, assignee_id: Optional[int]) -> None:
    if assignee_id is None:
        return
    if session.get(User, assignee_id) is None:
        raise NotFoundError(f"User {assignee_id} not found")


def create_task(session: Session, owner: User, data: TaskCreate, project_id: int) -> Task:
    # get_project enforces that the owner actually owns the target project.
    get_project(session, owner, project_id)
    _validate_assignee(session, data.assignee_id)

    task = Task(project_id=project_id, **data.model_dump())
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def get_task(session: Session, owner: User, task_id: int) -> Task:
    task = session.get(Task, task_id)
    if task is None:
        raise NotFoundError(f"Task {task_id} not found")
    # Enforce ownership via the parent project (also raises NotFound if not owned).
    get_project(session, owner, task.project_id)
    return task


def list_tasks(
    session: Session, owner: User, filters: TaskFilters, *, limit: int, offset: int
) -> tuple[list[Task], int]:
    base = select(Task).where(Task.project_id.in_(_owned_project_ids(session, owner)))

    if filters.project_id is not None:
        # Confirm ownership of the named project so a foreign id yields 404, not an empty list.
        get_project(session, owner, filters.project_id)
        base = base.where(Task.project_id == filters.project_id)
    if filters.status is not None:
        base = base.where(Task.status == filters.status)
    if filters.assignee_id is not None:
        base = base.where(Task.assignee_id == filters.assignee_id)
    if filters.due_before is not None:
        base = base.where(Task.due_date <= filters.due_before)
    if filters.due_after is not None:
        base = base.where(Task.due_date >= filters.due_after)

    total = session.exec(select(func.count()).select_from(base.subquery())).one()

    column = _SORT_FIELDS.get(filters.sort, Task.created_at)
    order = column.desc() if filters.descending else column.asc()
    items = session.exec(base.order_by(order).offset(offset).limit(limit)).all()
    return list(items), total


def update_task(session: Session, owner: User, task_id: int, data: TaskUpdate) -> Task:
    task = get_task(session, owner, task_id)
    updates = data.model_dump(exclude_unset=True)
    if "assignee_id" in updates:
        _validate_assignee(session, updates["assignee_id"])

    for field, value in updates.items():
        setattr(task, field, value)
    if updates:
        task.updated_at = datetime.now(timezone.utc)

    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def delete_task(session: Session, owner: User, task_id: int) -> None:
    task = get_task(session, owner, task_id)
    session.delete(task)
    session.commit()
