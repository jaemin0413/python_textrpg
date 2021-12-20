#창 띄우기, 트킨터 사용
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("로그인하세용")
root.geometry("400x300")

#id 라벨
lb1=Label(root, text="ID")
lb1.pack()

#id 입력창
entry1=Entry(root)
entry1.insert(0,"@email.com")
def clear(event):
    if entry1.get() =="@email.com":
        entry1.delete(0,len(entry1.get()))

entry1.bind("<Button-1>",clear)
entry1.pack()

#pw 라벨
lb2=Label(root,text="PW")
lb2.pack()

#pw 입력창
entry2=Entry(root, show="*")
entry2.pack()

#로그인버튼

button=Button(root,text="로그인")
def login():
    inid=entry1.get()
    inpw=entry2.get()
    lab3.config(text="id={0},pw={1}".format(inid,inpw))
    

button.config(command=login)
button.pack()

#로그인시 라벨 발생
lab3=Label(root)
lab3.pack()

root.mainloop()
