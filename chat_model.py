from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()
hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN", "")
openai_api_key = os.getenv("OPENAI_API_KEY", "")
gemini_api_key = os.getenv("GOOGLE_API_KEY", "")

if hf_api_key is not None:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key
if openai_api_key is not None:
    os.environ["OPENAI_API_KEY"] = openai_api_key
if gemini_api_key is not None:
    os.environ["GOOGLE_API_KEY"] = gemini_api_key   


st.set_page_config(page_title="Chat with LLMs", page_icon="🤖")
st.title("🤖 Chat with LLMs")

# Session state
if "session_messages" not in st.session_state:
    st.session_state.session_messages = [SystemMessage(content="You are a helpful assistant.")]

# Function to get answer
openai_chat = ChatOpenAI(model="gpt-4", temperature=0.0)

def load_answer(question):
    st.session_state.session_messages.append(HumanMessage(content=question))
    assistant_answer = openai_chat(st.session_state.session_messages)
    st.session_state.session_messages.append(AIMessage(content=assistant_answer.content))
    return assistant_answer.content

# User input
user_input = st.text_input("You: ", "", key="input")
submit = st.button("Submit")

if submit and user_input:
    output = load_answer(user_input)
    st.text_area("AI: ", value=output, height=200)
