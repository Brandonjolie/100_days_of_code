import requests
import datetime

lat = 43.653225
lon = -79.383186
response = requests.get(
    f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0"
).json()["results"]
sunrise = response["sunrise"]
sunset = response["sunset"]
sunset_time = sunset.split("T")[1][:2]
sunrise_time = sunrise.split("T")[1][:2]
print(sunrise_time)

iss_data_link = "http://api.open-notify.org/iss-now.json"
