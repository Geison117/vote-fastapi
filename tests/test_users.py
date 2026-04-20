import pytest
from app import schemas    
from jose import jwt
from app.config import settings



def test_root(client):
    response =client.get("/")
    print(response.json().get("message"))
    assert response.json().get("message") == "Hello World XD"
    assert response.status_code == 200


def test_create_user(client):
    response = client.post("/users/", json={"email": "gei2@gmail.com", "password": "1234"})
    new_user = schemas.UserOut(**response.json())

    assert new_user.email == "gei2@gmail.com"
    assert response.status_code == 201

def test_login_user(client, test_user):
    response = client.post(
        "/login", data={"username": test_user["email"], "password": test_user["password"]})
    
    login_res = schemas.Token(**response.json())
    payload = jwt.decode(login_res.access_token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    id = payload.get("user_id")
    assert response.status_code == 200
    assert login_res.token_type == "bearer"
    assert id == test_user["id"]

@pytest.mark.parametrize("email, password, status_code", [
    ("gei2@gmail.com", "wrong_password", 403),
    ("nonexistent@gmail.com", "password123", 403),
    (None, "password123", 422),
    ("nonexistent@gmail.com", None, 422),
    ("gei2@gmail.com", None, 422)
    ])
def test_incorrect_login(client, test_user, email, password, status_code):
    response = client.post(
        "/login", data={"username": email, "password": password})
    
    assert response.status_code == status_code    
    #assert response.json().get("detail") == "Invalid credentials"

       