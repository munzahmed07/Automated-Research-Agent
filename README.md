# Automated Research Agent with LangGraph & Llama 3

## 🚀 Overview
This project is a local, privacy-first **Multi-Agent RAG System** designed to automate the research and synthesis of technical literature. 

It leverages **LangGraph** for stateful orchestration, moving beyond simple linear chains to create a cyclic workflow where agents can retrieve, analyze, and synthesize information autonomously.

## 🏗 Architecture
The system follows a graph-based architecture:
* **Retrieval Agent:** Fetches relevant context from a local vector store (ChromaDB) containing ingested technical documents.
* **Synthesis Agent:** Utilizes **Llama 3** (via Ollama) to generate concise, factual reports grounded in the retrieved data.
* **State Management:** Uses a shared state schema (`TypedDict`) to pass context, documents, and generation history between nodes.

## 🛠 Tech Stack
* **Orchestration:** LangGraph (Stateful workflow management)
* **LLM:** Llama 3 (Quantized, running locally via Ollama)
* **Vector Database:** ChromaDB (Local persistent storage)
* **Embeddings:** Nomic-Embed-Text
* **Framework:** LangChain

## ⚙️ How to Run Locally
1.  **Clone the Repository**
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup Ollama:**
    * Download [Ollama](https://ollama.com/)
    * Run: `ollama run llama3` & `ollama pull nomic-embed-text`
4.  **Ingest Knowledge Base:**
    ```bash
    python ingest.py
    ```
5.  **Run the Agent:**
    ```bash
    python main.py
    ```