import requests
from twilio.rest import Client
import os


API_KEY = os.environ.get("API_KEY")
LONGITUDE = -75.626190
LATITUDE = 45.341480
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "ACf7dca9c6d5e0a4fb61d80fec0bae5413"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


response = requests.get(ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
weather_ids = [item["weather"][0]["id"] for item in weather_slice]

will_rain = False

for weather_id in weather_ids:
    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella mate!☔️",
        from_='+19285648193',
        to='+16138525167'
    )
    print(message.status)


