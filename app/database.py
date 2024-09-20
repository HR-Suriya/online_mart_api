from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the database URL from the environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment")

# Create the engine with the database URL
engine = create_engine(DATABASE_URL)

# Function to get a database session
def get_session():
    with Session(engine) as session:
        yield session
