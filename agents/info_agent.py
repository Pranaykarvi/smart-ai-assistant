from llm_utils import smart_query

def handle_info(query: str) -> str:
    if not query.strip():
        return "⚠️ Please enter a question."

    return smart_query(query)
