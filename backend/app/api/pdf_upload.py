from fastapi import APIRouter, UploadFile, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models import database, document as models
from ..config import UPLOAD_FOLDER
from ..services.pdf_service import extract_text_and_chunk
import os
import shutil

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile, db: Session = Depends(database.get_db)):
    # Verify if the uploaded file is a PDF
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    # Create the upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Save the uploaded PDF to the local filesystem
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Save metadata in the database
    new_doc = models.Document(filename=file.filename, file_path=file_path)
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)

    # Extract and chunk text
    chunks = extract_text_and_chunk(file_path)

    # Store text chunks in the database
    for index, chunk in enumerate(chunks):
        db.add(models.TextChunk(document_id=new_doc.id, chunk_index=index, chunk_text=chunk))
    db.commit()

    return {"message": "PDF uploaded and processed successfully.", "document_id": new_doc.id}
