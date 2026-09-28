# 📚 LangChain Document Q&A using RAG

A Generative AI application that allows users to upload a document and ask questions about its content.

The project uses **LangChain**, **Retrieval-Augmented Generation (RAG)**, **Sentence Transformers**, **ChromaDB**, and **Ollama** to retrieve relevant information from the document and generate context-aware answers using a locally running Large Language Model.

---

## 📌 Project Overview

Traditional Large Language Models may not know the information contained in a user's private or newly uploaded documents.

This project solves that problem using a **Retrieval-Augmented Generation (RAG)** pipeline.

The application:

1. Accepts a document from the user.
2. Extracts the document text.
3. Splits the text into smaller chunks.
4. Converts the chunks into vector embeddings.
5. Stores the embeddings in a vector database.
6. Searches for relevant chunks when a question is asked.
7. Sends the retrieved context to a local LLM.
8. Generates an answer based on the retrieved document content.

---

## 🎯 Objectives

- Build a practical Generative AI application using LangChain.
- Understand the Retrieval-Augmented Generation architecture.
- Process and retrieve information from documents.
- Generate semantic embeddings using Sentence Transformers.
- Store and search document embeddings using ChromaDB.
- Use a locally running LLM through Ollama.
- Build an interactive user interface using Streamlit.
- Create a complete end-to-end RAG application.

---

## 🧠 What is RAG?

**RAG (Retrieval-Augmented Generation)** is a technique that combines information retrieval with Large Language Models.

Instead of asking the LLM to answer a question only from its pretrained knowledge, the application first retrieves relevant information from the user's document.

The retrieved information is then provided to the LLM as context.

### RAG Process

```text
Document
   ↓
Text Extraction
   ↓
Text Splitting
   ↓
Text Chunks
   ↓
Embeddings
   ↓
ChromaDB
   ↓
User Question
   ↓
Similarity Search
   ↓
Relevant Document Chunks
   ↓
LLM
   ↓
Generated Answer
```

---

## 🔄 RAG Workflow

### Step 1: Document Upload

The user uploads a supported document through the Streamlit interface.

```text
User
 ↓
Upload Document
```

---

### Step 2: Document Loading

The application reads the uploaded document and extracts its text.

```text
Document
   ↓
Document Loader
   ↓
Extracted Text
```

---

### Step 3: Text Splitting

Large documents are divided into smaller chunks.

This makes it easier to search for relevant information.

```text
Large Document
      ↓
Text Splitter
      ↓
Chunk 1
Chunk 2
Chunk 3
...
Chunk N
```

---

### Step 4: Embedding Generation

Each document chunk is converted into a numerical vector using the Sentence Transformers model.

The project uses:

```text
all-MiniLM-L6-v2
```

These vectors represent the semantic meaning of the text.

```text
Text Chunk
    ↓
Sentence Transformer
    ↓
Vector Embedding
```

---

### Step 5: Vector Database

The generated embeddings are stored in **ChromaDB**.

ChromaDB allows the application to efficiently search for document chunks that are semantically similar to the user's question.

```text
Document Chunks
      ↓
Embeddings
      ↓
ChromaDB
```

---

### Step 6: User Question

The user enters a question related to the uploaded document.

Example:

```text
What are the main objectives mentioned in the document?
```

---

### Step 7: Similarity Search

The user's question is converted into an embedding.

ChromaDB compares the question embedding with the stored document embeddings and retrieves the most relevant chunks.

```text
User Question
      ↓
Question Embedding
      ↓
Similarity Search
      ↓
Relevant Chunks
```

---

### Step 8: Context + Question

The retrieved document chunks are combined with the user's question and passed to the LLM.

```text
Relevant Context
       +
User Question
       ↓
      LLM
```

---

### Step 9: Answer Generation

The LLM generates a response using the retrieved document context.

```text
Retrieved Context
       ↓
Ollama LLM
       ↓
Generated Answer
```

---

## 🏗️ Project Architecture

```text
                    ┌──────────────────┐
                    │  User Uploads    │
                    │    Document      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Document Loader   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Text Splitter   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Embeddings     │
                    │ all-MiniLM-L6-v2 │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    ChromaDB      │
                    │ Vector Database  │
                    └────────┬─────────┘
                             │
                             │
User Question ───────────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Similarity Search│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Relevant Context │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Ollama      │
                    │     Local LLM    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Generated Answer │
                    └──────────────────┘
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| LangChain | Framework for building LLM and RAG applications |
| RAG | Retrieval-Augmented Generation architecture |
| Sentence Transformers | Generates semantic text embeddings |
| all-MiniLM-L6-v2 | Embedding model |
| ChromaDB | Vector database for storing and retrieving embeddings |
| Ollama | Runs the LLM locally |
| Streamlit | Web application interface |

---

## 📁 Project Structure

```text
LangChain_Document_QA/
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
├── data/
│   └── sample_document.pdf
│
└── chroma_db/
    └── Vector database files
```

### File Description

| File / Folder | Description |
|---|---|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `data/` | Stores sample or input documents |
| `chroma_db/` | Stores the generated ChromaDB vector database |

---

## ⚙️ How the Application Works

The application follows this pipeline:

```text
Upload Document
      ↓
Extract Text
      ↓
Split Text into Chunks
      ↓
Generate Embeddings
      ↓
Store in ChromaDB
      ↓
Enter Question
      ↓
Generate Question Embedding
      ↓
Retrieve Relevant Chunks
      ↓
Send Context + Question to Ollama
      ↓
Generate Answer
      ↓
Display Answer in Streamlit
```

---

## 🧩 Key Components

### 1. LangChain

LangChain is used to connect different components of the RAG pipeline.

It helps manage:

- Document loading
- Text splitting
- Embeddings
- Vector stores
- Retrievers
- LLM interaction
- Prompt construction

---

### 2. Sentence Transformers

Sentence Transformers converts text into numerical vector representations.

The project uses:

```text
all-MiniLM-L6-v2
```

This allows the application to compare the semantic similarity between the user's question and document chunks.

---

### 3. ChromaDB

ChromaDB is used as the vector database.

It stores:

```text
Document Chunk
     +
Embedding
     +
Metadata
```

When the user asks a question, ChromaDB retrieves the most relevant document chunks.

---

### 4. Ollama

Ollama is used to run a Large Language Model locally.

The LLM receives:

```text
Retrieved Context
+
User Question
```

and generates the final answer.

Running the model locally helps keep document content within the local environment rather than sending it to a paid external LLM API.

---

### 5. Streamlit

Streamlit provides the user interface.

The application allows the user to:

- Upload a document
- Enter a question
- Submit the question
- View the generated answer

---

## 🖥️ Application Interface

The application contains a simple interface with:

```text
-----------------------------------------
       📚 Document Q&A using RAG
-----------------------------------------

Upload your document

[ Choose a file ]

Ask a question about the document

[ Enter your question here ]

[ Ask Question ]

-----------------------------------------

Answer:
Generated answer from the document
-----------------------------------------
```

---

## 📦 Installation

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

Navigate to the project directory:

```bash
cd LangChain_Document_QA
```

---

### Step 2: Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

---

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🦙 Ollama Setup

Install Ollama on your system and make sure the Ollama service is running.

After installation, verify that Ollama is available:

```bash
ollama --version
```

Download the LLM model used by the project.

For example:

```bash
ollama pull llama3.2
```

Verify the installed models:

```bash
ollama list
```

The exact model can be changed depending on the model available in your local Ollama installation.

---

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser.

If it does not open automatically, Streamlit will display a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## 📝 Example Usage

### Step 1

Upload a document.

Example:

```text
sample_document.pdf
```

### Step 2

Enter a question.

Example:

```text
What is the main topic of this document?
```

### Step 3

Click:

```text
Ask Question
```

### Step 4

The application retrieves relevant information from the document and generates an answer using the local LLM.

---

## 💡 Example

### User Question

```text
What are the main objectives mentioned in the document?
```

### RAG Process

```text
Question
   ↓
Question Embedding
   ↓
ChromaDB Similarity Search
   ↓
Relevant Document Chunks
   ↓
Ollama
   ↓
Answer
```

### Generated Answer

```text
The main objectives mentioned in the document are to
improve efficiency, automate processes, and provide
better decision-making support.
```

The actual answer depends on the uploaded document.

---

## 🔍 Why Use RAG?

A normal LLM application may generate an answer based on its pretrained knowledge.

RAG adds external knowledge from a specific document.

### Without RAG

```text
User Question
      ↓
     LLM
      ↓
General Answer
```

### With RAG

```text
User Question
      ↓
Retrieve Relevant Information
      ↓
Document Context
      ↓
     LLM
      ↓
Context-Aware Answer
```

This makes RAG useful for applications involving:

- Documents
- Reports
- Manuals
- Research papers
- Company documents
- Educational materials
- Knowledge bases

---

## 🔐 Advantages

- Uses document-specific information.
- Can work with private documents locally.
- Reduces dependence on the LLM's pretrained knowledge.
- Supports semantic document search.
- Uses a local LLM through Ollama.
- Avoids requiring a paid cloud LLM API for generation.
- Provides an interactive Streamlit interface.
- Demonstrates a complete Generative AI workflow.

---

## ⚠️ Limitations

- Answer quality depends on the quality of the document.
- Incorrect or incomplete document extraction can affect results.
- Retrieval quality depends on chunking and embedding quality.
- Local LLM performance depends on available system resources.
- Very large documents may require additional optimization.
- The application may not answer questions that are not supported by the uploaded document.

---

## 🚀 Future Improvements

Possible future improvements include:

- Support for multiple documents.
- Support for DOCX, TXT, and other document formats.
- Conversation history.
- Chat memory.
- Source document references.
- Displaying retrieved document chunks.
- Improved prompt engineering.
- Advanced retrieval strategies.
- Hybrid search.
- Reranking retrieved documents.
- Streaming LLM responses.
- Better document processing.
- Deployment to a cloud platform.

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented and practiced:

- Generative AI
- Large Language Models
- Retrieval-Augmented Generation
- LangChain
- Document processing
- Text chunking
- Semantic search
- Vector embeddings
- Sentence Transformers
- ChromaDB
- Vector databases
- Local LLMs
- Ollama
- Prompt construction
- Streamlit
- End-to-end AI application development

---

## 🎓 Project Type

```text
Generative AI
        +
Natural Language Processing
        +
Retrieval-Augmented Generation
        +
Large Language Models
        +
Vector Database
```

---

## 📌 Conclusion

This project demonstrates how a **Retrieval-Augmented Generation system** can be built using LangChain to answer questions from user-provided documents.

The system combines:

```text
LangChain
   +
Sentence Transformers
   +
ChromaDB
   +
Ollama
   +
Streamlit
```

to create an end-to-end document question-answering application.

The project provides practical experience with modern Generative AI concepts including **RAG, embeddings, vector databases, semantic search, and local Large Language Models**.

---

## 👩‍💻 Author

**Greeshma**

B.Tech – Artificial Intelligence and Data Science

---

## ⭐ Project Highlights

```text
📄 Document Processing
🧠 Semantic Embeddings
🔎 Similarity Search
🗄️ ChromaDB Vector Store
🔗 LangChain RAG Pipeline
🦙 Local LLM with Ollama
💬 Document Question Answering
🖥️ Streamlit Interface
```

---

## 📜 License

This project is created for educational and portfolio purposes.
