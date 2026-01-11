# 🤖 Automated Research Agent (Local RAG)

A privacy-first, multi-agent AI system that autonomously researches, analyzes, and synthesizes technical literature using local Large Language Models.

---

## 🚀 Overview

This project implements a local-first RAG (Retrieval-Augmented Generation) pipeline designed to automate literature reviews. Instead of using a simple linear chain, this system uses LangGraph to model the workflow as a state machine, allowing multiple agents to work together.

### Key Capabilities

* Autonomous Research: Retrieves relevant context from a local vector store using semantic search.
* Privacy-First: Runs completely offline using Ollama and Llama 3. No API keys required.
* Stateful Orchestration: Maintains shared memory across agents using a typed state schema.

---

## 🏗 Architecture

Workflow

Start → Retrieve Node → Generate Node → End

Explanation

1. Ingestion – Documents are loaded, chunked, and embedded into ChromaDB.
2. Retrieval Node – Fetches semantically relevant document chunks.
3. Generation Node – Llama 3 generates responses grounded strictly in retrieved context.

---

## 🛠 Tech Stack

* Orchestration: LangGraph
* LLM Engine: Ollama (Llama 3)
* Vector Database: ChromaDB
* Embeddings: Nomic-Embed-Text
* Framework: LangChain

---

## 📂 Project Structure

chroma_db/          # Persistent vector database (auto-generated)
ingest.py           # Builds the knowledge base
main.py             # Multi-agent workflow entry point
requirements.txt    # Python dependencies
README.md           # Documentation
.gitignore          # Ignored files

---

## ⚙️ Setup & Usage

1. Prerequisites

Install Ollama and pull required models:

ollama run llama3
ollama pull nomic-embed-text

2. Installation

git clone [https://github.com/YOUR_USERNAME/automated-research-agent.git](https://github.com/YOUR_USERNAME/automated-research-agent.git)
cd automated-research-agent

python -m venv venv

Windows:
.\venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt

3. Build the Knowledge Base

python ingest.py

4. Run the Agent

python main.py

---

## 📄 Example Output

Query: What are the key components of an autonomous agent?

FINAL RESEARCH REPORT

Based on the provided context, the key components of an autonomous agent system are:

1. Planning

   * Subgoal decomposition
   * Reflection and refinement

2. Memory

   * Short-term memory (in-context learning)
   * Long-term memory (vector databases)

3. Tool Use

   * Calling external APIs for information retrieval and execution

---

## 🔮 Future Improvements

* Web Search Node for real-time retrieval
* Hallucination Grader Agent
* Streamlit-based UI

---

## Created By

Built by Munzer Ahmed
