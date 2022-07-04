import smtplib
import os
import datetime, random


def send_motivational_email():
    data = []
    with open("/home/bjolie/100daysofpython/Day 32/quotes.txt") as quotes_file:
        data = quotes_file.readlines()
    quote = random.choice(data)
    gmail_user = os.environ.get("gmail_user")
    gmail_pass = os.environ.get("gmail_pass")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(gmail_user, gmail_pass)
    connection.sendmail(
        from_addr=gmail_user,
        to_addrs=gmail_user,
        msg=f"Subject:Hello\n\n{quote}",
    )
    connection.close()


current_day = datetime.datetime.today().weekday()
if current_day == 1:
    send_motivational_email()
