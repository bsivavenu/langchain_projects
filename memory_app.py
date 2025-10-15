import os
from dotenv import load_dotenv
import gradio as gr
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI

# Load environment variables (OpenAI API key, etc.)
load_dotenv()

# Set up the LLM once (not every time)
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# Use memory to preserve chat context
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, verbose=True, memory=memory)

# Preload a few example interactions (optional)
conversation.predict(input="Hi! My name is Trish. I live in Hyderabad. Where do you live?")
conversation.predict(input="I work as an SDE. What about you?")
conversation.predict(input="What is my name and where do I live?")
conversation.predict(input="What is my profession?")
conversation.predict(input="I stay in Delhi and Hyderabad, India. Which is better?")

# ---- Respond function ----
def respond(user_input, history):
    if not user_input:
        return history, ""

    reply = conversation.predict(input=user_input)
    history = history or []
    history.append((user_input, reply))
    return history, ""


# ---- Gradio UI ----
with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    state = gr.State([])  # stores chat history
    txt = gr.Textbox(show_label=False, placeholder="Type a message and press Enter")

    # When user presses Enter, call `respond`
    txt.submit(respond, [txt, state], [chatbot, txt])

demo.launch()
