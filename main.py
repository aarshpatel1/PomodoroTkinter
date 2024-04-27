from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# creating canvas so that we can layer things like images and text
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# a way to read through file like image
tomato_image = PhotoImage(file="tomato.png")

# created image in the canvas
canvas.create_image(100, 112, image=tomato_image)

# created text in the canvas
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark_label.grid(column=1, row=3)

window.mainloop()
