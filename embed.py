import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables from .env file
load_dotenv()

# Load all .txt documents from a folder
def load_documents_from_folder(folder_path):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            full_path = os.path.join(folder_path, filename)
            loader = TextLoader(os.path.join(folder_path, filename), encoding="utf-8")
            documents.extend(loader.load())
    return documents

# Split documents into smaller chunks
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
    )
    return splitter.split_documents(documents)

# Store the chunks into a Chroma vector index
def store_in_chroma(chunks, use_openai=False):
    if use_openai:
        # Use OpenAI embeddings (requires credits)
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        print("Using OpenAI embeddings...")
    else:
        # Use free HuggingFace embeddings
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Using free HuggingFace embeddings...")
    
    print("Generating embeddings...")
    chroma_db = Chroma.from_documents(
        chunks, 
        embedding_model,
        persist_directory="./chroma_db"
    )
    chroma_db.persist()
    print("Chroma vector store saved to './chroma_db'")

# Run the full pipeline when script is executed
if __name__ == "__main__":
    # Use current directory for deployment compatibility
    folder_path = '.'  # Look for .txt files in the current directory

    print("🔍 Loading documents...")
    documents = load_documents_from_folder(folder_path)
    print(f"✅ Loaded {len(documents)} documents")

    print("✂️ Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"✅ Created {len(chunks)} chunks")

    print("💾 Storing chunks in Chroma vector store...")
    # Use free embeddings instead of OpenAI (set to True when you have credits)
    store_in_chroma(chunks, use_openai=False)

    print("🚀 Embedding complete. Your vector store is ready!")
