'''
import turtle as t
import random as r

def snow(l,color,x,y):
    
    t.up()
    t.goto(x,y)
    t.down()
    
    
    t.color(color)
    t.begin_fill()
    t.circle(l)
    t.lt(180)
    t.circle(l)
    t.end_fill()

t.ht()
t.speed(0)
t.title("park sang hyeok")
t.bgcolor("black")

for i in range(100):
    color=r.choice(["yellow","gray", "white","skyblue"])
    x=r.randint(-350,300)
    y=r.randint(-350,300)
    l=r.randint(10,30)

    snow(l,color,x,y)


dic = {"그래픽카드":30,"노트북":3,"마우스":20,"마이크":5,"메모리":20,"스피커":5}

while True:
    print("# 재고 목록 #")
    for key, value in dic.items():
        print(key,value)

    print("*********************")
    print("0.종료")
    print("1.재고 추가")
    print("2.재고 삭제")
    print("*********************")
    a=input("무엇을 하시겠습니까?:")
    
    if a==0:
        break
    elif a=="1":
        b=input("물건의 이름을 입력하시오:")
        if b in dic:
            c=int(input("몇 개를 추가하시겠습니까?:"))
            dic[b]=c+dic[b]
        else:
            c=int(input("몇 개를 추가하시겠습니까?:"))
            dic.update({b:c})
            
    elif a=="2":
        b=input("물건의 이름을 입력하시오:")
        c=int(input("몇 개를 삭제하시겠습니까?:"))
        dic[b]=dic[b]-c
    else:
        continue

'''
dic = {"그래픽카드":30,"노트북":3,"마우스":20,"마이크":5,"메모리":20,"스피커":5}
print(dic)
del(dic["노트북"])
print(dic)
dic["노트북"]=3
print(dic)
print(dic.get("그래픽카드"))
print(dic.keys())
print(dic.values())
print(list(dic.keys()))
print(list(dic.values()))
