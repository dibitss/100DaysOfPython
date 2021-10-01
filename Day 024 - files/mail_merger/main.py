#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("/home/dibits/Repos/100DaysOfPython/Day 024/mail_merger/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

for name in names:
    with open("/home/dibits/Repos/100DaysOfPython/Day 024/mail_merger/Input/Letters/starting_letter.txt") as template_file:
        template = template_file.read()

    new_template = template.replace("[name]", name.strip())
    with open(f"/home/dibits/Repos/100DaysOfPython/Day 024/mail_merger/Output/ReadyToSend/letter_to_{name}.txt", mode="w") as ready_file:
        ready_file.write(new_template)
