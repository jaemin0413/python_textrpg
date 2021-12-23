#창 띄우기, 트킨터 사용
from tkinter import *
from tkinter import ttk
import random


#창의 형태 
root = Tk()
root.title("TEXTRPG")
root.geometry("300x400")


#이름 입력창
entry = ttk.Entry(root, width=37)
entry.insert(0,"당신의 이름은 무엇인가요?")
entry.grid(row=0, columnspan=3)



#랜덤스탯
def stat():    
    global atk
    global hp
    atk=random.randrange(3,7)  #플레이어 공격력
    hp=random.randrange(3,10)  #플레이어 체력


#클래스-몬스터 공체

class monster:
    def setmon(self,atk1,hp1): #atk1 몬스터 공격력, hp1 몬스터 체력
        self.atk1=atk1
        self.hp1=hp1
        
#몬스터 생성
a=monster() #1번 몬스터
a.setmon(random.randrange(1,3),random.randrange(3,6))

b=monster() #2번 몬스터
b.setmon(random.randrange(1,3),random.randrange(3,6))

c=monster() #3번 몬스터
c.setmon(random.randrange(1,3),random.randrange(3,6))

d=monster() #4번 몬스터
d.setmon(random.randrange(1,3),random.randrange(3,6))


#리스트-몬스터 목록
monlist=["좀비","해골","미라","흡혈귀"]
name1=random.choice(monlist)
name2=random.choice(monlist)
name3=random.choice(monlist)
name4=random.choice(monlist)


#몬스터 랜덤 생성

def monspawn1():
    global label4
    global mhp
    mhp =a.hp1
    
    label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}".format(name1,a.atk1,a.hp1))
    label4.grid(row=1, columnspan=10, padx=60)
    
    if mhp<0:
        monspawn2()

def monspawn2():
    global label4
    #label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}".format(name2,b.atk1,b.hp1))
    #label4.grid(row=1, columnspan=10, padx=60)

    if mhp<0:
        monspawn3()

def monspawn3():
    global label4
    label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}".format(name3,c.atk1,c.hp1))
    label4.grid(row=1, columnspan=10, padx=60)

    if mhp<0:
        monspawn4()

def monspawn4():
    global label4
    label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}".format(name4,d.atk1,d.hp1))
    label4.grid(row=1, columnspan=10, padx=60)

#공격
def attak():
    global mhp #이거 글로벌 선언 안 하면 mhp로 이름이 같은 다른 변수로 인식함. 꼭 글로벌 붙일 것!!
    global atk
    mhp=mhp-atk
    label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,a.atk1,mhp,a.hp1))
    monspawn1()

#회복
def heal():    
    global php
    global hp

    php=hp
    if php < hp:
        php=hp+3
        label3.config(text= "{0} \n공격력 {1} \n체력 {2}/{3}".format(name,atk,php,hp))
    



#그리드 초기화

def des():
    global label3
    for wg in root.grid_slaves():
        wg.destroy()

    b1 = ttk.Button(root, text="공격")
    b1.config(command=attak)
    b1.grid(row=2, column=0, pady=70)

    b2 = ttk.Button(root, text="회복")
    b2.config(command=heal)
    b2.grid(row=2, column=1, pady=70)

    b3 = ttk.Button(root, text="도망")
    
    b3.grid(row=2, column=2, pady=70)

    label3=Label(root)
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}".format(name,atk,hp))
    label3.grid(row=1, column=0)
    monspawn1()
        

#이름 초기화
def clear(event):
    if entry.get()=="당신의 이름은 무엇인가요?":
        entry.delete(0,len(entry.get()))
    stat()
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

#des 함수 시동
b5= ttk.Button(root, text="다음")
b5.config(command=des)
b5.grid(row=3, column=2)


#이름 나타내기
def NAME():
    global name
    global atk
    global hp
    name=entry.get()
    label1.config(text="안녕하세요 {0}".format(name))
    label2.config(text="공격력 {0} 체력 {1}".format(atk,hp))
b4.config(command=NAME)

b4.grid(row=2, column=1, pady=20)


#라벨 생성
label1=Label(root)
label1.grid(row=3,column=1,pady=10)

label2=Label(root)
label2.grid(row=4,column=1,pady=10)


#창 실행
root.mainloop()
