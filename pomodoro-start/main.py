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
rep = 0
works = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(works)
    label.config(text="Timer")
    checkmark.config(text="")
    canvas.itemconfig(timer,text="00:00")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global rep
    rep+=1
    work_min = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    
    if rep % 8 == 0:
        label.config(text="Break",fg=RED)
        countdown_mechanism(long_break)
    elif rep % 2 == 0:
        label.config(text="Break",fg=PINK)
        countdown_mechanism(short_break)
    else:
        label.config(text="WORK",fg=GREEN)
        countdown_mechanism(work_min)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown_mechanism(count):
    global works
    work_min = math.floor(count/60)
    work_sec = count%60
    if work_sec < 10:
        work_sec = f"0{work_sec}"
    canvas.itemconfig(timer,text = f"{work_min}:{work_sec}")
    if count > 0:
        works = window.after(1000,countdown_mechanism,count-1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(rep/2)):
            mark+="✓"
        checkmark.config(text=mark)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
label = Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"))
label.grid(column=2,row=1)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)
starts = Button(text="start",font=(FONT_NAME),highlightthickness=0,command=start)
starts.grid(row=3,column=1)
reset = Button(text="reset",font=(FONT_NAME),highlightthickness=0,command=reset)
reset.grid(row=3,column=3)
checkmark = Label(fg=GREEN,background=YELLOW,font=FONT_NAME)
checkmark.grid(row=3,column=2)
window.mainloop()
