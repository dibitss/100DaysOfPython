import requests

url = "https://opentdb.com/api.php"

params = {
    "amount": 100,
    "type": "boolean"
}

question_data = requests.get(url=url, params=params).json()["results"]