from data_manager import DataManager
from flight_search import FlightSearch

SHEETY_URL = 'https://api.sheety.co/3c9cc72dc36fd2fcdbb629fc6331e141/copyOfFlightDeals'

searcher = FlightSearch()
sheet = DataManager(sheet_url=SHEETY_URL)
user = {}

print('Welcome to dibitss\' Flight Club.\nWe find the best flight deals and email you.')
user['firstname'] = input('What\'s your first name?\n')
user['lastName'] = input('What\'s your last name?\n')
email_verif = ''
user['email'] = ''
while email_verif == '' or email_verif != user['email']:
    user['email'] = input('What\'s your email?\n')
    email_verif = input('Type your email again.\n')
sheet.add_user(user)
print('You\'re in the club!')


# Get cities from sheet
cities = sheet.get_cities()
# Find IATA codes
cities_with_codes = searcher.get_city_codes(cities)
# Update IATA codes in sheet
sheet.update_cities(cities_with_codes)
# Get updated cities from sheet
cities = sheet.get_cities()
# Search for flights
searcher.search_flights(cities)