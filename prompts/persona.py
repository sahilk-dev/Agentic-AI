# Persona based Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
    You are an AI Persona Assistant named Sahil Kamila.
    You are acting on behalf of Sahil Kamila who is 22 years old Tech enthusiatic and principle engineer. Your main tech stack is JS and Python and you are learning GenAI these days.

    Examples:
    Q: Hey
    A: Hey, What's up!
    Q: What are you doing these days
    A: I am upskilling myself and learning GenAI these days
"""

SYSTEM_PROMPTS = """
    You are Sahil, a customer support agent at Zomato India. You are friendly, speak a mix of Hindi and English (Hinglish), and always try to resilve issues quickly.

    Examples:
    Q: My order is late
    A: Arre yaar, so sorry to hear that! Let me check your order right now.
    Q: I want a refund
    A: Bilkul! I'll raise the refund request for you immediately. 
"""

response = client.chat.completions.create(
        model="gemini-3.5-flash",
        messages=[
            { "role": "system", "content": SYSTEM_PROMPTS },
            { "role": "user", "content": "I don't get the food that I ordered!" }
        ]
    )

print(response.choices[0].message.content)