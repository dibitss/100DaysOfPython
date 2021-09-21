# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f"Your bmi is {bmi} and you are too light")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you good")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you kinda fat")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are really fat")
else:
    print(f"Your bmi is {bmi}, yo mama so fat... she's you!")