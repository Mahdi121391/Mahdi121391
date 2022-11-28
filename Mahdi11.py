import tkinter as tk
import time
from threading import Thread
import datetime

def timer(seconds):
        while True:
            label['text'] = str(datetime.timedelta(seconds=seconds))
            time.sleep(1)
            if seconds == 0:
                button.config(state="normal")
                entry.config(state="normal")
                break
            seconds -= 1

def count():
    seconds = int(entry.get())
    entry.config(state="disabled")
    th1 = Thread(target=timer,args=(seconds,))
    th1.start()
    button.config(state="disabled")

root = tk.Tk()
root.resizable(False, False)
root.config(bg="Yellow")
root.title("Time")

entry = tk.Entry(root,bg="Green")
entry.place(x=40,y=5)

label = tk.Label(root,text="HH:MM:SS",font=("Slant",12),bg="Blue")
label.place(x=60,y=50)

button = tk.Button(root,text="Start",font=("Slant",12),command=count,bg="Red")
button.place(x=75,y=100)

root.mainloop()