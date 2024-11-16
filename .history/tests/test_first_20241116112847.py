from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    # item_id と q の両方を指定してテスト
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": "test"}

    # q を指定せずにテスト
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}
