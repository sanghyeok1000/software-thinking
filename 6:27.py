'''
날짜 : 6월 27일
작성자 : 박상혁
실습 내용 : 반복문(for)
'''
'''
#ex1) 이름 10번 출력하기
for i in range(10):
    print("박상혁", end=" ")

#ex2) 10부터 15까지 출력하기
for i in range(10, 16):
    print(i, end=" ")

#ex3) 1부터 10까지 합
a = 0
for i in range(1, 11):
    a = a + i
print(a)

#ex4) 1부터 10까지 홀수 출력
for i in range(1,11):
    if i%2==1:
        print(i, end=" ")
    else:
        pass

#ex5) 1부터 10까지 곱 출력
a = 1
for i in range(1,11):
    a = a*i
print(a)
'''
import turtle as t
import random as r
t.shape("turtle")
t.speed(0)
'''
for i in range(6):
    t.circle(100)
    t.lt(360/6)

for i in range(3):
    t.fd(100)
    t.lt(360/3)

t.up()
t.goto(200,0)
t.down()

for i in range(4):
    t.fd(100)
    t.lt(360/4)

s=t.textinput("", "몇각형을 원하시나요?:")
n = int(s)

for i in range(n):
    t.fd(100)
    t.lt(360/n)

#ex6) 사각형 4개 그리기(한개는 색칠하기)
t.bgcolor("blue")
a = r.randint(1,5)
for i in range(1,5):
    t.up()
    t.goto(50*i,0)
    t.down()
    if i == a:
        t.fillcolor("yellow")
        t.begin_fill()
        for j in range(4):
            t.fd(50)
            t.lt(360/4)
        t.end_fill()
    else:
        for j in range(4):
            t.fd(50)
            t.lt(360/4)
    
        

#ex7) 사용자로부터 정수 n을 입력받아 n각형 그리기
s = t.textinput("", "몇각형을 원하시나요?:")
n = int(s)

for i in range(n):
    t.fd(100)
    t.lt(360/n)
'''
import turtle
import random as r

turtle.ht()

t1 = turtle.Turtle()
t2 = turtle.Turtle()

s = turtle.Screen()

s.title("20201916 박상혁")
s.bgpic("배경화면.png")

turtle = '거북이.gif'
rabbit = '토끼.gif'

s.addshape(turtle)
s.addshape(rabbit)

t1.shape(turtle)
t2.shape(rabbit)

t1.up()
t2.up()

t1.speed(0)
t2.speed(0)

t1.goto(-400,150)
t2.goto(-400,-150)

t1.speed(1)
t2.speed(1)

for i in range(35):
    t1.fd(r.randint(1,40))
    t2.fd(r.randint(1,40))
