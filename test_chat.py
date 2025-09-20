import requests

def ask_bot(question):
    url = "http://127.0.0.1:8000/chat"
    response = requests.post(url, json={"question": question})
    return response.json()["answer"]

if __name__ == "__main__":
    print("🔹 Testing Ritz Chatbot")
    while True:
        q = input("You: ")
        if q.lower() in ["exit", "quit"]:
            break
        try:
            answer = ask_bot(q)
            print("Bot:", answer)
        except Exception as e:
            print("Error:", e)