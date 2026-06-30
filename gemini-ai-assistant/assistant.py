import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

headers = {
    "Content-Type": "application/json",
    "X-goog-api-key": API_KEY,
    "User-Agent": "curl/8.0"
}

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

print("=" * 50)
print("Gemini AI Assistant")
print("=" * 50)

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        break

    response = requests.post(
        url,
        headers=headers,
        json={
            "contents": [
                {
                    "parts": [
                        {
                            "text": prompt
                        }
                    ]
                }
            ]
        }
    )

    print("Status:", response.status_code)

    if response.status_code == 200:
        print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
    else:
        print(response.text)
