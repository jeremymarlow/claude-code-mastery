"""Service-layer unit tests that exercise the domain logic directly (no HTTP).

These demonstrate that the services are usable and testable without the web layer — handy for the
course's testing unit.
"""

from __future__ import annotations

import pytest

from app.models import ProjectCreate, TaskCreate, TaskStatus, TaskUpdate
from app.services import projects as project_service
from app.services import tasks as task_service
from app.services.exceptions import NotFoundError
from app.services.tasks import TaskFilters
from tests.factory import create_user


def test_get_project_rejects_non_owner(session):
    owner = create_user(session, email="o@taskflow.test")
    other = create_user(session, email="x@taskflow.test")
    project = project_service.create_project(session, owner, ProjectCreate(name="P"))

    with pytest.raises(NotFoundError):
        project_service.get_project(session, other, project.id)


def test_list_tasks_filters_by_status(session):
    owner = create_user(session)
    project = project_service.create_project(session, owner, ProjectCreate(name="P"))
    task_service.create_task(session, owner, TaskCreate(title="a", status=TaskStatus.todo), project.id)
    task_service.create_task(session, owner, TaskCreate(title="b", status=TaskStatus.done), project.id)

    items, total = task_service.list_tasks(
        session, owner, TaskFilters(status=TaskStatus.done), limit=10, offset=0
    )
    assert total == 1
    assert items[0].title == "b"


def test_update_task_partial(session):
    owner = create_user(session)
    project = project_service.create_project(session, owner, ProjectCreate(name="P"))
    task = task_service.create_task(session, owner, TaskCreate(title="a"), project.id)

    updated = task_service.update_task(session, owner, task.id, TaskUpdate(title="renamed"))
    assert updated.title == "renamed"
    assert updated.status == TaskStatus.todo  # untouched
