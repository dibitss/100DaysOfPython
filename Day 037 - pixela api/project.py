import requests
from requests.api import head
from requests.models import Response
import datetime as dt

USER_NAME = "ausername"
TOKEN = "atoken"
GRAPH_NAME = "cycling"
PIXELA_URL = "https://pixe.la/v1/users"
GRAPH_URL = f"{PIXELA_URL}/{USER_NAME}/graphs"
PIXEL_URL = f"{GRAPH_URL}/{GRAPH_NAME}"

headers = {
    "X-USER-TOKEN": TOKEN
}


def create_user():
    params = {
        "token": TOKEN, 
        "username": USER_NAME, 
        "agreeTermsOfService": "yes", 
        "notMinor": "yes"
        }

    response = requests.post(url=PIXELA_URL, json=params)
    response.raise_for_status()
    print(response.text)


def create_graph():
    graph_params = {
        "id": GRAPH_NAME,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "kuro"
    }
    
    response = requests.post(url=GRAPH_URL, json=graph_params, headers=headers)
    response.raise_for_status()
    print(response.text)


def create_pixel(date, amount, destination):
    pixel_params = {
        "date": date,
        "quantity": amount,
        "optionalData": '{\"Destination\": \"%s\"}' % destination
    }

    response = requests.post(url=PIXEL_URL, json=pixel_params, headers=headers)
    response.raise_for_status()
    print(response.text)


def update_pixel(date, amount, destination):
    pixel_params = {
        "date": date,
        "quantity": amount,
        "optionalData": '{\"Destination\": \"%s\"}' % destination
    }

    response = requests.put(url=f"{PIXEL_URL}/{date}", json=pixel_params, headers=headers)
    response.raise_for_status()
    print(response.text)


def delete_pixel(date):
    response = requests.delete(url=f"{PIXEL_URL}/{date}", headers=headers)
    response.raise_for_status()
    print(response.text)


today = dt.date.today().strftime("%Y%m%d")
# create_user()
# create_graph()
create_pixel(today, "20", "Kfar Saba")
update_pixel(today, "30", "Kfar Saba")
# delete_pixel(today)