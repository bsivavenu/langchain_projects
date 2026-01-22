import os
from dotenv import load_dotenv, find_dotenv
import streamlit as st

# Core component imports
from langchain_core.prompts import PromptTemplate 
from langchain_core.prompts import FewShotPromptTemplate # Use langchain_core for FewShotPromptTemplate
from langchain_core.example_selectors import LengthBasedExampleSelector # Use langchain_core for selectors

# LLM imports
from langchain_openai import OpenAI
# from langchain_openai import ChatOpenAI # Unused, but correct path if needed



load_dotenv(find_dotenv())


######################################################################################################################

from langchain_openai import ChatOpenAI
def getLLMResponse(query,age_option,tasktype_option):

    llm = OpenAI(temperature=0.5, model="gpt-3.5-turbo-instruct")


    # if age_option=="Kid":  
    # example_template = """
    # Question: {query}
    # Response: {answer}
    # """

    template = """
    You are a {age_option} who needs to {tasktype_option}.
    Respond naturally in the tone, vocabulary, and emotion suitable for that age group.
    
    User Input: {query}
    """

    # example_prompt = PromptTemplate(
    #     input_variables=["query", "answer"],
    #     template=example_template
    # )


    # prefix = """You are a {template_ageoption}, and {template_tasktype_option}: 
    # Here are some examples: 
    # """

    # suffix = """
    # Question: {template_userInput}
    # Response: """

    # example_selector = LengthBasedExampleSelector(
    #     examples=examples,
    #     example_prompt=example_prompt,
    #     max_length=200
    # )


    new_prompt_template = PromptTemplate(
        # example_selector=example_selector,  # use example_selector instead of examples
        # example_prompt=example_prompt,
        input_variables=["query",  "age_option", "tasktype_option"],
        template=template
    )
    final_prompt = new_prompt_template.format(
                    query=query,
                    age_option=age_option, 
                    tasktype_option=tasktype_option
                    )
    #     prefix=prefix,
    #     suffix=suffix,
    #     input_variables=["template_userInput","template_ageoption","template_tasktype_option"],
    #     example_separator="\n"
    # )

  
    # print(new_prompt_template.format(template_userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option))
    response=llm.invoke(final_prompt)
    print(final_prompt)
    print(response)

    return response


st.set_page_config(page_title="Marketing Tool App",
                    page_icon='✅',
                    layout='centered',
                    initial_sidebar_state='collapsed')
st.header("Hey, How can I help you?")

form_input = st.text_area('Enter text', height=275)

tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('Write a sales copy', 'Create a tweet', 'Write a product description'),key=1)

age_option= st.selectbox(
    'For which age group?',
    ('Kid', 'Adult', 'senior Citizen'),key=2)

numberOfWords= st.slider('Words limit', 1, 200, 25)

submit = st.button("Generate")

if submit:
    st.write(getLLMResponse(form_input,age_option,tasktype_option))
