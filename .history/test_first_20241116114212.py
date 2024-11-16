from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_user():
    response = client.get("/users/user1")
    assert response.status_code == 200, f"Expected status 200 for /users/user1, got {response.status_code}"
    assert response.json() == {"user_password": "password1"}, f"Expected password 'password1' for user1, got {response.json()}"

    response = client.get("/users/user3")
    assert response.status_code == 200, f"Expected status 200 for /users/user3, got {response.status_code}"
    assert response.json() == {"user_password": "null"}, f"Expected password 'null' for user3, got {response.json()}"

