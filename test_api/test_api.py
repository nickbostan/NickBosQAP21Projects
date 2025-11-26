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
