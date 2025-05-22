import os
import requests

API_KEY = os.getenv("FINANCE_API_KEY")
# agents/finance_agent.py

from llm_utils import smart_query # Adjust import if it's named differently

def explain_finance_term(term: str) -> str:
    prompt = (
        f"Explain the financial term '{term}' in simple, beginner-friendly language. "
        f"Provide a short explanation in 2–3 sentences with examples if relevant."
    )
    try:
        return smart_query(prompt)
    except Exception as e:
        return f"❌ Failed to generate explanation: {str(e)}"

def get_stock_price(symbol: str) -> str:
    try:
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": API_KEY
        }
        response = requests.get(url, params=params)
        data = response.json()

        if "Global Quote" not in data or not data["Global Quote"]:
            return f"❌ No data found for symbol {symbol}"

        price = data["Global Quote"].get("05. price")
        if price is None:
            return f"❌ Price data unavailable for {symbol}"

        return f"Current price of {symbol} is ${price}"

    except Exception as e:
        return f"❌ Error fetching stock price: {str(e)}"
