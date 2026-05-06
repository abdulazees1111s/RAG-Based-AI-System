from fastapi import FastAPI
from query import ask_question

app = FastAPI()

@app.get("/")
def home():
    return {"message": "RAG AI System Running"}

@app.get("/ask")
def ask(q: str):
    answer = ask_question(q)
    return {"answer": answer}