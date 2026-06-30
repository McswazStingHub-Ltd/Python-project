import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("Error: GEMINI_API_KEY not found.")
    exit()

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"

headers = {
    "X-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

print("=" * 50)
print("Gemini AI Assistant")
print("=" * 50)

while True:
    prompt = input("You: ")

    if prompt.lower() == "exit":
        print("Goodbye!")
        break

    data = {
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

    try:
        response = requests.post(
            url,
            headers=headers,
            json=data,
            timeout=30
        )

        print("Status:", response.status_code)

        if response.ok:
            print(response.json()["candidates"][0]["content"]["parts"][0]["text"])
        else:
            print(response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
