import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def randomize_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    random_password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, random_password)
    pyperclip.copy(random_password)
    messagebox.showinfo(title="Info", message=f"{random_password} copied")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_credential():
    web = web_entry.get()
    email = web_id_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops: error 01", message=f"field cannot be empty!")
    elif len(password) < 8:
        messagebox.showerror(title="Oops: error 2", message=f"password must contain minimum 8")
    else:
        confirmation = messagebox.askokcancel(title=web, message=f"email: {email}\npassword: {password}\n"
                                                                 f"\nclick ok to confirm")
        if confirmation:
            web_email = f"{web}, {email}, {password}\n"
            file = open("data.txt", "a")
            file.write(web_email)
            file.close()
            web_entry.delete(0, tk.END)
            web_id_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
padlock_bg = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_bg)
canvas.grid(column=1, row=0)

web_label = tk.Label(text="Website: ", anchor="w", width=15)
web_label.grid(column=0, row=1)

web_entry = tk.Entry(width=43)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

web_id = tk.Label(text="Email/Username: ", anchor="w", width=15)
web_id.grid(column=0, row=2)

web_id_entry = tk.Entry(width=43)
web_id_entry.grid(column=1, row=2, columnspan=2)
web_id_entry.insert(0, "deddiapermana97@gmail.com")

web_password = tk.Label(text="Password: ", anchor="w", width=15)
web_password.grid(column=0, row=3)

password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3)

gen_button = tk.Button(text="Generate", command=randomize_password)
gen_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save_credential)
add_button.grid(column=1, row=4, columnspan=2)


tk.mainloop()
