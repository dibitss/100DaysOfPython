import os
from twilio.rest import Client
from flight_data import FlightData

class NotificationManager:
    def __init__(self) -> None:
        self.account_sid = os.environ.get("TWILIO_SID")
        self.auth_token = os.environ.get("TWILIO_TOKEN")
        self.from_phone = os.environ.get("TWILIO_FROM")
        self.to_phone = os.environ.get("TWILIO_TO")
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms(self, data: FlightData) -> None:
        body = f'''Low Price Alert! Only {data.price} GBP to fly from {data.from_city}-{data.from_airport} to {data.to_city}-{data.to_airport}, from {data.date_from} to {data.date_to}.'''
        
        self.client.messages.create(
            body=body, 
            from_=self.from_phone, 
            to=self.to_phone
            )