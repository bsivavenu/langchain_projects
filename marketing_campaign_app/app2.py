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

load_dotenv(os.path.join(os.path.dirname(__file__), "..", ".env"))


def getLLMResponse(query, age_option, tasktype_option):
    # LangChain's OpenAI constructor will automatically look for the 
    # OPENAI_API_KEY in the environment variables (os.environ)
    # The ChatOpenAI class is generally preferred for "gpt-3.5-turbo" models, 
    # but since you specified "gpt-3.5-turbo-instruct," the OpenAI class is correct.
    llm = OpenAI(temperature=0.5, model="gpt-3.5-turbo-instruct")

    # --- (Your examples dictionary and conditional logic remain the same) ---
    examples = []
    if age_option == "Kid":
        # ... your Kid examples ...
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile is a magical device that fits in your pocket, like a mini-enchanted playground. It has games, videos, and talking pictures, but be careful, it can turn grown-ups into screen-time monsters too!"
            }, # ... add all your Kid examples here
            {
                "query": "What is your fear?",
                "answer": "Sometimes I'm scared of thunderstorms and monsters under my bed. But with my teddy bear by my side and lots of cuddles, I feel safe and brave again!"
            }
        ]
    elif age_option == "Adult":
        # ... your Adult examples ...
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile is a portable communication device, commonly known as a mobile phone or cell phone. It allows users to make calls, send messages, access the internet, and use various applications. Additionally, 'mobile' can also refer to a type of kinetic sculpture that hangs and moves in the air, often found in art installations or as decorative pieces."
            }, # ... add all your Adult examples here
            {
                "query": "What is your fear?",
                "answer": "Let me share with you one of my fears. It's like a shadow that lurks in the corners of my mind. It's the fear of not living up to my potential, of missing out on opportunities. But I've learned that fear can be a motivator, pushing me to work harder, take risks, and embrace new experiences. By facing my fears, I grow stronger and discover the vastness of my capabilities"
            }
        ]
    elif age_option == "Senior Citizen":
        # ... your Senior Citizen examples ...
        examples = [
            {
                "query": "What is a mobile?",
                "answer": "A mobile, also known as a cellphone or smartphone, is a portable device that allows you to make calls, send messages, take pictures, browse the internet, and do many other things. In the last 50 years, I have seen mobiles become smaller, more powerful, and capable of amazing things like video calls and accessing information instantly."
            }, # ... add all your Senior Citizen examples here
            {
                "query": "What is your fear?",
                "answer": "As an old guy, one of my fears is the fear of being alone. It's a feeling that creeps in when I imagine a world without loved ones around. But I've learned that building meaningful connections and nurturing relationships can help dispel this fear, bringing warmth and joy to my life."
            }
        ]


    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )

    prefix = """You are a {template_ageoption}, and {template_tasktype_option}: 
    Here are some examples: 
    """

    suffix = """
    Question: {template_userInput}
    Response: """
    
    # NOTE: Your imports for FewShotPromptTemplate and LengthBasedExampleSelector
    # were using old or core imports. I've updated them to the standard location 
    # for clarity, but the functionality remains the same.
    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )

    # Use the imported FewShotPromptTemplate
    new_prompt_template = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=prefix,
        suffix=suffix,
        input_variables=["template_userInput", "template_ageoption", "template_tasktype_option"],
        example_separator="\n"
    )

    final_prompt = new_prompt_template.format(
        template_userInput=query,
        template_ageoption=age_option,
        template_tasktype_option=tasktype_option
    )

    print(final_prompt)

    # The LangChain LLM class uses .invoke() for a single call
    response = llm.invoke(final_prompt)
    print(response)

    return response

# UI Starts here (The rest of your Streamlit code is correct)

st.set_page_config(page_title="Marketing Tool App2",
                     page_icon='✅',
                     layout='centered',
                     initial_sidebar_state='collapsed')
st.header("Hey, How can I help you? 🚀")

form_input = st.text_area('Enter text', height=275)

tasktype_option = st.selectbox(
    'Please select the action to be performed?',
    ('Write a sales copy', 'Create a tweet', 'Write a product description'), key=1)

age_option = st.selectbox(
    'For which age group?',
    ('Kid', 'Adult', 'Senior Citizen'), key=2)

numberOfWords = st.slider('Words limit', 1, 200, 25)

submit = st.button("Generate")

if submit:
    st.write(getLLMResponse(form_input, age_option, tasktype_option))