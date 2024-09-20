import pytest
from sqlmodel import Session, create_engine, SQLModel
from app.database import DATABASE_URL
from app.users.models import User
from app.users.crud import create_user, get_user_by_username, get_user_by_email
from app.users.schemas import UserCreate
from typing import Generator

# Create an in-memory SQLite database for testing
sqlite_url = "sqlite:///"
engine = create_engine(sqlite_url, echo=True)
SQLModel.metadata.create_all(engine)

@pytest.fixture
def session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

def test_create_user(session: Session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="hashed_password")
    user = create_user(session, user_data)
    assert user.id is not None
    assert user.username == "testuser"
    assert user.email == "test@example.com"

def test_get_user_by_username(session: Session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="hashed_password")
    create_user(session, user_data)
    user = get_user_by_username(session, "testuser")
    assert user is not None
    assert user.username == "testuser"

def test_get_user_by_email(session: Session):
    user_data = UserCreate(username="testuser", email="test@example.com", password="hashed_password")
    create_user(session, user_data)
    user = get_user_by_email(session, "test@example.com")
    assert user is not None
    assert user.email == "test@example.com"
