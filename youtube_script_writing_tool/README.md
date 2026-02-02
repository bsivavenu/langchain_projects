# YouTube Script Writing Tool

AI assistant for creating YouTube video scripts and content outlines with SEO optimization suggestions.

## Features

- ✍️ **Script Generation** - Full video scripts from concept
- 📝 **Outline Creation** - Structured content planning
- 🎬 **Scene Breakdown** - Shot-by-shot descriptions
- 🔍 **SEO Optimization** - Keywords and title suggestions
- 📊 **Analytics Ready** - Metadata and hashtag generation
- ⏱️ **Timing Calculator** - Script duration estimation

## Tech Stack

- **Framework**: Streamlit
- **LLM**: OpenAI GPT / Google Gemini
- **Content Generation**: LangChain
- **Data Processing**: Pandas, Python

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

### Create YouTube Script

1. **Define Video Concept**
   - Video title and topic
   - Target audience
   - Video length (5 min, 10 min, etc.)
   - Tone/Style (educational, entertainment, vlog)

2. **Provide Details**
   - Main points to cover
   - Call-to-action message
   - Keywords for SEO
   - Any special segments

3. **Generate Script**
   - AI creates full script
   - Includes timing cues
   - Scene descriptions
   - Visual suggestions

4. **Optimize & Export**
   - Review script
   - Check timing
   - Generate metadata
   - Download in various formats

## Project Structure

```
youtube_script_writing_tool/
├── app.py                          # Main Streamlit app
├── config.py                       # Configuration
├── .env.example                   # Environment template
├── requirements.txt               # Dependencies
├── utils/
│   ├── script_generator.py        # Script creation
│   ├── seo_analyzer.py            # SEO optimization
│   ├── timing_calculator.py       # Duration estimation
│   ├── outline_builder.py         # Content structure
│   └── metadata_generator.py      # Title/tags/description
├── prompts/
│   ├── script_prompt.txt          # Main script prompt
│   ├── seo_prompt.txt             # SEO optimization
│   └── metadata_prompt.txt        # Metadata generation
└── templates/
    ├── educational_template.txt   # Educational videos
    ├── vlog_template.txt          # Vlog format
    ├── tutorial_template.txt      # Tutorial format
    └── entertainment_template.txt # Entertainment videos
```

## Video Types Supported

### Educational
- Tutorials
- How-to guides
- Lessons
- Explanations

### Entertainment
- Comedy sketches
- Vlogs
- Reviews
- Reactions

### Professional
- Presentations
- Case studies
- Product demos
- Testimonials

### Creative
- Storytelling
- Documentaries
- Animations
- Music videos

## Configuration

### Video Settings
```python
VIDEO_LENGTHS = {
    "short": "1-3 minutes",
    "medium": "5-10 minutes",
    "long": "15-30 minutes",
    "evergreen": "unlimited"
}

TONES = [
    "educational",
    "entertaining",
    "professional",
    "casual",
    "humorous",
    "inspirational"
]
```

## Output Examples

### Full Script
```
TITLE: "5 Python Tips to Write Better Code"

[0:00-0:05] INTRO
Voiceover: "Writing clean Python code is essential for 
every developer. In this video, I'll share 5 powerful tips..."

[0:05-0:15] TIP #1: List Comprehensions
Visual: Show code examples
Voiceover: "First up, list comprehensions make your code..."

[MIDDLE CONTENT]

[DURATION-10s] CALL-TO-ACTION
Visual: Subscribe button animation
Voiceover: "If you found these tips helpful, smash that 
subscribe button..."

[END] OUTRO
Total Duration: Approximately 8 minutes 45 seconds
```

### SEO Metadata
```
Title: "5 Python Tips to Write Better Code | 2024 Guide"
Description: "Learn 5 essential Python tips to write cleaner, 
faster code. Perfect for beginners and intermediate developers..."
Tags: #Python, #Programming, #CodingTips, #Tutorial, #WebDevelopment
Keywords: python tips, clean code, python tutorial
```

### Video Outline
```
1. Introduction (0:00-0:15)
   - Hook the audience
   - Preview the 5 tips

2. Tip #1: List Comprehensions (0:15-2:00)
   - What they are
   - Example code
   - Benefits

3. Tip #2: Context Managers (2:00-3:45)
   - Use cases
   - Syntax
   - Practical examples

4. Tip #3: Decorators (3:45-5:30)
5. Tip #4: Type Hints (5:30-7:00)
6. Tip #5: Generator Functions (7:00-8:30)

7. Call-to-Action (8:30-8:45)
```

## Features Explained

### Script Generation
- Natural language conversational scripts
- Multiple style options
- Timing estimates
- Scene descriptions
- Visual cues

### SEO Optimization
- Keyword suggestions
- Title optimization
- Description ideas
- Tag recommendations
- Trending topics

### Timing Calculator
- Word count to duration
- Pacing adjustments
- Segment timing
- Buffer suggestions

### Metadata Generator
- YouTube titles
- Descriptions
- Tags and hashtags
- Playlist categories
- Thumbnail descriptions

## API Keys Required

| Service | Key |
|---------|-----|
| OpenAI | OPENAI_API_KEY |
| Google | GOOGLE_API_KEY |

## Best Practices

1. **Hook Viewers** - Strong opening (first 5 seconds)
2. **Clear Structure** - Logical progression of ideas
3. **Call-to-Action** - Include subscribe/like prompts
4. **SEO Optimization** - Use relevant keywords naturally
5. **Pacing** - Vary pace to maintain interest
6. **Visual Cues** - Describe visuals clearly
7. **Timestamps** - Break into chapters

## Customization

### Custom Video Template
```python
CUSTOM_TEMPLATE = {
    "structure": ["intro", "main", "cta", "outro"],
    "intro_duration": "10-15 seconds",
    "cta_placement": "before_outro",
    "tone": "professional",
    "target_audience": "developers"
}
```

### Brand Voice Settings
```python
BRAND_VOICE = {
    "personality": "friendly",
    "formality": "casual",
    "humor": "light",
    "energy_level": "high"
}
```

## Performance Metrics

- Script generation: 20-60 seconds
- Words per minute (spoken): 140-160
- Average video length suggestion: 8-12 minutes
- SEO score calculation available

## Export Formats

- Plain text (.txt)
- Markdown (.md)
- PDF document (.pdf)
- Google Docs (link)
- Teleprompter format

## Troubleshooting

**Q: Script too long?**
- Reduce video length target
- Be more specific with main points
- Use bullet points format

**Q: SEO suggestions not relevant?**
- Specify niche/category
- Add competitor titles to analyze
- Include target keywords

**Q: Timing seems off?**
- Adjust speaking pace
- Review word count
- Account for visual segments

## Advanced Features

### SEO Analysis
- Competitor title analysis
- Keyword difficulty scores
- Search volume estimates
- Ranking potential

### Content Planning
- Series planning
- Content calendar
- Playlist organization
- Collaboration tools

### Analytics Integration
- View predictions
- CTR optimization
- Thumbnail suggestions
- A/B test ideas

## Metrics to Track

- Script quality ratings
- Video performance
- SEO effectiveness
- Viewer engagement
- CTR and click-through

## Workflow Example

1. **Brainstorm** - Concept and audience
2. **Research** - Keywords and trends
3. **Outline** - Main points structure
4. **Generate** - AI creates script
5. **Refine** - Edit and personalize
6. **Optimize** - SEO and metadata
7. **Export** - Download formats
8. **Publish** - Upload to YouTube

## Future Enhancements

- [ ] Automatic thumbnail concepts
- [ ] Transcript generation
- [ ] Multi-language scripts
- [ ] Trending topic suggestions
- [ ] Video analytics predictions
- [ ] Voiceover script formatting
- [ ] Storyboard generation

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open issues on GitHub.
