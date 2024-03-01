import tkinter as tk
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
card = {}
list_dict = {}

try:
    # first time scenario:
    # this file only exist when the program already run before, otherwise it will give an error file not found
    used_data = pd.read_csv("data/remaining_words_to_learn.csv")

# first time scenario:
# catch the file not found error exception
# read file from original data
except FileNotFoundError:
    original_data = pd.read_csv("data/en-id.csv")
    list_dict = original_data.to_dict(orient="records")

# if the try ever run before or there is file exist, then execute this line
else:
    list_dict = used_data.to_dict(orient="records")


def get_next_data():
    global card, window_delay
    window.after_cancel(window_delay)

    card = choice(list_dict)
    canvas.itemconfig(en_word, text=card["English"])
    canvas.itemconfig(canvas_bg, image=card_front_bg)
    canvas.itemconfig(en_title, fill="black")
    canvas.itemconfig(en_word, fill="black")

    window_delay = window.after(3000, flip)


def remain_data():
    list_dict.remove(card)

    df = pd.DataFrame(list_dict)
    df.to_csv("data/remaining_words_to_learn.csv", index=False)

    get_next_data()


def flip():
    canvas.itemconfig(canvas_bg, image=card_back_bg)
    canvas.itemconfig(en_title, fill="white")
    canvas.itemconfig(en_word, text=card["Bahasa"], fill="white")
    window.after_cancel(window_delay)


window = tk.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window_delay = window.after(3000, flip)

card_front_bg = tk.PhotoImage(file="image/card_front.png")
card_back_bg = tk.PhotoImage(file="image/card_back.png")
cross_image = tk.PhotoImage(file="image/wrong.png")
check_image = tk.PhotoImage(file="image/right.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_bg = canvas.create_image(400, 263, image=card_front_bg)
en_title = canvas.create_text(400, 150, text="English", fill="black", font=("Ariel", 40, "italic"))
en_word = canvas.create_text(400, 263, text="Words", fill="black", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


button_cross = tk.Button(image=cross_image, highlightthickness=0, command=get_next_data)
button_cross.grid(row=1, column=0)

button_check = tk.Button(image=check_image, highlightthickness=0, command=remain_data)
button_check.grid(row=1, column=1)

get_next_data()
tk.mainloop()
