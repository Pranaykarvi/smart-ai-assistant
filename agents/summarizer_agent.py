# agents/summarizer_agent.py

from llm_utils import smart_query

def summarize_text(text):
    prompt = f"Summarize the following text in 3-4 bullet points:\n\n{text}"
    return smart_query(prompt)
