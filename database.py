from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Correct database URL (be careful with the password — the '@' sign inside it may break the URL)
URL_DATABASE = "postgresql://postgres:@localhost:5432/QuizAppYt"


# Create engine
engine = create_engine(URL_DATABASE)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare base class for models
Base = declarative_base()
