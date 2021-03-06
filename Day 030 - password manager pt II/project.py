from json.decoder import JSONDecodeError
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)

    pyperclip.copy(password)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    record = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops...", message="Please complete all required fields")
    else:
        try: 
            with open("/home/dibits/Repos/100DaysOfPython/Day 030/data.json", "r") as data_file:
                existing_data = json.load(data_file)
        except (FileNotFoundError, JSONDecodeError):
            existing_data = record
        else:
            existing_data.update(record)
        finally:
            with open("/home/dibits/Repos/100DaysOfPython/Day 030/data.json", "w") as data_file:    
                json.dump(existing_data, data_file, indent=2)
        
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("/home/dibits/Repos/100DaysOfPython/Day 030/data.json", "r") as data_file:
            existing_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message="No data file found.")
    else:
        searched = existing_data.get(website)
        if searched is None:
            messagebox.showwarning(title="Oops", message=f"No record found for {website}")
        else:
            messagebox.showinfo(title=website, message=f"Email: {searched.get('email')}\nPassword: {searched.get('password')}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("???? MyPass")
window.config(padx=50, pady=50, bg="black")

image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 029/logo.png")
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
canvas.create_image(100,100,image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("courier", 16), fg="white", bg="black", padx=10)
website_label.grid(row=1, column=0)

website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)

add_button = Button(text="Search", command=search, width=16, pady=-5, padx=0)
add_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:", font=("courier", 16), fg="white", bg="black", padx=10)
email_label.grid(row=2, column=0)

email_entry = Entry(width=50)
email_entry.insert(0, "@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", font=("courier", 16), fg="white", bg="black", padx=10)
password_label.grid(row=3, column=0)

password_entry = Entry(width=33, show="*")
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", pady=-5, padx=-5, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", command=save, width=50, pady=-5, padx=0)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()