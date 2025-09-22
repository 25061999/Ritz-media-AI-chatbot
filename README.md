# Ritz-media-AI-chatbot
# Ritz-media-AI-chatbot

![GitHub Repo Size](https://img.shields.io/github/repo-size/25061999/Ritz-media-AI-chatbot)
![Python Version](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Overview
**Ritz-media-AI-chatbot** is an intelligent conversational AI chatbot built using **Python**, **LangChain**, and **OpenAI APIs**. It can answer user queries dynamically by accessing a knowledge base and performing context-aware responses. Ideal for AI-driven customer support, educational tools, or personal projects.

---

## Features
- Conversational AI using **LLM (Large Language Models)**  
- Knowledge base integration with **RAG (Retrieval-Augmented Generation)**  
- Dynamic question-answering and content retrieval  
- Local deployment via **VS Code**  
- Extensible and modular architecture for future enhancements  

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/25061999/Ritz-media-AI-chatbot.git
   cd Ritz-media-AI-chatbot
## Navigate to the project folder:

cd Ritz-media-AI-chatbot


## Create a virtual environment:

python -m venv venv


## Activate the environment:

# Windows
.\venv\Scripts\activate


## Install dependencies:

pip install -r requirements.txt

## Usage

Create a .env file in the root folder with your API keys:

OPENAI_API_KEY=your_openai_api_key


## Run the chatbot:

python app.py ||
uvicorn app:app --reload

## Project Structure
Ritz-media-AI-chatbot/
├─ app.py
├─ build_kb.py
├─ cli_chat.py
├─ index.html
├─ requirements.txt
├─ ritz_content.txt
├─ ritz_db/
├─ test.py
├─ test_chat.py
├─ .vscode/
└─ README.md

## Contributing

Feel free to fork the project, create branches, and submit pull requests.

## License

MIT License


