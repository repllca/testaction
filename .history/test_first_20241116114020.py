from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_user():
    response = client.get("/users/user1")
    assert response.status_code == 200
    assert response.json() == {"user_password": "password1"}

    response = client.get("/users/user3")
    assert response.status_code == 200
    assert response.json() == {"user_password": "null"}
