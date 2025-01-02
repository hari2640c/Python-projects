import tkinter as tk
window=tk.Tk()




def Bmi():
    w = float(entry2.get())
    h = float(entry1.get())
    bm=w/(h*h)
    if  bm<18.5:
        print("underweight")
        re="underweight"
    elif 18.5< bm <=24.9:
        print("normal weight")
        re="normal weight"
    elif 25<= bm <=29.9:
        print("over weight")
        re="over weight"
    else:
        print("obesity")
        re="obese"
    label4.config(text=f"your BMI is {bm:.2f} \n you are {re}")

window.geometry("500x500")
window.title("BMI calculator")
label1=tk.Label(window,text="Calculate your Body mass Index \nusing height and weight",font="Arial 20 italic")
label1.pack()
label2=tk.Label(window,text="enter your height in meters",font="Times 20 bold")
label2.place(x=95,y=100)
label3=tk.Label(window,text="enter your weight in kilograms",font="Times 20 bold")
label3.place(x=80,y=200)
label4=tk.Label(window,text="",font="Times 15 bold")
label4.place(x=160,y=350)
entry1=tk.Entry(window,bg="sky blue",font="Time 20 bold")
entry1.place(x=150,y=150,width="200",height="50")
entry2=tk.Entry(window,bg="sky blue",font="Time 20 bold")
entry2.place(x=150,y=250,width="200",height="50")
button1=tk.Button(window,text="Submit",command=Bmi,bd="5px")
button1.place(x=175,y=300,width=150,height=50)
window.mainloop()