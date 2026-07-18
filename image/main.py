from dotenv import load_dotenv
from google import genai
from google.genai import types
import requests
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

image_url = "https://images.pexels.com/photos/17767237/pexels-photo-17767237.jpeg"
image_bytes = requests.get(image_url).content

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
        "Generate a caption for this image in about 50 words"
    ]
)

print("Response:", response.text)