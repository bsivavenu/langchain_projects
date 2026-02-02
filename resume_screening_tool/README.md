# Resume Screening Tool

Automated resume screening system using LLM-powered analysis to evaluate candidates and generate scoring reports.

## Features

- 📋 **Resume Parsing** - Extracts key information from resumes
- 🤖 **AI Evaluation** - LLM-based candidate assessment
- ⭐ **Scoring System** - Generates candidate scores
- 📊 **Report Generation** - Creates detailed evaluation reports
- 🔍 **Skill Matching** - Matches skills to job requirements
- 📈 **Batch Processing** - Process multiple resumes efficiently

## Tech Stack

- **Framework**: Streamlit
- **LLM**: OpenAI GPT or Google Gemini
- **Document Processing**: pypdf, docx2txt, LangChain
- **Analysis**: Pandas, Python
- **Database**: Optional SQLite/PostgreSQL for candidates

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

### 3. Prepare Job Requirements
- Define job descriptions
- List required skills
- Set evaluation criteria
- Configure scoring rubric

### 4. Run the Application
```bash
streamlit run app.py
```

Access at `http://localhost:8501`

## Usage Guide

### Single Resume Screening

1. **Upload Resume**
   - Click "Upload Resume" button
   - Select PDF or DOCX file
   - System extracts information

2. **View Analysis**
   - Candidate information extracted
   - Skills identified and matched
   - Experience level assessed

3. **Get Score**
   - Overall score (0-100)
   - Category scores (Skills, Experience, etc.)
   - Recommendation (Recommended/Consider/Pass)

### Batch Screening

1. **Upload Multiple Resumes**
   - ZIP file with multiple resumes
   - or select folder with resumes

2. **Configure Job Requirements**
   - Enter job title
   - List key requirements
   - Set must-have skills

3. **Process & Export**
   - System scores all resumes
   - Downloads ranking CSV
   - Generates summary report

## Project Structure

```
resume_screening_tool/
├── app.py                      # Main Streamlit app
├── config.py                   # Configuration
├── .env.example               # Environment template
├── requirements.txt           # Dependencies
├── utils/
│   ├── resume_parser.py       # Extract resume info
│   ├── llm_evaluator.py       # LLM-based scoring
│   ├── skill_matcher.py       # Skill matching logic
│   └── report_generator.py    # Report creation
├── prompts/
│   ├── system_prompt.txt      # Evaluation prompt
│   └── scoring_rubric.json    # Scoring criteria
└── templates/
    └── report_template.html   # Report HTML template
```

## Configuration

### Scoring Rubric (config.py)
```python
SCORING_CATEGORIES = {
    "experience": 0.30,        # 30% weight
    "skills": 0.40,            # 40% weight
    "education": 0.20,         # 20% weight
    "soft_skills": 0.10        # 10% weight
}

MUST_HAVE_SKILLS = [
    "Python",
    "Machine Learning",
    "AWS"
]

NICE_TO_HAVE = [
    "Docker",
    "Kubernetes"
]
```

### Job Requirements Format
```json
{
    "position": "Senior ML Engineer",
    "required_experience": "5+ years",
    "key_skills": ["Python", "TensorFlow", "AWS"],
    "education": "BS/MS in CS or related field",
    "salary_range": "$150k - $200k"
}
```

## Evaluation Criteria

### Experience Assessment
- Years of relevant experience
- Industry domain expertise
- Career progression
- Role complexity

### Skills Evaluation
- Technical skill match (0-100%)
- Proficiency level assessment
- Tool/framework knowledge
- Language proficiency

### Education Review
- Degree relevance
- Certifications
- Continuous learning
- Special training

### Soft Skills
- Leadership qualities
- Communication
- Problem-solving
- Team collaboration

## Output Formats

### Individual Report
```
Candidate: John Doe
Score: 82/100
Recommendation: RECOMMENDED

Skills Match: 90% (7/8 required)
Experience: 6 years (Meets requirement)
Education: MS in Computer Science

Missing Skills: Cloud Architecture
Strengths: Strong Python, ML background
Concerns: Limited AWS experience
```

### Batch CSV Export
```
Rank | Name | Score | Experience | Skills_Match | Status
1    | Jane | 92    | 7 years    | 100%        | Recommended
2    | John | 82    | 6 years    | 88%         | Recommended
3    | Mike | 71    | 4 years    | 75%         | Consider
```

## API Keys Required

| Service | Key |
|---------|-----|
| OpenAI | OPENAI_API_KEY |
| Google | GOOGLE_API_KEY |

## Supported File Formats

- **PDF** (.pdf)
- **Word** (.docx, .doc)
- **Text** (.txt)
- **Batch** (.zip with multiple files)

## Best Practices

1. **Keep Requirements Updated** - Regular job description updates
2. **Review Scores** - Don't rely solely on AI scoring
3. **Consistent Criteria** - Use same rubric for all positions
4. **Test** - Try tool with known candidates first
5. **Feedback Loop** - Update criteria based on hiring results

## Advanced Features

### Custom Evaluation Prompts
Modify `prompts/system_prompt.txt` for custom evaluation logic

### Integration with ATS
Export data to:
- CSV (for spreadsheets)
- JSON (for APIs)
- PDF (for reports)

### Analytics Dashboard
View metrics:
- Average candidate score
- Skill distribution
- Experience level breakdown
- Recommendation distribution

## Troubleshooting

**Q: Resume parsing fails?**
- Check file format (ensure valid PDF/DOCX)
- Try re-uploading file
- Check API quota

**Q: Scores seem inaccurate?**
- Review evaluation prompt
- Adjust scoring weights
- Update job requirements
- Provide feedback to improve model

**Q: Slow processing?**
- Process fewer resumes at once
- Use simpler LLM model
- Enable result caching

## Performance Tips

- Batch size: 10-20 resumes per batch
- Average time: 10-15 seconds per resume
- Caching enabled for identical resumes
- Parallel processing available

## Metrics to Track

- Average processing time
- Score distribution
- Agreement with human reviewers
- False positive/negative rate
- Hiring success rate vs. score

## Future Enhancements

- [ ] Multi-language resume support
- [ ] LinkedIn profile integration
- [ ] Video interview scheduling
- [ ] Salary negotiation automation
- [ ] Diversity metrics
- [ ] Real-time score updates
- [ ] Custom AI training on past hires

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open issues on GitHub for questions or bugs.
