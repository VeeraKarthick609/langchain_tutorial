from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser # default output parser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv; load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))


# langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template(
            "You are a helpful assistant please respond to user queries"
        ),
        HumanMessagePromptTemplate.from_template(
            "Question:{question}"
        )
    ]
)

# streamlit app

st.title("Langchain ChatBot")
input_text = st.text_input("Search what you doubt about...")

# LLM
ollama_LLM = ollama.Ollama(model= "gemma")

output_parser = StrOutputParser()

# define chain
chain = prompt | ollama_LLM |  output_parser

if input_text:
    st.write(
        chain.invoke(
            {
                "question" : input_text
            }
        )
    )

