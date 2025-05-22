import streamlit as st
import json

from agents import (
    info_agent, weather_agent, translator_agent, summarizer_agent,
    reminder_agent, system_control_agent, coder_agent, file_manager_agent,
    finance_agent, news_agent, automation_agent
)
from voice_utils import text_to_speech, speech_to_text

# Page config
st.set_page_config(page_title="🤖 Smart AI Assistant", layout="wide")
st.image("assets/assistant_avatar.jpg", width=100)
st.title("💡 Smart AI Assistant")

st.sidebar.header("🧠 Select an Agent")
agent = st.sidebar.selectbox("Agent", [
    "General Q&A", "Weather", "News", "Translation", "Summarizer",
    "Reminder", "System Control", "Coding Assistant", "File Manager",
    "Finance", "Voice Command Mode"
])

def get_input_with_voice(prompt, key="input"):
    # Initialize session state before rendering the input widget
    if key not in st.session_state:
        st.session_state[key] = ""

    col1, col2 = st.columns([4, 1])

    with col2:
        if st.button("🎙 Speak", key=f"{key}_speak"):
            spoken_text = speech_to_text()
            st.session_state[key] = spoken_text
            st.success(f"You said: {spoken_text}")

    with col1:
        user_input = st.text_input(prompt, value=st.session_state[key], key=key)

    return user_input


import streamlit as st
import html

def display_code_output(code: str):
    escaped_code = html.escape(code)  # Ensure Python code shows up literally
    st.markdown(
        f"""
        <style>
        .code-box {{
            max-height: 600px;
            overflow-y: auto;
            background-color: #f0f0f0;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #ccc;
            font-family: monospace;
            white-space: pre;
        }}
        </style>
        <div class="code-box"><pre>{escaped_code}</pre></div>
        """,
        unsafe_allow_html=True
    )


def get_textarea_with_voice(prompt, key="textarea"):
    if key not in st.session_state:
        st.session_state[key] = ""

    col1, col2 = st.columns([4, 1])

    with col2:
        if st.button("🎙 Speak", key=f"{key}_speak"):
            spoken_text = speech_to_text()
            st.session_state[key] = spoken_text
            st.success(f"You said: {spoken_text}")

    with col1:
        content = st.text_area(prompt, value=st.session_state[key], key=key)

    return content




# --- AGENT HANDLERS ---

if agent == "General Q&A":
    query = get_input_with_voice("Ask me anything:", "qa_input")
    if st.button("Submit"):
        response = info_agent.handle_info(query)
        st.text_area("Response:", response, height=150)
        text_to_speech(response)

elif agent == "Weather":
    city = get_input_with_voice("Enter a city:", "weather_input")
    if st.button("Get Weather"):
        response = weather_agent.get_weather(city)
        try:
            weather_data = json.loads(response)
            st.success(f"🌤️ Weather in {weather_data.get('city', city)}:")
            st.write(f"**Temperature:** {weather_data.get('temperature', 'N/A')}")
            st.write(f"**Condition:** {weather_data.get('condition', 'N/A')}")
            st.write(f"**Wind:** {weather_data.get('wind', 'N/A')}")
            st.write(f"**Visibility:** {weather_data.get('visibility', 'N/A')}")
            st.write(f"**Humidity:** {weather_data.get('humidity', 'N/A')}")

            speech_text = (
                f"The current weather in {weather_data.get('city', city)} is {weather_data.get('condition', 'unknown')} "
                f"with a temperature of {weather_data.get('temperature', 'unknown')}. "
                f"Wind speed is {weather_data.get('wind', 'unknown')}, visibility {weather_data.get('visibility', 'unknown')}, "
                f"and humidity is {weather_data.get('humidity', 'unknown')}."
            )
            text_to_speech(speech_text)
        except Exception as e:
            st.error("❌ Error fetching weather.")
            st.text(str(e))

elif agent == "News":
    st.info("🎤 You can speak or select a category")

    col1, col2 = st.columns([4, 1])
    with col1:
        category = st.selectbox("News Category", ["technology", "business", "science", "health", "sports"], key="news_category")
    with col2:
        if st.button("🎙 Speak", key="speak_news_cat"):
            category_voice = speech_to_text()
            if category_voice.lower() in ["technology", "business", "science", "health", "sports"]:
                st.success(f"Category set to: {category_voice}")
                category = category_voice.lower()
            else:
                st.warning("Category not recognized. Please say one of: technology, business, science, health, sports.")

    if st.button("Get News"):
        try:
            markdown_news, spoken_news = news_agent.get_news(category)
            st.markdown(markdown_news, unsafe_allow_html=True)
            text_to_speech(spoken_news)
        except Exception as e:
            st.error("❌ Error fetching news.")
            st.text(str(e))



elif agent == "Translation":
    text = get_textarea_with_voice("Text to Translate:", "translate_text")
    lang = st.selectbox("Target Language", ["French", "Hindi", "German", "Spanish"])
    if st.button("Translate"):
        response = translator_agent.translate_text(text, lang)
        st.text_area("Translated:", response, height=150)
        text_to_speech(response)

elif agent == "Summarizer":
    content = get_textarea_with_voice("Paste content to summarize:", "summarize_content")
    if st.button("Summarize"):
        response = summarizer_agent.summarize_text(content)
        st.text_area("Summary:", response, height=150)
        text_to_speech(response)

elif agent == "Reminder":
    reminder = get_input_with_voice("Set a Reminder:", "reminder_input")
    if st.button("Set"):
        response = reminder_agent.set_reminder(reminder)
        st.success(response)

    if st.button("Show Reminders"):
        reminder_list = reminder_agent.list_reminders()
        st.text_area("Reminders:", reminder_list, height=150)

elif agent == "System Control":
    action = st.radio("Select Action:", ["Shutdown", "Restart", "Sleep"])
    if st.button("Execute"):
        result = getattr(system_control_agent, action.lower())()
        st.warning(result)

elif agent == "Coding Assistant":
    code_prompt = get_textarea_with_voice("What should I code?", "code_prompt")
    lang = st.selectbox("Language", ["python", "javascript", "java", "c++"])
    if st.button("Generate Code"):
        response = coder_agent.generate_code(code_prompt, lang)
        display_code_output(response)



elif agent == "File Manager":
    directory = get_input_with_voice("Directory (default is current):", "file_dir")
    if st.button("List Files"):
        file_list = file_manager_agent.list_files(directory)
        st.text_area("Files:", file_list, height=150)

    filename = get_input_with_voice("File to delete:", "file_delete")
    if st.button("Delete File"):
        result = file_manager_agent.delete_file(filename)
        st.warning(result)

elif agent == "Finance":
    term = get_input_with_voice("Enter finance term or stock symbol:", "finance_term")
    if st.button("Explain / Get Stock Price"):
        # Check if input looks like a stock symbol (e.g., all uppercase letters, length <6)
        if term.isalpha() and term.isupper() and len(term) <= 5:
            response = finance_agent.get_stock_price(term)  # Make sure finance_agent has this method
        else:
            response = finance_agent.explain_finance_term(term)
        st.text_area("Finance Info:", response, height=300)
        text_to_speech(response)


elif agent == "Voice Command Mode":
    st.info("🎤 Say a command like 'open file explorer' or 'search AI agents on YouTube'")
    if st.button("🎧 Listen Now"):
        raw_command = speech_to_text()
        st.write(f"You said: {raw_command}")

        if raw_command:
            response = automation_agent.handle_task(raw_command)
            st.text_area("Automation Response:", response, height=150)
            text_to_speech(response)
        else:
            st.warning("Didn't catch that. Try again.")
