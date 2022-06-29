# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.from
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

dm = DataManager()
fs = FlightSearch()
nm = NotificationManager()

for destination in dm.codes:
    flight_data = FlightData(fs.get_flight_data(destination["iataCode"]))
    for current_booking in flight_data.flights:
        if current_booking["price"] <= destination["lowestPrice"]:
            city = destination["city"]
            arrival = current_booking["utc_arrival"]
            departure = current_booking["utc_departure"]
            msg = f"There are currently cheap flights to {city},leaving at {departure} and arriving at {arrival}"
            nm.messages.append(msg)
nm.send_messages()
