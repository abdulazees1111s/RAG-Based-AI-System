# RAG AI System

A simple Retrieval-Augmented Generation (RAG) AI system using LangChain, OpenAI, and FAISS.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key in `.env`:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Usage

1. Ingest documents:
   ```
   python ingest.py
   ```
   This will process the text files in `data/` and create a vectorstore in `vectorstore/`.

2. Run the app:
   ```
   python app.py
   ```
   Enter queries to get answers based on the ingested documents.

3. Or query directly:
   ```
   python query.py
   ```

## Files

- `app.py`: Main application with interactive CLI.
- `ingest.py`: Script to ingest documents and build vectorstore.
- `query.py`: Script to query the system.
- `data/`: Directory for input documents.
- `vectorstore/`: Directory for the FAISS vectorstore.