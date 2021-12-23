#창 띄우기, 트킨터 사용
from tkinter import *
from tkinter import ttk
import random
import time


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
    global php
    atk=random.randrange(3,7)  #플레이어 공격력
    hp=random.randrange(3,10)  #플레이어 체력

    php=hp

#클리어시
def rpgclear():
    for wg in root.grid_slaves():
        wg.destroy()
    label=Label(root,text="텍스트 알피지 클리어 축하합니다!!")
    label.pack()

#클리어 실패시
def rpgfail():
    for wg in root.grid_slaves():
        wg.destroy()
    label=Label(root,text="텍스트 알피지 클리어에 실패했습니다")
    label.pack()

#리스트-몬스터 목록
monlist=["좀비","해골","미라","흡혈귀"]
random.shuffle(monlist)
n=0

#몬스터 생성 함수

def monspawn():
    global n
    global label4
    global mhp
    global atk1
    global hp1
    global name1
    
    atk1=random.randrange(2,4)
    hp1=random.randrange(5,7)
    mhp=hp1
    name1=monlist[n]

    label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,atk1,mhp,hp1))
    label4.grid(row=1, columnspan=10, padx=60)


#보스 생성 함수
def bossspawn():
    global n
    global label4
    global mhp
    global atk1
    global hp1
    global name1
    
    atk1=random.randrange(8,14)
    hp1=random.randrange(50,60)
    mhp=hp1

    label4=Label(root)
    label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format("보스",atk1,mhp,hp1))
    label4.grid(row=1, columnspan=10, padx=60)


#몬스터 스탯 흡수
def statadd():
    global atk
    global atk1
    global hp
    global hp1
    global label3
    global n
    global bossspawn
    global php

    atk=atk+atk1
    hp=hp+hp1
    php=hp
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}".format(name,atk,hp))
    n+=1

    if n == 4:
        bossspawn()
    elif n<4:
        monspawn()
    elif n==5:
        rpgclear()


#몬스터 체력 체크

def moncheck():
    global mhp
    global n
    global label5

    la=Label(root,text=n)
    la.grid(row=4,column=1)

    if mhp<=0:
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,atk1,mhp,hp1))
        time.sleep(0.2)
        label5=Label(root,text="{0} 처치!".format(name1))
        label5.grid(row=3,column=1)
        statadd()
                

#이름 나타내기
def NAME():
    global name
    global atk
    global hp
    name=entry.get()
    label1.config(text="안녕하세요 {0}".format(name))
    label2.config(text="공격력 {0} 체력 {1}".format(atk,hp))


#공격
def attack():
    global mhp #이거 글로벌 선언 안 하면 mhp로 이름이 같은 다른 변수로 인식함. 꼭 글로벌 붙일 것!!
    global atk
    global atk1
    global hp1
    global name1
   
    mhp=mhp-atk
    
    if n <= 3:
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,atk1,mhp,hp1))
    else:
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format("보스",atk1,mhp,hp1))

    moncheck()
    attacked()

#공격받기
def attacked():
    global php
    global atk
    global atk1
    global hp1
    global name
    global label3
    
    php=php-atk1
    label3.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name,atk,php,hp))

    if php<0:
        rpgfail()

    

#회복
def heal():    
    global php
    global hp
    global label3

    php=hp+5
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}/{3}".format(name,atk,php,hp))

    attacked()

#도망

def run():
    monspawn()






#그리드 초기화

def des():
    global label3
    for wg in root.grid_slaves():
        wg.destroy()

    b1 = ttk.Button(root, text="공격")
    b1.config(command=attack)
    b1.grid(row=2, column=0, pady=70)

    b2 = ttk.Button(root, text="회복")
    b2.config(command=heal)
    b2.grid(row=2, column=1, pady=70)

    b3 = ttk.Button(root, text="도망")
    b2.config(command=run)
    b3.grid(row=2, column=2, pady=70)

    label3=Label(root)
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}".format(name,atk,hp))
    label3.grid(row=1, column=0)
    monspawn()
        

#이름 초기화
def clear(event):
    if entry.get()=="당신의 이름은 무엇인가요?":
        entry.delete(0,len(entry.get()))
    stat()
entry.bind("<Button-1>",clear)


#버튼 만들기, 첫번째 화면에선 필요없음
#b1 = ttk.Button(root, text="공격")
#b1.grid(row=1, column=0)

#b2 = ttk.Button(root, text="회복")
#b2.grid(row=1, column=1)

#b3 = ttk.Button(root, text="도망")
#b3.grid(row=1, column=2)


#엔트리에서 받아온 이름 저장, 출력
b4 = ttk.Button(root, text="확인")
b4.config(command=NAME)
b4.grid(row=2, column=1, pady=20)

#des 함수 시동
b5= ttk.Button(root, text="다음")
b5.config(command=des)
b5.grid(row=3, column=2)





#라벨 생성
label1=Label(root)
label1.grid(row=3,column=1,pady=10)

label2=Label(root)
label2.grid(row=4,column=1,pady=10)


#창 실행
root.mainloop()
