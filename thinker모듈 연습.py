#창 띄우기, 트킨터 사용
from tkinter import *
from tkinter import ttk
 
 
#창의 형태 
root = Tk()
root.title("TEXTRPG")
root.geometry("300x400")
 

#이름 입력창
entry = ttk.Entry(root, width=37)
entry.insert(0,"당신의 이름은 무엇인가요?")
entry.grid(row=0, columnspan=3)
def clear(event):
    if entry.get()=="당신의 이름은 무엇인가요?":
        entry.delete(0,len(entry.get()))

entry.bind("<Button-1>",clear)
 

#버튼 만들기
b1 = ttk.Button(root, text="공격")
b1.grid(row=1, column=0)

b2 = ttk.Button(root, text="회복")
b2.grid(row=1, column=1)

b3 = ttk.Button(root, text="도망")
b3.grid(row=1, column=2)

#엔트리에서 받아온 이름 저장, 출력
b4 = ttk.Button(root, text="확인")

def NAME():
    name=entry.get()
    label1.config(text="안녕하세요 {0}".format(name))
b4.config(command=NAME)

b4.grid(row=2, column=1, pady=20)

#라벨 생성
label1=Label(root)
label1.grid(row=3,column=1,pady=10)



#창 실행
root.mainloop()
