from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    entry_password.delete(0, last=END)
    entry_password.insert(0,password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    webside = entry_website.get()
    email_user = entry_email_user.get()
    password = entry_password.get()
    new_data = {
        webside: {
            "email": email_user,
            "password": password
        }
    }

    if  webside == "" or email_user == "" or password == "":
        messagebox.showwarning(title="Ops",message="You have empty fields")
    else:
        is_ok = messagebox.askokcancel(title=webside,message=f"Your entries:\nWebsite = {webside}\nEmail: {email_user}\n"
                                                         f"Password: {password}\nIs ok to save?")

    if is_ok:
        # Write data to json
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
            # Clear entries
            entry_website.delete(0,last=END)
            entry_password.delete(0,last=END)


# ---------------------------- SEARCH DATA ------------------------------- #

def search_data():
    webside = entry_website.get()
    msg = ""
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        msg = "No data.json"
    else:
        if webside in data:
            msg= f"Website: {webside}\nEmail: {data[webside]["email"]}\nPassword: {data[webside]["password"]}"
        else:
            msg = "Not found"
    finally:
        messagebox.showinfo(title="Search", message=msg)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row=0,column=0,columnspan=3)

label_website = Label(text="Website:")
label_website.grid(row=1,column=0,sticky='e')
label_email_user = Label(text="Email/Username:")
label_email_user.grid(row=2,column=0,sticky='e')
label_password = Label(text="Password:")
label_password.grid(row=3,column=0,sticky='e')

entry_website = Entry(width=21)
entry_website.grid(row=1,column=1,sticky='w')
entry_email_user = Entry(width=42)
entry_email_user.insert(0,"name@gmail.com")
entry_email_user.grid(row=2,column=1,columnspan=3,sticky='w')
entry_password = Entry(width=21,show='*')
entry_password.grid(row=3,column=1,sticky='w')

button_generate = Button(width=17,text="Generate password",command=generate_password)
button_generate.grid(row=3,column=2,sticky='w')
button_add = Button(width=36, text="Add", command=add_data)
button_add.grid(row=4,column=1,columnspan=2,sticky='w')
button_search = Button(width=17, text="Search", command=search_data)
button_search.grid(row=1,column=2,sticky='w')

window.mainloop()