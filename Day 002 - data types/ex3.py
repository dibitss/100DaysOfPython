# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

int_age = int(age)
years_left = 90 - int_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(f"You have {months_left} months, {weeks_left} weeks or {days_left} days left...")