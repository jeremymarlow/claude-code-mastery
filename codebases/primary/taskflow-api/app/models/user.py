"""User entity and its API schemas."""

from datetime import datetime, timezone
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:  # avoid runtime import cycles; relationships resolve via string names
    from app.models.project import Project
    from app.models.task import Task


class UserBase(SQLModel):
    email: str = Field(index=True, unique=True)
    full_name: Optional[str] = None


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    is_active: bool = True
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    projects: list["Project"] = Relationship(back_populates="owner")
    assigned_tasks: list["Task"] = Relationship(back_populates="assignee")


class UserCreate(UserBase):
    password: str


class UserUpdate(SQLModel):
    full_name: Optional[str] = None
    password: Optional[str] = None


class UserRead(UserBase):
    id: int
    is_active: bool
    created_at: datetime
