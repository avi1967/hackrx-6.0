# app/routes/document.py

from fastapi import APIRouter, UploadFile, File
from app.utils.file_utils import process_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await process_file(file)
    return {"filename": file.filename, "content_snippet": content[:200]}
