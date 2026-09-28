from langchain_ollama import ChatOllama


# Create the Llama 3.2 model
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)


# Send a question to the model
response = llm.invoke(
    "What is Artificial Intelligence? Explain in two sentences."
)


print("LLM Response:")
print(response.content)