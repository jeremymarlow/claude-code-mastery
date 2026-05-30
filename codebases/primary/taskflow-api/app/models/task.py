"""Task entity and its API schemas.

A task lives in a project, has a workflow ``status``, an optional ``due_date`` and an optional
``assignee`` (a User).
"""

from datetime import date, datetime, timezone
from enum import Enum
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.comment import Comment
    from app.models.project import Project
    from app.models.user import User


class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TaskBase(SQLModel):
    title: str = Field(index=True)
    description: Optional[str] = None
    status: TaskStatus = Field(default=TaskStatus.todo, index=True)
    due_date: Optional[date] = None
    assignee_id: Optional[int] = Field(default=None, foreign_key="user.id", index=True)


class Task(TaskBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    project: "Project" = Relationship(back_populates="tasks")
    assignee: Optional["User"] = Relationship(back_populates="assigned_tasks")
    comments: list["Comment"] = Relationship(
        back_populates="task",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


class TaskCreate(TaskBase):
    pass


class TaskUpdate(SQLModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    due_date: Optional[date] = None
    assignee_id: Optional[int] = None


class TaskRead(TaskBase):
    id: int
    project_id: int
    created_at: datetime
    updated_at: datetime
