import os
import requests
import datetime
from dateutil.relativedelta import relativedelta


today = datetime.date.today()
six_months = today + relativedelta(months=+6)


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        tequila_api_key = os.environ.get("tequila_api_key")
        self.headers = {"apikey": tequila_api_key}
        self.today_date = today.strftime("%d/%m/%Y")
        self.six_month_date = six_months.strftime("%d/%m/%Y")

    def get_flight_data(self, destination_code):
        link = f"https://tequila-api.kiwi.com/v2/search?fly_from=YYZ&fly_to={destination_code}&dateFrom={self.today_date}&dateTo={self.six_month_date}&limit=5"
        flights = requests.get(link, headers=self.headers).json()["data"]
        return flights
