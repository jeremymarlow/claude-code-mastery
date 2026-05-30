"""Small test data helpers — just enough to keep the tests readable.

These work two ways:
- ``create_user`` / ``create_project`` / ``create_task`` write rows directly via a Session.
- ``register_and_login`` / ``auth_header`` drive the real HTTP endpoints for end-to-end tests.
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from fastapi.testclient import TestClient
from sqlmodel import Session

from app.core.security import hash_password
from app.models import Project, Task, TaskStatus, User

_counter = {"n": 0}


def _next() -> int:
    _counter["n"] += 1
    return _counter["n"]


def create_user(
    session: Session, *, email: Optional[str] = None, password: str = "password123"
) -> User:
    email = email or f"user{_next()}@taskflow.test"
    user = User(email=email, full_name="Test User", hashed_password=hash_password(password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def create_project(session: Session, owner: User, *, name: str = "Project") -> Project:
    project = Project(name=name, owner_id=owner.id)
    session.add(project)
    session.commit()
    session.refresh(project)
    return project


def create_task(
    session: Session,
    project: Project,
    *,
    title: str = "Task",
    status: TaskStatus = TaskStatus.todo,
    due_date: Optional[date] = None,
    assignee_id: Optional[int] = None,
) -> Task:
    task = Task(
        title=title,
        status=status,
        due_date=due_date,
        assignee_id=assignee_id,
        project_id=project.id,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


def register_and_login(
    client: TestClient, *, email: str = "owner@taskflow.test", password: str = "password123"
) -> str:
    """Register a user via the API and return a bearer token."""
    client.post("/auth/register", json={"email": email, "password": password})
    resp = client.post("/auth/login", data={"username": email, "password": password})
    assert resp.status_code == 200, resp.text
    return resp.json()["access_token"]


def auth_header(token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {token}"}
