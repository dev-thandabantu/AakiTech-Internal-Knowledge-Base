# AakiTech Internal Knowledge Base

A RAG (Retrieval-Augmented Generation) system for searching through internal documents using semantic search.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.41.0-red.svg)
![LangChain](https://img.shields.io/badge/langchain-v0.3.12-green.svg)

## Features

- 🔍 **Semantic Search**: Find relevant information using natural language queries
- 🌐 **Web Interface**: Easy-to-use Streamlit web UI
- 🔄 **Flexible Embeddings**: Switch between OpenAI and free HuggingFace embeddings
- 📊 **Similarity Scores**: See how relevant each result is
- 📄 **Source Attribution**: Know which document each answer came from
- ⚡ **Fast Performance**: Chroma vector store for quick retrieval
- 🔒 **Secure**: API keys stored in environment variables

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aakitech-knowledge-base.git
cd aakitech-knowledge-base
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key (optional)
```

## Quick Start

### 1. Add Documents

Place your `.txt` files in the project folder or update the `folder_path` in `embed.py`

### 2. Create Embeddings

```bash
python embed.py
```

### 3. Start the Web Interface

```bash
streamlit run app.py
```

Or on Windows, double-click `run_app.bat`

### 4. Search!

Open your browser to `http://localhost:8501` and start asking questions!

## Sample Questions

- "What is AakiTech's Q3 sales goal?"
- "Tell me about Project Pinda"
- "What's the marketing strategy for Q3?"
- "Who is Brighton?"
- "How does AakiTech use AI?"

## Files

- `embed.py` - Creates embeddings from our documents
- `app.py` - Streamlit web interface
- `test_retrieval.py` - Command-line testing script
- `run_app.bat` - Easy launcher for Windows
- `.env` - Environment variables (API keys)

## Settings

### Embedding Models

- **HuggingFace** (Free): Uses `sentence-transformers/all-MiniLM-L6-v2`
- **OpenAI** (Paid): Uses `text-embedding-3-small` (requires API credits)

### Environment Variables

Set your OpenAI API key in `.env`:

```
OPENAI_API_KEY=your-api-key-here
```

## Troubleshooting

### "No module named 'sentence_transformers'"

```bash
pip install sentence-transformers
```

### "Error loading vector store"

Make sure you've run `embed.py` first to create the vector index.

### "Rate limit error"

You've exceeded your OpenAI quota. Switch to HuggingFace embeddings or add credits.

## Technical Details

- **Vector Store**: FAISS for fast similarity search
- **Text Splitting**: 500 characters with 50 character overlap
- **Web Framework**: Streamlit for the UI
- **Embeddings**: Sentence Transformers or OpenAI
- **Vector Store**: Chroma for similarity search

## Deployment

### Streamlit Community Cloud (Recommended)

1. **Push to GitHub**: Ensure your code is on GitHub
2. **Visit Streamlit Cloud**: Go to [share.streamlit.io](https://share.streamlit.io)
3. **Connect GitHub**: Sign in and connect your GitHub account
4. **Deploy**:
   - Click "New app"
   - Select your repository: `dev-thandabantu/AakiTech-Internal-Knowledge-Base`
   - Main file path: `streamlit_app.py`
   - Click "Deploy!"

### Environment Variables for Deployment

In Streamlit Cloud settings, add:

```
OPENAI_API_KEY=your-actual-api-key-here
```

### Local Development vs Production

- **Local**: Uses documents from your local folder
- **Production**: Uses sample documents included in the repo
- **Vector Store**: Will be created automatically on first run

## Live Demo

🚀 **[Try the live app here](https://your-app-name.streamlit.app)** (will be available after deployment)
