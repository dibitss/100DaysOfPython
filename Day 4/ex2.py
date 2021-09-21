# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random

sucker = random.randint(0, len(names) -1)
# sucker = random.choice(names)
print(f'Today {names[sucker]} is paying the bill')