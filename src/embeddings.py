from sentence_transformers import SentenceTransformer
from text_splitter import chunks


# Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create embeddings for the chunks
embeddings = model.encode(chunks)


print("Embeddings created successfully!")
print()
print("Number of chunks:", len(chunks))
print("Embedding shape:", embeddings.shape)
print()
print("First chunk embedding:")
print(embeddings[0])