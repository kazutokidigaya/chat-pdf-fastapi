from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)  # Add this line to include file_path
    upload_date = Column(DateTime, default=datetime.utcnow)

    chunks = relationship("TextChunk", back_populates="document")

class TextChunk(Base):
    __tablename__ = "text_chunks"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    chunk_index = Column(Integer, nullable=False)
    chunk_text = Column(Text, nullable=False)

    document = relationship("Document", back_populates="chunks")
