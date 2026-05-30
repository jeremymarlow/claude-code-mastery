"""Auth endpoint tests: registration, login, and the authenticated identity route."""

from __future__ import annotations

from tests.factory import auth_header, register_and_login


def test_register_returns_created_user_without_password(client):
    resp = client.post(
        "/auth/register",
        json={"email": "new@taskflow.test", "password": "password123", "full_name": "New"},
    )
    assert resp.status_code == 201
    body = resp.json()
    assert body["email"] == "new@taskflow.test"
    assert body["full_name"] == "New"
    assert "id" in body
    assert "password" not in body
    assert "hashed_password" not in body


def test_duplicate_registration_conflicts(client):
    payload = {"email": "dupe@taskflow.test", "password": "password123"}
    assert client.post("/auth/register", json=payload).status_code == 201
    resp = client.post("/auth/register", json=payload)
    assert resp.status_code == 409


def test_login_with_bad_password_is_unauthorized(client):
    client.post("/auth/register", json={"email": "u@taskflow.test", "password": "rightpassword"})
    resp = client.post(
        "/auth/login", data={"username": "u@taskflow.test", "password": "wrongpassword"}
    )
    assert resp.status_code == 401


def test_login_unknown_user_is_unauthorized(client):
    resp = client.post("/auth/login", data={"username": "ghost@taskflow.test", "password": "x"})
    assert resp.status_code == 401


def test_me_requires_authentication(client):
    assert client.get("/users/me").status_code == 401


def test_me_returns_current_user(client):
    token = register_and_login(client, email="me@taskflow.test")
    resp = client.get("/users/me", headers=auth_header(token))
    assert resp.status_code == 200
    assert resp.json()["email"] == "me@taskflow.test"


def test_invalid_token_is_rejected(client):
    resp = client.get("/users/me", headers={"Authorization": "Bearer not.a.jwt"})
    assert resp.status_code == 401
