from fastapi import APIRouter

router = APIRouter()

@router.post("/webhook/receive")
def receive_webhook(payload: dict):
    query = payload.get("query")
    doc_id = payload.get("document_id")
    # process query as usual...
    return {"status": "received", "query": query}
