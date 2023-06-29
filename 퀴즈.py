'''
이름 : 박상혁
날짜 : 6월 28일
'''

import turtle as t
import random as r

#1)
import turtle as t
t.shape("turtle")
t.bgcolor("blue")
t.color("yellow")
t.speed(0)
t.fillcolor("red")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.lt(72)
t.end_fill()

#2)
import random as r
a= r.randrange(2)
if a == 1:
    print("동전 앞면")
else:
    print("동전 뒷면")
print("게임 종료")

#3)

a = 0
for i in range(30,41):
    a = a + i
print(a)

#4)
for i in range(6):
    a = r.randint(1,46)
    print(a)

#5)
color = input("색깔을 입력하세요:")
if color == "G" or color == "GREEN":
    print("진행")
elif color == "R" or color == "RED":
    print("정지")
elif color == "Y" or color == "YELLOW":
    print("주의")
else:
    pass

#6)
a,b = input("성별과 이름을 입력하세요:").split()
if a == "남자":
    print(b+"님은", a+"입니다.")
elif a == "여자":
    print(b+"님은", a+"입니다.")
else:
    pass
    
