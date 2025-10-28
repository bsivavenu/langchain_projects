import streamlit as st
from utils import *
import constants
import os
from dotenv import load_dotenv

st.title('🤖 AI Assistance For Website') 

dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, '.env')
load_dotenv(dotenv_path)


# Read API keys from environment (preferred). You can set these in your .env file:
# HUGGINGFACEHUB_API_TOKEN and PINECONE_API_KEY
hf_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
pinecone_key = os.environ.get("PINECONE_API_KEY", "")

if hf_key:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_key
if pinecone_key:
    os.environ["PINECONE_API_KEY"] = pinecone_key

# Sidebar / manual load UI removed — the app now expects API keys to be available
# via environment variables (or your system environment).

# Main page Load button to push website data to Pinecone (replaces sidebar flow)
load_button = st.button("Load data to Pinecone")

if load_button:
    if hf_key != "" and pinecone_key != "":
        st.info("Loading website data and pushing to Pinecone...")
        # Fetch data from site
        site_data = get_website_data(constants.WEBSITE_URL)
        st.write(f"Fetched {len(site_data)} documents from site")

        # Split data into chunks
        chunks_data = split_data(site_data)
        st.write(f"Split into {len(chunks_data)} document chunks")

        # Create embeddings
        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")

        # Push to Pinecone
        # push_to_pinecone(pinecone_key, constants.PINECONE_ENVIRONMENT, constants.PINECONE_INDEX, embeddings, chunks_data)
        push_to_pinecone(pinecone_key, constants.PINECONE_INDEX, embeddings, chunks_data)

        st.success("Data pushed to Pinecone successfully!")
    else:
        st.error("Ooopssss!!! Please provide API keys in the environment (.env or system env).")

#Captures User Inputs
prompt = st.text_input('How can I help you my friend ❓',key="prompt")  # The box for the text prompt
document_count = st.slider('No.Of links to return 🔗 - (0 LOW || 5 HIGH)', 0, 5, 2,step=1)

submit = st.button("Search") 

if submit:
    # Proceed only if API keys are provided via environment
    if hf_key != "" and pinecone_key != "":

        # Creating embeddings instance
        embeddings = create_embeddings()
        st.write("Embeddings instance creation done...")

        # Pull index data from Pinecone

        index = pull_from_pinecone(pinecone_key, constants.PINECONE_INDEX, embeddings)

        st.write("Pinecone index retrieval done...")

        # Fetch relevant documents from Pinecone index
        relavant_docs = get_similar_docs(index, prompt, document_count)
        st.write(relavant_docs)

        # Displaying search results
        st.success("Please find the search results :")
        st.write("search results list....")
        for document in relavant_docs:
            st.write("👉**Result : " + str(relavant_docs.index(document) + 1) + "**")
            st.write("**Info**: " + document.page_content)
            st.write("**Link**: " + document.metadata['source'])
    else:
        st.error("Ooopssss!!! Please provide API keys in the environment (.env or system env).")

