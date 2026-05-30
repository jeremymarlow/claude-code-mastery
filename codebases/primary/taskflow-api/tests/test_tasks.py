"""Task endpoint tests: nested creation, filtering, sorting, pagination, and ownership."""

from __future__ import annotations

from datetime import date, timedelta

from tests.factory import auth_header, register_and_login


def _setup_project(client):
    h = auth_header(register_and_login(client, email="owner@taskflow.test"))
    pid = client.post("/projects", json={"name": "Board"}, headers=h).json()["id"]
    return h, pid


def test_create_task_under_project(client):
    h, pid = _setup_project(client)
    resp = client.post(
        f"/projects/{pid}/tasks",
        json={"title": "Write spec", "status": "in_progress"},
        headers=h,
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["title"] == "Write spec"
    assert body["status"] == "in_progress"
    assert body["project_id"] == pid


def test_create_task_in_foreign_project_is_404(client):
    h, _ = _setup_project(client)
    other_h = auth_header(register_and_login(client, email="other@taskflow.test"))
    other_pid = client.post("/projects", json={"name": "Theirs"}, headers=other_h).json()["id"]
    resp = client.post(f"/projects/{other_pid}/tasks", json={"title": "X"}, headers=h)
    assert resp.status_code == 404


def test_filter_tasks_by_status(client):
    h, pid = _setup_project(client)
    client.post(f"/projects/{pid}/tasks", json={"title": "a", "status": "todo"}, headers=h)
    client.post(f"/projects/{pid}/tasks", json={"title": "b", "status": "done"}, headers=h)
    client.post(f"/projects/{pid}/tasks", json={"title": "c", "status": "done"}, headers=h)

    done = client.get("/tasks?status=done", headers=h).json()
    assert done["total"] == 2
    assert {t["status"] for t in done["items"]} == {"done"}


def test_filter_tasks_by_due_window(client):
    h, pid = _setup_project(client)
    today = date.today()
    client.post(
        f"/projects/{pid}/tasks",
        json={"title": "soon", "due_date": str(today + timedelta(days=1))},
        headers=h,
    )
    client.post(
        f"/projects/{pid}/tasks",
        json={"title": "later", "due_date": str(today + timedelta(days=30))},
        headers=h,
    )
    cutoff = str(today + timedelta(days=7))
    resp = client.get(f"/tasks?due_before={cutoff}", headers=h).json()
    assert resp["total"] == 1
    assert resp["items"][0]["title"] == "soon"


def test_sort_tasks_by_due_date_ascending(client):
    h, pid = _setup_project(client)
    today = date.today()
    client.post(
        f"/projects/{pid}/tasks",
        json={"title": "second", "due_date": str(today + timedelta(days=5))},
        headers=h,
    )
    client.post(
        f"/projects/{pid}/tasks",
        json={"title": "first", "due_date": str(today + timedelta(days=1))},
        headers=h,
    )
    items = client.get("/tasks?sort=due_date&order=asc", headers=h).json()["items"]
    assert [t["title"] for t in items] == ["first", "second"]


def test_list_tasks_pagination(client):
    h, pid = _setup_project(client)
    for i in range(7):
        client.post(f"/projects/{pid}/tasks", json={"title": f"t{i}"}, headers=h)
    page = client.get("/tasks?limit=3&offset=6", headers=h).json()
    assert page["total"] == 7
    assert len(page["items"]) == 1


def test_update_task_changes_status_and_touches_updated_at(client):
    h, pid = _setup_project(client)
    created = client.post(f"/projects/{pid}/tasks", json={"title": "t"}, headers=h).json()
    tid = created["id"]
    resp = client.patch(f"/tasks/{tid}", json={"status": "done"}, headers=h)
    assert resp.status_code == 200
    updated = resp.json()
    assert updated["status"] == "done"
    assert updated["updated_at"] >= created["updated_at"]


def test_assign_task_to_unknown_user_is_404(client):
    h, pid = _setup_project(client)
    resp = client.post(
        f"/projects/{pid}/tasks", json={"title": "t", "assignee_id": 9999}, headers=h
    )
    assert resp.status_code == 404


def test_delete_task(client):
    h, pid = _setup_project(client)
    tid = client.post(f"/projects/{pid}/tasks", json={"title": "t"}, headers=h).json()["id"]
    assert client.delete(f"/tasks/{tid}", headers=h).status_code == 204
    assert client.get(f"/tasks/{tid}", headers=h).status_code == 404


def test_cannot_read_task_in_foreign_project(client):
    h, pid = _setup_project(client)
    tid = client.post(f"/projects/{pid}/tasks", json={"title": "secret"}, headers=h).json()["id"]
    other_h = auth_header(register_and_login(client, email="nosy@taskflow.test"))
    assert client.get(f"/tasks/{tid}", headers=other_h).status_code == 404


def test_deleting_project_cascades_to_tasks(client):
    h, pid = _setup_project(client)
    client.post(f"/projects/{pid}/tasks", json={"title": "t"}, headers=h)
    assert client.get("/tasks", headers=h).json()["total"] == 1
    client.delete(f"/projects/{pid}", headers=h)
    assert client.get("/tasks", headers=h).json()["total"] == 0
