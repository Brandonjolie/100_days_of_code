import requests, os


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        flight_sheet_url = os.environ.get("sheety_flight")
        self.data = requests.get(flight_sheet_url).json()
        self.codes = self.data["prices"]
