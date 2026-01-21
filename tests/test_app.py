from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from app import app, get_db

def mock_get_db():
    return MagicMock()

app.dependency_overrides[get_db] = mock_get_db
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World with Database"}
