import tkinter as tk

def prs():
    f =open("About Google Chrome.txt",'a')
    f.write('Google Chrome Copyright 2022 Google LLC.All rights reserved.Chrome is made possible by the Chromium open source project and other open source software.Terms of Service\n')
    f.write(u7.get()+"\n")
    f.close()

def lkd():
    x = u7.get()
    f = open("Google Chrome.txt" , "r")
    lines = f.readlines()
    f.close()
    f9.delete("1.0" , tk.END)
    for f in lines:
        if x in f :
            f9.insert(tk.END,f )

root = tk.Tk()
root.geometry("600x400")
root.title("Google Chrome")
root.resizable(False, False)
root.config(bg="#013d3a")

a1=tk.Label(root,text="G",fg="Blue",font=("Normal", 30))
a1.place(x=230,y=20)

e2=tk.Label(root,text="o",fg="Red",font=("Normal",30))
e2.place(x=265,y=20)

r3=tk.Label(root,text="o",fg="Orange",font=("Normal",30))
r3.place(x=290,y=20)

s4=tk.Label(root,text="g",fg="Blue",font=("Normal",30))
s4.place(x=315,y=20)

t5=tk.Label(root,text="l",fg="Green",font=("Normal",30))
t5.place(x=340,y=20)

y6=tk.Label(root,text="e",fg="Red",font=("Normal",30))
y6.place(x=350,y=20)

u7=tk.Entry(root)
u7.place(x=245,y=95)

k8=tk.Button(root,text="Search" , command=lkd)
k8.place(x=280,y=135)

f9 = tk.Text(root , height=10 , width=40)
f9.place(x=155,y=200)


menubar=tk.Menu(root)

filemenu=tk.Menu(menubar, tearoff=0)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu=tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About",command=prs)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)





root.mainloop()