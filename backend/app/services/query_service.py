from sqlalchemy.orm import Session
from ..models import document as models
from ..config import GEMINI_API_KEY
import requests

def get_relevant_chunks(db: Session, document_id: int, question: str):
    # Simple retrieval of all chunks (In practice, use LangChain/LLamaIndex for relevance)
    chunks = db.query(models.TextChunk).filter_by(document_id=document_id).all()
    return [chunk.chunk_text for chunk in chunks]

def generate_answer(db: Session, document_id: int, question: str):
    # Get relevant chunks from the database
    relevant_chunks = get_relevant_chunks(db, document_id, question)
    context = " ".join(relevant_chunks[:3])  # Just using the first 3 chunks for simplicity

    # Call the Gemini API with the question and context
    response = requests.post(
        "https://api.gemini.com/generate",
        json={"prompt": f"Context: {context}\nQuestion: {question}"},
        headers={"Authorization": f"Bearer {GEMINI_API_KEY}"}
    )
    return response.json().get("text")
