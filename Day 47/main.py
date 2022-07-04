import requests, pdb
from bs4 import BeautifulSoup
import smtplib
import os

gmail_user = os.environ.get("gmail_user")
gmail_pass = os.environ.get("gmail_pass")
preferred_price = 50
item_track_link = "https://www.amazon.ca/Portable-Conditioner-Personal-Humidifier-Cooling/dp/B09VNV88GC/ref=sr_1_5?crid=YOC7056JLZFL&keywords=portable+ac&qid=1656954412&sprefix=portable+ac%2Caps%2C88&sr=8-5"
headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US"}

data = requests.get(item_track_link, headers=headers)
soup = BeautifulSoup(data.text, "html.parser")
found_price = soup.find_all(name="span", class_="a-offscreen")[0].text
dollar_amount = float(found_price.split("$")[1])
if dollar_amount < preferred_price:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(gmail_user, gmail_pass)
    connection.sendmail(
        from_addr=gmail_user,
        to_addrs=gmail_user,
        msg=f"Subject:Price is within range!\n\nCurrently at ${found_price} while your maximum is {preferred_price}",
    )
    connection.close()
    print("Sent")
else:
    print("Price too high")
