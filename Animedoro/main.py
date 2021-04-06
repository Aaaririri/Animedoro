
"""
if you only using using this particular file copy and change the ralative path of the sound alarm and the image
you need to install pygames in order to work to do so 
pip install pygame
"""
import tkinter as tk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bddaf"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 20
LONG_BREAK_MIN = 40
reps = 0
timer = None
# ---------------------------- SOUND EFECTS ------------------------------ #
"""
sound efect from the link: https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
Alarm Fast High Pitch A1 Sound Effect
"""
import pygame


pygame.mixer.init()
def play_music():
    pygame.mixer.music.load("Alarm-Fast-High-Pitch-A1-www.fesliyanstudios.com.mp3")
    pygame.mixer.music.play()

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps 
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text = "00:00")
    mode.config(text="                ")
    times_study.config(text=f"Study Session: 0.0")

def parcial_reset():
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    if reps > 0:
        parcial_reset()
    reps += 1
    if reps % 8 == 0:
        mode.config(text="    Long Break   ")
        countdown(LONG_BREAK_MIN * 60)
        sessions = reps / 2
        times_study.config(text=f"Study Session: {sessions}")
    elif reps % 2 == 0:
        mode.config(text="    Anime Time   ")
        countdown(SHORT_BREAK_MIN * 60)
        sessions = reps / 2
        times_study.config(text=f"Study Session: {sessions}")
    else:
        mode.config(text="    Work Time   ")
        countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    all_seconds = count
    minutes = math.trunc(all_seconds / 60)
    seconds = all_seconds % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0 :
        timer = window.after(1000, countdown, count - 1)
    if count == 0:
        play_music()
        if checked_state.get():
            start_timer()

# ---------------------------- UI SETUP ------------------------------- #
"""
image found online
"""
window = tk.Tk()
window.title("Animedoro")
window.config(padx=50, pady=0, bg = RED)
canvas = tk.Canvas(width = 700, height = 580, bg = RED, highlightthickness = 0)
img = tk.PhotoImage(file = "PngItem_947459.png")
canvas.create_image(300, 1300, image = img)
timer_text = canvas.create_text(350, 200, text = "00:00", font = (FONT_NAME, 35, "bold"), fill = PINK)
canvas.grid(column = 1, row = 1)
# title
my_label = tk.Label(text="TIMER", font=(FONT_NAME, 30, "bold"), bg = GREEN, fg = YELLOW)
my_label.grid(column=1, row=0)
# start button
b1 = tk.Button(text="Start", highlightthickness = 0, fg = GREEN, bg = RED, font=(FONT_NAME, 20, "bold"), command = start_timer)
b1.grid(column=0, row=1)
# reset button 
b2 = tk.Button(text="Reset", highlightthickness = 0, fg = GREEN, bg = RED, font=(FONT_NAME, 20, "bold"), command = reset_timer)
b2.grid(column=2, row=1)
# mode
mode = tk.Label(text="                ", font=(FONT_NAME, 30, "bold"), bg = GREEN, fg = YELLOW)
mode.grid(column=1, row=2)
# auto -> makes your pomodoro run alone
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Auto", variable=checked_state, highlightthickness = 0, fg = GREEN, bg = RED, font=(FONT_NAME, 15, "bold"))
checkbutton.grid(column=0, row=0)
#sessions -> display number of times you completed a ciclo of studing and resting  
times_study = tk.Label(text=f"Study Session: 0.0", font=(FONT_NAME, 12, "bold"), bg = RED, fg = GREEN)
times_study.place(x = 700, y= 650)
window.mainloop()