import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# UI layout
st.set_page_config(page_title="Motivational Chatbot", page_icon="💬")
st.title("💬 🌟 Your Motivational Chatbot ")
st.write("Type something you're struggling with or need advice on:")

# Input from user
user_input = st.text_input("You:", "")

if user_input:
    prompt = f"Give a short motivational message or advice for: {user_input}"
    
    try:
        response = model.generate_content(prompt)
        st.success(response.text)
    except Exception as e:
        st.error("Something went wrong. Check your API key or internet connection.")
        st.exception(e)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Gemini API")
