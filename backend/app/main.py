from fastapi import FastAPI
from .api import pdf_upload, questions
from .models.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register the routers
app.include_router(pdf_upload.router, prefix="/pdf")
app.include_router(questions.router, prefix="/questions")
