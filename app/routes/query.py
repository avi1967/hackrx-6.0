# app/routes/query.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.embedding_engine import EmbeddingEngine
from app.services.llm_parser import answer_with_context

router = APIRouter()

embedding_engine = EmbeddingEngine()

class QueryPayload(BaseModel):
    question: str

@router.post("/query")
async def query_document(payload: QueryPayload):
    # Retrieve similar clauses from FAISS
    results = embedding_engine.search(payload.question, top_k=3)
    
    # Use LLM to produce answer
    answer, reasoning = answer_with_context(payload.question, results)

    return {
        "question": payload.question,
        "answer": answer,
        "evidence": results,
        "reasoning": reasoning
    }
