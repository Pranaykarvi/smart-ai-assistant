import requests

# Replace with your actual API keys
WEATHER_API_KEY = "0e56b4ad4e1b58cd59cb51acd8bfd9a3"
NEWS_API_KEY = "b27dfadb2f004a019cf843e03051e92b"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "main" not in data:
        return "Could not retrieve weather data."

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    return f"🌤️ Weather in {city.title()}: {weather}, {temp}°C (feels like {feels_like}°C)."

def get_news(topic="technology"):
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWS_API_KEY}&pageSize=3"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200 or "articles" not in data:
        return "Could not retrieve news."

    articles = data["articles"]
    summaries = [f"📰 {article['title']} - {article['url']}" for article in articles]
    return "\n".join(summaries)
