import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers

#Function to get the response back
def getLLMResponse(form_input,email_sender,email_recipient,email_style):
    #llm = OpenAI(temperature=.9, model="gpt-3.5-turbo-instruct")

    # Wrapper for Llama-2-7B-Chat, Running Llama 2 on CPU

    #Quantization is reducing model precision by converting weights from 16-bit floats to 8-bit integers, 
    #enabling efficient deployment on resource-limited devices, reducing model size, and maintaining performance.

    #C Transformers offers support for various open-source models, 
    #among them popular ones like Llama, GPT4All-J, MPT, and Falcon.


    #C Transformers is the Python library that provides bindings for transformer models implemented in C/C++ using the GGML library


    llm = CTransformers(
    model='TheBloke/Mistral-7B-Instruct-v0.1-GGUF',
    model_type='mistral',
    config={'max_new_tokens': 256, 'temperature': 0.3}
)

    
    #Template for building the PROMPT
    template = """
    Write a email with {style} style and includes topic :{email_topic}.\n\nSender: {sender}\nRecipient: {recipient}
    \n\nEmail Text:
    
    """

    #Creating the final PROMPT
    prompt = PromptTemplate(
    input_variables=["style","email_topic","sender","recipient"],
    template=template,)

  
    #Generating the response using LLM
    response=llm.invoke(prompt.format(email_topic=form_input,sender=email_sender,recipient=email_recipient,style=email_style))
    print(response)

    return response


st.set_page_config(page_title="Generate Emails",
                    page_icon='📧',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Generate Emails 📧")

form_input = st.text_area('Enter the email topic', height=275)

#Creating columns for the UI - To receive inputs from user
col1, col2, col3 = st.columns([10, 10, 5])
with col1:
    email_sender = st.text_input('Sender Name')
with col2:
    email_recipient = st.text_input('Recipient Name')
with col3:
    email_style = st.selectbox('Writing Style',
                                    ('Formal', 'Appreciating', 'Not Satisfied', 'Neutral'),
                                       index=0)


submit = st.button("Generate")

#When 'Generate' button is clicked, execute the below code
if submit:
    st.write(getLLMResponse(form_input,email_sender,email_recipient,email_style))
