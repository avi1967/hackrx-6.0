import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    VECTOR_DB = os.getenv("VECTOR_DB", "faiss")
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_ENV")
    MODEL_NAME = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

config = Config()
