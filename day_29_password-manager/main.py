from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_password(website, email_username, password):
    if len(website) == 0 or len(email_username.get()) == 0 or len(password.get()) == 0:
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

    is_ok = check_password(website, email_username, password)

    if is_ok:
        with open('data.txt', 'a') as file:
            file.write(website + " | " + email_username + " | " + password + '\n')
            entry_website.delete(0, END)
            entry_password.delete(0,END)


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
entry_website = Entry(width=54)
entry_website.grid(column=1, row=1, columnspan=2,  sticky='w')
entry_website.focus()

entry_email_username = Entry(width=54)
entry_email_username.grid(column=1, row=2, columnspan=2, sticky='w')
entry_email_username.insert(0, "chelikofficial@gmail.com")

entry_password = Entry(width=35)
entry_password.grid(column=1, row=3, sticky='w')


# Buttons

button_generate_password = Button(text="Generate password", bg="#ffffff")
button_generate_password.grid(column=2, row=3, sticky='w')

button_add = Button(text="Add", width=45, bg="#ffffff", command=save_password)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()
