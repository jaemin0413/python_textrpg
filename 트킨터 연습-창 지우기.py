from tkinter import *
#트킨터 생성

txt=Tk()
txt.title("창 초기화, 버튼 랜덤")
txt.geometry("500x150")

#엔트리 만들기
ent=Entry(txt)
ent.grid (row=0,column=1, padx=20, pady=20)

#버튼 만들기

btn1=Button(txt,text="시작")
btn1.grid (row=1,column=0,columnspan=2)

def btnf():
    for wg in txt.grid_slaves():
        wg.destroy()
    name=ent.get()
    lab2.config(text="안녕하세요 {0}".format(name))
btn1.config(command=btnf)

#라벨 만들기
lab1=Label(txt,text="당신은 누구입니까?")
lab1.grid (row=0,column=0, padx=20, pady=20)

lab2=Label(txt)
lab2.grid(row=0,column=0)



txt.mainloop()