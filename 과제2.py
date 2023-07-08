import turtle as t
import random as r

#1)

s=t.Screen()
s.title("park sang hyeok")
t.bgcolor("black")
t.speed(0)

def snow(color,l,x,y):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.down()

    for i in range(5):
        t.circle(l)
        t.rt(180)
        t.circle(l)
        t.rt(180)
    t.end_fill()
    t.ht()

for i in range(90):
    color = r.choice(['yellow','white','skyblue','silver'])
    l=r.randint(5,30)
    x = r.randint(-350,300)
    y = r.randint(-350,300)

    snow(color,l,x,y)

#2)

dic ={"그래픽카드":30,"노트북":3,"마우스":20,"마이크":5,"메모리":20,"스피커":5}

while True:
    print("# 재고 목록 #")
    for key, value in dic.items():
        print(key,value)
    
    print("***************")
    print("0. 종료")
    print("1. 재고 추가")
    print("2. 재고 삭제")
    print("***************")

    
    a=int(input("무엇을 하시겠습니까?:"))
    if a==0:
        print("프로그램 종료~")
        break
    elif a==1:
        b=input("물건의 이름을 입력하시오:")
        if b in dic:
            c=int(input("몇개를 추가하시겠습니까?:"))
            dic[b]=c+dic[b]
        else:
            dic.update({b:0})
            c=int(input("몇개를 추가하시겠습니까?:"))
            dic[b]=c+dic[b]
        
    elif a==2:
        b=input("물건의 이름을 입력하시오:")
        c=int(input("몇개를 추가하시겠습니까?:"))
        dic[b]=dic[b]-c
    else:
        continue
