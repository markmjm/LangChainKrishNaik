from dotenv import load_dotenv
import streamlit as st
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
#
#these 2 lines are for LangSmith Tracking
LANGCHAIN_TRACING_V2='true'
LANGCHAIN_PROJECT="Tutorial_CHATBOX"
os.environ['LANGCHAIN_TRACING_V2'] = LANGCHAIN_TRACING_V2
os.environ['LANGCHAIN_PROJECT'] = LANGCHAIN_PROJECT


## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the user queries."),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title('LangChain Demo with OPENAI API')
input_text = st.text_input('Search the topic you want')

# openAI llm
llm = ChatOpenAI(model='gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


