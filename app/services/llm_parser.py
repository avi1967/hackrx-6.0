import openai
from app.config import config

openai.api_key = config.OPENAI_API_KEY

def parse_query_with_llm(user_query: str) -> dict:
    system_prompt = "Extract the intent, entities, jurisdiction, and time range from this query. Return a JSON object."
    
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    )
    return completion.choices[0].message['content']

# app/services/llm_parser.py

def parse_query(query):
    # Dummy parser (replace with OpenAI/LLM logic)
    return {"parsed_intent": "retrieve", "entities": ["invoice", "March 2023"]}
