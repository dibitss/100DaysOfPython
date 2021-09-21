# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

true = 0
love = 0

names = (name1 + name2).lower()

true += names.count("t") + names.count("r") + names.count("u") + names.count("e")
love += names.count("l") + names.count("o") + names.count("v") + names.count("e")

true_love = int(str(true) + str(love))

if (true_love < 10) or (true_love > 90):
    print(f"Your score is {true_love}, you go together like coke and mentos")
elif (true_love >= 40) and (true_love <= 50):
    print(f"Your score is {true_love}, you are alright together")
else:
    print(f"Your score is {true_love}")