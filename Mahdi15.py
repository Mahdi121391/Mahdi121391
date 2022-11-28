import tkinter as tk
from PIL import ImageTk,Image
from random import choice

def callback(a, b, c):
    v = ch.get()
    if v == 0:
        label['image'] = img
    elif v == 1:
        label['image'] = img1
    else:
        label['image'] = img2
        

def play():
    pc ['image'] = choice([img,img1,img2])

root = tk.Tk()
img = ImageTk.PhotoImage(Image.open("Images/rock.jpg").resize((200,200),Image.ANTIALIAS))
img1 = ImageTk.PhotoImage(Image.open("Images/paper.jpg").resize((200,200),Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("Images/scisor.jpg").resize((200,200),Image.ANTIALIAS))

f1 = tk.LabelFrame(root,text="Your Choice")
f1.grid(row=0,column=0)

ch=tk.IntVar()
ch.trace('w',callback)

f2=tk.Radiobutton(f1,text="Rock",variable=ch,value=0)
f2.grid(row=0,column=0)

f3=tk.Radiobutton(f1,text="Paper",variable=ch,value=1)
f3.grid(row=1,column=0)

f4=tk.Radiobutton(f1,text="Scisor",variable=ch,value=2)
f4.grid(row=2,column=0)

label = tk.Label(root,image=img)
label.grid(row=0,column=1)

pc = tk.Label(root,image=img1)
pc.grid(row=0,column=2)

f5=tk.Button(root,text="Let's Play",command=play)
f5.grid(row=1,column=0)


root.mainloop()