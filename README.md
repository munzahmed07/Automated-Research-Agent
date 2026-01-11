# 🤖 Automated Research Agent (Local RAG)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-v0.2-green?style=for-the-badge&logo=chainlink&logoColor=white)
![Llama 3](https://img.shields.io/badge/Model-Llama_3-purple?style=for-the-badge&logo=meta&logoColor=white)
![LangGraph](https://img.shields.io/badge/Orchestrator-LangGraph-orange?style=for-the-badge)

> **A privacy-first, multi-agent AI system that autonomously researches, analyzes, and synthesizes technical literature using local Large Language Models.**

---

## 🚀 Overview

This project implements a **local-first RAG (Retrieval-Augmented Generation) pipeline** designed to automate literature reviews. Unlike standard linear chains, this system uses **LangGraph** to model the workflow as a state machine, enabling decoupled retrieval and synthesis agents.

Key capabilities:
* **Autonomous Research:** Fetches relevant context from a local vector store based on semantic meaning.
* **Privacy-First:** Runs 100% offline using **Ollama** and quantized **Llama 3**, requiring no API keys.
* **Stateful Orchestration:** Maintains context across agent steps using a shared state schema (`TypedDict`).

---

## 🏗 Architecture

The system utilizes a graph-based control flow where "Nodes" represent agents and "Edges" represent the transition logic.

```mermaid
graph LR
    Start([Start]) --> Retrieve(🔍 Retrieve Node);
    Retrieve --> Generate(✍️ Generate Node);
    Generate --> End([End]);

    style Retrieve fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Generate fill:#fff3e0,stroke:#e65100,stroke-width:2px
Ingestion: Documents are loaded, split recursively, and embedded into ChromaDB.Retrieval Node: The agent queries the vector store for semantic matches.Generation Node: Llama 3 synthesizes an answer, grounded strictly in the retrieved context to minimize hallucinations.🛠 Tech Stack & Engineering DecisionsComponentTechnologyReason for ChoiceOrchestrationLangGraphTo move beyond rigid chains and enable cyclic/stateful agent workflows.LLM EngineOllama (Llama 3)High-performance local inference; eliminates cloud latency and cost.Vector DatabaseChromaDBLightweight, persistent, and integrates natively with local file systems.EmbeddingsNomic-Embed-TextOptimized for RAG tasks with higher semantic density than standard BERT models.FrameworkLangChainFor standardized document loading and prompt templating.📂 Project StructureBash├── chroma_db/          # Persistent Vector Database (Generated automatically)
├── ingest.py           # Script to load docs & build the Knowledge Base
├── main.py             # Main entry point: The Multi-Agent Workflow
├── requirements.txt    # Python dependencies
├── README.md           # Documentation
└── .gitignore          # Ignored files (venv, cache, db)
⚙️ Setup & Usage1. PrerequisitesEnsure you have Ollama installed and running.Bash# Pull the necessary models (Run in terminal)
ollama run llama3
ollama pull nomic-embed-text
2. InstallationBash# Clone the repository
git clone [https://github.com/YOUR_USERNAME/automated-research-agent.git](https://github.com/YOUR_USERNAME/automated-research-agent.git)
cd automated-research-agent

# Create virtual environment & install dependencies
python -m venv venv
# Activate Venv (Windows):
.\venv\Scripts\activate
# Activate Venv (Mac/Linux):
source venv/bin/activate

pip install -r requirements.txt
3. Build the Knowledge BaseThis script scrapes the sample documentation and creates the vector embeddings.Bashpython ingest.py
4. Run the AgentExecute the research workflow.Bashpython main.py
📄 Example OutputQuery: "What are the key components of an autonomous agent?"Plaintext🔎 Starting Research Task...
--- RETRIEVING INFO ---
--- GENERATING INSIGHTS ---

FINAL RESEARCH REPORT
========================================
Based on the provided context, the key components of an autonomous agent system are:

1. **Planning**: 
    - Subgoal decomposition (breaking complex tasks into smaller steps).
    - Reflection and refinement (critiquing and improving plans).

2. **Memory**:
    - Short-term memory (in-context learning).
    - Long-term memory (storing and recalling information via vector databases).

3. **Tool Use**: 
    - The ability to call external APIs for information gathering or code execution.
🔮 Future Improvements[ ] Web Search Node: Integrate Tavily Search API to fetch real-time data if local context is insufficient.[ ] Hallucination Grader: Add a "Grader Agent" to verify if the answer is supported by the documents before showing it to the user.[ ] Streamlit UI: Build a frontend for easier interaction.
