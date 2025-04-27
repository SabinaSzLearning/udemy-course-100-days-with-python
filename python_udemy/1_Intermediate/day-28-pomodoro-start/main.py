import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def button_reset_clicked():
    window.after_cancel(timer)
    check_symbol.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def button_start_clicked():
    global reps
    reps += 1

    working_time = 60 * WORK_MIN
    long_break = 60 * LONG_BREAK_MIN
    short_break = 60 * SHORT_BREAK_MIN

    if reps%8 == 0:
        count_down(long_break)
        label.config(text="Break")
    elif reps%2 == 0:
        count_down(short_break)
        label.config(text="Break")
    else:
        count_down(working_time)
        label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    global timer

    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        button_start_clicked()
        if reps%2 == 0:
            check_symbol.config(text = "✔"*math.floor(reps/2))

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)

timer_text = canvas.create_text(100,130,text="00:00",fill='white', font=(FONT_NAME,26,'bold'))
canvas.grid(column=1,row=1)


label = Label()
label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME,30,'bold'))
label.grid(column=1,row=0)


button_start = Button(text="START", command=button_start_clicked)
button_start.grid(column = 0, row = 2)

button_reset = Button(text="REST", command=button_reset_clicked)
button_reset.grid(column = 2, row = 2)


check_symbol = Label()
check_symbol.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME,15,'bold'))
check_symbol.grid(column=1,row=3)


window.mainloop()
