import os
import json
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Get the directory where this script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build path to config.json in the same directory
config_path = os.path.join(current_dir, "config.json")

# Debug print to check path
# st.write(f"Loading config from: {config_path}")

# Load API key
with open(config_path) as f:
    config = json.load(f)

GROQ_API_KEY = config.get("GROQ_API_KEY")

# Initialize the Groq model
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama3-8b-8192")

# Chatbot prompt template
template = PromptTemplate.from_template("""
You are a helpful health assistant. Answer the user's health-related question concisely and accurately.

Question: {question}
""")

# Streamlit UI
st.title("🩺 Health Chatbot + Navigation")

# Chat input
user_input = st.text_input("Ask your health question:")
if user_input:
    prompt = template.format(question=user_input)
    response = llm.invoke(prompt)
    st.markdown("**Response:**")
    st.write(response.content)

# Navigation Buttons
st.markdown("---")
st.subheader("Explore our Health Tools")
col1, col2, col3 = st.columns(3)

import streamlit.components.v1 as components

with col1:
    st.markdown(
        '<a href="https://huggingface.co/spaces/Supriyas-04/diet-workout" target="_blank">'
        '<button style="width: 100%;">🏋️ Diet & Workout</button></a>',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        '<a href="https://stress-management.streamlit.app/" target="_blank">'
        '<button style="width: 100%;">🧘 Stress Management</button></a>',
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        '<a href="https://huggingface.co/spaces/Supriyas-04/medico_ai" target="_blank">'
        '<button style="width: 100%;">💊 Medicine Recommender</button></a>',
        unsafe_allow_html=True,
    )
