import tkinter as tk


def miles_km():
    new_input = float(input_form.get())
    converted = round(new_input * 1.609)
    label_result.config(text=converted)


window = tk.Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

input_form = tk.Entry(width=10)
input_form.grid(column=1, row=0)

label_miles = tk.Label()
label_miles.config(text="Mill")
label_miles.grid(column=2, row=0)

label_equal = tk.Label()
label_equal.config(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = tk.Label()
label_result.config(text="0")
label_result.grid(column=1, row=1)

label_km = tk.Label()
label_km.config(text="Km")
label_km.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=miles_km)
button.grid(column=1, row=2)


window.mainloop()
