🚀 LangGraph RAG Engine

A fast, modular Retrieval-Augmented Generation (RAG) system using LangChain, LangGraph, FAISS, and OpenAI/Ollama/OpenRouter-compatible LLMs.

This project builds a production-style RAG pipeline with:

PDF, TXT, and URL ingestion

Chunking and embeddings

FAISS vector search

A LangGraph-powered RAG workflow

Optional Agentic RAG (REACT + Tools)

Streamlit UI for interaction

✨ Features
📄 Document Ingestion

Supports:

PDF files

Plain text files

URL lists inside .txt files

Entire directory ingestion (data/)

🧩 Smart Text Chunking

Uses RecursiveCharacterTextSplitter for clean document splitting with overlap.

🔍 Embedding + FAISS Vector Store

Fast semantic search

Local CPU-friendly

Vector retriever auto-integrated with LangGraph nodes

🔗 LangGraph Workflow

Custom RAG pipeline:

[USER QUESTION]
       ↓
 ┌────────────┐
 │ Retriever  │ → selects top-k document chunks
 └────────────┘
       ↓
 ┌────────────┐
 │ LLM Answer │ → generates context-grounded answer
 └────────────┘
       ↓
   Final Output

🤖 Agentic RAG (optional)

REACT agent with tools:

Vector store retriever

Wikipedia search

Enhanced answer reasoning

🖥️ Streamlit UI

Simple and clean:

Input box

Result display

Source document preview

History of queries

📁 Project Structure
Project1/
│
├── streamlit.py                 # Main UI application
├── README.md
├── .env                         # API keys (ignored in git)
│
├── src/
│   ├── config/
│   │   └── config.py            # LLM model + settings
│   │
│   ├── document_ingestion/
│   │   └── document_processor.py # Load PDF/TXT/URLs + chunking
│   │
│   ├── vectorstore/
│   │   └── vectorstore.py       # Embeddings + FAISS retriever
│   │
│   ├── graphbuilder/
│   │   └── graph_builder.py     # LangGraph RAG pipeline
│   │
│   ├── nodes/
│   │   ├── nodes.py             # Basic RAG nodes
│   │   └── reactnode.py         # Agentic RAG node (React + tools)
│   │
│   └── states/
│       └── rag_state.py         # Shared state object
│
└── data/                        # Place PDFs, Text files, URL lists
    ├── myfile.pdf
    ├── urls.txt
    └── notes.txt

⚙️ Installation
1️⃣ Clone repo
git clone git@github.com:dinesh43431/langgraph-rag-engine.git
cd langgraph-rag-engine

2️⃣ Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

3️⃣ Install dependencies
pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

OPENROUTER_API_KEY=your_key_here


To use Ollama locally:

LLM_MODEL=ollama:llama3

▶️ Run the Streamlit App
streamlit run streamlit.py

🧪 Test RAG from CLI
python test.py

🧠 How RAG Works in This Project

Documents are loaded from the data/ folder

Text is split into overlapping chunks

Embeddings are computed for each chunk

FAISS indexes these vectors

Query → converted to embedding

FAISS retrieves top-k matching chunks

LLM generates answer using ONLY retrieved context

Streamlit displays answer + supporting documents

💡 Example Query
Who is India’s T20I vice-captain?


RAG will:

Find matching chunk in vector DB

Extract only contextually correct info

Prevent hallucinations

🚀 Future Enhancements

Add reranking (BGE, Cohere)

Tool-using agent for multi-step reasoning

Chat memory integration

Upload files directly from UI

Multi-model switching interface
