import os
from typing import List
from typing_extensions import TypedDict

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import START, END, StateGraph

# --- CONFIGURATION ---
LLM_MODEL = "llama3"
EMBEDDING_MODEL = "nomic-embed-text"
VECTOR_STORE_PATH = "./chroma_db"  # This must match where ingest.py saved it

print(f"🚀 Initializing Research Agent with {LLM_MODEL}...")

# --- 1. LOAD THE DATABASE (created in Step 1) ---
# We don't ingest again. We just load what you already built.
vectorstore = Chroma(
    collection_name="rag-chroma",
    embedding_function=OllamaEmbeddings(model=EMBEDDING_MODEL),
    persist_directory=VECTOR_STORE_PATH
)
retriever = vectorstore.as_retriever()
print("✅ Loaded Knowledge Base from disk.")

# --- 2. DEFINE GRAPH STATE ---
# This is the "memory" that is passed between the agents


class AgentState(TypedDict):
    question: str
    generation: str
    documents: List[str]

# --- 3. DEFINE NODES (The Agents) ---


# Initialize LLM
llm = ChatOllama(model=LLM_MODEL, temperature=0)


def retrieve_node(state):
    """
    Agent 1: The Researcher. 
    Retrieves relevant documents from the vector store.
    """
    print(f"\n--- RETRIEVING INFO FOR: {state['question']} ---")
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}


def generate_node(state):
    """
    Agent 2: The Synthesizer.
    Takes the documents and synthesizes an answer/insight.
    """
    print("--- GENERATING INSIGHTS ---")
    question = state["question"]
    documents = state["documents"]

    # Simple RAG Prompt
    prompt = PromptTemplate(
        template="""You are an expert research assistant. Use the following context to answer the question. 
        If you don't know, say you don't know. Keep the answer professional and concise.
        
        Context: {context}
        
        Question: {question}
        
        Answer:""",
        input_variables=["question", "context"],
    )

    rag_chain = prompt | llm | StrOutputParser()
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

# --- 4. BUILD THE GRAPH ---


workflow = StateGraph(AgentState)

# Add Nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

# Add Edges (Logic Flow)
workflow.add_edge(START, "retrieve")
workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", END)

# Compile the Graph
app = workflow.compile()

# --- 5. EXECUTION ---

if __name__ == "__main__":
    # You can change this question to test different things!
    query = "What are the key components of an autonomous agent system?"
    inputs = {"question": query}

    print(f"\n🔎 Starting Research Task...")
    result = app.invoke(inputs)

    print("\n" + "="*40)
    print("FINAL RESEARCH REPORT")
    print("="*40 + "\n")
    print(result["generation"])
