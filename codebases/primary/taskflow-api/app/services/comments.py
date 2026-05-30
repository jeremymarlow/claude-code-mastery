"""Comment domain logic. Comments are reached through a task the acting user owns."""

from __future__ import annotations

from sqlmodel import Session, func, select

from app.models import Comment, CommentCreate, User
from app.services.tasks import get_task


def add_comment(session: Session, owner: User, task_id: int, data: CommentCreate) -> Comment:
    # get_task enforces that the owner owns the task's parent project.
    get_task(session, owner, task_id)
    comment = Comment(body=data.body, task_id=task_id, author_id=owner.id)
    session.add(comment)
    session.commit()
    session.refresh(comment)
    return comment


def list_comments(
    session: Session, owner: User, task_id: int, *, limit: int, offset: int
) -> tuple[list[Comment], int]:
    get_task(session, owner, task_id)
    base = select(Comment).where(Comment.task_id == task_id)
    total = session.exec(select(func.count()).select_from(base.subquery())).one()
    items = session.exec(
        base.order_by(Comment.created_at.asc()).offset(offset).limit(limit)
    ).all()
    return list(items), total
