from tkinter import *
import random
from datetime import datetime

#창 만들기

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

#k번째 버튼임을 알리는 상수

k=1

#버튼이 사라지고 난 다음의 버튼

def nxtb():
    global k
    if k<numt:
        k+=1
        btn.destroy()
        ranb()
    else:
        fin=datetime.now()
        tme=(fin-start).total_seconds()
        btn.destroy()
        lab1=Label(win,text="clear" + str(tme) + "초")
        lab1.pack()

#무작위 버튼 생성

def ranb():
    global btn
    btn=Button(win)
    btn.config(bg="red")
    btn.config(command=nxtb)
    btn.config(text=k)
    btn.place(relx=random.random(),rely=random.random())

#횟수 버튼을 누른 뒤 모든 버튼 날리기

def btf():
    global numt
    global start
    numt=int(ent.get())
    for wg in win.grid_slaves():
        wg.destroy()
    win.geometry("500x500")
    ranb()
    start=datetime.now()

#버튼 생성

btn=Button(win,text="시작")
btn.config(command=btf)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()

#a를 작동하는 함수 b를 적을 때 a-b 순서로 적어야 함