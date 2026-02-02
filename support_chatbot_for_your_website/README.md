# Support Chatbot for Your Website

Production-ready chatbot implementation for customer support integration with document QA and retrieval-augmented generation (RAG).

## Features

- 💬 **Multi-turn Conversations** - Maintains context across messages
- 🔍 **Document QA** - Answers questions from uploaded documents
- 🧠 **RAG Implementation** - Retrieval-Augmented Generation for accurate responses
- 🚀 **Web Integration** - Easily embed in your website
- 📚 **Knowledge Base** - Build from documents, PDFs, and web content
- ⚡ **Real-time Responses** - Fast and contextual answers

## Tech Stack

- **Framework**: Streamlit (Web UI)
- **LLM**: OpenAI GPT / Google Gemini
- **Vector Database**: Pinecone / Chroma / FAISS
- **Document Processing**: LangChain, pypdf, docx2txt
- **Backend**: Python with LangChain

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
```

Add required API keys:
```env
OPENAI_API_KEY=sk-proj-your-key
GOOGLE_API_KEY=your-google-key
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENVIRONMENT=us-east-1
```

### 3. Prepare Knowledge Base
- Collect documents (PDF, DOCX, TXT)
- Place in `/documents` folder or upload via UI
- System automatically processes and indexes them

### 4. Run the Chatbot
```bash
streamlit run app.py
```

Open `http://localhost:8501` in your browser

## Usage Guide

### Starting a Conversation
1. Open the web interface
2. Type your question in the chat input
3. Chatbot responds with context-aware answers
4. Continue multi-turn conversation

### Uploading Documents
1. Use document upload feature
2. Supported formats: PDF, DOCX, TXT, MD
3. System indexes documents for Q&A
4. Automatic text splitting and embedding

### Customization
- Modify system prompts in `config.py`
- Adjust temperature and response length
- Configure vector database connection
- Set up conversation history limits

## Project Structure

```
support_chatbot_for_your_website/
├── app.py                 # Main Streamlit application
├── config.py             # Configuration settings
├── .env.example          # Environment template
├── requirements.txt      # Dependencies
├── documents/            # Knowledge base documents
│   └── sample_doc.pdf
├── utils/
│   ├── rag_pipeline.py   # RAG implementation
│   ├── embeddings.py     # Embedding utilities
│   └── chat_utils.py     # Chat functions
└── prompts/              # Prompt templates
    └── system_prompt.txt
```

## Configuration

### Basic Settings (config.py)
```python
MODEL = "gpt-3.5-turbo"  # or "gpt-4"
TEMPERATURE = 0.7
MAX_TOKENS = 500
VECTOR_STORE = "pinecone"  # or "chroma", "faiss"
```

### RAG Parameters
- **Chunk Size**: 1000 tokens
- **Overlap**: 200 tokens
- **Top K Retrieval**: 3 documents

## API Keys Required

| Service | Key Name | Where to Get |
|---------|----------|-------------|
| OpenAI | OPENAI_API_KEY | https://platform.openai.com |
| Google | GOOGLE_API_KEY | https://makersuite.google.com |
| Pinecone | PINECONE_API_KEY | https://www.pinecone.io |

## Features Explained

### Document QA
- Upload customer manuals, FAQs, policies
- Chatbot searches relevant sections
- Provides accurate answers with citations

### Conversation Memory
- Remembers previous questions
- Maintains context for follow-ups
- Customizable memory length

### Response Quality
- Filters low-confidence responses
- Shows source documents
- Handles out-of-domain queries gracefully

## Deployment Options

### Local Development
```bash
streamlit run app.py
```

### Production (Streamlit Cloud)
```bash
# Push to GitHub
git push origin main

# Deploy via Streamlit Cloud dashboard
# https://share.streamlit.io
```

### Self-hosted (Docker)
```dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["streamlit", "run", "app.py"]
```

## Performance Optimization

- **Caching**: Embeddings are cached for speed
- **Batch Processing**: Multiple documents processed efficiently
- **Connection Pooling**: Vector DB connections optimized
- **Response Streaming**: Real-time token streaming

## Troubleshooting

**Q: Chatbot gives irrelevant answers?**
- Improve knowledge base documents
- Adjust similarity threshold in config
- Increase `top_k` retrieval parameter

**Q: Slow response times?**
- Check API key rate limits
- Reduce document chunk size
- Switch to faster LLM model

**Q: Document not being retrieved?**
- Verify document upload succeeded
- Check embedding quality
- Re-index knowledge base

## Best Practices

1. **Document Quality**: Use clear, well-structured documents
2. **Testing**: Test with diverse user queries
3. **Monitoring**: Track conversation logs for improvements
4. **Updates**: Regularly update knowledge base
5. **Fine-tuning**: Adjust prompts based on user feedback

## Integration Example

```python
from chatbot import SupportChatbot

chatbot = SupportChatbot(
    model="gpt-3.5-turbo",
    vector_store="pinecone"
)

response = chatbot.chat("How do I reset my password?")
print(response)
```

## Metrics & Analytics

- Response time per query
- Document relevance score
- User satisfaction rating
- Common questions tracking
- Coverage metrics

## Future Enhancements

- [ ] Multi-language support
- [ ] Sentiment analysis
- [ ] Handoff to human agents
- [ ] Analytics dashboard
- [ ] Mobile app integration
- [ ] Voice input/output

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open an issue on GitHub for questions or problems.
