# Email Generator Tool

Intelligent email composition system powered by LLMs for generating professional and personalized emails.

## Features

- 📧 **Email Templates** - Pre-built templates for common scenarios
- 🎯 **Personalization** - Dynamic variable insertion
- ✍️ **AI Composition** - LLM-powered email generation
- 📋 **Email Types** - Business, sales, support, HR, etc.
- 🔄 **Variations** - Generate multiple versions
- 📤 **Export** - Plain text, HTML, or draft formats

## Tech Stack

- **Framework**: Streamlit
- **LLM**: OpenAI GPT / Google Gemini
- **Framework**: LangChain for prompting
- **Data**: Pandas for batch processing

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
```

Required keys:
```env
OPENAI_API_KEY=sk-proj-your-key
GOOGLE_API_KEY=your-google-key
```

### 3. Run Application
```bash
streamlit run app.py
```

Open `http://localhost:8501`

## Usage Guide

### Generate Single Email

1. **Select Email Type**
   - Business correspondence
   - Sales outreach
   - Customer support
   - HR/recruitment
   - Newsletter
   - Other

2. **Fill in Details**
   - Recipient name/email
   - Purpose and context
   - Key points to cover
   - Tone preference

3. **Generate & Refine**
   - AI generates email
   - Review and edit
   - Generate variations
   - Copy to clipboard

## Project Structure

```
email_generator_tool/
├── app.py                          # Main Streamlit app
├── config.py                       # Configuration
├── .env.example                   # Environment template
├── requirements.txt               # Dependencies
├── utils/
│   ├── email_generator.py         # Core generation
│   ├── template_manager.py        # Template system
│   ├── personalization.py         # Variable substitution
│   └── batch_processor.py         # Batch generation
├── templates/
│   ├── business.json              # Business email templates
│   ├── sales.json                 # Sales templates
│   ├── support.json               # Support templates
│   ├── hr.json                    # HR templates
│   └── general.json               # General templates
└── prompts/
    └── generation_prompt.txt      # Main generation prompt
```

## Supported Email Types

### Business Correspondence
- Meeting requests
- Project updates
- Status reports
- Introduction emails

### Sales & Outreach
- Cold outreach
- Follow-ups
- Proposal emails
- Closing emails

### Customer Support
- Issue resolution
- Complaint responses
- Help desk tickets
- Escalations

### HR & Recruitment
- Job offers
- Rejection letters
- Onboarding
- Performance feedback

### Marketing
- Newsletter content
- Promotional emails
- Event invitations
- Announcements

### General
- Thank you emails
- Apologies
- Resignation letters
- Custom emails

## Configuration

### Email Templates (config.py)
```python
EMAIL_TYPES = {
    "business": "Professional, formal tone",
    "sales": "Persuasive, value-focused",
    "support": "Helpful, empathetic",
    "hr": "Formal, clear expectations",
    "casual": "Friendly, approachable"
}

TONES = ["professional", "casual", "formal", "friendly", "urgent"]
```

## Output Examples

### Business Email
```
Subject: Project Status Update - Week of Jan 15

Dear [Recipient Name],

I wanted to provide you with a brief update on the current 
status of [Project Name].

Progress:
- Completed [Task 1] on schedule
- [Task 2] 80% complete, on track
- [Task 3] starting next week

Next Steps:
- [Milestone 1] - Due [Date]
- [Milestone 2] - Due [Date]

Please let me know if you need any additional information 
or have any questions.

Best regards,
[Your Name]
```

### Sales Outreach
```
Subject: Quick question about your [Challenge]

Hi [First Name],

I noticed that [Company] has been [Observation/Challenge], 
and I thought you might find this helpful.

We've helped similar companies [Benefit], resulting in 
[Specific Result].

Would you be open to a brief 15-minute conversation to 
explore how this might apply to [Company]?

Best,
[Your Name]
```

### Customer Support
```
Subject: RE: Your issue with [Product]

Hi [Customer Name],

Thank you for reaching out about [Issue]. I sincerely 
apologize for the inconvenience this has caused.

I've investigated the issue and here's what I found:
[Explanation]

To resolve this, please:
1. [Step 1]
2. [Step 2]
3. [Step 3]

Please let me know if this resolves the issue or if you 
need any further assistance.

Best regards,
[Your Name]
```

## Features Explained

### Template System
- Pre-built for common scenarios
- Customizable templates
- Variable substitution
- Multi-language support

### Personalization
```python
Variables = {
    "recipient_name": "John",
    "company": "Acme Corp",
    "product": "Widget Pro",
    "value_prop": "50% faster processing"
}
```

### Tone Adjustment
- Professional/Formal
- Casual/Friendly
- Urgent/Time-sensitive
- Empathetic/Supportive
- Persuasive/Sales

## API Keys Required

| Service | Key |
|---------|-----|
| OpenAI | OPENAI_API_KEY |
| Google | GOOGLE_API_KEY |

## Batch Email Generation

### Process Multiple Emails
```python
emails = [
    {
        "type": "sales",
        "recipient": "john@company.com",
        "company": "Acme Corp",
        "subject_theme": "problem solving"
    },
    {
        "type": "sales",
        "recipient": "jane@startup.io",
        "company": "StartupXYZ",
        "subject_theme": "efficiency"
    }
]

# Generates all emails with CSV export
```

## Best Practices

1. **Personalization** - Always use recipient-specific details
2. **Proof Reading** - Review AI-generated content
3. **Tone Match** - Ensure tone fits relationship
4. **Clear CTA** - Always include call to action
5. **Mobile Friendly** - Keep paragraphs short

## Customization

### Add Email Type
1. Create template file in `templates/`
2. Add to config.py
3. Create generation prompt
4. Test with samples

### Custom Variables
```python
CUSTOM_VARIABLES = {
    "company_name": "Required",
    "recipient_title": "Optional",
    "custom_detail": "Optional"
}
```

## Performance

- Single email generation: 5-15 seconds
- Variations per request: 2-3
- Batch processing: Efficient parallelization
- API usage: Optimized for cost

## Troubleshooting

**Q: Generated email too long/short?**
- Adjust length preferences
- Try different tone
- Edit template specificity

**Q: Email not personalized enough?**
- Provide more context
- Add custom details
- Use specific template

**Q: API errors?**
- Check API key validity
- Verify quota availability
- Check network connection

## Advanced Features

### Email Analytics
- Generation history
- Performance tracking
- Recipient engagement
- A/B test results

### Integration
- Email client plugins
- CRM integration
- Marketing automation
- Signature management

### Export Options
- Plain text (.txt)
- HTML (.html)
- Markdown (.md)
- PDF (.pdf)

## Metrics to Track

- Generation success rate
- Average generation time
- Email quality ratings
- Response rates
- User satisfaction

## Future Enhancements

- [ ] Real-time collaboration
- [ ] Email scheduling
- [ ] Sentiment analysis
- [ ] Grammar/style checker
- [ ] Multi-language support
- [ ] Email template library
- [ ] Spam checker integration

## Example Use Cases

- Reaching out to 100 prospects with personalized emails
- Creating templated responses for support team
- Drafting professional business communications
- Generating newsletter content
- Creating job offer letters

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open issues on GitHub.
