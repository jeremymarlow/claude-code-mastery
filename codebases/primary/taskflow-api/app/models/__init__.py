"""SQLModel entities and their request/response schemas.

Importing this package registers every table model with SQLModel's metadata, which the database
bootstrap (``app.db.session.init_db``) relies on. Import order matters only in that all three
modules must be imported before ``SQLModel.metadata.create_all`` runs.
"""

from app.models.user import User, UserCreate, UserRead, UserUpdate
from app.models.project import (
    Project,
    ProjectCreate,
    ProjectRead,
    ProjectStats,
    ProjectUpdate,
)
from app.models.task import (
    Task,
    TaskCreate,
    TaskRead,
    TaskStatus,
    TaskUpdate,
)
from app.models.comment import Comment, CommentCreate, CommentRead

__all__ = [
    "User",
    "UserCreate",
    "UserRead",
    "UserUpdate",
    "Project",
    "ProjectCreate",
    "ProjectRead",
    "ProjectStats",
    "ProjectUpdate",
    "Task",
    "TaskCreate",
    "TaskRead",
    "TaskUpdate",
    "TaskStatus",
    "Comment",
    "CommentCreate",
    "CommentRead",
]
