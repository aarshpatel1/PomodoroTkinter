from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None  # "None" indicates that there is no datatype of the timer variable, but we just created the variable


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps

    # cancels the timer count mechanism loop using after_cancel method
    window.after_cancel(timer)

    # resets heading label, time and checkmarks to initial values
    timer_label["text"] = "Timer"
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_label["text"] = ""

    # resets reps to 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1  # increases reps by one so that every time function is called the reps can be changed

    # calculated times in the seconds
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    # checking that what is the current cycle running
    if reps == 8:
        count_down(long_break_time)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_time)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_time)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    # calculates minutes and seconds
    minutes = math.floor(count / 60)
    seconds = count % 60

    # keeps the format of minutes to double digits
    if seconds < 10:
        seconds = f"0{seconds}"

    # updates the time in output
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        # creating loop using after method of tkinter module
        # and here recursion is used by calling the count_down(count) function to itself
        # and changing and decreasing its arguments value by 1
        timer = window.after(1000, count_down, count - 1)
    else:
        # when the count_down goes to 0 it again calls start timer to change the timer mode
        start_timer()
        # displaying checkmarks to indicate that work cycle is over
        # and increasing by one for indicating which time work cycle is over
        if reps % 2 == 0:
            checkmark_label["text"] += "✔"


# ---------------------------- UI SETUP ------------------------------- #
# creating window object from Tk class and setting up output window screen
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
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# timer heading label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

# timer start button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

# timer reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# checkmark label for displaying completion of work-break cycle
checkmark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 16, "bold"))
checkmark_label.grid(column=1, row=3)

# the mainloop which keep the output screen hold
window.mainloop()
