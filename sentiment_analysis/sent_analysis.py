import openai
import streamlit as st 
from pathlib import Path 
import configparser


openai.api_key = ""

def get_response_from_chatGPT(text):
    prompt = f"Identify and return either positive or negative in give text. text: {text}"
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {"role": "system", "content": "You are a helpful sentiment analyzer that returns consise sentiments"},
            {"role": "user", "content": prompt}
        ],
        temperature = 0.1
    )

    sentiment = response['choices'][0]['message']['content']
    return sentiment

st.title("ChatGPT Text Sentiment Analyzer")
model = 'gpt-3.5-turbo'
text = st.text_input("Enter Text: ", value="I love to read AI Books")

if st.button('Submit'):
    with st.spinner("OpenAI processing in Progress"):
        sentiment = get_response_from_chatGPT(text)
        st.success("OpenAI Processing Complete")

    st.write(f"Sentiment: {sentiment}")
    # Dispalying the sentiment