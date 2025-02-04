from fastapi.testclient import TestClient
from main import app
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

client = TestClient(app)

def test_read_main():
    print("テスト [/]エンドポイント")
    response = client.get("/")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200, f"Expected status 200 for /, got {response.status_code}"
    assert response.json() == {"message": "Hello, FastAPI!"}, f"Expected response {'message': 'Hello, FastAPI!'}, got {response.json()}"

def test_read_user():
    print("テスト [/users/user1]エンドポイント")
    response = client.get("/users/user1")
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    assert response.status_code == 200, f"Expected status 200 for /users/user1, got {response.status_code}"
    assert response.json() == {"user_password": "password1"}, f"Expected password 'password1' for user1, got {response.json()}"

    # print("テスト [/users/user3]エンドポイント")
    # response = client.get("/users/user3")
    # print(f"Status Code: {response.status_code}")
    # print(f"Response JSON: {response.json()}")
    # assert response.status_code == 200, f"Expected status 200 for /users/user3, got {response.status_code}"
    # assert response.json() == {"user_password": "null"}, f"Expected password 'null' for user3, got {response.json()}"


