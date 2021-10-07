import requests
import os
import datetime as dt

NUTRITIONIX_URL = 'https://trackapi.nutritionix.com'
NUTRITIONIX_EXERCISE_ENDPOINT = '/v2/natural/exercise'

SHEETY_URL = 'https://api.sheety.co/3c9cc72dc36fd2fcdbb629fc6331e141/myWorkouts/workouts'


def get_activity_data(query: str) -> None:
    headers = {
        'x-app-id': os.environ.get('APP_ID'),
        'x-app-key': os.environ.get('API_KEY'),
        'x-remote-user-id': '0'
    }

    data = {
        'query': query
    }
    
    now = dt.datetime.now()
    date = now.strftime('%d/%m/%Y')
    time = now.strftime('%X')

    response = requests.post(url=f'{NUTRITIONIX_URL}{NUTRITIONIX_EXERCISE_ENDPOINT}', data=data, headers=headers)
    response.raise_for_status()
    for exercise in response.json()["exercises"]:
        row = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': exercise['name'].title(),
                'duration': exercise['duration_min'],
                'calories': exercise['nf_calories']
            }
        }
        write_to_sheet(row)

def write_to_sheet(row: dict) -> None:
    headers = {
        'Authorization': f'Bearer {os.environ.get("SHEETY_TOKEN")}',
        # 'Content-Type': 'application/json'
    }

    response = requests.post(url=SHEETY_URL, json=row, headers=headers)
    print(response.text)
    response.raise_for_status()

get_activity_data(input('What sports did you do today? '))