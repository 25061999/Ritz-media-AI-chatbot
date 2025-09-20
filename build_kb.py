import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DB_PATH = "ritz_db"

def build_kb():
    print("🌐 Scraping https://ritzmediaworld.com/ ...")
    loader = WebBaseLoader("https://ritzmediaworld.com/")
    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)
    print(f"📄 Extracted {len(splits)} chunks.")

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = FAISS.from_documents(splits, embeddings)
    db.save_local(DB_PATH)

    print(f"✅ Vector DB saved to {DB_PATH}")

if __name__ == "__main__":
    build_kb()
