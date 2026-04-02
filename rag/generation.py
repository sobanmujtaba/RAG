import requests
import json
from rag.config import *

def generate(context, query):
    prompt = f"""
You are a precise and factual assistant.

Use ONLY the provided context.
If not found, say so.

Context:
{context}

Question:
{query}

Answer:
"""

    response = requests.post(
        OLLAMA_URL,
        json={"model": MODEL, "prompt": prompt, "stream": True},
        stream=True
    )

    for line in response.iter_lines():
        if line:
            try:
                data = json.loads(line.decode("utf-8"))
                print(data.get("response", ""), end="", flush=True)
            except:
                continue
    print()