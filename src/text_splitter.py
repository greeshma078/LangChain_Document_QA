from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loader import load_text_file


# Load the document
file_path = "data/company_info.txt"

document_text = load_text_file(file_path)


# Create the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)


# Split the document into chunks
chunks = text_splitter.split_text(document_text)


# Display the results
print("Document split successfully!")
print()
print("Number of chunks:", len(chunks))

print("\n" + "=" * 60)

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk)