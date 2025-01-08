import tkinter as tk
from tkinter import messagebox
from datetime import datetime
window=tk.Tk()
def age():
    try:
        b=entry1.get()
        b1=datetime.strptime(b,"%d-%m-%Y")
        today=datetime.today()
        ag=today.year-b1.year-((today.month,today.day)<(b1.month,b1.day))
        l2.config(text=f"your age is:\n{ag} years")
    except ValueError:
        messagebox.showerror("invalid format")

window.geometry("300x300")
window.title("Age Calculator")

b1=tk.Button(window,text="submit",command=age,bg="#00FFFF")
b1.place(x=60,y=100,width=200,height=50)

l1=tk.Label(window,text="enter DOB")
l1.place(x=20,y=50)
l3=tk.Label(window,text="format=DD-MM-YYYY")
l3.place(x=90,y=70)
entry1=tk.Entry(window,text="")
entry1.place(x=90,y=50,width=200,height=20)
l2=tk.Label(window,text="your age is",font="Times 20 bold")
l2.place(x=80,y=170)

window.mainloop()