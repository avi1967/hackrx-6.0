# app/routes/retrieval.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.logic_engine import retrieve_relevant_documents

router = APIRouter()

class RetrievalInput(BaseModel):
    query: str

@router.post("/")
def retrieve_docs(data: RetrievalInput):
    results = retrieve_relevant_documents(data.query)
    return {"results": results}
