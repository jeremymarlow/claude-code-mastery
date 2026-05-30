"""Comment endpoint tests: nested creation, listing order, and ownership."""

from __future__ import annotations

from tests.factory import auth_header, register_and_login


def _task(client):
    h = auth_header(register_and_login(client, email="owner@taskflow.test"))
    pid = client.post("/projects", json={"name": "Board"}, headers=h).json()["id"]
    tid = client.post(f"/projects/{pid}/tasks", json={"title": "t"}, headers=h).json()["id"]
    return h, tid


def test_add_and_list_comments_in_order(client):
    h, tid = _task(client)
    for body in ("first", "second", "third"):
        resp = client.post(f"/tasks/{tid}/comments", json={"body": body}, headers=h)
        assert resp.status_code == 201

    listed = client.get(f"/tasks/{tid}/comments", headers=h).json()
    assert listed["total"] == 3
    assert [c["body"] for c in listed["items"]] == ["first", "second", "third"]


def test_empty_comment_is_rejected(client):
    h, tid = _task(client)
    assert client.post(f"/tasks/{tid}/comments", json={"body": ""}, headers=h).status_code == 422


def test_cannot_comment_on_foreign_task(client):
    h, tid = _task(client)
    other_h = auth_header(register_and_login(client, email="nosy@taskflow.test"))
    assert client.post(f"/tasks/{tid}/comments", json={"body": "hi"}, headers=other_h).status_code == 404
    assert client.get(f"/tasks/{tid}/comments", headers=other_h).status_code == 404


def test_comments_require_auth(client):
    _, tid = _task(client)
    assert client.get(f"/tasks/{tid}/comments").status_code == 401
