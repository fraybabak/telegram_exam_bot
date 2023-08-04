from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create the engine, connecting to an SQLite database (it can be in-memory or file-based)
engine = create_engine('sqlite:///mydatabase.db') # File-based
# engine = create_engine('sqlite:///:memory:')    # In-memory

# Define the declarative base class
Base = declarative_base()

Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()