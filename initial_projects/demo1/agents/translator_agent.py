# agents/translator_agent.py
from llm_utils import smart_query

def translate_text(text, target_lang="fr"):
    prompt = f"Translate this to {target_lang}:\n{text}"
    return smart_query(prompt)
