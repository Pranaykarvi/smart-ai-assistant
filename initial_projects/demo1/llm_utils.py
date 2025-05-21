import os
from dotenv import load_dotenv
import requests
from openai import OpenAI, OpenAIError
import cohere

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables
openai_key = os.getenv("OPENAI_API_KEY")
cohere_key = os.getenv("COHERE_API_KEY")

# Initialize clients
client = OpenAI(api_key=openai_key)
cohere_client = cohere.Client(cohere_key)

def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        # Return None on quota error to fallback to Cohere
        if "quota" in str(e).lower():
            return None
        return f"❌ OpenAI error: {str(e)}"
    except Exception as e:
        return f"❌ OpenAI error: {str(e)}"

def query_cohere(prompt):
    try:
        response = cohere_client.generate(
    model='command',  # or 'command-small' or 'command-medium'
    prompt=prompt,
    max_tokens=100,
    temperature=0.7,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE'
)

        return response.generations[0].text.strip()
    except Exception as e:
        return f"❌ Cohere error: {str(e)}"

def smart_query(prompt):
    # First try OpenAI
    result = query_openai(prompt)
    if result is None or (result and "quota" in result.lower()):
        # Fallback to Cohere if OpenAI fails or quota exceeded
        return query_cohere(prompt)
    return result

# Quick test when running this file standalone
if __name__ == "__main__":
    test_prompt = "What is the capital of India?"
    print("Result:", smart_query(test_prompt))
