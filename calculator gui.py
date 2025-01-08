import random
import tkinter as tk

window = tk.Tk()
window.geometry("500x500")
window.title("Calculator")
def colo():
    li=["#ff0000","#ffff00","#66ff33","#00ffff","#0066ff","#ff00ff"]
    r=random.choice(li)
    er = random.choice(li)
    window.config(bg=r)
    re.config(bg=er)

def equal():
    e=entry1.get()
    re=eval(e)
    entry1.delete(0,tk.END)
    entry1.insert(tk.END,re)
def on():
    entry1.insert(tk.END,'1')
def tw():
    entry1.insert(tk.END,'2')
def thr():
    entry1.insert(tk.END,'3')
def fo():
    entry1.insert(tk.END,'4')
def fi():
    entry1.insert(tk.END,'5')
def si():
    entry1.insert(tk.END,'6')
def se():
    entry1.insert(tk.END,'7')
def ei():
    entry1.insert(tk.END,'8')
def ni():
    entry1.insert(tk.END,'9')
def ze():
    entry1.insert(tk.END,'0')
def clear():
    entry1.delete(0, tk.END)
def plus():
    entry1.insert(tk.END,'+')
def minus():
    entry1.insert(tk.END,'-')
def pro():
    entry1.insert(tk.END,'*')
def div():
    entry1.insert(tk.END,'/')


entry1 = tk.Entry(window, text='', font='Times ')
entry1.place(x=50, y=50, width='400', height='40')

b1 = tk.Button(window, text='1',command=on)
b1.place(x=50, y=100, width='50', height='50')
b2 = tk.Button(window, text='2',command=tw)
b2.place(x=150, y=100, width='50', height='50')
b3 = tk.Button(window, text='3',command=thr)
b3.place(x=250, y=100, width='50', height='50')
p = tk.Button(window, text='+', font='Times 30 bold',command=plus)
p.place(x=350, y=100, width='50', height='50')

b4 = tk.Button(window, text='4',command=fo)
b4.place(x=50, y=190, width='50', height='50')
b5 = tk.Button(window, text='5',command=fi)
b5.place(x=150, y=190, width='50', height='50')
b6 = tk.Button(window, text='6',command=si)
b6.place(x=250, y=190, width='50', height='50')
m = tk.Button(window, text='-', font='Times 30 bold',command=minus)
m.place(x=350, y=190, width='50', height='50')

b7 = tk.Button(window, text='7',command=se)
b7.place(x=50, y=280, width='50', height='50')
b8 = tk.Button(window, text='8',command=ei)
b8.place(x=150, y=280, width='50', height='50')
b9 = tk.Button(window, text='9',command=ni)
b9.place(x=250, y=280, width='50', height='50')
mu = tk.Button(window, text='*', font='Times 30 bold',command=pro)
mu.place(x=350, y=280, width='50', height='50')

b10 = tk.Button(window, text='C', font='Times 30 bold', command=clear)
b10.place(x=50, y=370, width='50', height='50')
b11 = tk.Button(window, text='0',command=ze)
b11.place(x=150, y=370, width='50', height='50')
b12 = tk.Button(window, text='=',command=equal)
b12.place(x=250, y=370, width='50', height='50')
d = tk.Button(window, text='/', font='Times 30 bold',command=div)
d.place(x=350, y=370, width='50', height='50')

re = tk.Button(window, text='c\no\nl\no\nr', font='Arial 20 italic',command=colo)
re.place(x=410, y=100, width='50', height='320')

window.mainloop()