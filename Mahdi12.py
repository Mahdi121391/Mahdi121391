import tkinter as tk
from tkinter import filedialog as fd
import shutil
import os

def b_press():
    f = fd.askopenfilename(title="Open Files")
    fn,ext = os.path.splitext(f)
    name = entry.get()+ "" + entry1.get()
    shutil.copyfile(f,"Images/"+name+ext)

root = tk.Tk()
root.geometry("600x400")
root.config(bg="Red")
root.title("Upload")
root.resizable(False, False)

label = tk.Label(root , text="Upload Your Image:")
label.place(x=220,y=0)

button = tk.Button(root,text="Browse",command=b_press)
button.place(x=330,y=0)

label1 = tk.Label(root,text="Last Name:")
label1.place(x=350,y=40)

label2 = tk.Label(root,text="Name:")
label2.place(x=180,y=40)

entry = tk.Entry(root)
entry.place(x=180,y=60)

entry1 = tk.Entry(root)
entry1.place(x=350,y=60)

root.mainloop()