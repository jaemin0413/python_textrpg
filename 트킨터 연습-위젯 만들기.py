from tkinter import *

#창 만들기
star=Tk()
star.geometry("400x200")
star.title("위젯클릭")

#버튼 만들기
button=Button(star, text="클릭")
def insert():
    button.pack(side=entry.get())

button.config(command=insert)
button.pack(side="bottom")

#엔트리 만들기
entry=Entry(star)
entry.pack(side="top")
entry.insert(0,"방향을 입력해주세여")
def clear(event):
    if entry.get()=="방향을 입력해주세여":
        entry.delete(0,len(entry.get()))
entry.bind("<Button-1>",clear)
entry.pack()


star.mainloop()