import streamlit as st
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
import httpx

# --- Streamlit UI ---
st.title("LangChain App with Fallback")

question = st.text_input("Ask me something:")

if question:
    try:
        # Try Ollama first
        llm = ChatOllama(
            model="llama2",
            base_url="http://localhost:11434",  # Ollama local endpoint
        )
        response = llm.invoke(question)
        st.success("✅ Answer from Ollama:")
        st.write(response.content)

    except httpx.ConnectError:
        st.warning("⚠️ Ollama not reachable. Falling back to OpenAI...")
        # Fallback to OpenAI
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",   # or gpt-4
            temperature=0.7
        )
        response = llm.invoke(question)
        st.success("✅ Answer from OpenAI:")
        st.write(response.content)

    except Exception as e:
        st.error(f"Unexpected error: {e}")
