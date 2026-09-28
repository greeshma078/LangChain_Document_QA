import chromadb

from text_splitter import chunks
from sentence_transformers import SentenceTransformer


# Load the embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Create embeddings for all chunks
embeddings = embedding_model.encode(chunks).tolist()


# Create a ChromaDB client
client = chromadb.PersistentClient(
    path="chroma_db"
)


# Create or get the collection
collection = client.get_or_create_collection(
    name="company_documents"
)


# Add the chunks and embeddings
collection.add(
    ids=[f"chunk_{i}" for i in range(len(chunks))],
    documents=chunks,
    embeddings=embeddings
)


print("Vector database created successfully!")
print()
print("Number of documents stored:", collection.count())