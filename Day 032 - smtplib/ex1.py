import smtplib
import datetime as dt
import random

PASSWORD = ""
USER_EMAIL = "@gmail.com"
RECIPIENT_EMAIL = "@gmail.com"

try:
    with open("/home/dibits/Repos/100DaysOfPython/Day 032/ex1_quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
except FileNotFoundError as error:
    print("Seems like the quotes file is missing!")
else:    
    now = dt.datetime.now().weekday()
    if now == 0:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=USER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=USER_EMAIL, 
                to_addrs=RECIPIENT_EMAIL, 
                msg=f"Subject:Friyay\n\n{random.choice(quotes)}"
                )
