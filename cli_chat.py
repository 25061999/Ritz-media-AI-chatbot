import requests

API_URL = "http://127.0.0.1:8000/chat"

def chat(query: str):
    payload = {"query": query}  # Must match your Pydantic model
    try:
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            data = response.json()
            print(f"\n🤖 Answer:\n{data['answer']}")
            print("\n📚 Sources:")
            for src in data['sources']:
                print(f"- {src}")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except Exception as e:
        print("❌ Request failed:", str(e))

def main():
    print("🟢 Ritz Media AI Chatbot CLI")
    print("Type 'exit' to quit.\n")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        chat(query)

if __name__ == "__main__":
    main()
