import os
from typing import TypedDict, List
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langgraph.graph import StateGraph, END

# --- 1. CONFIGURATION ---
DB_PATH = "./chroma_db"
MODEL_NAME = "llama3"

# --- 2. SETUP RETRIEVER ---
# Load the existing vector database (built by ingest.py)
print("⏳ Loading Vector Database...")
embedding_function = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma(persist_directory=DB_PATH,
                     embedding_function=embedding_function)
retriever = vectorstore.as_retriever()

# --- 3. SETUP LLM & PROMPT ---
llm = ChatOllama(model=MODEL_NAME, temperature=0)

prompt = PromptTemplate(
    template="""
    You are an expert research assistant. Use the provided context to answer the question. 
    If the answer is not in the context, say "I don't know" based on the context. 
    Keep the answer concise and professional.

    Context: {context}

    Question: {question}

    Answer:
    """,
    input_variables=["question", "context"],
)

rag_chain = prompt | llm | StrOutputParser()

# --- 4. DEFINE STATE ---


class AgentState(TypedDict):
    question: str
    context: List[str]
    generation: str

# --- 5. DEFINE NODES ---


def retrieve_node(state: AgentState):
    """
    Agent 1: The Researcher
    Retrieves relevant documents from the vector store.
    """
    print("--- RETRIEVING INFO ---")
    question = state["question"]
    documents = retriever.invoke(question)
    # Extract just the text content
    return {"context": [doc.page_content for doc in documents]}


def generate_node(state: AgentState):
    """
    Agent 2: The Writer
    Generates an answer using the retrieved context.
    """
    print("--- GENERATING INSIGHTS ---")
    question = state["question"]
    context = "\n\n".join(state["context"])

    # Run the RAG chain
    generation = rag_chain.invoke({"context": context, "question": question})
    return {"generation": generation}


# --- 6. BUILD GRAPH ---
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("generate", generate_node)

# Add edges (Logic flow)
workflow.set_entry_point("retrieve")      # Start here
workflow.add_edge("retrieve", "generate")  # Go to generate
workflow.add_edge("generate", END)        # Finish

# Compile the application
app = workflow.compile()

# --- 7. EXECUTION (Runs only if you type 'python main.py') ---
if __name__ == "__main__":
    query = "What are the key components of an autonomous agent?"

    print(f"\n🔎 Starting Research Task for: '{query}'")

    inputs = {"question": query}
    result = app.invoke(inputs)

    print("\nFINAL RESEARCH REPORT")
    print("========================================")
    print(result['generation'])
    print("========================================")


