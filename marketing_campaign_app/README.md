# Marketing Campaign App

AI-powered marketing content generation and campaign planning tool using LLMs.

## Features

- ✍️ **Content Generation** - Create marketing copy and campaigns
- 🎯 **Audience Targeting** - AI-powered audience analysis
- 📱 **Multi-Channel** - Email, social media, SMS content
- 💡 **Campaign Ideas** - Brainstorm marketing strategies
- 📊 **Copy Variations** - Generate A/B testing variants
- 📝 **Template System** - Reusable campaign templates

## Tech Stack

- **Framework**: Streamlit
- **LLM**: OpenAI GPT / Google Gemini
- **Content Generation**: LangChain prompts
- **Data**: Pandas for campaign data

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

### Create Marketing Campaign

1. **Define Campaign Details**
   - Campaign name and goal
   - Target audience profile
   - Product/service description
   - Budget and timeline

2. **Select Campaign Type**
   - Email campaign
   - Social media content
   - SMS marketing
   - Landing page copy

3. **Generate Content**
   - AI generates multiple variations
   - Review and edit content
   - Export ready-to-use copy

## Project Structure

```
marketing_campaign_app/
├── app.py                          # Main Streamlit app
├── config.py                       # Configuration
├── .env.example                   # Environment template
├── requirements.txt               # Dependencies
├── utils/
│   ├── content_generator.py       # Copy generation
│   ├── campaign_builder.py        # Campaign logic
│   ├── audience_analyzer.py       # Audience insights
│   └── templates.py               # Template management
├── prompts/
│   ├── email_prompt.txt           # Email generation
│   ├── social_prompt.txt          # Social media prompt
│   └── headlines.txt              # Headline ideas
└── templates/
    ├── email_template.html        # Email template
    └── campaign_template.json     # Campaign structure
```

## Campaign Types

### Email Marketing
- Subject lines (multiple variants)
- Email body copy
- Call-to-action buttons
- A/B testing variants

### Social Media
- Instagram captions
- Twitter/X posts
- LinkedIn articles
- TikTok video scripts

### SMS & Push
- Short punchy messages
- Promo codes and offers
- Time-sensitive urgency
- Emoji-enhanced variants

### Content Marketing
- Blog post outlines
- Landing page copy
- Product descriptions
- Case study templates

## Configuration

### Campaign Settings
```python
CHANNELS = ["email", "social", "sms", "web"]
TONES = ["professional", "casual", "humorous", "urgent"]
TARGET_AUDIENCES = [
    "Enterprise",
    "SMB",
    "Startups",
    "Individual"
]
```

## Content Examples

### Email Subject Lines
- "🎉 Exclusive 30% off - Today only!"
- "Don't miss out: Your discount expires soon"
- "See what our top customers are loving"

### Social Media Posts
- Instagram: Visually appealing, hashtag-rich
- LinkedIn: Professional insights and thought leadership
- Twitter: Concise, shareable, trending-aware

### SMS Copy
- 160 characters or less
- Clear CTAs
- Offer-driven
- Time-sensitive language

## Features Explained

### Audience Insights
- Demographics analysis
- Psychographics
- Behavior patterns
- Pain points
- Motivation analysis

### Copy Generation
- Multiple style variations
- Different tone options
- Various lengths
- A/B test variants
- Localization options

### Performance Optimization
- Readability scoring
- Keyword density
- CTA effectiveness
- Engagement prediction

## API Keys Required

| Service | Key |
|---------|-----|
| OpenAI | OPENAI_API_KEY |
| Google | GOOGLE_API_KEY |

## Output Examples

### Email Campaign
```
Subject: "🎁 Unlock Your Exclusive 25% Off - Limited Time"

Body:
Hi [First Name],

We've been thinking about you! As one of our valued 
customers, we wanted to offer you something special.

Use code: SPECIAL25
Valid until: [Date]

[CTA Button: Claim Your Discount]
```

### Social Media Post
```
Instagram Caption:
"Your goals deserve a partner who gets it. 💪 
See how 10k+ professionals are achieving more with 
[Product]. Limited time: 25% off. Link in bio 🔗
#GoalGetter #Productivity #Success"
```

## Best Practices

1. **Personalization** - Include audience-specific details
2. **A/B Testing** - Always test multiple versions
3. **Compliance** - Follow marketing regulations
4. **Data Privacy** - Handle customer data responsibly
5. **Authenticity** - Maintain brand voice

## Customization

### Add Custom Prompts
Create in `prompts/` folder:
```txt
Generate [type] marketing content for:
- Product: [product]
- Audience: [audience]
- Tone: [tone]
- Goal: [goal]
```

### Brand Voice Settings
```python
BRAND_VOICE = {
    "tone": "friendly",
    "formality": "casual",
    "vocabulary_level": "accessible",
    "personality_traits": ["innovative", "trustworthy"]
}
```

## Performance Metrics

- Content generation time: 10-30 seconds
- Variants generated per request: 3-5
- Average character count: 50-500 (varies)
- Engagement rate prediction: Available

## Troubleshooting

**Q: Generated content sounds generic?**
- Add more specific audience details
- Provide brand voice guidelines
- Use custom prompts for your industry
- Refine through multiple iterations

**Q: Content too long/short?**
- Adjust length parameters in config
- Specify character count in prompt
- Choose appropriate channel

## Advanced Features

### Campaign Performance Tracking
- Track which content performs best
- A/B test results
- Conversion metrics
- ROI calculations

### Integration Options
- Email platform APIs
- Social media schedulers
- Marketing automation tools
- Analytics dashboards

### Export Formats
- PDF campaigns
- CSV with content variants
- HTML templates
- Markdown documents

## Metrics to Track

- Content generation quality
- User satisfaction ratings
- Campaign performance
- A/B test results
- ROI per campaign

## Future Enhancements

- [ ] Real-time market trend integration
- [ ] Competitor analysis
- [ ] Automated A/B testing
- [ ] Multi-language support
- [ ] Brand consistency checker
- [ ] Campaign calendar
- [ ] Email deliverability checker

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open issues on GitHub.
