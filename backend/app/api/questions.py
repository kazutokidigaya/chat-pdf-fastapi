from groq import Groq
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models import database
from ..models.document import TextChunk
import os

router = APIRouter()

class QuestionRequest(BaseModel):
    document_id: int
    question: str

@router.post("/ask-question/")
async def ask_question(request: QuestionRequest, db: Session = Depends(database.get_db)):
    document_id = request.document_id
    question = request.question

    # Retrieve text chunks from the database
    chunks = db.query(TextChunk).filter(TextChunk.document_id == document_id).all()
    MAX_CONTEXT_LENGTH = 2000  # Adjust as necessary to fit within the model's context length limit.
    context = " ".join([chunk.chunk_text for chunk in chunks])
    if len(context) > MAX_CONTEXT_LENGTH:
        context = context[:MAX_CONTEXT_LENGTH]  # Trim the context to the maximum allowed length.

    # Groq API integration
    client = Groq()
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\nQuestion: {question}"},
        ],
        model="llama3-8b-8192",
        temperature=0.4,
        max_tokens=1025,
        stream=False,
    )
    answer = chat_completion.choices[0].message.content
    return {"answer": answer}
