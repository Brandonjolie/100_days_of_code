import os, requests
from twilio.rest import Client
import pdb
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday
alpha_api_key = os.environ.get("alpha_api_key")
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={alpha_api_key}"
data = requests.get(stock_url).json()
daily_data = data["Time Series (Daily)"]
today = datetime.today()
yesterday = today - timedelta(days=1)
yesterday_2 = today - timedelta(days=2)
yesterdays_date = yesterday.strftime("%Y-%m-%d")
yesterday_2s_date = yesterday_2.strftime("%Y-%m-%d")
yesterday_closing = float(daily_data[yesterdays_date]["4. close"])
yesterday_2_closing = float(daily_data[yesterday_2s_date]["4. close"])
difference_between_days = (
    abs(yesterday_closing - yesterday_2_closing) / yesterday_2_closing
) * 100
difference_between_days = round(difference_between_days, 2)

# Get the first 3 news pieces for the COMPANY_NAME.
if difference_between_days < 5:
    news_api_key = os.environ.get("news_api_key")
    data_link = (
        f"https://newsapi.org/v2/top-headlines?q={COMPANY_NAME}&apiKey={news_api_key}"
    )
    news_data = requests.get(data_link).json()["articles"][:3]
    news_str = ""
    for article in news_data:
        title = article["title"]
        description = article["description"]
        news_str += f"Title: {title}\nDescription: {description}\n"

    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    from_number = os.environ.get("trial_number")
    to_number = os.environ.get("to_number")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {difference_between_days}% change\n{news_str}",
        from_=from_number,
        to=to_number,
    )
