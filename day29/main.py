import tkinter as tk
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


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


def save_credential():
    web = web_entry.get()
    email = web_id_entry.get()
    password = password_entry.get()

    credentials = {
        web: {
            "email": email,
            "password": password
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops: erno 01", message=f"field cannot be empty!")
    elif len(password) < 8:
        messagebox.showerror(title="Oops: erno 02", message=f"password must contain minimum 8")
    else:
        try:
            # first time scenario:
            # try open and reading data, if the file do not exist then catch the exception
            with open("data.json", "r") as file:
                # reading old data
                data = json.load(file)

        # if the data.json file exist it tries to parse the json file.
        # But if that file is empty, then there is no valid json in the file so it errors
        except json.decoder.JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(credentials, file, indent=4)

        # first time scenario:
        # catch file not found error exception, create new file with write properties,
        # then dump data to the file for the first time
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # update old data with the new data
                json.dump(credentials, file, indent=4)

        # this block will onl run when try block is successful
        # if file found and already exist, then just update the file with new data
        else:
            data.update(credentials)
            with open("data.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            web_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)


def retrieve_data():

    user_input = web_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops: erno 03", message="No data file found")
    else:
        if user_input in data:
            email = data[user_input]["email"]
            password = data[user_input]["password"]
            messagebox.showinfo(title=f"{user_input}", message=f"Website: {user_input}"
                                                               f"\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops: erno 04", message="No details for the website exists")


window = tk.Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
padlock_bg = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_bg)
canvas.grid(column=1, row=0)

web_label = tk.Label(text="Website: ", anchor="w", width=15)
web_label.grid(column=0, row=1)

web_entry = tk.Entry(width=33)
web_entry.grid(column=1, row=1)
web_entry.focus()

web_entry_find = tk.Button(text="Search", width=7, command=retrieve_data)
web_entry_find.grid(column=2, row=1)

web_id = tk.Label(text="Email/Username: ", anchor="w", width=15)
web_id.grid(column=0, row=2)

web_id_entry = tk.Entry(width=43)
web_id_entry.grid(column=1, row=2, columnspan=2)
web_id_entry.insert(0, "deddiapermana97@gmail.com")

web_password = tk.Label(text="Password: ", anchor="w", width=15)
web_password.grid(column=0, row=3)

password_entry = tk.Entry(width=33)
password_entry.grid(column=1, row=3)

gen_button = tk.Button(text="Generate", width=7, command=randomize_password)
gen_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=36, command=save_credential)
add_button.grid(column=1, row=4, columnspan=2)


tk.mainloop()
