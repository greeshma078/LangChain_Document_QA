from pathlib import Path


def load_text_file(file_path):
    path = Path(file_path)

    with open(path, "r", encoding="utf-8") as file:
        text = file.read()

    return text


if __name__ == "__main__":
    file_path = "data/company_info.txt"

    document_text = load_text_file(file_path)

    print("Document loaded successfully!")
    print()
    print("Number of characters:", len(document_text))
    print()
    print("First 500 characters:")
    print(document_text[:500])