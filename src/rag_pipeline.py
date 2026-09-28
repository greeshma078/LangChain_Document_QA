import chromadb

from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate


# --------------------------------------------------
# 1. Load the embedding model
# --------------------------------------------------

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# --------------------------------------------------
# 2. Connect to ChromaDB
# --------------------------------------------------

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="company_documents"
)


# --------------------------------------------------
# 3. Create the Llama 3.2 model
# --------------------------------------------------

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# --------------------------------------------------
# 4. Create the prompt template
# --------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    """
You are a helpful document question-answering assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not present in the context, say:
"I don't know based on the provided document."

Context:
{context}

Question:
{question}

Answer:
"""
)


# --------------------------------------------------
# 5. Retrieve relevant documents
# --------------------------------------------------

def retrieve_documents(question):

    question_embedding = embedding_model.encode(
        [question]
    ).tolist()

    results = collection.query(
        query_embeddings=question_embedding,
        n_results=2
    )

    documents = results["documents"][0]

    return documents


# --------------------------------------------------
# 6. Generate the RAG answer
# --------------------------------------------------

def ask_question(question):

    documents = retrieve_documents(question)

    context = "\n\n".join(documents)

    formatted_prompt = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(
        formatted_prompt
    )

    return response.content, documents


# --------------------------------------------------
# 7. Test the RAG pipeline
# --------------------------------------------------

question = "What are the working hours of ABC Technologies?"

answer, documents = ask_question(question)


print("Question:")
print(question)

print("\n" + "=" * 60)

print("\nRetrieved Context:")

for i, document in enumerate(documents):
    print(f"\nDocument {i + 1}:")
    print(document)

print("\n" + "=" * 60)

print("\nRAG Answer:")
print(answer)