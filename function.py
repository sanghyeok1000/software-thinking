import turtle as t
import random as r
'''
실습 내용: 함수

s=t.Screen()
s.listen()
t.mainloop()
onkey(함수명, "코드")
onscreenclick() : 화면을 클릭했을 때 함수를 실행

#ex1) 화면을 마우스로 클릭하면 해당 좌표로 이동하여 선을 그려주는 예제
import turtle as t

def draw(x,y):
    t.goto(x,y)

t.shape("turtle")
t.pensize(5)
t.color("red")
s=t.Screen()
s.onscreenclick(draw)
s.onkey(t.up,"Up")
s.onkey(t.down, "Down")
s.listen()


#ex2) 화면을 클릭하면 사각형이 그려지는 프로그램
t.ht()
t.speed(0)

def squ(d,color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.fd(d)
        t.lt(90)
    t.end_fill()
def draw(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    squ(100, "yellow")
s=t.Screen()
s.onscreenclick(draw)

#ex3) 지정한 위치에 별그리기
t.ht()
t.speed(0)

def star(d,color):
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(100)
        t.lt(144)
    t.end_fill()
def draw(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    star(100, "yellow")
s=t.Screen()
t.bgcolor("gray")
s.onscreenclick(draw)

#ex4) 임의의 위치에 여러가지 크기의 별 그리는 프로그램
import random as r
t.write("박상혁", font=("Arial",20,"bold"))
t.ht()
t.speed(0)

def star(x,y):
    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    a=r.randint(10, 50)
    for i in range(5):
        t.fd(a)
        t.lt(144)
    t.end_fill()

s=t.Screen()
t.bgcolor("gray")
for i in range(30):
    star(r.randint(-300,300),r.randint(-300,300))

#ex1)
import random as r
t.write("박상혁", font=("Arial",20,"bold"))
t.ht()
t.speed(0)

def star(x,y):
    t.up()
    t.goto(x,y)
    t.down()

    t.begin_fill()
    a=r.randint(10, 50)
    for i in range(5):
        t.fd(a)
        t.lt(144)
    t.end_fill()

s=t.Screen()
t.bgcolor("gray")
t.onscreenclick(star)

#ex2)
def Print(x,y):
    t.goto(x,y)
    t.stamp()
    t.write("x:%d, y:%d"%(x,y))
def Clear(x,y):
    t.reset()

#onscreenclick 함수의 두번째 인수
#1:왼쪽 버튼, 2:가운데 버튼, 3:오른쪽 버튼
t.shape("circle")
t.setup(500, 500)
t.up()
t.onscreenclick(Print)
t.onscreenclick(Clear, 3)


#ex3) 눈그리기

t.color("yellow")
t.color("blue")
t.write("소프트웨어적사고", align="center", font=("arial",30,"bold"))

def snow():
    size = r.randint(10,30)
    for i in range(12):
        t.fd(size)
        t.back(size)
        t.rt(30)

t.bgcolor("black")
t.color("white")
t.pensize(2)

t.ht()
t.speed(0)

for i in range(40):
    t.up()
    x = r.randint(-400, 400)
    y = r.randint(-400, 400)
    t.goto(x,y)
    t.down()
    snow()

#ex4)
t.bgcolor("black")
t.speed(0)

def draw_star(color,length,x,y):
    t.color(color)
    t.begin_fill()
    t.up()
    t.goto(x,y)
    t.down()

    for i in range(5):
        t.fd(length)
        t.lt(144)
    t.end_fill()
    t.ht()

for i in range(90):
    color = r.choice(['yellow','white','skyblue','silver','gold'])
    length=r.randint(10,60)
    x = r.randint(-350,300)
    y = r.randint(-350,300)

    draw_star(color,length,x,y)
'''
#ex5)
dic ={"우유":1,"종이컵":2,"책":5,"커피음료":7,"콜라":4,"펜":3}

while True:
    print("# 재고 목록 #")
    print('우유',dic['우유'])
    print("종이컵",dic["종이컵"])
    print("책",dic["책"])
    print("커피음료",dic["커피음료"])
    print("콜라",dic["콜라"])
    print("펜",dic["펜"])
    
    print("***************")
    print("0. 종료")
    print("1. 재고 추가")
    print("2. 재고 삭제")
    print("***************")

    
    a=int(input("무엇을 하시겠습니까?:"))
    if a==0:
        break
    elif a==1:
        b=input("물건의 이름을 입력하시오:")
        c=int(input("몇개를 추가하시겠습니까?:"))
        dic[b]=c+dic[b]
        
    elif a==2:
        b=input("물건의 이름을 입력하시오:")
        c=int(input("몇개를 추가하시겠습니까?:"))
        dic[b]=dic[b]-c
    else:
        continue
    
