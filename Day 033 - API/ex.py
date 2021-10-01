import requests
import datetime as dt
import time

PASSWORD = "CJyFs3JZ9eHwBf9bc8pMzce5e"
USER_EMAIL = "123testertesting123123@gmail.com"

LOCAL_LATITUDE = 32.164860
LOCAL_LONGITUDE = 34.844170


def iss_is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if LOCAL_LATITUDE -5 <= iss_latitude <= LOCAL_LATITUDE +5 and LOCAL_LONGITUDE -5 < iss_longitude < LOCAL_LATITUDE +5:
        return True
    
    return False


def send_email():
    import smtplib

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=USER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL, 
            to_addrs=USER_EMAIL, 
            msg=f"Subject:Look Up!\n\nThe ISS should be visible in the sky about now"
            )


def is_dark_outside():
    parameters = {
        "lat": LOCAL_LATITUDE,
        "lng": LOCAL_LONGITUDE,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

    return False

while True:
    if is_dark_outside() and iss_is_close():    
        send_email()
    
    time.sleep(60)


