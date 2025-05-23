import yfinance as yf
import wikipedia

def get_stock_price(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = stock.info

        if 'regularMarketPrice' not in info:
            return f"Could not fetch data for stock symbol '{symbol}'. Please try a valid symbol like AAPL or TSLA."

        name = info.get("longName", symbol)
        current_price = info["regularMarketPrice"]
        day_high = info.get("dayHigh", "N/A")
        day_low = info.get("dayLow", "N/A")
        open_price = info.get("open", "N/A")
        prev_close = info.get("previousClose", "N/A")
        currency = info.get("currency", "")

        return (
            f"📈 **{name} ({symbol})**\n\n"
            f"- **Current Price:** {current_price} {currency}\n"
            f"- **Open:** {open_price}\n"
            f"- **Previous Close:** {prev_close}\n"
            f"- **Day High:** {day_high}\n"
            f"- **Day Low:** {day_low}"
        )
    except Exception as e:
        return f"❌ Error fetching stock price for {symbol}: {e}"

def explain_finance_term(term):
    try:
        summary = wikipedia.summary(term, sentences=4, auto_suggest=False)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        return f"❗️The term '{term}' is ambiguous. Possible meanings include: {', '.join(e.options[:5])}"
    except wikipedia.exceptions.PageError:
        return f"❌ Could not find any information on '{term}'."
    except Exception as e:
        return f"❌ An error occurred while fetching information: {e}"
