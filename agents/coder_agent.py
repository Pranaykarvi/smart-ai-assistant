# agents/coder_agent.py

from llm_utils import smart_query

def generate_code(prompt, language="python"):
    full_prompt = (
        f"You are an expert {language} developer. "
        f"Generate complete, well-documented {language} code for the following task. "
        f"Wrap the code in triple backticks using proper markdown.\n\nTask: {prompt}"
    )
    return smart_query(full_prompt)
