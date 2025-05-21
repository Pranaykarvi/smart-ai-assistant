# agents/coder_agent.py
from llm_utils import smart_query

def solve_code(query):
    prompt = f"Write Python code for the following task:\n{query}"
    return smart_query(prompt)
