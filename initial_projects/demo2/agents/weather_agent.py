import requests
import os
import json

API_KEY = os.getenv("WEATHER_API_KEY", "your_key_here")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str) -> str:
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        print("Status Code:", response.status_code)  # Add this line
        print("Response Text:", response.text)       # Add this line

        response.raise_for_status()
        data = response.json()

        weather_data = {
            "city": data["name"],
            "temperature": f"{data['main']['temp']} °C",
            "condition": data["weather"][0]["description"],
            "wind": f"{data['wind']['speed']} m/s",
            "visibility": f"{data.get('visibility', 0)} meters",
            "humidity": f"{data['main']['humidity']}%"
        }

        return json.dumps(weather_data)

    except requests.exceptions.HTTPError as e:
        return f"❌ HTTP error: {str(e)}"
    except json.decoder.JSONDecodeError:
        return "❌ Received invalid JSON response."
    except Exception as e:
        return f"❌ Other error: {str(e)}"
