# CSV Data Analysis Agent

Autonomous agent for analyzing CSV data and generating insights using natural language queries.

## Features

- 📊 **Natural Language Queries** - Ask questions about your data
- 🔍 **Data Exploration** - Automatic data profiling and analysis
- 📈 **Statistical Analysis** - Descriptive stats, correlations, trends
- 🤖 **Autonomous Agent** - AI agent decides analysis approach
- 💡 **Smart Insights** - Generates actionable recommendations
- 📉 **Visualization** - Automatic chart generation

## Tech Stack

- **Framework**: Streamlit
- **LLM**: OpenAI GPT / Google Gemini
- **Data Analysis**: Pandas, NumPy, Scikit-learn
- **Visualization**: Matplotlib, Plotly
- **Agent Framework**: LangChain

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

### Upload and Analyze Data

1. **Upload CSV File**
   - Click "Upload CSV"
   - Select your CSV file
   - System auto-loads and profiles

2. **Ask Questions**
   - Natural language queries
   - "What's the average sales by region?"
   - "Show me top 10 customers"
   - "Analyze trends in Q4"

3. **Get Insights**
   - Detailed analysis results
   - Relevant visualizations
   - Statistical summaries
   - Actionable recommendations

## Project Structure

```
csv_data_analysis_agent/
├── app.py                          # Main Streamlit app
├── config.py                       # Configuration
├── .env.example                   # Environment template
├── requirements.txt               # Dependencies
├── utils/
│   ├── data_loader.py             # CSV loading
│   ├── data_profiler.py           # Data analysis
│   ├── agent_builder.py           # Agent creation
│   ├── tools/
│   │   ├── query_tool.py          # Query execution
│   │   ├── stats_tool.py          # Statistical analysis
│   │   ├── visualization_tool.py  # Chart generation
│   │   └── summary_tool.py        # Summary generation
│   └── utils.py                   # Helper functions
└── samples/
    └── sample_data.csv            # Sample CSV file
```

## Supported Query Types

### Data Exploration
- "Show me the first 10 rows"
- "What columns do we have?"
- "What's the data shape?"
- "Are there any missing values?"

### Statistical Analysis
- "Calculate mean and median of sales"
- "Show correlation between age and income"
- "Detect outliers in revenue"
- "Distribution of customer segments"

### Aggregation
- "Total sales by month"
- "Average order value by region"
- "Count of customers per category"
- "Top 5 products by revenue"

### Filtering
- "Sales above $10,000"
- "Customers from New York"
- "Transactions in 2024"
- "Items with rating > 4.5"

### Trends
- "Sales trend over time"
- "Growth rate by quarter"
- "Seasonal patterns"
- "Year-over-year comparison"

## Features Explained

### Agent Tools

The autonomous agent has access to:
1. **SQL/Pandas Query Tool** - Execute data queries
2. **Statistics Tool** - Calculate metrics and correlations
3. **Visualization Tool** - Create charts and graphs
4. **Summary Tool** - Generate text summaries

### Analysis Capabilities

- **Descriptive Statistics** - Mean, median, std dev, quartiles
- **Correlation Analysis** - Identify relationships
- **Trend Analysis** - Time-series analysis
- **Outlier Detection** - Statistical anomalies
- **Grouping & Aggregation** - Multi-level summaries
- **Comparisons** - Period vs period analysis

### Visualizations

- Line charts (trends)
- Bar charts (comparisons)
- Pie charts (distributions)
- Scatter plots (relationships)
- Histograms (distributions)
- Heatmaps (correlations)

## Configuration

### Agent Settings (config.py)
```python
MODEL = "gpt-3.5-turbo"
TEMPERATURE = 0.3  # Lower = more deterministic
MAX_TOKENS = 2000

# Data analysis settings
MAX_ROWS_DISPLAY = 100
NUMERIC_PRECISION = 2  # Decimal places
```

### Sample CSV Format
```
Date,Region,Product,Sales,Quantity,Customer_ID
2024-01-01,North,Widget A,1500.00,10,C001
2024-01-02,South,Widget B,2000.00,15,C002
2024-01-03,East,Widget A,1800.00,12,C003
```

## API Keys Required

| Service | Key |
|---------|-----|
| OpenAI | OPENAI_API_KEY |
| Google | GOOGLE_API_KEY |

## Supported File Formats

- CSV (.csv)
- Excel (.xlsx, .xls)
- TSV (.tsv)
- Parquet (.parquet)

## Output Examples

### Query: "What are the top 5 customers by total spending?"

**Output:**
```
Based on the analysis of your data:

Top 5 Customers by Spending:
1. Customer C001: $45,320.00
2. Customer C002: $38,900.00
3. Customer C003: $35,670.00
4. Customer C004: $32,145.00
5. Customer C005: $29,876.00

Total from Top 5: $182,011.00
Percentage of Total Revenue: 42.5%

Insight: These 5 customers represent a significant portion 
of your revenue. Consider loyalty programs or VIP support.
```

### Query: "Show sales trends by month"

**Output:**
```
Monthly Sales Trend:
January: $125,430
February: $142,560
March: $156,780
April: $149,320
May: $168,900

Growth Analysis:
Month-over-month growth: 8.2% average
Q1 vs Q2: +12.5%
Best month: May (+7.9%)
Slowest month: January
```

## Best Practices

1. **Data Quality** - Clean data first
2. **Columns Names** - Use descriptive names
3. **Date Format** - ISO format (YYYY-MM-DD)
4. **File Size** - Optimal: <50MB
5. **Reviews Results** - Always validate outputs

## Performance Tips

- Use cleaner datasets for faster analysis
- Ask specific questions for better results
- Limit to <100 columns for best performance
- Pre-process large files

## Troubleshooting

**Q: Agent gives generic answers?**
- Ask more specific questions
- Provide context in query
- Upload cleaner data
- Check column names are descriptive

**Q: Visualization not showing?**
- Check data has numeric columns
- Verify data types are correct
- Try simpler visualization query

**Q: API errors?**
- Check API key and quota
- Verify network connection
- Try smaller dataset

## Advanced Features

### Custom Analysis Tools
Add tools in `utils/tools/`:
```python
def custom_tool(df, **kwargs):
    # Custom analysis logic
    return results
```

### Export Capabilities
- PDF reports
- Excel with charts
- JSON data export
- SQL query logs

### Scheduling
- Daily analysis runs
- Automated reports
- Email notifications

## Metrics to Track

- Query success rate
- Average analysis time
- Tool usage distribution
- User satisfaction

## Future Enhancements

- [ ] Real-time data streaming
- [ ] Predictive analytics
- [ ] Anomaly detection alerts
- [ ] Multi-file correlation
- [ ] Advanced forecasting
- [ ] Custom report templates
- [ ] Database connectors

## Example Queries

```
"What's the revenue breakdown by region?"
"Show me customer acquisition trends"
"Which product has highest profit margin?"
"Analyze customer churn patterns"
"Compare this month vs last year"
"Find customers with declining sales"
"What's our inventory turnover?"
```

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

MIT License - See [LICENSE](../LICENSE)

## Support

Open issues on GitHub.
