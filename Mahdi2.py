import tkinter as tk



def password_toggle():
    if n8.cget('show') == "":
        n8.config(show="*")
    else:
        n8.config(show="")

def prs():
    name = f5.get()
    last = r6.get()
    f =open("Register.txt",'a')
    f.write(f5.get()+','+r6.get()+","+b7.get()+","+n8.get()+"\n")
    f.close()




root =tk.Tk()
root.geometry("600x400")
root.title("Register")
root.config(bg="Blue")

l1 = tk.Label(root , text="Name:" , font=("Normal",12))
l1.grid(row=0 , column=0)

e2 = tk.Label(root , text="Last Name:" , font=("Normal",12))
e2.grid(row=1 , column=0)

d3= tk.Label(root , text="Username:", font=("Normal",12))
d3.grid(row=2,column=0)

v4 = tk.Label(root , text="Password:", font=("Normal",12))
v4.grid(row=3,column=0)

f5 = tk.Entry(root)
f5.grid(row=0 , column=1)

r6 = tk.Entry(root)
r6.grid(row=1 , column=1)

b7 = tk.Entry(root)
b7.grid(row=2 ,column=1)

n8 = tk.Entry(root , show="•")
n8.grid(row=3 , column=1)

t9 = tk.Button(root , text="Register" , font=("Normal",12), command=prs)
t9.grid(row=4 , column=1)

m10 = tk.Button(root , text="Show" ,command=password_toggle)
m10.grid(row=3 , column=2)





root.mainloop()