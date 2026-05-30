"""Comment entity and its API schemas.

A comment is authored by a user against a task — a simple activity/discussion thread on a task.
"""

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.task import Task
    from app.models.user import User


class CommentBase(SQLModel):
    body: str = Field(min_length=1)


class Comment(CommentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task_id: int = Field(foreign_key="task.id", index=True)
    author_id: int = Field(foreign_key="user.id", index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    task: "Task" = Relationship(back_populates="comments")
    author: "User" = Relationship()


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    task_id: int
    author_id: int
    created_at: datetime
