"""Task routes.

Creation is nested under a project (``POST /projects/{id}/tasks``); the remaining operations are
flat (``/tasks/{id}``) with a rich filtered/sorted/paginated list at ``GET /tasks``.
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, Query, status
from sqlmodel import Session

from app.api.deps import Pagination, get_current_user, pagination_params
from app.api.schemas import Page
from app.db.session import get_session
from app.models import ProjectStats, Task, TaskCreate, TaskRead, TaskStatus, TaskUpdate, User
from app.services import tasks as task_service
from app.services.tasks import TaskFilters

router = APIRouter(tags=["tasks"])

_SORT_CHOICES = ("created_at", "due_date", "status", "title")


@router.post(
    "/projects/{project_id}/tasks",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    project_id: int,
    data: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Task:
    return task_service.create_task(session, current_user, data, project_id)


@router.get("/projects/{project_id}/stats", response_model=ProjectStats, tags=["projects"])
def project_stats(
    project_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> ProjectStats:
    counts = task_service.project_task_stats(session, current_user, project_id)
    return ProjectStats(project_id=project_id, total=sum(counts.values()), by_status=counts)


@router.get("/tasks", response_model=Page[TaskRead])
def list_tasks(
    project_id: Optional[int] = Query(default=None),
    status_filter: Optional[TaskStatus] = Query(default=None, alias="status"),
    assignee_id: Optional[int] = Query(default=None),
    due_before: Optional[date] = Query(default=None),
    due_after: Optional[date] = Query(default=None),
    sort: str = Query(default="created_at"),
    order: str = Query(default="desc", pattern="^(asc|desc)$"),
    page: Pagination = Depends(pagination_params),
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Page[TaskRead]:
    filters = TaskFilters(
        project_id=project_id,
        status=status_filter,
        assignee_id=assignee_id,
        due_before=due_before,
        due_after=due_after,
        sort=sort if sort in _SORT_CHOICES else "created_at",
        descending=(order == "desc"),
    )
    items, total = task_service.list_tasks(
        session, current_user, filters, limit=page.limit, offset=page.offset
    )
    return Page(items=items, total=total, limit=page.limit, offset=page.offset)


@router.get("/tasks/{task_id}", response_model=TaskRead)
def get_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Task:
    return task_service.get_task(session, current_user, task_id)


@router.patch("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    task_id: int,
    data: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> Task:
    return task_service.update_task(session, current_user, task_id, data)


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session),
) -> None:
    task_service.delete_task(session, current_user, task_id)
