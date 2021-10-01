from tkinter import *
from tkinter import messagebox
import random
import json
import pandas
from pandas.core.frame import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

NEW_LANGUAGE = "Hebrew"
NATIVE_LANGUAGE = "English"

DEFAULT_TIMER = 3

timer = None
new_random_word = ""

def load_words():
    '''
    Load words from file
    '''

    try:
        data = pandas.read_csv(f"/home/dibits/Repos/100DaysOfPython/Day 031/data/{NEW_LANGUAGE.lower()}_words_to_learn.csv")
    except FileNotFoundError as error:
        data = pandas.read_csv(f"/home/dibits/Repos/100DaysOfPython/Day 031/data/{NEW_LANGUAGE.lower()}_words.csv")
    finally:
        return data.to_dict(orient="records")

def save_words():
    '''
    Save "to learn" words to file.
    '''

    data = DataFrame(words)
    data.to_csv(f"/home/dibits/Repos/100DaysOfPython/Day 031/data/{NEW_LANGUAGE.lower()}_words_to_learn.csv", index=False)
    
def reverse(word):
    '''
    Returns a string reversed.
    '''

    return ' '.join(string[::-1] for string in word.split())


def new_word():
    ''' 
    Get a new random word.
    '''

    try:
        random_word = random.choice(words)
    except IndexError:
        return None
    else:
        return random_word
    

def flip_card():
    '''
    Count down from specified count. Flips cards at the end of the count.
    '''
    
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(title_label, text=NATIVE_LANGUAGE, fill="white")
    canvas.itemconfig(word_label, text=new_random_word.get(NATIVE_LANGUAGE), fill="white")


def next_card():
    '''
    Display a new word and start the timer.
    '''
    
    global timer, new_random_word
    
    window.after_cancel(timer)
    
    new_random_word = new_word()
    if not new_random_word:
        messagebox.showinfo(title="Wow!", message="You have learnt all the words there were!")
        exit()

    canvas.itemconfig(card, image=front_card_image)
    canvas.itemconfig(word_label, text=reverse(new_random_word.get(NEW_LANGUAGE)), fill="black")
    canvas.itemconfig(title_label, text=NEW_LANGUAGE, fill="black")
    timer = window.after(3000, func=flip_card)

def got_it():
    global words, new_random_word
    words.remove(new_random_word)
    save_words()
    next_card()

## ----------------------------- Read Data file ----------------------------- ##
words = load_words()
if not words:
    messagebox.showerror(title="Darn!", message="Couldn't find the specified language file")
    exit()

## ----------------------------- Setup Window ----------------------------- ##
window = Tk()
window.title("Language Flashcards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

front_card_image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 031/images/card_front.png")
back_card_image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 031/images/card_back.png")
canvas = Canvas(bg=BACKGROUND_COLOR, highlightthickness=0, width=800, height=526)
card = canvas.create_image(400, 263, image=front_card_image)
title_label = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
word_label = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

yes_image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 031/images/right.png")
yes_button = Button(image=yes_image, highlightthickness=0, command=got_it)
yes_button.grid(row=1, column=1)

no_image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 031/images/wrong.png")
no_button = Button(image=no_image, highlightthickness=0, command=next_card)
no_button.grid(row=1, column=0)

timer = window.after(3000, func=flip_card)
next_card()

window.mainloop()