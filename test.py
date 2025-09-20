import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/chat"

# The question you want to ask Gemini
payload = {
    "question": "Explain how AI works in a few words"
}

try:
    response = requests.post(API_URL, json=payload)
    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    response.raise_for_status()
    data = response.json()
    print("\nAnswer from FastAPI:", data.get("answer", "No answer field"))
except Exception as e:
    print("Request failed:", str(e))
