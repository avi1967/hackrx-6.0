import requests
import fitz  # PyMuPDF
from pathlib import Path
from tempfile import NamedTemporaryFile
from fastapi import UploadFile

async def process_file(file: UploadFile) -> str:
    content = await file.read()
    return content.decode("utf-8", errors="ignore")

def download_file(url: str) -> Path:
    response = requests.get(url)
    temp_file = NamedTemporaryFile(delete=False, suffix=".pdf")
    temp_file.write(response.content)
    temp_file.close()
    return Path(temp_file.name)

def extract_text_from_pdf(file_path: Path) -> str:
    doc = fitz.open(str(file_path))
    text = ""
    for page in doc:
        text += page.get_text()
    return text

