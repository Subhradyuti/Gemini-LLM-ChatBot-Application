import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Generative AI with API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    try:
        response = chat.send_message(question, stream=True)
        return response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return []

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Text input and button for user interaction
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask the question")
clear = st.button("Clear Chat")

# Handle submit button
if submit and input_text:
    response = get_gemini_response(input_text)
    if response:
        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("The Response is")
        response_text = "".join([chunk.text for chunk in response])
        st.write(response_text)
        st.session_state['chat_history'].append(("Bot", response_text))

# Handle clear button
if clear:
    st.session_state['chat_history'] = []

# Display chat history
st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
