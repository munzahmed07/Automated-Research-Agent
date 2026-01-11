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


