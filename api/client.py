import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']['content']


def get_llama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke",
                             json={'input': {'topic': input_text}})
    return response.json()['output']


## streamlit framework
st.title('LangChain Demo with OPENAI and OLLAMA APIs')
input_text_openai = st.text_input('Write an essay on -- calling openai')
input_text_llama = st.text_input('Write a poem on')

if input_text_openai:
    st.write(get_openai_response(input_text_openai))

if input_text_llama:
   st.write(get_llama_response(input_text_llama))
