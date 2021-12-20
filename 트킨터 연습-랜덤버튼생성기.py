from tkinter import *
import random


win=Tk()
win.title("aim game")
win.geometry("500x150")


#라벨
lab=Label(win)
lab.config(text="표적 갯수")
lab.grid(column=0, row=0, padx=20,pady=20)

#엔트리
ent=Entry(win)
ent.grid(column=1 ,row=0,padx=20,pady=20)

def ranb():
    btn=Button(win,bg="red")
    btn.place(relx=random.random(),rely=random.random())

def btf():
    global numt
    numt=int(ent.get())
    for wg in win.grid_slaves():
        wg.detroy()
    win.geometry("500x500")
    ranb()


btn=Button(win,text="시작")
btn.config(command=btf)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()
