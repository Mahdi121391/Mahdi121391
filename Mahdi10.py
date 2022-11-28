import tkinter as tk
from jdatetime import datetime

def get_hour():
    n = datetime.now()
    data = n.strftime("%A,%d %b")
    return data

def get_time():
    a = datetime.now()
    data = a.strftime("%H,%M,%S")
    return data

def get_number():
    b = datetime.now()
    data = b.strftime("")
    return data

def get_leftover():
    c = datetime.now()
    data = c.strftime("")


def prs():
    global t
    a1['text'] = get_hour()
    b2['text'] = get_time()
    t = t + 1
    c3['text'] = t
    t_list.append(t)
    d4['text'] = "باقی مانده:" + str(len(t_list)-1)

def call_1():
    if t_list:
        f6['text'] = t_list.pop(0)
        
    
def call_2():
    if t_list:
        g7['text'] = t_list.pop(0)

def call_3():
    if t_list:
        h8['text'] = t_list.pop(0)



root = tk.Tk()
t = 0
t_list = []
a1=tk.Label(root,text="")
a1.place(x=50,y=0)

b2=tk.Label(root,text="")
b2.place(x=70,y=30)

c3=tk.Label(root,text=0)
c3.place(x=90,y=55)

d4=tk.Label(root,text="باقی مانده:")
d4.place(x=70,y=80)

e5=tk.Button(root,text="Get",command=prs,bg="Yellow")
e5.place(x=80,y=110)

top = tk.Toplevel()

f6=tk.Label(top,text=0 , font=("Normal",12))
f6.place(x=30,y=0)

g7=tk.Label(top,text=0,font=("Normal",12))
g7.place(x=90,y=0)

h8=tk.Label(top,text=0,font=("Normal",12))
h8.place(x=150,y=0)

i9=tk.Button(top,text="Next",font=("Normal",12),bg="Blue",command=call_1)
i9.place(x=15,y=30)

j10=tk.Button(top,text="Next",font=("Normal",12),bg="Red",command=call_3)
j10.place(x=135,y=30)

k11=tk.Button(top,text="Next",font=("Normal",12),bg="Green",command=call_2)
k11.place(x=75,y=30)

root.mainloop()
