from app.utils.file_utils import extract_pdf_text, extract_docx_text, extract_email_text

def parse_document(filename: str, content: bytes) -> str:
    if filename.endswith(".pdf"):
        return extract_pdf_text(content)
    elif filename.endswith(".docx"):
        return extract_docx_text(content)
    elif filename.endswith(".eml") or filename.endswith(".msg"):
        return extract_email_text(content)
    return "Unsupported file type."
