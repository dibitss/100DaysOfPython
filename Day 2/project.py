#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip = input("What percentage of tip you want to give? ")
people = int(input("How many people are splitting the bill? "))

tip_percent = float(f"1.{tip}")
bill_with_tip = total * tip_percent
each_pay = format(round(bill_with_tip / people, 2), '.2f')

print(f"Each person should pay ${each_pay}")