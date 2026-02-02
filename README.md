# LangChain Projects

[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/bsivavenu/langchain_projects?style=social)](https://github.com/bsivavenu/langchain_projects)
[![Last Commit](https://img.shields.io/github/last-commit/bsivavenu/langchain_projects)](https://github.com/bsivavenu/langchain_projects)

A comprehensive collection of AI/LLM projects built with LangChain, demonstrating various use cases and integrations with OpenAI, Google GenAI, and other platforms.

## 📚 Project Overview

This repository contains multiple AI applications showcasing different aspects of LangChain:

### Core Learning Materials
- **LLM_Intro.ipynb** - Introduction to Large Language Models and LangChain basics
- **Chat Model Intro.ipynb** - Building conversational AI applications
- **Memory_Module.ipynb** - Implementing conversation memory and context management
- **Text Embeddings Example.ipynb** - Working with text embeddings and vector stores
- **Text_To_SQL_Query_Helper_Tool.ipynb** - Converting natural language to SQL queries
- **Text Embeddings_Intro.ipynb** - Advanced embedding techniques

### Production Applications

#### 1. **Automatic Ticket Classification Tool**
AI-powered system for automatically classifying support tickets using machine learning and LLM capabilities.
- **Features**: Document processing, SVM model training, ticket classification
- **Tech Stack**: Streamlit, scikit-learn, LangChain, Python
- **Location**: `automatic_ticket_classification_tool/`

#### 2. **Support Chatbot for Your Website**
Production-ready chatbot implementation for customer support integration.
- **Features**: Document QA, retrieval-augmented generation (RAG)
- **Location**: `support_chatbot_for_your_website/`

#### 3. **Resume Screening Tool**
Automated resume screening system using LLM-powered analysis.
- **Features**: Resume parsing, candidate evaluation, scoring
- **Location**: `resume_screening_tool/`

#### 4. **Invoice Data Extraction Tool**
Intelligent data extraction from invoice documents using document understanding.
- **Features**: PDF/Document parsing, field extraction, data validation
- **Location**: `invoice_data_extraction_tool/`

#### 5. **CSV Data Analysis Agent**
Autonomous agent for analyzing CSV data and generating insights.
- **Features**: Natural language queries on data, statistical analysis
- **Location**: `csv_data_analysis_agent/`

#### 6. **Marketing Campaign App**
AI-powered marketing content generation and campaign planning tool.
- **Features**: Content generation, campaign optimization
- **Location**: `marketing_campaign_app/`

#### 7. **Email Generator Tool**
Intelligent email composition system powered by LLMs.
- **Features**: Template-based generation, personalization
- **Location**: `email_generator_tool/`

#### 8. **YouTube Script Writing Tool**
AI assistant for creating YouTube video scripts and content outlines.
- **Features**: Script generation, SEO optimization suggestions
- **Location**: `youtube_script_writing_tool/`

#### 9. **Simple Question Answering Application**
Basic QA system demonstrating RAG implementation.
- **Features**: Document uploading, question answering
- **Location**: `Simple_Question_Answering_Application/`

## 🛠️ Tech Stack

- **LangChain** - Core framework for LLM applications
- **LangChain Integrations**:
  - langchain-openai
  - langchain-google-genai
  - langchain-huggingface
  - langchain-pinecone
  - langchain-chroma
  
- **Vector Stores**: 
  - Pinecone
  - FAISS
  - Chroma

- **Web Frameworks**: Streamlit
- **Data Processing**: Pandas, NumPy, scikit-learn
- **Document Handling**: pypdf, docx2txt, BeautifulSoup4

## 📋 Requirements

- Python >= 3.11, < 3.13
- Virtual environment (recommended: `python -m venv .venv`)

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/bsivavenu/langchain_projects.git
cd langchain_projects
```

### 2. Set Up Environment
```bash
# Using uv (recommended)
uv sync

# Or using pip
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Environment Variables
```bash
# Copy the example env file
cp .env.example .env

# Edit .env with your API keys
# Required keys:
# - OPENAI_API_KEY (for OpenAI models)
# - GOOGLE_API_KEY (for Google GenAI models)
# - PINECONE_API_KEY (if using Pinecone)
```

### 4. Run a Project
```bash
# Example: Run Streamlit app
streamlit run automatic_ticket_classification_tool/app.py

# Or run Jupyter notebooks
jupyter notebook LLM_Intro.ipynb
```

## 📖 Usage Examples

### Running Notebook Examples
```bash
# Start Jupyter
jupyter notebook

# Open any .ipynb file to explore LangChain concepts
```

### Running Streamlit Applications
```bash
# Automatic Ticket Classification
streamlit run automatic_ticket_classification_tool/app.py

# Support Chatbot
streamlit run support_chatbot_for_your_website/app.py
```

## 🔑 API Keys Required

To use various features, you'll need to set up API keys in your `.env` file:

1. **OpenAI API Key** - For GPT models
   - Sign up at https://platform.openai.com
   
2. **Google AI API Key** - For Gemini models
   - Get key at https://makersuite.google.com/app/apikey
   
3. **Pinecone API Key** - For vector database (optional)
   - Create account at https://www.pinecone.io

## 📁 Project Structure

```
langchain_projects/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
│
├── 📓 Learning Notebooks/
│   ├── LLM_Intro.ipynb
│   ├── Chat Model Intro.ipynb
│   ├── Memory_Module.ipynb
│   └── ... (other educational notebooks)
│
└── 🚀 Applications/
    ├── automatic_ticket_classification_tool/
    ├── support_chatbot_for_your_website/
    ├── resume_screening_tool/
    ├── invoice_data_extraction_tool/
    ├── csv_data_analysis_agent/
    ├── marketing_campaign_app/
    ├── email_generator_tool/
    ├── youtube_script_writing_tool/
    └── Simple_Question_Answering_Application/
```

## 🎯 Key Features

- ✅ **Multiple LLM Integrations** - OpenAI, Google GenAI, HuggingFace, and more
- ✅ **RAG Implementation** - Examples of Retrieval-Augmented Generation
- ✅ **Vector Store Integration** - Pinecone, FAISS, Chroma examples
- ✅ **Production Ready** - Streamlit-based deployment-ready apps
- ✅ **Educational** - Learn LangChain from basics to advanced patterns
- ✅ **Well-Documented** - Code examples and notebooks with explanations

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🚀 Getting Help

- Check individual project README files in their respective folders
- Review the notebook examples for detailed implementation patterns
- Open an issue for bugs or feature requests
- See existing issues for Q&A

## 📚 Resources

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API Docs](https://platform.openai.com/docs)
- [Google AI Studio](https://makersuite.google.com/)
- [Pinecone Vector Database](https://www.pinecone.io/)

## 🙏 Acknowledgments

Built with:
- [LangChain](https://www.langchain.com/) - LLM application framework
- [OpenAI](https://openai.com/) - GPT models
- [Google AI](https://ai.google/) - Gemini models
- [Streamlit](https://streamlit.io/) - Web app framework
- [Pinecone](https://www.pinecone.io/) - Vector database

---

**Last Updated**: February 2, 2026

For the latest updates, visit: [GitHub Repository](https://github.com/bsivavenu/langchain_projects)
