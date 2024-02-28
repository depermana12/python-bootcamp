import math
import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
window_update = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(window_update)
    ui_title.config(text="Timer")
    canvas.itemconfig(canvas_timer, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1

    work_timer = WORK_MIN * 60
    short_break_timer = SHORT_BREAK_MIN * 60
    long_break_timer = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        start_count(long_break_timer)
        ui_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        start_count(short_break_timer)
        ui_title.config(text="Break", fg=PINK)
    else:
        start_count(work_timer)
        ui_title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def start_count(count):

    count_min = math.floor((count / 60))
    count_sec = count % 60

    canvas.itemconfig(canvas_timer, text=f"{count_min}:{count_sec:02d}")
    if count > 0:
        global window_update
        window_update = window.after(1000, start_count, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW,)

ui_title = tk.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
ui_title.grid(column=1, row=0)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_bg = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_bg)
canvas_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = tk.Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

check_label = tk.Label(text="✔️", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

reset_button = tk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


tk.mainloop()
