# decision.py
from fastapi import APIRouter
from app.services.logic_engine import evaluate_logic

router = APIRouter()

@router.post("/evaluate")
def evaluate_decision(query: str, clauses: list):
    return evaluate_logic(query, clauses)
