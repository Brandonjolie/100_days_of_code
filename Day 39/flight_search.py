import os
import requests

tequila_api_key = os.environ.get("tequila_api_key")
link = f"https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=15/06/2022&dateTo=30/06/2022"
headers = {"apikey": tequila_api_key}
import pdb

data = requests.get(link, headers=headers).json()
print(data)
pdb.set_trace()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    pass
