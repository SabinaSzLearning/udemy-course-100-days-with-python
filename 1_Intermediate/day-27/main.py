from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(300,150)
window.config(padx=40,pady=40)

label1 = Label(text="Km")
label2 = Label(text="is equal to")
label3 = Label(text="Miles")
label4 = Label(text="0")
label1.grid(column = 2, row = 1)
label2.grid(column = 0, row = 1)
label3.grid(column = 2, row = 0)
label4.grid(column = 1, row = 1)

def button_clicked():
    km = int(input.get())
    label4["text"] = str(round(km*1.6))

button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row = 2)

input = Entry()
input.grid(column = 1, row = 0)


window.mainloop()


# def add(*args):
#     sum1=0
#     for a in args:
#         sum1 += a
#     return sum1
#
# print(add(1,2,3,4,5))
