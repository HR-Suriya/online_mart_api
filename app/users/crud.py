from sqlmodel import Session, select
from .models import User
from .schemas import UserCreate

def create_user(session: Session, user: UserCreate) -> User:
    db_user = User(username=user.username, email=user.email, hashed_password=user.password)  # Password should be hashed
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

def get_user_by_username(session: Session, username: str) -> User | None:
    statement = select(User).where(User.username == username)
    return session.exec(statement).first()

def get_user_by_email(session: Session, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    return session.exec(statement).first()
