from pypdf import PdfReader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAI
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
import pandas as pd
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

import os
dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, '.env')
load_dotenv(dotenv_path)
import os
print("Loaded Pinecone key:", os.getenv("PINECONE_API_KEY"))


hf_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
pinecone_key = os.environ.get("PINECONE_API_KEY", "")

if hf_key:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_key
if pinecone_key:
    os.environ["PINECONE_API_KEY"] = pinecone_key

#**********Functions to help you load documents to PINECONE************

#Read PDF data
def read_pdf_data(pdf_file):
    pdf_page = PdfReader(pdf_file)
    text = ""
    for page in pdf_page.pages:
        text += page.extract_text()
    return text

#Split data into chunks
def split_data(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
    docs = text_splitter.split_text(text)
    docs_chunks =text_splitter.create_documents(docs)
    return docs_chunks

#Create embeddings instance
def create_embeddings_load_data():
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#Function to push data to Pinecone
# def push_to_pinecone(pinecone_apikey,pinecone_index_name,embeddings,docs):

#     Pinecone(
#     api_key=pinecone_apikey,
#     environment="us-east-1"
#     )

#     pc = Pinecone(api_key=pinecone_key)

#     # Create index if it does not exist
#     existing_indexes = [i["name"] for i in pc.list_indexes()]
#     if pinecone_index_name not in existing_indexes:
#         pc.create_index(
#             name=pinecone_index_name,
#             dimension=384,  # match your embeddings dimension
#             metric="cosine",
#             spec=ServerlessSpec(cloud="aws", region="us-east-1")
#         )
#         print("Index created.")
#         index_name = pinecone_index_name

#     index = PineconeVectorStore.from_documents(docs, embeddings, index_name=pinecone_index_name)
#     return index

def push_to_pinecone(pinecone_key, index_name, embeddings, docs):
    """
    Push a list of documents (docs) to Pinecone using LangChain PineconeVectorStore.
    Compatible with latest Pinecone SDK (2025+).
    """


    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_key)

    # Fetch existing index names (new SDK returns an object, not list of dicts)
    existing_indexes = [idx.name for idx in pc.list_indexes()]

    # Create index if not exists
    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=384,  # dimension of all-MiniLM-L6-v2 embeddings
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print(f"🆕 Created Pinecone index '{index_name}'")

    # Push docs to Pinecone
    vectorstore = PineconeVectorStore.from_documents(
        documents=docs,
        embedding=embeddings,
        index_name=index_name
    )

    print(f"✅ Pushed {len(docs)} documents to Pinecone index '{index_name}' successfully.")
    return vectorstore




#*********Functions for dealing with Model related tasks...************

#Read dataset for model creation
def read_data(data):
    df = pd.read_csv(data,delimiter=',', header=None)  
    return df

#Create embeddings instance
def get_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#Generating embeddings for our input dataset
def create_embeddings(df,embeddings):
    df[2] = df[0].apply(lambda x: embeddings.embed_query(x))
    return df

#Splitting the data into train & test
def split_train_test__data(df_sample):
    # Split into training and testing sets
    sentences_train, sentences_test, labels_train, labels_test = train_test_split(
    list(df_sample[2]), list(df_sample[1]), test_size=0.25, random_state=0)
    print(len(sentences_train))
    return sentences_train, sentences_test, labels_train, labels_test

#Get the accuracy score on test data
def get_score(svm_classifier,sentences_test,labels_test):
    score = svm_classifier.score(sentences_test, labels_test)
    return score
