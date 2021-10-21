import requests
import os
import datetime as dt
from flight_data import FlightData
from notification_manager import NotificationManager

KIWI_QUERY_URL = 'https://tequila-api.kiwi.com/locations/query'
KIWI_SEARCH_URL = 'https://tequila-api.kiwi.com/v2/search'

class FlightSearch:
    def __init__(self) -> None:
        self.kiwi_key = os.environ.get("KIWI_KEY")
        self.query_url = KIWI_QUERY_URL
        self.search_url = KIWI_SEARCH_URL
        self.headers = {'apikey': self.kiwi_key, 'accept': 'application/json'}

    def get_city_codes(self, cities: list[dict]) -> str:
        for city in cities:
            if city['iataCode'] == '':
                params = {
                    'term': city['city'],
                    'limit': 1
                }

                response = requests.get(url=self.query_url, params=params, headers=self.headers)
                response.raise_for_status()
                city['iataCode'] = response.json()['locations'][0]['code']

        return cities

    def search_flights(self, cities):
        tomorrow = (dt.date.today() + dt.timedelta(days=1)).strftime('%d/%m/%Y')
        six_months = (dt.date.today() + dt.timedelta(days=6*30)).strftime('%d/%m/%Y')
        flight = FlightData()
        notifications = NotificationManager()
        
        for city in cities:
            params = {
                'fly_from': 'LON',
                'fly_to': city['iataCode'],
                'dateFrom': tomorrow,
                'date_to': six_months,
                'curr': 'GBP',
                'price_to': city['lowestPrice'],
                'max_stopovers': 0,
                'nights_in_dst_from': 7,
                'nights_in_dst_to': 28,
                'flight_type': 'round', 
                'limit': 1
            }
            
            response = requests.get(url=self.search_url, params=params, headers=self.headers)
            response.raise_for_status()

            data = response.json()
            if len(data['data']) == 0:
                continue
            else:
                data = data['data'][0]
            price = data['price']

            if float(price) < float(city['lowestPrice']):
                flight.price = price
                flight.from_city = data['cityFrom']
                flight.to_city = data['cityTo']
                flight.from_airport = data['routes'][0][0]
                flight.to_airport = data['routes'][0][1]
                flight.date_from = data['route'][0]['local_departure'].split('T')[0]
                flight.date_to = data['route'][1]['local_departure'].split('T')[0]

                notifications.send_sms(flight)