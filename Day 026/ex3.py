with open("/home/dibits/Repos/100DaysOfPython/Day 026/ex3_file1.txt") as f1, open("/home/dibits/Repos/100DaysOfPython/Day 026/ex3_file2.txt") as f2:
    n1 = f1.readlines()
    n2 = f2.readlines()

result = [int(n.strip()) for n in n1 if n in n2]

# Write your code above 👆

print(result)
