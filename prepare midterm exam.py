'''
print("*** Item ***")
print("1. apple")
print("2. banana")
print("3. kiwi")
a = int(input("select Item (1~3)? ="))
b = int(input("Input the number of Item(1~)?"))
if a == 1:
    print("*** Total Price ***")
    print(3000*b)
elif a==2:
    print("*** Total Price ***")
    print(4000*b)
else:
    print("*** Total Price ***")
    print(6000*b)


import turtle
import random as r

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

s = turtle.Screen()

t1.color("pink")
t2.color("blue")
t3.color("green")

t1.shapesize(2)
t2.shapesize(2)
t3.shapesize(2)

t1.shape("turtle")
t2.shape("turtle")
t3.shape("turtle")

t1.speed(0)
t2.speed(0)
t3.speed(0)

t1.up()
t2.up()
t3.up()

t1.goto(-300,50)
t2.goto(-300,0)
t3.goto(-300,-50)

t1.speed(1)
t2.speed(1)
t3.speed(1)

for i in range(15):
    t1.fd(r.randint(1,50))
    t2.fd(r.randint(1,50))
    t3.fd(r.randint(1,50))
'''
money = 10000

while True:

    print("---menu---")
    print("메뉴를 선택하세요.")
    a = int(input("1.아메리카노 2.루이보스티 3.카라멜마끼아또"))
    
    if a==1:
        if money >= 4000:
            print("총 주문금액 4000원")
            money = money - 4000
            print("카드잔액", money)
        else:
            print("잔액이 부족합니다. 현재잔액", money)
            break
        
    elif a==2:

        if money >= 5000:
            print("총 주문금액 5000원")
            money = money - 5000
            print("카드잔액", money)
        else:
            print("잔액이 부족합니다. 현재잔액", money)
            break
        
    elif a==3:
        if money >= 6000:
            print("총 주문금액 6000원")
            money = money - 6000
            print("카드잔액", money)
        else:
            print("잔액이 부족합니다. 현재잔액", money)
            break
    else:
        continue
    
