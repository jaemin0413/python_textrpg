from tkinter import *

qwer=Tk()
qwer.geometry("400x200")
qwer.title("트킨터연습")

entry=Entry(qwer)
entry.pack(side="top")

button=Button(qwer)
button.config(text="클릭")

def qqqq():
    button.pack(side=entry.get())
button.config(command=qqqq)
button.pack()

qwer.mainloop()