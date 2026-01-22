import streamlit as st
from dotenv import load_dotenv
from utils import query_agent
from pathlib import Path

# 1. Load environment variables
env_path = Path("..") / ".env"
load_dotenv(dotenv_path=env_path)

# 2. App title & instructions
st.title("CSV Analysis with AI")
st.header("Upload your CSV and ask questions about it")

# 3. File uploader
data = st.file_uploader("Upload CSV file", type="csv")

# 4. Query input
query = st.text_area("Enter your query here")

# 5. Generate response button
if st.button("Generate Response"):
    if not data:
        st.warning("Please upload a CSV file first.")
    elif not query.strip():
        st.warning("Please enter a query before generating a response.")
    else:
        # 6. Call agent
        answer = query_agent(data, query)
        # 7. Display result
        st.markdown(answer)
