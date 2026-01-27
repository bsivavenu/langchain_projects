import streamlit as st
from dotenv import load_dotenv
from pages.admin_utils import *


dotenv_path = os.path.join(os.path.dirname(__file__), os.pardir, '.env')
load_dotenv(dotenv_path)

hf_key = os.environ.get("HUGGINGFACEHUB_API_TOKEN", "")
pinecone_key = os.environ.get("PINECONE_API_KEY", "")

if hf_key:
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_key
if pinecone_key:
    os.environ["PINECONE_API_KEY"] = pinecone_key

import os
print("Loaded Pinecone key:", os.getenv("PINECONE_API_KEY"))


def main():
    load_dotenv()
    st.set_page_config(page_title="Dump PDF to Pinecone - Vector Store")
    st.title("Please upload your files...📁 ")

    # Upload the pdf file...
    pdf = st.file_uploader("Only PDF files allowed", type=["pdf"], accept_multiple_files=True)

    # Extract the whole text from the uploaded pdf file
    if pdf is not None:
        for single_pdf in pdf:
            with st.spinner(f'Processing {single_pdf.name}...'):
                text = read_pdf_data(single_pdf)
                st.write(f"👉 Reading {single_pdf.name} done")

                docs_chunks = split_data(text)
                st.write("👉 Splitting data into chunks done")

                embeddings = create_embeddings_load_data()
                st.write("👉 Creating embeddings instance done")

                push_to_pinecone(
                    pinecone_key,
                    index_name="tickets",
                    embeddings=embeddings,
                    docs=docs_chunks
                )


        st.success("Successfully pushed the embeddings to Pinecone")


if __name__ == '__main__':
    main()
