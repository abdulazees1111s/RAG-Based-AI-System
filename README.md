# 🚀 RAG-Based AI Knowledge Assistant

A **Retrieval-Augmented Generation (RAG)** system built with FastAPI that answers questions using **your own data** instead of relying on generic LLM knowledge.

---

## 🧠 Overview

This project implements a **document-based question answering system** where:

* Documents are ingested and converted into embeddings
* Stored in a vector database (FAISS)
* Retrieved based on user query
* Passed to an LLM for **context-aware, grounded answers**

👉 The system avoids hallucination by answering **only from provided data**

---

## 🔥 Features

* ✅ Retrieval-Augmented Generation (RAG)
* ✅ Semantic search using embeddings
* ✅ FAISS vector database for fast retrieval
* ✅ FastAPI backend with REST endpoints
* ✅ Environment-based configuration (.env)
* ✅ Support for multiple LLM providers (OpenRouter / others)
* ✅ No hallucination (strict context-based answers)

---

## ⚙️ Tech Stack

| Component  | Technology            |
| ---------- | --------------------- |
| Backend    | FastAPI               |
| Vector DB  | FAISS                 |
| Embeddings | sentence-transformers |
| LLM        | OpenRouter API        |
| Language   | Python                |

---

## 📁 Project Structure

```
rag-ai-system/
│
├── data/              # Input documents
│   └── sample.txt
│
├── vectorstore/       # FAISS index (ignored in git)
│
├── app.py             # FastAPI server
├── ingest.py          # Data ingestion script
├── query.py           # RAG pipeline
├── llm.py             # LLM integration
│
├── .env               # API keys (not committed)
├── .env.example       # Sample config
├── requirements.txt
├── README.md
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/rag-ai-system.git
cd rag-ai-system
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Configure environment variables

Create a `.env` file:

```
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=meta-llama/llama-3-8b-instruct
```

---

### 4️⃣ Add your data

Edit:

```
data/sample.txt
```

Example:

```
Stack:
A stack is a LIFO (Last In First Out) data structure.

Queue:
A queue is a FIFO (First In First Out) data structure.
```

---

### 5️⃣ Run ingestion

```
python ingest.py
```

👉 This creates the vector database

---

### 6️⃣ Start the API

```
python -m uvicorn app:app --reload
```

---

### 7️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 🧪 Example Usage

### Query:

```
GET /ask?q=What is a stack?
```

### Response:

```json
{
  "answer": "A stack is a LIFO (Last In First Out) data structure."
}
```

---

## ⚠️ Important Behavior

* The system answers **only from provided data**
* If answer is not found:

```json
{
  "answer": "Not found in provided context."
}
```

👉 This ensures **no hallucination**

---

## 🧠 How It Works

1. Documents are loaded and split into chunks
2. Each chunk is converted into embeddings
3. Stored in FAISS vector database
4. User query is embedded and matched
5. Relevant chunks are retrieved
6. LLM generates answer using retrieved context

---

## 🔄 Future Enhancements

* AI Interview System (MCQ + coding questions)
* Answer evaluation and scoring
* Multi-document support
* PDF and file upload support
* Frontend UI (chat interface)
* Deployment on cloud (Render/Vercel)

---

## 💡 Key Learning Outcomes

* RAG architecture implementation
* Vector databases and semantic search
* LLM integration with external APIs
* Backend API development using FastAPI
* Secure configuration using environment variables

---

## 📌 Author

**Abdul Azees**
Full-stack Developer | AI Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
