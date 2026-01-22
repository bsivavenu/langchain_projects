from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks import get_openai_callback
import joblib


# #Function to pull index data from Pinecone...
# def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):

#     Pinecone(
#     api_key=pinecone_apikey,
#     environment=pinecone_environment
#     )

#     index_name = pinecone_index_name

#     index = PineconeVectorStore.from_existing_index(index_name, embeddings)
#     return index

#this is the updated function to pull index data from Pinecone (v3 SDK compatible).
def pull_from_pinecone(pinecone_key, index_name, embeddings):
    """
    Connect to an existing Pinecone index and return a PineconeVectorStore.
    Args:
        pinecone_key (str): Pinecone API key
        index_name (str): Name of Pinecone index
        embeddings: LangChain Embeddings instance
    Returns:
        vectorstore: PineconeVectorStore instance
    """
    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_key)

    # Ensure index exists
    existing_indexes = [i["name"] for i in pc.list_indexes()]
    if index_name not in existing_indexes:
        raise ValueError(f"Pinecone index '{index_name}' does not exist. Existing indexes: {existing_indexes}")

    # Connect to index
    vectorstore = PineconeVectorStore.from_existing_index(
        embedding=embeddings,
        index_name=index_name
    )

    print(f"✅ Connected to Pinecone index '{index_name}'")
    return vectorstore

def create_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings

#This function will help us in fetching the top relevent documents from our vector store - Pinecone Index
def get_similar_docs(index,query,k=2):

    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

def get_answer(docs,user_input):
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    with get_openai_callback() as cb:
        response = chain.invoke(input={'input_documents':docs, 'question':user_input})
    return response['output_text']


def predict(query_result):
    Fitmodel = joblib.load('modelsvm.pk1')
    result=Fitmodel.predict([query_result])
    return result[0]