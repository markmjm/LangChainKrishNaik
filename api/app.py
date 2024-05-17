import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes

load_dotenv()
#
# these 2 lines are for LangSmith Tracking
LANGCHAIN_TRACING_V2 = 'true'
LANGCHAIN_PROJECT = "Tutorial_CHATBOX"
os.environ['LANGCHAIN_TRACING_V2'] = LANGCHAIN_TRACING_V2
os.environ['LANGCHAIN_PROJECT'] = LANGCHAIN_PROJECT

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)
openai_llm = ChatOpenAI()
ollama_llm = Ollama(model="gemma:2b")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about  {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about  {topic} with 100 words")

add_routes(
    app,
    prompt1 | openai_llm,
    path="/essay"
)
add_routes(
    app,
    prompt2 | ollama_llm,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
