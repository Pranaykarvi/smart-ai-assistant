import streamlit as st

# Import your agents
from agents import (
    info_agent,
    summarizer_agent,
    reminder_agent,
    coder_agent,
    translator_agent
)

# Import API utilities
from utils import api_utils

# Streamlit UI
st.set_page_config(page_title="Smart AI Assistant", page_icon="🧠")
st.title("🧠 Smart AI Assistant")

# Task selection
task = st.selectbox(
    "Choose a task:",
    [
        "Q&A",
        "Summarize Text",
        "Translate Text",
        "Set Reminder",
        "Code Help",
        "Get Weather",
        "Get News"
    ]
)

# User input
user_input = st.text_area("Enter your input here:")

# Optional input (for some tasks)
if task == "Translate Text":
    target_lang = st.text_input("Target Language (e.g., fr, es, hi):", value="fr")

# Run button
if st.button("Run"):
    if not user_input and task not in ["Get News"]:
        st.warning("Please enter some input!")
    else:
        with st.spinner("Processing..."):
            try:
                if task == "Q&A":
                    st.write(info_agent.answer_question(user_input))

                elif task == "Summarize Text":
                    st.write(summarizer_agent.summarize_text(user_input))

                elif task == "Translate Text":
                    st.write(translator_agent.translate_text(user_input, target_lang))

                elif task == "Set Reminder":
                    st.write(reminder_agent.save_reminder(user_input))

                elif task == "Code Help":
                    st.write(coder_agent.solve_code(user_input))

                elif task == "Get Weather":
                    st.write(api_utils.get_weather(user_input))

                elif task == "Get News":
                    st.write(api_utils.get_news(user_input if user_input else "technology"))

            except Exception as e:
                st.error(f"An error occurred: {e}")
