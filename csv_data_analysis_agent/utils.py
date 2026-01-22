from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import OpenAI
import pandas as pd
import streamlit as st

def query_agent(data, query):
    messages = []

    # 1. Read CSV safely
    try:
        df = pd.read_csv(data)
        if df.empty:
            return "The uploaded CSV is empty."
    except Exception as e:
        return f"Error reading CSV file: {e}"

    # 2. Preprocess: detect numeric and date columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    date_cols = []
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col])
            date_cols.append(col)
        except:
            continue

    # 3. Limit large CSVs
    MAX_ROWS = 5000
    if len(df) > MAX_ROWS:
        df = df.head(MAX_ROWS)
        messages.append(f"CSV has more than {MAX_ROWS} rows. Only first {MAX_ROWS} rows are processed.")

    # # 4. Create info message for user
    # messages.append(f"Available columns: {', '.join(df.columns)}\n\n")
    # if numeric_cols:
    #     messages.append(f"Numeric columns available: {', '.join(numeric_cols)}\n\n")
    # if date_cols:
    #     messages.append(f"Date columns available: {', '.join(date_cols)}\n\n")
    # if not numeric_cols:
    #     messages.append("No numeric columns available for aggregation queries (min, max, mean).")

    # 5. Create LLM agent
    llm = OpenAI()
    agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=False,
        allow_dangerous_code=True
    )

    # 6. Invoke query safely
    try:
        answer = agent.invoke(query)
    except Exception as e:
        answer = f"Error processing query: {e}"

    # 7. Return combined messages + answer
    return "\n".join(messages) + "\n\n**Query Result:**\n" + str(answer)
