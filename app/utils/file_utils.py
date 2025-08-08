import fitz  # PyMuPDF
import docx

def extract_pdf_text(content: bytes) -> str:
    doc = fitz.open(stream=content, filetype="pdf")
    return "\\n".join([page.get_text() for page in doc])

def extract_docx_text(content: bytes) -> str:
    from io import BytesIO
    doc = docx.Document(BytesIO(content))
    return "\\n".join([p.text for p in doc.paragraphs])

def extract_email_text(content: bytes) -> str:
    return content.decode(errors='ignore')

# app/utils/file_utils.py

async def process_file(file):
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    return text
