from dotenv import load_dotenv
import streamlit as st
from user_utils import *

#Creating session variables
if 'HR_tickets' not in st.session_state:
    st.session_state['HR_tickets'] =[]
if 'IT_tickets' not in st.session_state:
    st.session_state['IT_tickets'] =[]
if 'Transport_tickets' not in st.session_state:
    st.session_state['Transport_tickets'] =[]

import os
dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, '.env')
load_dotenv(dotenv_path)


from pinecone import Pinecone

pinecone = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# Example: list indexes
print(pinecone.list_indexes())


hf_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
pinecone_key = os.environ.get("PINECONE_API_KEY", "")

if hf_key:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_key
if pinecone_key:
    os.environ["PINECONE_API_KEY"] = pinecone_key

def main():
    load_dotenv()

    st.header("Automatic Ticket Classification Tool")
    #Capture user input
    st.write("We are here to help you, please ask your question:")
    user_input = st.text_input("🔍")

    if user_input:

        #creating embeddings instance...
        embeddings=create_embeddings()
        
        
        index=pull_from_pinecone(pinecone_key,"tickets",embeddings)
        
        #This function will help us in fetching the top relevent documents from our vector store - Pinecone Index
        relavant_docs=get_similar_docs(index,user_input)

        #This will return the fine tuned response by LLM
        response=get_answer(relavant_docs,user_input)
        st.write(response)

        
        #Button to create a ticket with respective department
        button = st.button("Submit ticket?")

        if button:
            #Get Response
            
            embeddings = create_embeddings()
            query_result = embeddings.embed_query(user_input)

            #loading the ML model, so that we can use it to predit the class to which this compliant belongs to...
            department_value = predict(query_result)
            st.write("your ticket has been sumbitted to : "+department_value)

            #Appending the tickets to below list, so that we can view/use them later on...
            if department_value=="HR":
                st.session_state['HR_tickets'].append(user_input)
            elif department_value=="IT":
                st.session_state['IT_tickets'].append(user_input)
            else:
                st.session_state['Transport_tickets'].append(user_input)



if __name__ == '__main__':
    main()



