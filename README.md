# 🤖 Automated Research Agent (Local RAG)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-v0.2-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Llama 3](https://img.shields.io/badge/Model-Llama_3-purple?style=for-the-badge&logo=meta&logoColor=white)
![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph-orange?style=for-the-badge)

> **A privacy-first, multi-agent AI system that autonomously researches, analyzes, and synthesizes technical literature using local Large Language Models.**

---

## 🚀 Overview

This project implements a **local-first RAG (Retrieval-Augmented Generation) pipeline** designed to automate literature reviews. Unlike standard linear chains, this system uses **LangGraph** to model the workflow as a state machine, enabling decoupled retrieval and synthesis agents.

### Key Capabilities
- **Autonomous Research** – Fetches relevant context from a local vector store using semantic search.  
- **Privacy-First** – Runs 100% offline with **Ollama** and quantized **Llama 3** (no API keys required).  
- **Stateful Orchestration** – Maintains context across agents using a shared `TypedDict` state schema.

---

## 🏗 Architecture

The system uses a **graph-based control flow** where:

- **Nodes** → Individual agents  
- **Edges** → Transition logic  

```mermaid
graph LR
    Start([Start]) --> Retrieve(🔍 Retrieve Node);
    Retrieve --> Generate(✍️ Generate Node);
    Generate --> End([End]);

    style Retrieve fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Generate fill:#fff3e0,stroke:#e65100,stroke-width:2px
Workflow
Ingestion – Documents are loaded, chunked, and embedded into ChromaDB.

Retrieval Node – Queries the vector store for semantically relevant content.

Generation Node – Llama 3 synthesizes answers grounded strictly in retrieved context.

🛠 Tech Stack & Engineering Decisions
Component	Technology	Reason for Choice
Orchestration	LangGraph	Enables cyclic, stateful agent workflows
LLM Engine	Ollama (Llama 3)	Fast local inference, no cloud dependency
Vector Database	ChromaDB	Lightweight, persistent, file-system friendly
Embeddings	Nomic-Embed-Text	High semantic density for RAG
Framework	LangChain	Standardized loaders & prompt templates

📂 Project Structure
bash
Copy code
├── chroma_db/          # Persistent Vector DB (auto-generated)
├── ingest.py          # Builds the knowledge base
├── main.py            # Multi-agent workflow entry point
├── requirements.txt   # Python dependencies
├── README.md          # Documentation
└── .gitignore         # Ignored files (venv, cache, db)
⚙️ Setup & Usage
1. Prerequisites
Make sure Ollama is installed and running.

bash
Copy code
# Pull required models
ollama run llama3
ollama pull nomic-embed-text
2. Installation
bash
Copy code
# Clone repository
git clone https://github.com/YOUR_USERNAME/automated-research-agent.git
cd automated-research-agent

# Create virtual environment
python -m venv venv

# Activate (Windows)
.\venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
3. Build the Knowledge Base
bash
Copy code
python ingest.py
4. Run the Agent
bash
Copy code
python main.py
📄 Example Output
Query:

What are the key components of an autonomous agent?

text
Copy code
🔎 Starting Research Task...
--- RETRIEVING INFO ---
--- GENERATING INSIGHTS ---

FINAL RESEARCH REPORT
========================================
Based on the provided context, the key components of an autonomous agent system are:

1. Planning  
   - Subgoal decomposition  
   - Reflection and refinement  

2. Memory  
   - Short-term memory (in-context learning)  
   - Long-term memory (vector databases)  

3. Tool Use  
   - Calling APIs for data retrieval and execution
🔮 Future Improvements
 Web Search Node – Integrate Tavily for real-time retrieval

 Hallucination Grader – Add a verification agent for factual grounding

 Streamlit UI – Build a user-friendly frontend
