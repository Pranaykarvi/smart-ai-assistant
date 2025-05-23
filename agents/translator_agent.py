# agents/translator_agent.py

from llm_utils import smart_query

def translate_text(text, target_language="French"):
    prompt = f"Translate the following text to {target_language}:\n\n{text}"
    return smart_query(prompt)
