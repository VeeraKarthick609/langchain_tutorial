from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_community.llms.ollama import Ollama
from langserve import add_routes

import uvicorn
import os

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple Langchain Server"
)

add_routes(
    app, 
    Ollama(),
    path="/gemma"
)

model = Ollama(model="gemma")

prompts = [
    ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                "You are a poet, please respond to user queries"
            ),
            HumanMessagePromptTemplate.from_template(
                "Question:{question}"
            )
        ]
    ),
    ChatPromptTemplate.from_messages(
        [
            SystemMessagePromptTemplate.from_template(
                "You are a story writer, please respond to user queries"
            ),
            HumanMessagePromptTemplate.from_template(
                "Question:{question}"
            )
        ]
    ),
]

add_routes(app, (prompts[0] | model), path="/poet")
add_routes(app, (prompts[1] | model), path="/essay")


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="localhost",
        port=8080,
        log_level="debug"
    )
