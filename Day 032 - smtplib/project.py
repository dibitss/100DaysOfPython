import datetime as dt

PASSWORD = ""
USER_EMAIL = "@gmail.com"

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
def load_bdays():
    import pandas

    try:
        data = pandas.read_csv(f"/home/dibits/Repos/100DaysOfPython/Day 032 - smtplib/birthdays.csv")
    except FileNotFoundError as error:
        print("No birthdays file!")
        exit()
    else:
        return data.to_dict(orient="records")


def send_email(email, bday_letter):
    import smtplib

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=USER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=USER_EMAIL, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{bday_letter}"
            )


def write_letter(name):
    import glob, random

    chosen_template = random.choice(glob.glob("/home/dibits/Repos/100DaysOfPython/Day 032 - smtplib/letter_templates/*.txt"))
    with open(chosen_template) as templ_file:
        return templ_file.read().replace("[NAME]", name)
    

data = load_bdays()
today = (dt.datetime.now().month, dt.datetime.now().day)
for bday in data:
    bday_date = (bday.get("month"), bday.get("day"))
    if bday_date == today:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        letter = write_letter(bday.get("name"))
# 4. Send the letter generated in step 3 to that person's email address.
        send_email(bday.get("email"), letter)





