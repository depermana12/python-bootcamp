import requests
from twilio.rest import Client
import config

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=config.parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

incoming_rain = False
for hour_data in weather_data["list"]:
    weather_code = int(hour_data["weather"][0]["id"])
    if weather_code < 700:
        incoming_rain = True

if incoming_rain:
    client = Client(config.account_sid, config.auth_token)
    message = client.messages.create(
        body="It's going to rain today, remember to bring umbrella ella ella e e e ☔",
        from_=config.sender,
        to=config.receiver
    )
    print(message.status)
    print(message.sid)
    print("Umbrella ella ella e e e")