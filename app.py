import streamlit as st
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
import os

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AakiTech Knowledge Base",
    page_icon="🔍",
    layout="wide"
)

@st.cache_resource
def load_vector_store(use_openai=False):
    """Load the FAISS vector store (cached for better performance)"""
    try:
        if use_openai:
            embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")
        else:
            embedding_model = HuggingFaceEmbeddings(
                model_name="sentence-transformers/all-MiniLM-L6-v2"
            )
        
        faiss_index = FAISS.load_local(
            "vector_index", 
            embedding_model, 
            allow_dangerous_deserialization=True
        )
        return faiss_index
    except Exception as e:
        st.error(f"Error loading vector store: {e}")
        return None

def search_knowledge_base(query, num_results=3, use_openai=False):
    """Search the knowledge base and return results"""
    vector_store = load_vector_store(use_openai)
    
    if vector_store is None:
        return []
    
    try:
        results = vector_store.similarity_search_with_score(query, k=num_results)
        return results
    except Exception as e:
        st.error(f"Error searching: {e}")
        return []

# Main app
def main():
    # Header
    st.title("🔍 AakiTech Internal Knowledge Base")
    st.markdown("**Ask questions about your documents and get instant answers!**")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Embedding model selection
        use_openai = st.checkbox(
            "Use OpenAI Embeddings", 
            value=False,
            help="Check this if you have OpenAI credits. Leave unchecked to use free HuggingFace embeddings."
        )
        
        # Number of results
        num_results = st.slider(
            "Number of results", 
            min_value=1, 
            max_value=10, 
            value=3,
            help="How many relevant documents to show"
        )
        
        # Show similarity scores
        show_scores = st.checkbox(
            "Show similarity scores", 
            value=True,
            help="Display how relevant each result is"
        )
        
        st.markdown("---")
        st.markdown("### 💡 Sample Questions")
        st.markdown("""
        - What is AakiTech's Q3 sales goal?
        - Tell me about Project Pinda
        - What's the marketing strategy for Q3?
        - Who is Brighton?
        - How does AakiTech use AI?
        """)
    
    # Main search interface
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_input(
            "Ask a question:",
            placeholder="e.g., What is AakiTech's Q3 sales goal?",
            label_visibility="collapsed"
        )
    
    with col2:
        search_button = st.button("🔍 Search", type="primary", use_container_width=True)
    
    # Handle search
    if search_button and query:
        with st.spinner("Searching knowledge base..."):
            results = search_knowledge_base(query, num_results, use_openai)
        
        if results:
            st.success(f"Found {len(results)} relevant documents:")
            
            # Display results
            for i, (doc, score) in enumerate(results):
                with st.expander(f"📄 Result {i+1}" + (f" (Score: {score:.4f})" if show_scores else ""), expanded=True):
                    
                    # Content
                    st.markdown("**Content:**")
                    content = doc.page_content
                    if len(content) > 1000:
                        st.markdown(content[:1000] + "...")
                        with st.expander("Show full content"):
                            st.markdown(content)
                    else:
                        st.markdown(content)
                    
                    # Source
                    if hasattr(doc, 'metadata') and doc.metadata:
                        source = doc.metadata.get('source', 'Unknown')
                        if source != 'Unknown':
                            filename = os.path.basename(source)
                            st.markdown(f"**Source:** `{filename}`")
                    
                    # Separator
                    if i < len(results) - 1:
                        st.markdown("---")
        else:
            st.warning("No results found. Try rephrasing your question.")
    
    elif search_button and not query:
        st.warning("Please enter a question to search.")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>"
        "Built with ❤️ using Streamlit • AakiTech Knowledge Base"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
