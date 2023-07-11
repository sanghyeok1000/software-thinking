import turtle as t
import random as r
'''
s=t.Screen()
t.title("park sang hyeok")
t.bgcolor("black")
t.speed(0)
t.ht()

def star(x,y,d,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(d)
        t.lt(144)
    t.end_fill()

for i in range(100):
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    color=r.choice(["blue","red","yellow","pink"])
    d=r.randint(10,30)
    star(x,y,d,color)
'''
dic={"그래픽카드":30,"노트북":3,"마우스":20,"마이크":5,"메모리":20,"스피커":5}
while True:
    print("# 재고 목록 #")
    for key, value in dic.items():
        print(key, value)
    print("********************")
    print("0 종료")
    print("1 재고 추가")
    print("2 재고 삭제")
    print("********************")
    a= int(input("무엇을 하시겠습니까?"))
    
    if a==0:
        print("프로그램 종료")
        break
    elif a==1:
        b=input("물건의 이름을 입력하세요:")
        c=int(input("몇 개를 추가하시겠습니까?"))
        if b in dic:
            dic[b]=dic[b] +c
        else:
            dic.update({b:c})
    elif a==2:
        b=input("물건의 이름을 입력하세요:")
        c=int(input("몇 개를 삭제하시겠습니까?"))
        dic[b]=dic[b]-c
    else:
        continue
        
