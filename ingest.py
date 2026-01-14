# Import the tools we need
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

# 1. LOAD: We grab content from these 3 websites to act as our "research material"
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

print(" Loading documents...")
docs = [WebBaseLoader(url).load() for url in urls]
# Flatten the list (technical detail: makes it a single list of docs)
docs_list = [item for sublist in docs for item in sublist]

# 2. SPLIT: Break text into 500-character chunks so the AI can digest it easily
text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
    chunk_size=500, chunk_overlap=50
)
doc_splits = text_splitter.split_documents(docs_list)

# 3. & 4. EMBED & STORE: Create the database
# We use 'nomic-embed-text' to understand the meaning of the words
print(" creating vector database...")
vectorstore = Chroma.from_documents(
    documents=doc_splits,
    collection_name="rag-chroma",
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    persist_directory="./chroma_db"  # This saves the DB to your hard drive
)

print(" Step 1 Complete! Database created in './chroma_db' folder.")

