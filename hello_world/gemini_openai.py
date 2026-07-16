from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {"role": "system", "content": "You are an expert in Maths and only and only answer maths related questions"},
        {"role": "user", "content": "Hey, can you help me to solve the a + b whole cube"}
    ]
)

print(response.choices[0].message.content)