# app/routes/query.py

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_parser import parse_query

router = APIRouter()

class QueryInput(BaseModel):
    query: str

@router.post("/")
def parse_user_query(data: QueryInput):
    structured_query = parse_query(data.query)
    return {"structured_query": structured_query}
