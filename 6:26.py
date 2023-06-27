'''
날짜 : 6월 26일
작성자 : 박상혁
실습 내용 : 조건문, 터틀 그래픽
'''
'''
import turtle as t
t.shape("turtle")

#삼각형 그리기
t.color("blue")
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)

#육각형 그리기
t.color("red")
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)
t.fd(100)
t.lt(60)

#별 그리기
t.pensize(5)
t.color("yellow")
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)
t.fd(100)
t.rt(144)

name=t.textinput("이름","이름을 입력하시오:")
t.write("안녕하세요?"+name+"님")
t.speed(0)
t.bgcolor("yellow")
t.color("white")
t.fillcolor("white")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.rt(144)
'''
'''
#실습 1)
#터틀그래픽 사용
#원하는 도형을 그린다.
import turtle as t
t.shape("turtle")
t.bgcolor("yellow")
t.speed(0)
name = t.textinput("이름", "이름을 입력하세요:")
t.write(name+"님 안녕하세요",font=("Arial", 20, "bold"))
t.color("white")
t.fillcolor("white")
t.begin_fill()
for i in range(4):
    t.fd(100)
    t.rt(90)
t.end_fill()
t.ht()
'''
#실습 2)
import turtle as t
import random as r

s = t.Screen()

image1="삼겹살.gif"
image2="스파게티.gif"
image3="햄버거.gif"

s.addshape(image1)
s.addshape(image2)
s.addshape(image3)

dinner = r.randrange(3)

if dinner == 0:
    t.shape(image1)
elif dinner ==1:
    t.shape(image2)
else:
    t.shape(image3)



