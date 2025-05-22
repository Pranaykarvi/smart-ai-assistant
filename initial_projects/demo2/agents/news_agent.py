import requests
import os

API_KEY = os.getenv("NEWS_API_KEY", "b27dfadb2f004a019cf843e03051e92b")
BASE_URL = "https://newsapi.org/v2/top-headlines"

def get_news(category: str = "technology", country: str = "us", max_articles: int = 5):
    try:
        params = {
            "apiKey": API_KEY,
            "category": category,
            "country": country,
            "pageSize": max_articles
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("status") != "ok":
            error_msg = f"❌ Failed to fetch news: {data.get('message', 'Unknown error')}"
            return error_msg, error_msg

        articles = data.get("articles", [])
        if not articles:
            no_news_msg = f"No news found for category '{category}'."
            return no_news_msg, no_news_msg

        news_md = f"### 🗞️ Top {category.capitalize()} News:\n"
        news_text = f"Here are the top {category} news headlines: "

        for idx, article in enumerate(articles, 1):
            title = article.get("title", "No title")
            source = article.get("source", {}).get("name", "Unknown source")
            url = article.get("url", "#")

            news_md += f"{idx}. [{title} ({source})]({url})\n\n"
            news_text += f"News {idx}: {title} from {source}. "

        return news_md.strip(), news_text.strip()

    except Exception as e:
        error_msg = f"❌ Error while fetching news: {str(e)}"
        return error_msg, error_msg
