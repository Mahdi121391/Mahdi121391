import tkinter as tk
from tkinter import ttk

def press():
    k = u7.get()
    f = open("Name.txt" , "r")
    lines = f.readlines()
    f.close()
    f9.delete("1.0" , tk.END)
    for l in lines:
        if k in l :
            f9.insert(tk.END, l )

def password_toggle():
    if n8.cget('show') == "":
        n8.config(show="*")
    else:
        n8.config(show="")

def prs():
    name = f5.get()
    last = r6.get()
    f =open("Name.txt",'a')
    f.write(f5.get()+','+r6.get()+","+b7.get()+","+n8.get()+"\n")
    f.close()

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title('Notebook Demo')
note = ttk.Notebook(root)
note.grid(row=0 , column=0)

f1 = tk.Frame(note , width=599, height=380)
f2 = tk.Frame(note , width=599, height=380)

note.add(f1 , text="Register")
note.add(f2 ,text="Google Chrome")



#  Google Chrome #####################################################


f2.config(bg="#013d3a")

a1=tk.Label(f2,text="G",fg="Blue",font=("Normal", 30))
a1.place(x=230,y=20)

e2=tk.Label(f2,text="o",fg="Red",font=("Normal",30))
e2.place(x=265,y=20)

r3=tk.Label(f2,text="o",fg="Orange",font=("Normal",30))
r3.place(x=290,y=20)

s4=tk.Label(f2,text="g",fg="Blue",font=("Normal",30))
s4.place(x=315,y=20)

t5=tk.Label(f2,text="l",fg="Green",font=("Normal",30))
t5.place(x=340,y=20)

y6=tk.Label(f2,text="e",fg="Red",font=("Normal",30))
y6.place(x=350,y=20)

u7=tk.Entry(f2)
u7.place(x=245,y=95)

k8=tk.Button(f2,text="Search" , font=("Normal",10) ,command=press)
k8.place(x=280,y=130)

f9 = tk.Text(f2 , height=10 , width=40)
f9.place(x=150,y=200)


# ##############################################################

# Register #####################################################


f1.config(bg="Blue")

l1 = tk.Label(f1 , text="Name:" , font=("Normal",12))
l1.grid(row=0 , column=0)

e2 = tk.Label(f1 , text="Last Name:" , font=("Normal",12))
e2.grid(row=1 , column=0)


d3= tk.Label(f1 , text="Username:", font=("Normal",12))
d3.grid(row=2,column=0)

v4 = tk.Label(f1 , text="Password:", font=("Normal",12))
v4.grid(row=3,column=0)

f5 = tk.Entry(f1)
f5.grid(row=0 , column=1)

r6 = tk.Entry(f1)
r6.grid(row=1 , column=1)

b7 = tk.Entry(f1)
b7.grid(row=2 ,column=1)

n8 = tk.Entry(f1 , show="*")
n8.grid(row=3 , column=1)

t9 = tk.Button(f1 , text="Register" , font=("Normal",12), command=prs)
t9.grid(row=4 , column=1)

m10 = tk.Button(f1 , text="Show" ,command=password_toggle)
m10.grid(row=3 , column=2)

# ##############################################################



root.mainloop()