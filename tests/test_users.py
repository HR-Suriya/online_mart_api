import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlmodel import SQLModel, create_engine
from app.database import get_session
from sqlmodel import Session

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)

@pytest.fixture(name="session")
def session_fixture():
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session: Session):
    app.dependency_overrides[get_session] = lambda: session
    with TestClient(app) as client:
        yield client

def test_create_user(client):
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "test@example.com"

def test_read_user(client):
    response = client.post("/users/", json={"username": "testuser", "email": "test@example.com"})
    user_id = response.json()["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
