# agents/coder_agent.py

from llm_utils import smart_query

def generate_code(prompt, language="python"):
    full_prompt = f"Write {language} code for the following task:\n\n{prompt}"
    return smart_query(full_prompt)
