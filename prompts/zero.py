# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Zero Shot Prompting: Directly giving the instructions to the model
SYSTEM_PROMPT = "You should only and only answer the coding questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding, just say sorry."


response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, can you help me to translate the word happy in hindi" }
    ]
)

print(response.choices[0].message.content)