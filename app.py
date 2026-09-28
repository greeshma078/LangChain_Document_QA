import streamlit as st

from src.rag_pipeline import ask_question


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="LangChain Document Q&A",
    page_icon="📚",
    layout="centered"
)


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📚 LangChain Document Q&A")

st.write(
    "Ask questions about the company document "
    "using LangChain, RAG, ChromaDB, and Llama 3.2."
)


# --------------------------------------------------
# Question input
# --------------------------------------------------

question = st.text_input(
    "Enter your question:",
    placeholder="Example: Where is ABC Technologies headquartered?"
)


# --------------------------------------------------
# Ask question
# --------------------------------------------------

if st.button("Ask Question"):

    if question.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching the document and generating answer..."):

            answer, documents = ask_question(question)


        # --------------------------------------------------
        # Display answer
        # --------------------------------------------------

        st.subheader("💡 Answer")

        st.write(answer)


        # --------------------------------------------------
        # Display retrieved documents
        # --------------------------------------------------

        with st.expander("📄 View Retrieved Context"):

            for i, document in enumerate(documents):

                st.markdown(f"### Document {i + 1}")

                st.write(document)