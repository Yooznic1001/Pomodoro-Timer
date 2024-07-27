from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_sec = 25 * 60
SHORT_BREAK_sec = 5 * 60
LONG_BREAK_sec = 20 * 60
rep = 1
time = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global time, rep
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text= "Timer", fg=GREEN)
    rep = 1
    check.config(text=f"", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer():
    mark = ''
    global rep

    if rep %2 != 0:
        label.config(text="Work", fg=RED, font=(FONT_NAME, 30, "bold"), bg=YELLOW)

        count_down(WORK_sec)

    elif rep == 8:
        label.config(text="GOOD WORK", fg=PINK, font=(FONT_NAME, 30, "bold"), bg=YELLOW)


        for _ in range(int(rep/2)):
            mark += "✔"

        check.config(text=f"{mark}", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)

        count_down(LONG_BREAK_sec)

    elif rep %2 == 0:
        label.config(text="Break", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)


        for _ in range(int(rep/2)):
            mark += "✔"

        check.config(text=f"{mark}", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg=YELLOW)

        count_down(SHORT_BREAK_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_dah = math.floor(count_sec / 10)
    count_san = count_sec % 10
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_dah}{count_san}")

    global rep
    if count > 0:
         global time
         time = window.after(1000, count_down, count - 1)

    if count_min == 0 and count_sec == 0:

        if rep <= 7:
            rep += 1
            timer()

        elif rep > 7:
            reset()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg= YELLOW)
label.grid(column=1, row=0)
check = Label(text="", fg=GREEN, font=(FONT_NAME, 10, "bold"), bg= YELLOW)
check.grid(column=1, row=3)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)












window.mainloop()


