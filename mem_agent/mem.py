from dotenv import load_dotenv
from mem0 import Memory
import os
import json

from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "models/gemini-embedding-001",
            "embedding_dims": 768
        }
    },
    "llm": {
        "provider": "gemini",
        "config": {
            "api_key": GEMINI_API_KEY,
            "model": "gemini-2.5-flash"
        }
    },
    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "neo4j+s://8e211fa8.databases.neo4j.io",
            "username": "8e211fa8",
            "password": "tNjuuc0f04P4a_-McXSPLxjIdjXEU3ZqgoQPjgJ5ahM"
        }
    },
    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": "localhost",
            "port": 6333,
            "embedding_model_dims": 768
        }
    }
}

mem_client = Memory.from_config(config)


while True:

    user_query = input("> ")

    search_memory = mem_client.search(
        query=user_query,
        filters={"user_id": "sahilkamila"}
    )

    memories = [
        f"ID: {mem.get('id')}\nMemory: {mem.get('memory')}" for mem in search_memory.get("results")
    ]

    print("Found Memories", memories)

    SYSTEM_PROMPT = f"""
    Here is the context about the user:
    {json.dumps(memories)}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{SYSTEM_PROMPT}\n\nUser: {user_query}"
    )

    ai_response = response.text

    print("AI:", ai_response)

    mem_client.add(
        user_id="sahilkamila",
        messages=[
            { "role": "user", "content": user_query },
            { "role": "assistant", "content": ai_response }
        ]
    )

    print("Memory has been saved...")