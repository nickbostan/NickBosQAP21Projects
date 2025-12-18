from datetime import datetime

import pytest
import requests

DOMAIN = "http://localhost:8000"


def test_create_new_user():
    user_data = {
        "username": "user666",
        "email": "user666@example.com",
        "password": "qwerty123!",
    }

    response = requests.post(f"{DOMAIN}/auth/register", json=user_data)

    assert response.status_code == 201
    response_json = response.json()
    print(response_json)
    assert response_json["token_type"] == "bearer"
    assert "access_token" in response_json


@pytest.fixture
def token():
    user_data = {
        "email": "users2@example.com",
        "password": "user123",
    }
    response = requests.post(f"{DOMAIN}/auth/login", json=user_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["access_token"]
    return response_json["access_token"]


def test_create_new_board(token):
    board_data = {"title": "string", "description": "abrakadabra", "public": False}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{DOMAIN}/boards/", json=board_data, headers=headers)
    assert response.status_code == 201
    response_json = response.json()
    print(response_json)
    assert response_json["title"] == "string"
    assert response_json["description"] == "abrakadabra"
    assert response_json["public"] is False
    assert "id" in response_json
    assert "created_at" in response_json


def test_create_board(token):
    user_data = {"title": "string", "description": "string", "public": False}

    headers = {"Authorization": f"Bearer {token}"}

    response = requests.post(f"{DOMAIN}/boards/", json=user_data, headers=headers)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["id"]
    assert response_json["archived"] is False
    assert response_json["created_by"]
    assert response_json["title"] == user_data["title"]
    assert response_json["description"] == user_data["description"]
    assert response_json["public"] == user_data["public"]

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_create_tasks(token):
    user_data = {
        "title": "Taskh",
        "description": "abrakadabra",
        "status": "todo",
        "priority": "high",
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        f"{DOMAIN}/boards/2/tasks", json=user_data, headers=headers
    )
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"]
    assert response_json["priority"] == "high"
    assert response_json["description"] == "abrakadabra"
