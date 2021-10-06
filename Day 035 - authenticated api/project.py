import requests
import os

def send_sms(message: str):
    from twilio.rest import Client

    account_sid = os.environ.get("TWILIO_SID")
    auth_token = os.environ.get("TWILIO_TOKEN")
    from_phone = os.environ.get("TWILIO_FROM")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        body=message,
                        from_=from_phone,
                        to=os.environ.get("TWILIO_TO")
                    )

    print(message.sid)


def get_12h_weather(lat: float, lon: float) -> list:
    api_key = os.environ.get("OWM_KEY")
    params = {
        "lat": lat, 
        "lon": lon, 
        "appid": api_key,
        "exclude": "current,minutely,daily",
    }
    url = "https://api.openweathermap.org/data/2.5/onecall"

    response = requests.get(url=url, params=params)
    response.raise_for_status()

    return response.json()["hourly"][:12]


for hour in get_12h_weather(32.164860, 34.844170):
    if hour["weather"][0]["id"] < 700:
        send_sms("It's raining man")
        break
