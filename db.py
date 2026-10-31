# SQLAlchemy helps this app connect to and use a database.
# create_engine prepares the database connection.
from sqlalchemy import create_engine

# A session is a temporary place to read or save database information.
# sessionmaker creates sessions. declarative_base is used to define database tables.
from sqlalchemy.orm import sessionmaker, declarative_base

# python-dotenv loads settings from a .env file so the app can use them.
from dotenv import load_dotenv

# os lets the app read system settings, such as the database connection address,
# instead of writing private details directly in the code.
import os

load_dotenv()  # Load environment variables from .env file
SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")  # Get the database URL from environment variables

engine = create_engine(SQLALCHEMY_DATABASE_URL)  # Create a database engine using the URL
Base = declarative_base()  # Create a base class for defining database tables
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """Provide a database session and close it when the caller is finished.

    Expected input: None.
    Output: Yields a database session for reading or saving data.
    What it does: Opens a session, gives it to the caller, then closes it.
    Why it is needed: Lets app code use the database without leaving sessions open.
    """
    # Open a temporary database session for the caller to use.
    db = SessionLocal()  # Create a database session for interacting with the database
    try:
        yield db  # Provide the database session to the caller
    finally:
        db.close()  # Ensure the database session is closed after use

def create_tables():
    """Create database tables described by the app's models.

    Expected input: None.
    Output: None.
    What it does: Creates any model tables that do not already exist.
    Why it is needed: Prepares the database to store the app's data.
    """
    # Create the tables described by the app's database models.
    Base.metadata.create_all(bind=engine)  # Create tables in the database based on the defined models