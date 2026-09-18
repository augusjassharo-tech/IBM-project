"""
agent.py
Combines Retrieval-Augmented Generation (RAG), Tool Calling, and Memory into a
single function that answers a student's question, grounded in the college's
own documents.
"""

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from tools import get_today, search_notices, load_notices_text

load_dotenv()

# Load the persisted vector database created by ingest.py
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# Language model
llm = ChatAnthropic(
    model="claude-sonnet-4-6",
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

SYSTEM_INSTRUCTIONS = """You are a helpful college support assistant.
Answer the student's question using ONLY the context provided below.
If the answer is not in the context, say you don't know and suggest they
contact the relevant department or office.
Be concise and clear."""


def answer(question: str, chat_history: str = "") -> str:
    """
    Answers a student's question, grounded in retrieved document context,
    with optional tool use and prior chat history for memory.
    """
    # Simple tool-routing: handle a couple of intents directly
    lowered = question.lower()
    if "today" in lowered and "date" in lowered:
        return get_today()

    if "notice" in lowered and "about" in lowered:
        keyword = lowered.split("about", 1)[-1].strip().rstrip("?")
        notices_text = load_notices_text()
        matches = search_notices(keyword, notices_text)
        return "\n".join(matches)

    # Otherwise, fall back to RAG + LLM
    context_docs = db.similarity_search(question, k=4)
    context = "\n\n".join(d.page_content for d in context_docs)

    prompt = f"""{SYSTEM_INSTRUCTIONS}

Chat history:
{chat_history}

Context:
{context}

Question: {question}"""

    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    # Quick command-line test loop
    history = []
    print("AI Student Support Assistant (type 'exit' to quit)")
    while True:
        q = input("\nYou: ")
        if q.lower() in ("exit", "quit"):
            break
        hist_text = "\n".join(history)
        a = answer(q, hist_text)
        print(f"Assistant: {a}")
        history.append(f"Q: {q}\nA: {a}")
