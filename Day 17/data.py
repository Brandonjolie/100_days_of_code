import requests, json

question_data = json.loads(requests.get("https://opentdb.com/api.php?amount=10").text)[
    "results"
]
