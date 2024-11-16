from fastapi.testclient import TestClient
from main import app
client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


    # q を指定せずにテスト
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "q": None}
