import os
from dotenv import load_dotenv
import gradio as gr
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

# Load environment variables (OpenAI API key, etc.)
load_dotenv()

# Set up the LLM once (not every time)
llm = ChatOpenAI(temperature=0.5, model="gpt-3.5-turbo", max_tokens=30) # type: ignore

# Use memory to preserve chat context
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, verbose=True, memory=memory)

##########################################################################################
# Preload a few example interactions (optional)
# conversation.predict(input="Hi! My name is Trish. I live in Hyderabad. Where do you live?")
# conversation.predict(input="I work as an SDE. What about you?")
# conversation.predict(input="What is my name and where do I live?")
# conversation.predict(input="What is my profession?")
# conversation.predict(input="I stay in Delhi and Hyderabad, India. Which is better?")

# # ---- Respond function ----
# def respond(user_input, history):
#     if not user_input:
#         return history, ""

#     reply = conversation.predict(input=user_input)
#     history = history or []
#     history.append((user_input, reply))
#     return history, ""


# # # ---- Gradio UI ----
# with gr.Blocks() as demo:
#     chatbot = gr.Chatbot()
#     state = gr.State([])  # stores chat history
#     txt = gr.Textbox(show_label=False, placeholder="Type a message and press Enter")

#     # When user presses Enter, call `respond`
#     txt.submit(respond, [txt, state], [chatbot, txt])

# demo.launch()

#new version with gradio wihth ChatInterface

# Define response function
def respond(message, history):
    reply = conversation.predict(input=message)
    return reply

# Use ChatInterface (auto handles history, UI, and clearing)
demo = gr.ChatInterface(fn=respond, title="Chat with Memory using LangChain")

demo.launch()

#############################################################################################

# # streamlit version
# import streamlit as st
# st.title("Chat with Memory using LangChain and OpenAI")
# if 'history' not in st.session_state:
#     st.session_state.history = []
# if 'input' not in st.session_state:
#     st.session_state.input = ""

# def submit():
#     if st.session_state.input:
#         reply = conversation.predict(input=st.session_state.input)
#         st.session_state.history.append((st.session_state.input, reply))
#         st.session_state.input = ""


# for user_input, reply in st.session_state.history:
#     # st.markdown(f"**You:** {user_input}")
#     # st.markdown(f"**Bot:** {reply}")
#     st.markdown(f"**🧑 You:** {user_input}")
#     st.markdown(f"**🤖 Bot:** {reply}")
#     st.markdown("---")

# st.text_input("You: ", key="input", on_change=submit)
# st.button("Submit", on_click=submit)