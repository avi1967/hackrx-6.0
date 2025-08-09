# app/routes/document.py

from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import process_file
from app.services.embedding_engine import EmbeddingEngine

router = APIRouter()

# Initialize embedding engine (FAISS)
embedding_engine = EmbeddingEngine()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Extract raw text from uploaded file
    content = await process_file(file)
    
    # Store in FAISS for retrieval
    embedding_engine.add_document(file.filename, content)

    return {
        "filename": file.filename,
        "content_snippet": content[:200],
        "message": "Document added to retrieval index."
    }
