from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Fetch the database URL from the environment
DATABASE_URL = os.getenv("DATABASE_URL")

# Check if the DATABASE_URL is None and raise an informative error if so
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set. Please check your .env file or environment variables.")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()