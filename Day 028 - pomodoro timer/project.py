from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"

laps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{str(WORK_MIN).zfill(2)}:00")
    timer_label.config(text="Timer")
    check_marks_label.config(text="")
    global laps
    laps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global laps
    laps += 1
    
    if laps % 2 != 0:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif laps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{str(count_min).zfill(2)}:{str(count_sec).zfill(2)}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        
        check_marks = ""
        for _ in range(laps // 2):
            check_marks += CHECKMARK

        check_marks_label.config(text=f"{check_marks}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro work")
window.config(padx=100, pady=50, bg=YELLOW)

tomato_image = PhotoImage(file="/home/dibits/Repos/100DaysOfPython/Day 028/tomato.png")
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=tomato_image)
timer_text = canvas.create_text(101, 145, text=f"{str(WORK_MIN).zfill(2)}:00", font=(FONT_NAME, 40, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks_label = Label(text="", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_marks_label.grid(row=3, column=1)

window.mainloop()