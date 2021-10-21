import requests
import os

class DataManager:
    def __init__(self, sheet_url) -> None:
        self.sheety_url = sheet_url
        self.sheety_token = os.environ.get("SHEETY_TOKEN")
        self.headers = {'Authorization': f'Bearer {self.sheety_token}'}

    def get_cities(self) -> list[dict]:
        response = requests.get(url=self.sheety_url, headers=self.headers)
        response.raise_for_status()
        
        rows = response.json()
        cities = rows['prices']

        return cities

    def update_cities(self, cities: list[dict]) -> None:
        for city in cities:
            data = {
                'price': city
            }

            response = requests.put(url=f'{self.sheety_url}/prices/{city["id"]}', json=data, headers=self.headers)
            response.raise_for_status()
    
    def add_user(self, user: dict) -> None:
        response = requests.post(url=f'{self.sheety_url}/users', json=user, headers=self.headers)
        response.raise_for_status()