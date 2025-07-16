from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

def search(query, use_openai=False):
    if use_openai:
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
    else:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    
    # Load the Chroma vector store
    chroma_db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )
    
    # Search for similar documents
    results = chroma_db.similarity_search(query, k=3)
    
    for i, res in enumerate(results):
        print(f"--- Result {i+1} ---")
        print(f"Content: {res.page_content[:500]}...")
        if hasattr(res, 'metadata') and res.metadata:
            print(f"Source: {res.metadata.get('source', 'Unknown')}")
        print()

def search_with_score(query, use_openai=False, k=3):
    """Search with similarity scores to see how relevant the results are"""
    if use_openai:
        embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        print("Using OpenAI embeddings for search...")
    else:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        print("Using HuggingFace embeddings for search...")
    
    chroma_db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding_model
    )
    
    # Search with similarity scores
    results_with_scores = chroma_db.similarity_search_with_score(query, k=k)
    
    print(f"\n🔍 Query: {query}")
    print(f"📄 Found {len(results_with_scores)} relevant documents with scores:\n")
    
    for i, (doc, score) in enumerate(results_with_scores):
        print(f"--- Result {i+1} (Score: {score:.4f}) ---")
        print(f"Content: {doc.page_content[:300]}...")
        if hasattr(doc, 'metadata') and doc.metadata:
            print(f"Source: {doc.metadata.get('source', 'Unknown')}")
        print()

# Test multiple queries
if __name__ == "__main__":
    # Test different queries
    queries = [
        "What is AakiTech's Q3 sales goal?",
        "Marketing strategy for Q3",
        "Project Pinda",
        "Brighton",
        "AI integrations"
    ]
    
    print("=" * 60)
    print("TESTING MULTIPLE QUERIES")
    print("=" * 60)
    
    for query in queries:
        search(query, use_openai=False)
        print("-" * 60)
