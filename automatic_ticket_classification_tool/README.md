# Automatic Ticket Classification Tool

Intelligent system for automatically classifying support tickets using machine learning and LLM capabilities.

## Features

- 🤖 **ML-Based Classification** - SVM model for ticket categorization
- 📄 **Document Processing** - Extracts text from PDF and DOCX files
- 💬 **LLM Integration** - Uses LangChain for intelligent analysis
- 🏷️ **Multi-Category Support** - Classifies tickets into multiple categories
- 📊 **Model Training** - Create and train ML models on custom data
- 🔍 **Smart Matching** - Matches tickets to appropriate categories

## Project Structure

```
automatic_ticket_classification_tool/
├── app.py                      # Main Streamlit application
├── .env.example               # Environment variables template
├── requirements.txt           # Project dependencies
├── Tickets.csv               # Sample ticket data
├── modelsvm.pk1              # Pre-trained SVM model
├── Documents/                # Sample policy documents
│   ├── HR Policy Manual.pdf
│   ├── IT Department Policy Manual.pdf
│   └── Transportation Policy Manual.pdf
└── pages/                    # Streamlit multi-page apps
    ├── Create_ML_Model.py    # Model training interface
    ├── Load_Data_Store.py    # Data loading functionality
    ├── Pending_tickets.py    # Ticket classification interface
    ├── admin_utils.py        # Utility functions
    └── user_utils.py         # User helper functions
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API keys if needed
```

### 3. Run the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

### Train a New Model
1. Go to "Create_ML_Model" page
2. Upload your CSV with ticket data
3. Select features and target column
4. Click "Train Model" to create the SVM classifier

### Classify Tickets
1. Go to "Pending_tickets" page
2. Upload new tickets (CSV or manual entry)
3. View automatic classification results
4. Adjust classifications if needed

### View Policy Documents
1. Go to "Load_Data_Store" page
2. Upload policy documents (PDF/DOCX)
3. System extracts and indexes documents
4. Use for knowledge-based classification

## Dependencies

- streamlit
- pandas
- scikit-learn
- langchain
- langchain-community
- python-dotenv
- docx2txt
- pypdf

## API Keys Required

- **OPENAI_API_KEY** (optional) - For LLM-based classification enhancement
- Add to `.env` file

## Data Format

### CSV Format for Tickets
```csv
Ticket_ID,Subject,Description,Category
T001,Login Issue,User cannot access account,Technical
T002,Billing Query,Question about invoice,Billing
```

### Document Support
- PDF files (.pdf)
- Word documents (.docx)

## Model Information

- **Algorithm**: Support Vector Machine (SVM)
- **Model File**: `modelsvm.pk1`
- **Training**: Scikit-learn based
- **Re-trainable**: Yes, create new models in the app

## Tips & Best Practices

1. **Training Data**: Ensure sufficient and balanced training data
2. **Document Updates**: Regularly update policy documents
3. **Model Evaluation**: Monitor classification accuracy over time
4. **Feature Selection**: Choose relevant features for classification

## Troubleshooting

**Q: Model not loading?**
- Ensure `modelsvm.pk1` exists in the directory
- Re-train the model if file is corrupted

**Q: API Key errors?**
- Verify API key is correctly set in `.env`
- Check API quota and permissions

**Q: Document parsing fails?**
- Ensure PDF/DOCX files are not corrupted
- Check file permissions

## Performance Metrics

- ⚡ Fast classification (< 1 second per ticket)
- 📈 Scalable to 1000s of tickets
- 🎯 Customizable accuracy vs speed tradeoff

## Future Enhancements

- [ ] Multi-language support
- [ ] Real-time model performance monitoring
- [ ] Integration with ticketing systems (Jira, ServiceNow)
- [ ] Advanced NLP techniques (BERT, GPT)
- [ ] Database persistence for tickets

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

For issues or questions, open an issue in the main repository.
