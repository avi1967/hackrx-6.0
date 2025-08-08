from app.services.embedding_engine import search_similar

def get_top_clauses(query: str) -> list:
    results = search_similar(query)
    return [{"clause": r, "score": "approx"} for r in results]
