# 🤖 Smart AI Assistant

An all-in-one, voice-activated AI assistant built with Python and Streamlit — designed to handle everyday tasks like question answering, fetching news and weather, translating, summarizing, managing finances, and automating your workflow. Powered by OpenAI's GPT-4 and multiple public APIs.

---

## 🧠 Key Highlights

### 🔊 Voice Command Mode *(Flagship Feature)*
Interact with the assistant completely hands-free. Just **speak** and let it:
- Answer your queries
- Fetch latest news or weather
- Summarize long content
- Translate across languages
- Execute automation tasks (like opening YouTube, Google, system apps)

### 💬 General Q&A Agent
Ask anything — educational, technical, factual, or conversational.  
> **Powered by:** OpenAI GPT-4 API

### 🌦️ Weather Agent
Get real-time weather data like temperature, humidity, and condition.
> **Powered by:** [OpenWeatherMap API](https://openweathermap.org/api)

### 📰 News Agent
Get trending headlines by topic or category — like business, tech, sports.
> **Powered by:** [NewsAPI](https://newsapi.org)

### 🌍 Translation Agent
Translate any text to 100+ languages with voice-enabled input.
> **Powered by:** `googletrans` (Google Translate unofficial wrapper)

### ✂️ Summarizer Agent
Shorten long paragraphs or documents with GPT-powered summarization.
> **Powered by:** OpenAI GPT-4 API

### 💹 Finance Agent
Track live stock prices and financial data using ticker symbols.
> **Powered by:** `yfinance` (Yahoo Finance)

---

## 🧩 Additional Agents (Fully Functional & Ready to Use)

These agents are included and operational, even if not demoed visually:

| Agent | Functionality |
|-------|---------------|
| ⏰ **Reminder Agent** | Create time-based reminders |
| 🧹 **Automation Agent** | Open websites, perform voice-driven searches |
| 🧠 **Coding Assistant** | Generate, explain or debug code using GPT |
| 🖥️ **System Control Agent** | Open apps, adjust volume, shutdown/restart PC |
| 📁 **File Manager Agent** | Browse, rename, delete local files via voice |
| 📊 **Data Analysis Agent** *(WIP)* | Summarize CSVs, generate plots |

---

## ⚙️ Technologies & Architecture

| Layer | Technologies Used |
|-------|-------------------|
| 🧠 LLM | OpenAI GPT-4 |
| 🧑‍💻 Backend | Python |
| 🎛️ UI | Streamlit |
| 🎙️ Voice Input | `speech_recognition`, `pyaudio` |
| 🔊 Voice Output | `pyttsx3` |
| 📡 APIs | OpenWeatherMap, NewsAPI, yfinance, googletrans |
| 🛠️ Utils | `webbrowser`, `os`, `datetime`, `dotenv` |

**Modular Agent Structure**
```
├── app.py
├── agents/
│ ├── coder_agent.py
│ ├── finance_agent.py
│ ├── news_agent.py
│ ├── weather_agent.py
│ ├── summarizer_agent.py
│ ├── translator_agent.py
│ ├── reminder_agent.py
│ ├── file_manager_agent.py
│ └── automation_agent.py
├── voice_utils.py
├── llm_utils.py
├── auto_start.py
├── .env
├── requirements.txt
```


---

## 🚀 Getting Started

### 📦 Prerequisites
- Python 3.8+
- Internet connection
- OpenAI API Key
- NewsAPI key
- OpenWeatherMap API key

### 🛠️ Installation
```bash
git clone https://github.com/yourusername/smart-ai-assistant.git
cd smart-ai-assistant
pip install -r requirements.txt
```
**Create a .env file in the root directory with your API keys:**
```
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_openweather_api_key
NEWS_API_KEY=your_newsapi_key
```

**Run the App**

```
streamlit run app.py
```

## How It Works
- app.py routes all inputs (typed or voice) to appropriate agents.

- Agents process the task using LLMs or APIs.

- Voice is captured using SpeechRecognition; responses are spoken via pyttsx3.

- Outputs are shown in a clean UI with copyable blocks, summaries, charts or audio.
---
## Use Cases
- Ask trivia, definitions, or code help

- Translate a sentence to German

- “What’s the weather in Tokyo?”

- “Summarize this long email”

- “Open YouTube and search for smart AI demos”
---

## 🔐 Security Notes
- API keys are loaded from environment variables (.env)

- Voice recordings are not saved

- All requests are processed locally (except LLM/API calls)
---

## 📽️ Demo Video
Check out the video walkthrough on [LinkedIn](https://www.linkedin.com/feed/update/urn:li:activity:7331699541068410881/)
---


## 🗺️ Roadmap
- Modular agent architecture

 - Voice command system

 - Weather, news, translation, summarizer, finance agents

-  Streamlit-based UI

-  Deployment to HuggingFace/Streamlit Cloud (pending)

- GUI mobile companion (pending)

- Chrome extension (pending)
---

## 🤝 Contributions
Open to contributors! Feel free to fork, add agents, or improve existing ones.
Suggestions and PRs are highly appreciated.

## 📝 License
This project is licensed under the MIT License.

