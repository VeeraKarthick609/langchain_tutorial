from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langserve import add_routes

import uvicorn
import os

