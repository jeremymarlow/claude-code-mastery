"""Project entity and its API schemas.

A project belongs to one owner (a User) and contains many tasks.
"""

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.models.task import Task
    from app.models.user import User


class ProjectBase(SQLModel):
    name: str = Field(index=True)
    description: Optional[str] = None


class Project(ProjectBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    owner_id: int = Field(foreign_key="user.id", index=True)
    archived: bool = Field(default=False, index=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    owner: "User" = Relationship(back_populates="projects")
    tasks: list["Task"] = Relationship(
        back_populates="project",
        sa_relationship_kwargs={"cascade": "all, delete-orphan"},
    )


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(SQLModel):
    name: Optional[str] = None
    description: Optional[str] = None


class ProjectRead(ProjectBase):
    id: int
    owner_id: int
    archived: bool
    created_at: datetime
