# Few Shot Prompting
# Zero Shot Prompting
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key = os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Prompting: Directly giving the instructions to the model and few examples to the model
SYSTEM_PROMPT = """You should only and only answer the coding questions. Do not answer anything else. Your name is Alexa. If user asks something other than coding, just say sorry.

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
    "code": "string" or null,
    "isCodingQuestion": boolean 
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{ "code": null, "isCodingQuestion": false }}

Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
        return a + b", "isCodingQuestion": true }}
"""


response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Can you explain the a + b whole square" }
    ]
)

print(response.choices[0].message.content)