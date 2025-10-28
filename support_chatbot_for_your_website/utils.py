import os
import asyncio
import pinecone

# Use the canonical LangChain import paths
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Pinecone as PineconeVectorStore
from langchain.document_loaders import SitemapLoader
from langchain_community.vectorstores import Pinecone
import constants
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore


from pinecone import Pinecone
pc = Pinecone(os.environ.get("PINECONE_API_KEY", ""))

#Function to fetch data from website
# https://python.langchain.com/docs/integrations/document_loaders/sitemap/
# here we are passing a limit value of 5 so that we dont end up getting every link as its just a demo project
def get_website_data(sitemap_url, limit=5):

    # SitemapLoader is synchronous in many LangChain versions; keep a new event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loader = SitemapLoader(sitemap_url)

    docs = loader.load()
    return docs[:limit]

#Function to split data into smaller chunks
def split_data(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )

    docs_chunks = text_splitter.split_documents(docs)
    return docs_chunks

#Function to create embeddings instance
def create_embeddings():
    # Create HuggingFace embeddings. Ensure HUGGINGFACEHUB_API_TOKEN is set in env.
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings



from pinecone import Pinecone, ServerlessSpec
#this is the updated function to push documents to Pinecone index (v3 SDK compatible).

def push_to_pinecone(pinecone_key, index_name, embeddings, docs):
    """
    Push a list of documents (docs) to Pinecone using LangChain PineconeVectorStore.
    Args:
        pinecone_key (str): Your Pinecone API key
        index_name (str): Name of the Pinecone index
        embeddings: LangChain Embeddings instance
        docs (list): List of LangChain Document objects
    Returns:
        vectorstore: PineconeVectorStore instance
    """
    # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_key)

    # Create index if it does not exist
    existing_indexes = [i["name"] for i in pc.list_indexes()]
    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=1536,  # match your embeddings dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print("Index created.")

    # Push documents to Pinecone
    vectorstore = PineconeVectorStore.from_documents(documents=docs, embedding=embeddings, index_name=index_name)

    print(f"✅ Pushed {len(docs)} documents to Pinecone index '{index_name}'")
    return vectorstore



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

#This function will help us in fetching the top relevent documents from our vector store - Pinecone Index
def get_similar_docs(index,query,k=2):

    # LangChain Pinecone wrappers expose `similarity_search` or `similarity_search_with_score`;
    # use similarity_search for compatibility with the app.
    similar_docs = index.similarity_search(query, k=k)
    return similar_docs

