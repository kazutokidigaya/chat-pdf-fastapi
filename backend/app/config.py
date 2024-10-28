import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration
DATABASE_URL = os.getenv("DATABASE_URL")

# File storage configuration
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "./uploads")

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
