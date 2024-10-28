from app.models.database import Base, engine

# Recreate all tables
Base.metadata.create_all(bind=engine)
print("All tables created successfully.")
