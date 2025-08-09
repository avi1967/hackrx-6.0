# app/services/embedding_engine.py

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

# Model for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS index (cosine similarity)
dimension = 384  # matches embedding size of the model
index = faiss.IndexFlatIP(dimension)
documents = []  # stores original text chunks

def _embed(text: str):
    return model.encode([text], convert_to_numpy=True, normalize_embeddings=True)

def add_document(text: str, chunk_size: int = 500):
    """
    Break text into chunks, embed them, and store in FAISS.
    """
    global documents
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    embeddings = model.encode(chunks, convert_to_numpy=True, normalize_embeddings=True)
    index.add(embeddings)
    documents.extend(chunks)

def search(query: str, top_k: int = 3):
    """
    Search the FAISS index for the most relevant chunks.
    """
    if index.ntotal == 0:
        return []

    query_vec = _embed(query)
    scores, ids = index.search(query_vec, top_k)
    results = []
    for idx, score in zip(ids[0], scores[0]):
        if idx != -1:
            results.append({"text": documents[idx], "score": float(score)})
    return results
