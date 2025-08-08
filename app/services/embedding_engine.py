from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
stored_chunks = []

def embed_and_store(chunks):
    embeddings = model.encode(chunks)
    index.add(np.array(embeddings))
    stored_chunks.extend(chunks)

def search_similar(query, top_k=3):
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    return [stored_chunks[i] for i in indices[0]]
