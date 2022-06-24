import os
import requests
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
from_number = os.environ.get("trial_number")
to_number = os.environ.get("to_number")
api_key = os.environ.get("openweathermap")
lat = 43.8384
lon = 79.0868
link = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}&exclude=current,minutely,daily"
data = requests.get(link)
data_json = data.json()
hourly = data_json["hourly"][:12]
raining_today = False
for hour in hourly:
    weather_id = hour["weather"][0]["id"]
    if int(weather_id) < 700:
        raining_today = True
if raining_today:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an umbrella!",
        from_=from_number,
        to=to_number,
    )
