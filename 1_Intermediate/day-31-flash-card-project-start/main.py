from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
random_data = {}

# Words to learn --------------------------------------------------------
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except:
    data = pd.read_csv('./data/french_words.csv')
finally:
    data = data.to_dict(orient="records")


# Change word ------------------------------------------------------------
def next_card():
    global random_data, flip_timer
    window.after_cancel(flip_timer)
    random_data = random.choice(data)
    canvas.itemconfig(image, image=front_img)
    canvas.itemconfigure(text_lang, text='French', fill='black')
    canvas.itemconfigure(text_word, text=random_data["French"], fill='black')
    flip_timer = window.after(3000, func=flip_card)

# Correct word ------------------------------------------------------------
def correct_answer():
    data.remove(random_data)
    dataFrame = pd.DataFrame(data)
    dataFrame.to_csv('./data/words_to_learn.csv', index=False)
    next_card()


# Flip the card ----------------------------------------------------------

def flip_card():
    canvas.itemconfig(image, image=back_image)
    canvas.itemconfigure(text_lang, text='English', fill='white')
    canvas.itemconfigure(text_word, text=random_data["English"], fill='white')


# UI ----------------------------------------------------------------------

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file=".\images\card_front.png")
back_image = PhotoImage(file=".\images\card_back.png")
image = canvas.create_image(400, 263, image = front_img)
canvas.config(highlightthickness=0,background=BACKGROUND_COLOR)
text_lang = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
text_word = canvas.create_text(400, 263, text="Test", font=("Ariel", 60, "bold"))

canvas.grid(row=0,column=0,columnspan=2)

image_right = PhotoImage(file=".\images\\right.png")
button_right = Button(image=image_right, highlightthickness=0, command=correct_answer)
button_right.grid(row=1,column=0)

image_wrong = PhotoImage(file=".\images\wrong.png")
button_wrong = Button(image=image_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1,column=1)

next_card()



window.mainloop()
