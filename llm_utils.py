# llm_utils.py

import os
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError
import cohere

# Load environment variables
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
cohere_key = os.getenv("COHERE_API_KEY")

client = OpenAI(api_key=openai_key)
cohere_client = cohere.Client(cohere_key)

def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        output = response.choices[0].message.content.strip()
        return ensure_code_wrapped(output)
    except OpenAIError as e:
        if "quota" in str(e).lower():
            return None
        return f"❌ OpenAI error: {str(e)}"
    except Exception as e:
        return f"❌ OpenAI error: {str(e)}"

def query_cohere(prompt):
    try:
        response = cohere_client.generate(
            model='command',
            prompt=prompt,
            max_tokens=400,
            temperature=0.7
        )
        return ensure_code_wrapped(response.generations[0].text.strip())
    except Exception as e:
        return f"❌ Cohere error: {str(e)}"

def smart_query(prompt):
    result = query_openai(prompt)
    if result is None or (result and "quota" in result.lower()):
        return query_cohere(prompt)
    return result

def ensure_code_wrapped(text):
    """Ensure that the response is wrapped in proper triple backtick markdown."""
    if "```" in text:
        return text  # Already wrapped
    return f"```python\n{text.strip()}\n```"
