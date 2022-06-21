import pandas
import datetime
import random
import smtplib
import os


def create_templates():
    letters = []
    letters.append(
        open("/home/bjolie/100daysofpython/Day 32/letter_templates/letter_1.txt").read()
    )
    letters.append(
        open("/home/bjolie/100daysofpython/Day 32/letter_templates/letter_3.txt").read()
    )
    letters.append(
        open("/home/bjolie/100daysofpython/Day 32/letter_templates/letter_2.txt").read()
    )
    return letters


def send_birthday_email(letters, name, sendto):
    letter_template = random.choice(letters)
    gmail_user = os.environ.get("gmail_user")
    gmail_pass = os.environ.get("gmail_pass")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(gmail_user, gmail_pass)
    connection.sendmail(
        from_addr=gmail_user,
        to_addrs={sendto},
        msg=f"Subject:Hello\n\n{letter_template}".replace("[NAME]", name),
    )


def main():
    today = datetime.datetime.today().date()
    birthday_data = pandas.read_csv("/home/bjolie/100daysofpython/Day 32/birthdays.csv")
    dict_data = birthday_data.to_dict(orient="records")
    letter_templates = create_templates()
    for birthday in dict_data:
        year = birthday["year"]
        day = birthday["day"]
        month = birthday["month"]
        email = birthday["email"]
        name = birthday["name"]
        new_date = datetime.datetime(year, month, day).date()
        if today == new_date:
            send_birthday_email(letter_templates, name, email)


main()
