import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# --------------------
# FastAPI setup
# --------------------
app = FastAPI(title="Ritz Media AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change to ["http://localhost:3000"] if frontend is fixed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------
# Pydantic model
# --------------------
class ChatQuery(BaseModel):
    question: str

# --------------------
# Google Gemini setup
# --------------------
API_KEY = os.getenv("GOOGLE_API_KEY", "AIzaSyD0vfTtd1dF54UySTFkzwQTD_KTKICPaek")
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

def call_gemini(question: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": question}
                ]
            }
        ]
    }
    try:
        response = requests.post(GEMINI_URL, headers=headers, json=payload)
        print("DEBUG STATUS:", response.status_code)
        print("DEBUG RESPONSE:", response.text)  # 👈 will show raw API response
        response.raise_for_status()
        data = response.json()

        return (
            data.get("candidates", [{}])[0]
            .get("content", {})
            .get("parts", [{}])[0]
            .get("text", "No response from Gemini")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")

# --------------------
# Chat endpoint
# --------------------
@app.post("/chat")
async def chat(query: ChatQuery):
    answer = call_gemini(query.question)
    return {"answer": answer}

# --------------------
# Health check endpoint
# --------------------
@app.get("/health")
async def health():
    return {"status": "ok"}
