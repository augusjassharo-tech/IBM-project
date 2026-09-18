# AI Student Support Assistant

An intelligent conversational assistant that answers college-related questions
from regulations, syllabus, FAQs, and notices. Built using **RAG (Retrieval-Augmented
Generation) + Tool Calling + Memory**.

## Author
- **Name:** Sharona. A
- **Department:** Computer Science and Engineering (CSE)
- **Year:** Final Year
- **College:** Holycross Engineering College
- **Email:** augusjassharo@gmail.com

## Features
- Answers student questions grounded in official college documents (no hallucinated answers).
- Retrieves relevant document chunks using a vector database (ChromaDB).
- Supports simple tool calls (e.g. today's date, notice search by keyword).
- Maintains conversational memory across a chat session.
- Simple Streamlit web interface.

## Project Structure
```
ai-student-support-assistant/
├── data/                # Source documents (regulations, syllabus, FAQs, notices)
├── ingest.py            # Builds the vector database from the data files
├── tools.py             # Callable tool functions used by the agent
├── agent.py             # Core RAG + Tools + Memory logic
├── app.py                # Streamlit chat UI
├── requirements.txt     # Python dependencies
├── .env.example          # Template for your API key (copy to .env)
└── .gitignore
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/<your-username>/ai-student-support-assistant.git
   cd ai-student-support-assistant
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Add your API key:
   Copy `.env.example` to `.env` and add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_key_here
   ```

5. Build the vector database (run once):
   ```
   python ingest.py
   ```

6. Run the app:
   ```
   streamlit run app.py
   ```

## Key Agent Capabilities
| Capability | Description |
|---|---|
| RAG | Retrieves relevant chunks from college documents before answering |
| Tools | Calls small functions (date lookup, notice search) when needed |
| Memory | Retains conversation history for context-aware follow-up answers |

## Use Case
This project was developed as **Use Case 1: AI Student Support Assistant** from a
5-day AI agent workshop, where students select one use case and build it into a
final project.
