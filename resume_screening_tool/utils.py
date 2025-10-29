from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from pinecone import Pinecone
from pypdf import PdfReader
from langchain_openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain_huggingface import HuggingFaceEndpoint

import time
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

#Extract Information from PDF file
def get_pdf_text(pdf_doc):
    text = ""
    pdf_reader = PdfReader(pdf_doc)
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text



# iterate over files in 
# that user uploaded PDF files, one by one
def create_docs(user_pdf_list, unique_id):
    docs=[]
    for filename in user_pdf_list:
        
        chunks=get_pdf_text(filename)

        #Adding items to our list - Adding data & its metadata
        docs.append(Document(
            page_content=chunks,
            metadata={"name": filename.name,"id":filename.file_id,"type=":filename.type,"size":filename.size,"unique_id":unique_id},
        ))

    return docs


#Create embeddings instance
def create_embeddings_load_data():
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings


#Function to push data to Vector Store - Pinecone here
def push_to_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,docs):

    # Pinecone(
    # api_key=pinecone_apikey,
    # environment=pinecone_environment
    # )
    
        # Initialize Pinecone client
    pc = Pinecone(api_key=pinecone_apikey)

    # Create index if it does not exist
    existing_indexes = [i["name"] for i in pc.list_indexes()]
    if pinecone_index_name not in existing_indexes:
        pc.create_index(
            name=pinecone_index_name,
            dimension=384,  # match your embeddings dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print("Index created.")
    PineconeVectorStore.from_documents(docs, embeddings, index_name=pinecone_index_name)
    


#Function to pull infrmation from Vector Store - Pinecone here
def pull_from_pinecone(pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings):
    # For some of the regions allocated in pinecone which are on free tier, the data takes upto 10secs for it to available for filtering
    #so I have introduced 20secs here, if its working for you without this delay, you can remove it :)
    #https://docs.pinecone.io/docs/starter-environment
    print("20secs delay...")
    time.sleep(20)
    Pinecone(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name

    index = PineconeVectorStore.from_existing_index(index_name, embeddings)
    return index


#Function to help us get relavant documents from vector store - based on user input
def similar_docs(query,k,pinecone_apikey,pinecone_environment,pinecone_index_name,embeddings,unique_id):

    Pinecone(
    api_key=pinecone_apikey,
    environment=pinecone_environment
    )

    index_name = pinecone_index_name

    index = pull_from_pinecone(pinecone_apikey,pinecone_environment,index_name,embeddings)
    similar_docs = index.similarity_search_with_score(query, int(k),{"unique_id":unique_id})
    #print(similar_docs)
    return similar_docs


# Helps us get the summary of a document
def get_summary(current_doc):
    llm = OpenAI(temperature=0)
    #llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.3")
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    summary = chain.invoke({"input_documents": [current_doc]})

    return summary['output_text']




    