import os
from dotenv import load_dotenv; load_dotenv()

def load_env_variables():
    """A function to load environment variables"""
    # langsmith tracking
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")