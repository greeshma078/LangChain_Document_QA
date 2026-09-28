# 📚 LangChain Document Q&A using RAG

A Generative AI application that allows users to ask questions about a document and receive answers using **Retrieval-Augmented Generation (RAG)**.

This project combines **LangChain, ChromaDB, Sentence Transformers, Ollama, Llama 3.2, and Streamlit** to build a local document question-answering system.

The application retrieves relevant information from the document before generating an answer, allowing the LLM to answer questions based on the provided knowledge source.

---

## 🚀 Project Overview

Large Language Models can generate useful answers, but they may not know information contained in private or custom documents.

This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

The document goes through the following process:

1. Document Loading
2. Text Splitting
3. Text Embedding
4. Vector Storage
5. Semantic Retrieval
6. Context Creation
7. Prompt Construction
8. LLM Generation
9. Final Answer

### RAG Workflow

```text
Document
    ↓
Document Loading
    ↓
Text Splitting
    ↓
Embeddings
    ↓
ChromaDB Vector Store
    ↓
User Question
    ↓
Question Embedding
    ↓
Similarity Search
    ↓
Relevant Document Chunks
    ↓
LangChain Prompt
    ↓
Llama 3.2
    ↓
Generated Answer
🧠 Technologies Used
Technology	Purpose
Python	Programming language
LangChain	Framework for building LLM applications
RAG	Retrieval-Augmented Generation architecture
Sentence Transformers	Text embedding generation
all-MiniLM-L6-v2	Embedding model
ChromaDB	Vector database
Ollama	Local LLM runtime
Llama 3.2	Local language model
Streamlit	Web application interface
PyPDF	PDF document processing
📂 Project Structure
LangChain_Document_QA/
│
├── data/
│   └── company_info.txt
│
├── src/
│   ├── __init__.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm_test.py
│   └── rag_pipeline.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
📄 Knowledge Source

The project currently uses a sample company document:

data/company_info.txt

The document contains information about ABC Technologies, including:

Company background
Services
Headquarters
Number of employees
Products
Training programs
Working hours

Example:

ABC Technologies is a software company founded in 2015.

The company headquarters is located in Bengaluru, India.

The company provides services in Artificial Intelligence,
Data Science, Cloud Computing, and Software Development.
🔄 RAG Pipeline
1. Document Loading

The document is loaded from the data directory.

File:

src/document_loader.py

The document text is read and passed to the next stage of the pipeline.

2. Text Splitting

Large documents are divided into smaller chunks using LangChain's:

RecursiveCharacterTextSplitter

Configuration:

chunk_size=300
chunk_overlap=50

Text splitting allows the retrieval system to work with smaller and more meaningful sections of the document.

3. Text Embeddings

Each document chunk is converted into a numerical vector using:

all-MiniLM-L6-v2

The embedding model generates:

384-dimensional embeddings

These embeddings represent the semantic meaning of the text.

4. Vector Database

The generated embeddings and document chunks are stored in:

ChromaDB

ChromaDB allows the application to efficiently perform semantic similarity searches.

The local vector database is stored in:

chroma_db/

The chroma_db/ directory is excluded from GitHub using .gitignore.

5. Semantic Retrieval

When the user asks a question, the question is converted into an embedding using the same embedding model.

The application searches ChromaDB for the most relevant document chunks.

For example:

Question:
Where is ABC Technologies headquartered?

The retrieval system finds the relevant information:

The company headquarters is located in Bengaluru, India.
6. Prompt Construction

The retrieved document chunks are inserted into a prompt.

The prompt instructs the LLM to answer the user's question using only the retrieved context.

If the required information is not available in the document, the system is instructed to respond:

I don't know based on the provided document.

This helps reduce unsupported answers from the LLM.

7. Local LLM

The project uses:

Llama 3.2

as the language model.

Llama 3.2 runs locally using:

Ollama

LangChain communicates with Ollama through:

ChatOllama

No paid cloud LLM API is required for this project.

💻 Streamlit Application

The project includes a Streamlit web interface where users can enter questions about the document.

Run the application using:

streamlit run app.py

The application provides:

Question input
RAG-based answer generation
Loading indicator
Retrieved document context
Interactive question answering
🧪 Example Questions
Question 1
Where is ABC Technologies headquartered?
Answer
ABC Technologies is headquartered in Bengaluru, India.
Question 2
What products does ABC Technologies offer?
Answer

The company offers:

AI Analytics Platform
Cloud Management System
Customer Support Automation Platform
Question 3
What are the working hours of ABC Technologies?
Answer
The working hours are from 9:00 AM to 6:00 PM, Monday to Friday.
Question 4
What programming languages are included in the training programs?
Answer

The training programs include:

Python
SQL
Data Science
Artificial Intelligence
🛠️ Installation
1. Clone the Repository
git clone https://github.com/greeshma078/LangChain_Document_QA.git

Move into the project directory:

cd LangChain_Document_QA
2. Install Python Dependencies

Install the required packages:

pip install -r requirements.txt
🦙 Ollama Setup

This project uses Ollama to run the Llama 3.2 model locally.

Install Ollama from:

https://ollama.com/

After installing Ollama, download the Llama 3.2 model:

ollama pull llama3.2

Verify that the model is installed:

ollama list

You should see:

llama3.2:latest
▶️ Running the Project
Test the LLM

Run:

python src/llm_test.py

This verifies the connection between:

Python
   ↓
LangChain
   ↓
ChatOllama
   ↓
Ollama
   ↓
Llama 3.2
Test the RAG Pipeline

Run:

python src/rag_pipeline.py

This tests the complete RAG workflow:

Question
   ↓
Question Embedding
   ↓
ChromaDB Retrieval
   ↓
Relevant Context
   ↓
LangChain Prompt
   ↓
Llama 3.2
   ↓
Answer
Run the Streamlit Application

Run:

streamlit run app.py

The Streamlit application will open in your browser.

🧩 Project Components
document_loader.py

Loads the document from the data directory.

text_splitter.py

Splits the document into smaller chunks using LangChain's RecursiveCharacterTextSplitter.

embeddings.py

Creates numerical embeddings for the document chunks using Sentence Transformers.

vector_store.py

Creates and stores document embeddings in ChromaDB.

retriever.py

Performs semantic similarity search and retrieves the most relevant document chunks for a user question.

llm_test.py

Tests the local Llama 3.2 model through LangChain and Ollama.

rag_pipeline.py

Combines:

Document retrieval
Context creation
LangChain prompt construction
Llama 3.2 response generation

to create the complete RAG pipeline.

app.py

Provides the Streamlit user interface for interacting with the RAG application.

🔐 Local Processing

One of the key features of this project is local LLM processing.

The application uses:

Ollama + Llama 3.2

instead of requiring a paid external LLM API.

The document retrieval and LLM generation can therefore be performed locally on the user's computer.

🎯 Learning Objectives

This project demonstrates practical knowledge of:

Generative AI
Retrieval-Augmented Generation
LangChain
Large Language Models
Prompt Engineering
Text Embeddings
Semantic Search
Vector Databases
ChromaDB
Sentence Transformers
Ollama
Llama 3.2
Streamlit
Document Question Answering
Local LLM Applications
🔮 Future Improvements

Possible improvements for future versions include:

PDF document support
Multiple document support
File upload functionality
Chat history
Conversation memory
Source citations
Metadata filtering
Improved chunking strategies
Multiple embedding models
Support for additional local LLMs
Document management
Cloud deployment
👩‍💻 Author

Greeshma Reddy

B.Tech – Artificial Intelligence & Data Science

GitHub:

https://github.com/greeshma078

⭐ Project Highlights
✔ Generative AI
✔ LangChain
✔ Retrieval-Augmented Generation (RAG)
✔ ChromaDB
✔ Sentence Transformers
✔ Semantic Search
✔ Ollama
✔ Llama 3.2
✔ Streamlit
✔ Local LLM
✔ Document Question Answering
✔ Prompt Engineering
📌 Summary

This project demonstrates an end-to-end Generative AI and RAG workflow.

A document is loaded and divided into chunks, converted into embeddings, and stored in ChromaDB. When a user asks a question, the system retrieves the most relevant document chunks and provides them as context to Llama 3.2 through LangChain.

The final answer is generated using the retrieved information, creating a local Document Question Answering system powered by LangChain, RAG, ChromaDB, Ollama, Llama 3.2, and Streamlit.
