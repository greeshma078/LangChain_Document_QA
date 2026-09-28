import chromadb

from sentence_transformers import SentenceTransformer


# Load the embedding model
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# Connect to the existing ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db"
)


# Get the existing collection
collection = client.get_collection(
    name="company_documents"
)


# User question
question = "Where is ABC Technologies headquartered?"


# Convert the question into an embedding
question_embedding = embedding_model.encode(
    [question]
).tolist()


# Search for the most relevant chunk
results = collection.query(
    query_embeddings=question_embedding,
    n_results=2
)


# Display the retrieved chunks
print("Question:")
print(question)

print("\n" + "=" * 60)

print("\nRetrieved Documents:")

for i, document in enumerate(results["documents"][0]):
    print(f"\nDocument {i + 1}:")
    print(document)