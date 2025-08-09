# app/services/llm_parser.py
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_answer(question, context_chunks):
    context = "\n".join(context_chunks)
    prompt = f"Answer the following question based on the provided document:\n\n{context}\n\nQuestion: {question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal/insurance assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    return response.choices[0].message["content"].strip()
