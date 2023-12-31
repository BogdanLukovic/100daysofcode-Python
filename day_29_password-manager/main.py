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

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for x in range(nr_letters)]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    entry_password.delete(0, END)
    entry_password.insert(0, password)
    pyperclip.copy(password)

    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_password(website, email_username, password):
    if len(website) == 0 or len(entry_email_username.get()) == 0 or len(entry_password.get()) == 0:
        messagebox.showerror(title='Error!', message='All fields must be filled out.')
        return False

    is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {email_username}\n'
                                                          f'Password: {password}\nIs it ok to save?')

    if is_ok:
        return True

    return False


def save_password():
    website = entry_website.get()
    email_username = entry_email_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    is_ok = check_password(website, email_username, password)

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title=website, message='Please make sure you havent left any fields empty.')
    else:
        if is_ok:
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)

                with open('data.json', 'w') as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_website.delete(0, END)
                entry_password.delete(0, END)

# -------------------------- SEARCH PASSWORD ---------------------------- #


def search():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)

            website = entry_website.get()
            email = data[website]["email"]
            password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="error", message="File is empty")
    except KeyError as key:
        messagebox.showerror(title="error", message=f"Website {key} does not exist.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("MyPass")
window.config(padx=20, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="#ffffff", highlightthickness=0)
padlock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="#ffffff")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:", bg="#ffffff")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:", bg="#ffffff")
label_password.grid(column=0, row=3)

# Entries
entry_website = Entry(width=35)
entry_website.grid(column=1, row=1, sticky='w')
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.grid(column=1, row=2, sticky='w')
entry_email_username.insert(0, "chelikofficial@gmail.com")

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3, sticky='w')


# Buttons

button_generate_password = Button(text="Generate password", width=15, bg="#ffffff", command=generate_password)
button_generate_password.grid(column=2, row=3, sticky='e')

button_add = Button(text="Add", width=45, bg="#ffffff", command=save_password)
button_add.grid(column=1, row=4, columnspan=2, sticky='e')

button_search = Button(text="Search", width=15, bg="#ffffff", command=search)
button_search.grid(column=2, row=1, sticky='e')

window.mainloop()
