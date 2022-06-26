import requests, os

user_endpoint = "https://pixe.la/v1/users"
key = os.environ.get("pixela_api_key")
user = os.environ.get("pixela_api_user")
headers = {"X-USER-TOKEN": user}
graph_endpoint = f"{user_endpoint}/{user}/graphs"
graph_parameters = {
    "id": "graphsatu",
    "name": "Coding Marathon",
    "unit": "hour",
    "type": "float",
    "color": "ajisai",
    "timezone": "Europe/Amsterdam",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
paras = {
    "token": key,
    "username": user,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

data = requests.post(
    user_endpoint,
    json=graph_parameters,
    headers=headers,
)
print(data.text)
