import requests
from datetime import datetime
import os, smtplib

MY_LAT = 43.653225  # Your latitude
MY_LONG = -79.383186  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.
def iss_compare():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    lattitude_difference = abs(iss_latitude - MY_LAT)
    longitude_difference = abs(iss_longitude - MY_LONG)
    if longitude_difference <= 5 and lattitude_difference <= 5:
        return True


def send_lookup_email():
    user = os.environ.get("gmail_user")
    passw = os.environ.get("gmail_pass")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user, passw)
    connection.sendmail(
        from_addr=user,
        to_addrs=user,
        msg="Subject:ISS Overhead\n\nLook up, the ISS is above!",
    )


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = int(str(datetime.now()).split()[1][:2])
time_now = datetime.now().hour

if time_now > sunset and time_now < sunrise:
    if iss_compare():
        send_lookup_email()
