import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Correct imports (NEW LangChain)
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load API details
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL")

# Load vector DB
embeddings = HuggingFaceEmbeddings()
db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)


def ask_question(question):
    # Retrieve relevant docs
    docs = db.similarity_search(question, k=3)

    # Build context
    context = "\n\n".join([doc.page_content for doc in docs])

    # Prompt
    prompt = f"""
You are an AI assistant. Answer ONLY using the context below.

Context:
{context}

Question:
{question}

If answer not found, say "Not found in provided context".
Also include brief source references.
"""

    # OpenRouter API call
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    return result["choices"][0]["message"]["content"]