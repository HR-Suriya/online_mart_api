from fastapi import FastAPI
from sqlmodel import SQLModel
from contextlib import asynccontextmanager

from .users.routes import router as user_router
from .database import engine


# Function to create tables in the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic (e.g., initializing the database)
    create_db_and_tables()
    yield  # Yield control back to FastAPI
    # Shutdown logic (if any) can be added here


# Create the FastAPI app instance with the lifespan context
app = FastAPI(lifespan=lifespan)


# Include the user routes
app.include_router(user_router , prefix="/api")


# A sample root route for testing
@app.get("/")
async def root():
    return {"message": "Welcome to the online mart API"}
