import os
from langchain_ollama import ChatOllama
import streamlit as st

llm = ChatOllama(model="llama2",
    base_url="http://localhost:11434")

st.title("Ask anything")

question = st.text_input("Enter your question")


if question:
        response = llm.invoke(question)
        st.write(response.content)
