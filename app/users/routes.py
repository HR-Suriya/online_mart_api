from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .schemas import UserCreate, UserRead
from .crud import create_user, get_user_by_username, get_user_by_email
from app.database import get_session

router = APIRouter()

@router.post("/users/", response_model=UserRead)
def create_user_route(user: UserCreate, session: Session = Depends(get_session)):
    db_user = get_user_by_username(session, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    db_user = get_user_by_email(session, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(session, user)

@router.get("/users/{username}", response_model=UserRead)
def read_user(username: str, session: Session = Depends(get_session)):
    db_user = get_user_by_username(session, username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
