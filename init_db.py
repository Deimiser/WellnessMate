# init_db.py

from src.db.database import engine, Base
from src.db import models  # Ensure models are imported so SQLAlchemy knows about them

# Create all tables in the database

Base.metadata.create_all(bind=engine)

print("Database initialized with tables!")
