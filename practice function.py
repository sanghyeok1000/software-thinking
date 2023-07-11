import turtle as t
import random as r
'''
def draw(x,y):
    t.goto(x,y)

t.shape("turtle")
t.speed(0)
t.pensize(2)
t.color("red")
s=t.Screen()
s.onscreenclick(draw)
s.onkey(t.up,"Up")
s.onkey(t.down,"Down")
s.listen()


#ex2) 화면을 클릭하면 사각형이 그려지는 프로그램
t.ht()
t.speed(0)

def squ(d, color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.fd(d)
        t.lt(90)
    t.end_fill()

def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    squ(100, "yellow")


s=t.Screen()
t.onscreenclick(go)

#ex3) 지정한 위치에 별그리기
t.speed(0)
t.ht()

def star(color, d):
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.fd(d)
        t.lt(144)
    t.end_fill()
def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    star("yellow",100)
s=t.Screen()
t.bgcolor("black")
t.onscreenclick(go)

#ex4) 임의의 위치에 여러가지 크기의 별 그리는 프로그램
t.ht()
t.speed(0)

def star(color):
    t.color(color)
    t.begin_fill()
    d=r.randint(10,30)
    for i in range(5):
        t.fd(d)
        t.lt(144)
    t.end_fill()
def go(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    star("yellow")
    
s=t.Screen()
for i in range(30):
    go(r.randint(-300,300),r.randint(-300,300))


t.speed(0)
t.ht()

def go(x, y):
    t.up()
    t.goto(x,y)
    t.down()
    star("yellow")

def star(color):
    t.color(color)
    t.begin_fill()
    a=r.randint(10,30)
    for i in range(5):
        t.fd(a)
        t.lt(144)
    t.end_fill()

t.bgcolor("black")
s=t.Screen()
t.onscreenclick(go)

def Print(x,y):
    t.goto(x,y)
    t.stamp()
    t.write("x:%d, y:%d" %(x,y))
def Clear(x,y):
    t.reset()
t.shape("turtle")
t.up()
t.setup(500,500)
t.onscreenclick(Print)
t.onscreenclick(Clear,2)

t.ht()
t.speed(0)
t.bgcolor("black")
t.color("white")
def snow():
    t.begin_fill()
    d=r.randint(10,30)
    t.circle(d)
    t.lt(180)
    t.circle(d)
    t.end_fill()
for i in range(40):
    t.up()
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    t.goto(x,y)
    t.down()
    snow()
'''
#색깔과 크기를 랜덤으로 그리는 별 그리기
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

for i in range(90):
    color=r.choice(["blue","red","pink","yellow"])
    x=r.randint(-300,300)
    y=r.randint(-300,300)
    d=r.randint(10,30)
    star(x,y,d,color)
