# app/main.py

from fastapi import FastAPI
from app.routes import document, query, retrieval

app = FastAPI(
    title="LLM Retrieval System",
    description="Query processing and retrieval over documents using LLMs.",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM Retrieval System!"}

# Register your routers
app.include_router(document.router, prefix="/documents", tags=["Documents"])
app.include_router(query.router, prefix="/query", tags=["Query"])
app.include_router(retrieval.router, prefix="/retrieval", tags=["Retrieval"])
