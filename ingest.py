"""
ingest.py
Loads college documents (regulations, syllabus, FAQs, notices), splits them into
chunks, converts them into embeddings, and stores them in a local ChromaDB
vector database. Run this once before starting the app, and again any time the
documents in the data/ folder are updated.
"""

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DATA_FILES = [
    "data/regulations.txt",
    "data/syllabus.txt",
    "data/faqs.txt",
    "data/notices.txt",
]


def main():
    # 1. Load all text documents
    docs = []
    for path in DATA_FILES:
        docs += TextLoader(path, encoding="utf-8").load()
    print(f"Loaded {len(docs)} documents")

    # 2. Split documents into smaller overlapping chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    print(f"Split into {len(chunks)} chunks")

    # 3. Convert chunks into embeddings and store them in ChromaDB
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks, embeddings, persist_directory="chroma_db")
    db.persist()

    print("Ingestion complete. Vector database saved to 'chroma_db' folder.")


if __name__ == "__main__":
    main()
