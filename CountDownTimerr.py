from tkinter import *

import time
 
def start_timer():
    try:
        hours = int(entry_hours.get())
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
    except ValueError:
        return
 
 
    total_seconds = hours * 3600 + minutes * 60 + seconds
 
 
    for t in range(total_seconds, -1, -1):
        mins, secs = divmod(t, 60)
        hours, mins = divmod(mins, 60)
        time_str = f"{hours:02d}:{mins:02d}:{secs:02d}"
        timer_label.config(text=time_str)
        root.update()
        time.sleep(1)
 
 
  # Time's up!
    timer_label.config(text="Time's up!")
    
 
root = Tk()
root.title("Countdown Timer - The Pycodes")
root.geometry("500x400")
root.config(bg="black")
Label(root, text="Countdown", font="arial 20 bold", bg="black", fg="orange").place(x=180, y=20)
 
 
entry_hours = Entry(root, width=5, font=("Arial", 20), bg="black", fg="#fff", bd=0)
entry_hours.place(x=100, y=100)
entry_hours.insert(3, "02")
label_hours = Label(root, text="Hours", font=("Arial", 15), bg="black", fg="#fff")
label_hours.place(x=30, y=100)
 
 
entry_minutes = Entry(root, width=5, font=("Arial", 20), bg="black", fg="#fff", bd=0)
entry_minutes.place(x=270, y=100)
entry_minutes.insert(0, "01")
label_minutes = Label(root, text="Minutes", font=("Arial", 15), bg="black", fg="#fff")
label_minutes.place(x=180, y=100)
 
 
entry_seconds = Entry(root, width=5, font=("Arial", 20), bg="black", fg="#fff", bd=0)
entry_seconds.place(x=450, y=100)
entry_seconds.insert(0, "15")
label_seconds = Label(root, text="Seconds", font=("Arial", 15), bg="black", fg="#fff")
label_seconds.place(x=350, y=100)
 
 
start_button = Button(root, text="Start", command=start_timer, font=("Arial", 15))
start_button.place(x=225, y=250)
 
 
timer_label = Label(root, text="00:00:00", font=("Arial", 40), bg="black", fg="orange", bd=0)
timer_label.place(x=150, y=180)
 
 
root.mainloop()
