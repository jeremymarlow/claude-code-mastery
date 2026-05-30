"""Optional development seed data.

Run with ``python -m app.db.seed`` to populate a fresh database with a demo user, a project and a
handful of tasks. Idempotent: it does nothing if the demo user already exists. Not used by the test
suite (tests build their own fixtures), but handy for exploring the running API.
"""

from __future__ import annotations

from datetime import date, timedelta

from sqlmodel import Session, select

from app.core.security import hash_password
from app.db.session import engine, init_db
from app.models import Project, Task, TaskStatus, User

DEMO_EMAIL = "demo@taskflow.test"
DEMO_PASSWORD = "demo-password"


def seed() -> None:
    init_db()
    with Session(engine) as session:
        existing = session.exec(select(User).where(User.email == DEMO_EMAIL)).first()
        if existing is not None:
            print(f"Seed: user {DEMO_EMAIL!r} already exists — nothing to do.")
            return

        user = User(
            email=DEMO_EMAIL,
            full_name="Demo User",
            hashed_password=hash_password(DEMO_PASSWORD),
        )
        session.add(user)
        session.commit()
        session.refresh(user)

        project = Project(name="Website redesign", description="Q3 marketing site", owner_id=user.id)
        session.add(project)
        session.commit()
        session.refresh(project)

        today = date.today()
        tasks = [
            Task(
                title="Draft homepage copy",
                status=TaskStatus.in_progress,
                due_date=today + timedelta(days=3),
                project_id=project.id,
                assignee_id=user.id,
            ),
            Task(
                title="Pick a color palette",
                status=TaskStatus.todo,
                due_date=today + timedelta(days=7),
                project_id=project.id,
            ),
            Task(
                title="Set up analytics",
                status=TaskStatus.done,
                project_id=project.id,
                assignee_id=user.id,
            ),
        ]
        session.add_all(tasks)
        session.commit()

        print(
            f"Seed: created user {DEMO_EMAIL!r} (password {DEMO_PASSWORD!r}), "
            f"project {project.name!r} with {len(tasks)} tasks."
        )


if __name__ == "__main__":
    seed()
