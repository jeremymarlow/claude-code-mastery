"""Project endpoint tests: CRUD, pagination, and ownership isolation."""

from __future__ import annotations

from tests.factory import auth_header, register_and_login


def _owner(client):
    return auth_header(register_and_login(client, email="owner@taskflow.test"))


def test_create_and_get_project(client):
    h = _owner(client)
    resp = client.post("/projects", json={"name": "Launch", "description": "Q3"}, headers=h)
    assert resp.status_code == 201
    project_id = resp.json()["id"]

    got = client.get(f"/projects/{project_id}", headers=h)
    assert got.status_code == 200
    assert got.json()["name"] == "Launch"


def test_list_projects_is_paginated(client):
    h = _owner(client)
    for i in range(5):
        client.post("/projects", json={"name": f"P{i}"}, headers=h)

    resp = client.get("/projects?limit=2&offset=0", headers=h)
    body = resp.json()
    assert body["total"] == 5
    assert len(body["items"]) == 2
    assert body["limit"] == 2 and body["offset"] == 0

    page2 = client.get("/projects?limit=2&offset=4", headers=h).json()
    assert len(page2["items"]) == 1


def test_update_project(client):
    h = _owner(client)
    pid = client.post("/projects", json={"name": "Old"}, headers=h).json()["id"]
    resp = client.patch(f"/projects/{pid}", json={"name": "New"}, headers=h)
    assert resp.status_code == 200
    assert resp.json()["name"] == "New"


def test_delete_project(client):
    h = _owner(client)
    pid = client.post("/projects", json={"name": "Temp"}, headers=h).json()["id"]
    assert client.delete(f"/projects/{pid}", headers=h).status_code == 204
    assert client.get(f"/projects/{pid}", headers=h).status_code == 404


def test_cannot_see_another_users_project(client):
    owner_h = _owner(client)
    pid = client.post("/projects", json={"name": "Private"}, headers=owner_h).json()["id"]

    other_h = auth_header(register_and_login(client, email="intruder@taskflow.test"))
    # Hidden as 404 (not 403) so existence doesn't leak.
    assert client.get(f"/projects/{pid}", headers=other_h).status_code == 404
    assert client.get("/projects", headers=other_h).json()["total"] == 0


def test_project_routes_require_auth(client):
    assert client.get("/projects").status_code == 401
    assert client.post("/projects", json={"name": "x"}).status_code == 401


def test_owner_can_archive_own_project(client):
    h = _owner(client)
    pid = client.post("/projects", json={"name": "Done with this"}, headers=h).json()["id"]
    resp = client.post(f"/projects/{pid}/archive", headers=h)
    assert resp.status_code == 200
    assert resp.json()["archived"] is True


def test_archived_project_shown_when_requested(client):
    h = _owner(client)
    pid = client.post("/projects", json={"name": "Keep visible on request"}, headers=h).json()["id"]
    client.post(f"/projects/{pid}/archive", headers=h)
    ids = {p["id"] for p in client.get("/projects?include_archived=true", headers=h).json()["items"]}
    assert pid in ids


def test_archived_project_excluded_from_default_list(client):
    # The review finding: archived projects must be hidden by default (include_archived=false).
    h = _owner(client)
    pid = client.post("/projects", json={"name": "Hide me by default"}, headers=h).json()["id"]
    client.post(f"/projects/{pid}/archive", headers=h)
    ids = {p["id"] for p in client.get("/projects", headers=h).json()["items"]}
    assert pid not in ids


def test_cannot_archive_another_users_project(client):
    # The security finding (IDOR): archiving must be ownership-scoped, hidden as 404.
    owner_h = _owner(client)
    pid = client.post("/projects", json={"name": "Not yours"}, headers=owner_h).json()["id"]

    intruder_h = auth_header(register_and_login(client, email="intruder2@taskflow.test"))
    assert client.post(f"/projects/{pid}/archive", headers=intruder_h).status_code == 404
    # …and the project is untouched.
    assert client.get(f"/projects/{pid}", headers=owner_h).json()["archived"] is False
