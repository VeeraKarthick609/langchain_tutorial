import requests
import streamlit as st

def get_api_response(input_text, type="essay"):
    try:
        response = requests.post(
            f"http://localhost:8080/{type}/invoke",  
            json={
                "input": {
                    "topic": input_text
                }
            }
        )

        response.raise_for_status()

        return response.json().get("output", "No output returned.")

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("LangServe demo with Ollama")

essay_input_text = st.text_input("Write an essay on the topic...")
poem_input_text = st.text_input("Write a poem on the topic...")

if essay_input_text:
    st.write(get_api_response(essay_input_text, type="essay"))

if poem_input_text:
    st.write(get_api_response(poem_input_text, type="poet")) 
