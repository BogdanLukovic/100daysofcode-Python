from tkinter import *
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
INDEX_OF_WORD = 0

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")


all_words_dict = data.to_dict()

# ----------------- GENERATE WORD -------------------- #


def generate_random_word():
    global flip_timer, INDEX_OF_WORD, all_words_dict

    window.after_cancel(flip_timer)

    list_of_french_words = list(all_words_dict["French"].items())
    index_word_pair = random.choice(list_of_french_words)

    word = index_word_pair[1]
    INDEX_OF_WORD = index_word_pair[0]

    canvas.itemconfig(card, image=card_front)
    canvas.itemconfig(language_on_card, text="French")
    canvas.itemconfig(word_on_card, text=all_words_dict["French"][INDEX_OF_WORD])

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global INDEX_OF_WORD, all_words_dict

    canvas.itemconfig(card, image=card_back)
    canvas.itemconfig(language_on_card, text="English")

    canvas.itemconfig(word_on_card, text=all_words_dict["English"][INDEX_OF_WORD])


def correct_guess():
    global INDEX_OF_WORD, all_words_dict
    all_words_dict["French"].pop(INDEX_OF_WORD)
    all_words_dict["English"].pop(INDEX_OF_WORD)

    generate_random_word()


# ---------------------- UI -------------------------- #


window = Tk()
window.geometry()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2, padx=50, pady=(50, 0))

# Card:

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front)

language_on_card = canvas.create_text(400, 150, text='Language', font=('Ariel', 40, "italic"))
word_on_card = canvas.create_text(400, 263, text='word', font=('Ariel', 60, "bold"))


# Buttons:
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")


wrong = Button(image=wrong_image, borderwidth=0, highlightthickness=0, command=generate_random_word)
wrong.grid(column=0, row=1, padx=50, pady=(0, 50))

right = Button(image=right_image, borderwidth=0, highlightthickness=0, command=correct_guess)
right.grid(column=1, row=1, padx=50, pady=(0, 50))

flip_timer = window.after(3000, func=flip_card)

generate_random_word()

window.mainloop()

print(all_words_dict)

data_frame = pandas.DataFrame.from_dict(all_words_dict)


data_frame.to_csv("data/words_to_learn.csv", index=False)
