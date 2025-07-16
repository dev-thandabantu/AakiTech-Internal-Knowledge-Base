# Contributing to AakiTech Knowledge Base

Thank you for your interest in contributing to the AakiTech Knowledge Base project!

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a new branch for your feature/fix
4. Make your changes
5. Test your changes
6. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/dev-thandabantu/AakiTech-Internal-Knowledge-Base.git
cd Aakitech-Knowledge-Base

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
```

## Code Style

- Follow PEP 8 for Python code
- Use descriptive variable and function names
- Add comments for complex logic
- Keep functions small and focused

## Testing

Before submitting a PR:

1. Test the embedding process: `python embed.py`
2. Test the web interface: `streamlit run app.py`
3. Test with different query types
4. Verify error handling

## Submitting Changes

1. Ensure your code follows the style guidelines
2. Add appropriate documentation
3. Test your changes thoroughly
4. Create a clear PR description

## Feature Requests

Open an issue to discuss new features before implementing them.

## Bug Reports

When reporting bugs, please include:

- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details (Python version, OS, etc.)
