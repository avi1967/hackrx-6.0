# app/main.py

from fastapi import FastAPI
from app.routes import document, query

app = FastAPI(
    title="LLM Query Retrieval System",
    version="1.0",
    description="Upload documents, ask questions, get answers with evidence."
)

# Mount routes
app.include_router(document.router, tags=["Document"])
app.include_router(query.router, tags=["Query"])

@app.get("/")
async def root():
    return {
        "message": "LLM Query Retrieval System is running. Use /upload to add docs and /query to ask questions."
    }

