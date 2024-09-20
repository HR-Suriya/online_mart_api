from database import DATABASE_URL, get_session
from sqlmodel import SQLModel, create_engine, Session

# Test the database connection
def test_connection():
    try:
        engine = create_engine(DATABASE_URL)
        SQLModel.metadata.create_all(engine)  # Create tables if they don't exist
        with Session(engine) as session:
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    test_connection()
