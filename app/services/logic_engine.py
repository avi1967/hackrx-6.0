import openai
from app.config import config

openai.api_key = config.OPENAI_API_KEY

def evaluate_logic(query: str, clauses: list):
    context = "\n\n".join([c['clause'] for c in clauses])
    prompt = (
        f"Given the query: {query}\n"
        f"And the following clauses:\n{context}\n"
        f"Return if the query is satisfied, confidence level, and rationale in JSON format."
    )

    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return completion.choices[0].message['content']

# app/services/logic_engine.py

def retrieve_relevant_documents(query):
    # Dummy logic (replace with embedding search + filtering)
    return ["Document A", "Document B", "Document C"]
