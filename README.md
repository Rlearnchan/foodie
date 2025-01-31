# foodie
AI-powered research assistant for analyzing food desert related documents.

## Installation & Setup

### 1. Install Dependencies with Poetry

Install Poetry if you haven't already:

```bash
pip install poetry
```

Then, install the dependencies:

```bash
poetry install
```

### 2. Environment Setup
Create a `.env` file in the root directory and add your API keys:

```plaintext
OPENAI_API_KEY=your_api_key_here
```

## Running the Application

Launch the Streamlit application:
```bash
poetry run streamlit run main.py
```

The web interface will automatically open in your default browser. You can:
- Enter your research question about food deserts
- Get AI-generated answers based on the document collection
- View relevant source documents with page references

## Features
- Document relevance grading
- AI-powered answer generation
- Clean web interface using Streamlit
- Source document tracking with page references

## Project Structure
```
.
├── main.py             # Streamlit application entry point
├── graph/              
│   ├── chains/         # LangChain components
│   └── nodes/          # Processing nodes
├── poetry.lock         # Poetry dependency lock file
└── pyproject.toml      # Project configuration
```
