from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load document
loader = TextLoader("data/sample.txt")
documents = loader.load()

# Split into chunks
splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Create embeddings
embeddings = HuggingFaceEmbeddings()

# Store in FAISS
db = FAISS.from_documents(docs, embeddings)
db.save_local("vectorstore")

print("✅ Vector DB created successfully!")