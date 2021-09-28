from tkinter import *

def convert():
    result_label.config(text=round(float(miles_input.get()) * 1.609, 2))

window = Tk()
window.title("Miles To Km")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles", font=("courier", 12, "bold"))
miles_label.config(padx=10, pady=10)
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to", font=("courier", 12, "bold"))
is_equal_label.grid(row=1, column=0)

result_label = Label(text="0", font=("courier", 12, "bold"))
result_label.config(padx=10, pady=10)
result_label.grid(row=1, column=1)

km_label = Label(text="Km", font=("courier", 12, "bold"))
km_label.grid(row=1, column=2)

convert_button = Button(text="Convert", command=convert)
convert_button.grid(row=2, column=1)

window.mainloop()
