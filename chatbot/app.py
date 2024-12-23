from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser # default output parser

import streamlit as st
import os
from dotenv import load_dotenv; load_dotenv()

# set env variables

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# langsmith tracking
os.environ["LANGCHAIN_TRACKING_V2"] = "true"
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
openAI_LLM = ChatOpenAI(model= "gpt-3.5-turbo")

output_parser = StrOutputParser()

# define chain
chain = prompt | openAI_LLM |  output_parser

if input_text:
    st.write(
        chain.invoke(
            {
                "question" : input_text
            }
        )
    )