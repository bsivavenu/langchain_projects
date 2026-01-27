#Hello! It seems like you want to import the Streamlit library in Python. Streamlit is a powerful open-source framework used for building web applications with interactive data visualizations and machine learning models. To import Streamlit, you'll need to ensure that you have it installed in your Python environment.
#Once you have Streamlit installed, you can import it into your Python script using the import statement,

import streamlit as st
import os
from dotenv import load_dotenv

st.cache_data.clear()
st.cache_resource.clear()

from langchain_openai import OpenAI, ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_classic.memory import ConversationBufferMemory

from langchain_classic.chains import ConversationChain

load_dotenv()

hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
openai_api_key = os.getenv("OPENAI_API_KEY")
gemini_api_key = os.getenv("GOOGLE_API_KEY")

if hf_api_key is not None:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_api_key
if openai_api_key is not None:
    os.environ["OPENAI_API_KEY"] = openai_api_key
if gemini_api_key is not None:
    os.environ["GOOGLE_API_KEY"] = gemini_api_key   


@st.cache_resource
def get_llm(provider: str):
    if provider == "huggingface":

        pipe = pipeline("text-generation",
                        model="microsoft/Phi-3-mini-4k-instruct",
                        max_new_tokens=20,    # limit output length
                        temperature=0.1,
                        top_p=0.9)
        # tiiuae/falcon-1b-instruct , Qwen/Qwen2.5-0.5B-Instruct , microsoft/Phi-3-mini-4k-instruct
        return HuggingFacePipeline(pipeline=pipe)
    
    elif provider == "openai":
        # OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)
        return ChatOpenAI(model="gpt-4",temperature=0.0)

    elif provider == "gemini":
        # model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.0)
    else:
        st.error("Invalid model provider selected.")
        return None



def load_answer(question, provider):
    llm = get_llm(provider)
    if llm is None:
        return "Error: No valid language model selected."
    response = llm.invoke(question)
    return response


def load_conversation(llm):
    template = """You are a concise assistant. Answer briefly and clearly.
    
    Chat history:
    {history}
    
    Human: {input}
    Assistant:"""

    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template=template
    )

    memory = ConversationBufferMemory(memory_key="history", return_messages=False)
    

    chain = ConversationChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=False
    )
    return chain


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")
provider = st.selectbox("Choose Model", ["huggingface", "openai", "gemini"])
llm = get_llm(provider)
conversation = load_conversation(llm=llm)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Get user input
user_input = st.text_input("You: ", key="input")

# Button click
if st.button("Generate") and user_input.strip() != "":
    # Run conversation only when button is clicked
    response = conversation.run(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

for speaker, text in st.session_state.chat_history:
    st.write(f"**{speaker}:** {text}")
    # Display the bot response
