from currency_converter import CurrencyConverter
import tkinter as tk
c=CurrencyConverter()
window=tk.Tk()
def getlist():
    return c.currencies
def valamount(char):
    return char.isdigit() or char=="."
def valcurrency(char):
    return  char.isalpha()
amountcmd=window.register(valamount)
currencycmd=window.register(valcurrency)

def clicked():
    amount=float(entry0.get())
    cur=entry1.get().upper()
    con=entry2.get().upper()
    data=c.convert(amount,cur,con)
    label5=tk.Label(window,text=data,font="Times 15 bold").place(x=215,y=290)
window.geometry("500x400")
window.title("Currency Converter")
label=tk.Label(window,text="Currency Converter",font="Arial 30 italic").pack()
label1=tk.Label(window,text="Enter amount",font="Times 15 bold").place(x=50,y=100)
label2=tk.Label(window,text="Enter currency",font="Times 15 bold").place(x=50,y=130)
label3=tk.Label(window,text="Enter currency \nto convert to",font="Times 15 bold").place(x=50,y=160)
label4=tk.Label(window,text="Converted amount",font="Times 15 bold").place(x=50,y=290)
entry0=tk.Entry(window,validatecommand=(valamount,"%S"))
entry1=tk.Entry(window,validatecommand=(valcurrency,"%S"))
entry2=tk.Entry(window,validatecommand=(valcurrency,"%S"))
entry0.place(x=200,y=105)
entry1.place(x=200,y=135)
entry2.place(x=200,y=165)
button=tk.Button(window,text="Convert",font="Times 15 bold",command=clicked).place(x=200,y=230)
currencylist=tk.Listbox(window,height=15,width=15)
currencylist.place(x=400,y=100)
currencies=getlist()
for currencies in currencies:
    currencylist.insert(tk.END,currencies)
window.mainloop()
