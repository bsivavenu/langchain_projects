import joblib
import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.callbacks import get_openai_callback

# Modern Chain & Prompt Imports
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

def pull_from_pinecone(pinecone_key, index_name, embeddings):
    # Initialize Pinecone client (v3 SDK)
    pc = Pinecone(api_key=pinecone_key)

    # Connect to index via the VectorStore partner package
    vectorstore = PineconeVectorStore.from_existing_index(
        embedding=embeddings,
        index_name=index_name
    )
    print(f"✅ Connected to Pinecone index '{index_name}'")
    return vectorstore

def create_embeddings():
    # Standard local embeddings
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def get_similar_docs(index, query, k=2):
    return index.similarity_search(query, k=k)

def get_answer(docs, user_input):
    # 1. Use ChatOpenAI (modern) instead of OpenAI (legacy)
    llm = ChatOpenAI(model="gpt-4o") 
    
    # 2. Define a prompt (REQUIRED for create_stuff_documents_chain)
    # The chain expects a '{context}' variable for documents
    prompt = ChatPromptTemplate.from_template("""
    Answer the following question using the provided context:
    <context>{context}</context>
    Question: {input}
    """)

    # 3. Create the chain
    chain = create_stuff_documents_chain(llm, prompt)

    # 4. Invoke the chain
    # Note: the input keys must match the prompt variables
    with get_openai_callback() as cb:
        response = chain.invoke({
            "context": docs,
            "input": user_input
        })
        print(f"Total Tokens: {cb.total_tokens}")

    # response is a direct string in modern stuff chains
    return response

def predict(query_result):
    # Ensure the model file exists in your directory
    Fitmodel = joblib.load('modelsvm.pkl')
    result = Fitmodel.predict([query_result])
    return result[0]