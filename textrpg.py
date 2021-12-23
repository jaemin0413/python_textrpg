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
    php=hp #플레이어의 현재체력 정의

#텍스트 알피지 클리어시
def rpgclear():
    for wg in root.grid_slaves():
        wg.destroy()
    label=Label(root,text="텍스트 알피지 클리어 축하합니다!!")
    label.pack()

#텍스트 알피지 클리어 실패시
def rpgfail():
    for wg in root.grid_slaves():
        wg.destroy()
    label=Label(root,text="텍스트 알피지 클리어에 실패했습니다")
    label.pack()

#리스트-몬스터 목록
monlist=["좀비","해골","미라","흡혈귀"]
random.shuffle(monlist) #몬스터 리스트를 섞은 후 list[n]을 사용하여 몬스터를 만들어냄
n=0

#몬스터 생성 함수

def monspawn():
    global n
    global label4
    global mhp
    global atk1
    global hp1
    global name1
    
    atk1=random.randrange(2,5) # 생성 몬스터의 랜덤 공격력
    hp1=random.randrange(5,8)  # 생성 몬스터의 랜덤 체력
    mhp=hp1                    # 몬스터의 현재체력 정의
    name1=monlist[n]           # 몬스터의 이름

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
    
    atk1=random.randrange(8,12) #보스의 랜덤 공격력
    hp1=random.randrange(40,50) #보스의 랜덤 체력
    mhp=hp1                     #보스의 체력 정의

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

    atk=atk+atk1 #몬스터의 공격력 흡수
    hp=hp+hp1    #몬스터의 체력 흡수
    php=hp       #기존 체력 회복
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}".format(name,atk,hp))
    n+=1         #나오는 몬스터의 이름을 바꿈

    if n == 4:          #n이 4일 때 보스 스폰
        bossspawn() 
    elif n<4:           #n이 3 이하일 때 일반 몬스터 스폰
        monspawn()
    elif n==5:          #보스를 클리어시 n이 1 올라감, 이때 알피지 클리어 함수 수행
        rpgclear()


#몬스터 체력 체크

def moncheck():  #공격 후 몬스터의 체력을 주기적으로 체크하여 체력이 음수일 때 함수 수행
    global mhp
    global n
    global label5

    if mhp<=0:
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,atk1,mhp,hp1))
        time.sleep(0.2)
        label5=Label(root,text="{0} 처치!".format(name1))
        label5.grid(row=3,column=1)
        statadd() # 몬스터의 스텟 흡수
                

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
    
    if n <= 3: #n이 3 이하일 때 일반 몬스터를 상대할 경우
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name1,atk1,mhp,hp1))
    else:      #n이 4일 때 보스 몬스터를 상대할 경우
        label4.config(text="{0} \n공격력{1} \n체력{2}/{3}".format("보스",atk1,mhp,hp1))

    moncheck() #몬스터 체력 확인
    attacked() #공격받기

#공격받기
def attacked():
    global php
    global atk
    global atk1
    global hp1
    global name
    global label3
    
    php=php-atk1 #플레이어의 현재체력에서 몬스터의 공격력 빼기
    label3.config(text="{0} \n공격력{1} \n체력{2}/{3}".format(name,atk,php,hp))

    if php<0:    #체력이 0 이하로 떨어지면 클리어 실패
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
    for wg in root.grid_slaves(): #그리드로 지정된 모든 함수 파괴
        wg.destroy()

    b1 = ttk.Button(root, text="공격") #공격버튼
    b1.config(command=attack)          #공격 커맨드 실행
    b1.grid(row=2, column=0, pady=70)

    b2 = ttk.Button(root, text="회복") #회복버튼
    b2.config(command=heal)            #회복 커맨드 실행
    b2.grid(row=2, column=1, pady=70)

    b3 = ttk.Button(root, text="도망") #도망버튼
    b2.config(command=run)             #도망 커맨드 실행
    b3.grid(row=2, column=2, pady=70)

    label3=Label(root)  #플레이어의 체력을 나타내는 3번째 라벨
    label3.config(text= "{0} \n공격력 {1} \n체력 {2}".format(name,atk,hp))
    label3.grid(row=1, column=0)
    monspawn() # 첫번째 몹 스폰
        

#이름 초기화
def clear(event):
    if entry.get()=="당신의 이름은 무엇인가요?":
        entry.delete(0,len(entry.get()))
    stat()
entry.bind("<Button-1>",clear)


#엔트리에서 받아온 이름 저장, 출력
b4 = ttk.Button(root, text="확인")
b4.config(command=NAME)
b4.grid(row=1, column=1, pady=20)

#des 함수 시동
b5= ttk.Button(root, text="다음")
b5.config(command=des)
b5.grid(row=1, column=2)


#라벨 생성, 미리 생성해둔 라벨들
label1=Label(root)
label1.grid(row=3,column=1,pady=10)

label2=Label(root)
label2.grid(row=4,column=1,pady=10)


#창 실행
root.mainloop()
