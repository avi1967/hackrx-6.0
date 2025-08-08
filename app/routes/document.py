# app/routes/document.py

from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from app.utils.file_utils import process_file, download_file, extract_text_from_pdf

router = APIRouter()

# Model for URL-based document upload
class UploadPayload(BaseModel):
    url: str

# Upload file via form (PDF/DOCX/email)
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await process_file(file)
    return {"filename": file.filename, "content_snippet": content[:200]}

# Upload document via remote URL
@router.post("/upload-document")
async def upload_document(payload: UploadPayload):
    file_path = download_file(payload.url)
    text = extract_text_from_pdf(file_path)
    # You can later pass this `text` to the embedding engine
    return {
        "filename": file_path.name,
        "extracted_text": text[:500]  # Preview only
    }
