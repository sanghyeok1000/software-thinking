'''
날짜 : 6월 28일
이름 : 박상혁
실습 내용 : 반복문(while)

#예제1) 20부터 30까지 합을 구하는 프로그램
a=0
for i in range(20,31):
    a= a+i
print(a)

#예제2) 정수를 입력받아 짝수인지 판별하는 프로그램
a = int(input())
if a%2 == 0:
    print(str(a)+"은 짝수입니다")
else:
    print(str(a)+"은 홀수입니다.")

#예제3) 별그리기             
import turtle as t
t.shape("turtle")
t.speed(0)
t.title("별")
t.color("yellow")
t.fillcolor("yellow")
t.begin_fill()
for i in range(5):
    t.fd(100)
    t.lt(144)
t.end_fill()

#예제4) 출력하고 싶은 단을 입력받아 해당 단을 출력하는 프로그램
num= int(input("출력하고 싶은 단을 입력하세요:"))
for i in range(1, 10):
    print(num,"*",i,"=",num*i)

#예제5) 정수를 입력받아 제곱을 구하는 프로그램
a=int(input("정수를 입력하세요:"))
print(a**2)
print(pow(a,2))

#예제6) 혈액형을 입력받아 출력하는 프로그램
blood= input("혈액형을 입력하세요:")

if blood=="a"or blood=="A":
    print("A형 입니다.")
elif blood=="b" or blood=="B":
    print("B형입니다.")
elif blood=="o" or blood=="O":
    print("O형입니다.")
elif blood=="ab" or blood=="AB"or blood=="aB" or blood=="Ab":
    print("AB형입니다.")
else:
    print("혈액형을 입력하세요")

#예제7) 20부터 30까지 합을 구하는 프로그램
a=20
b=0
while a<=30:
    b = a + b
    a +=1
print(b)

#예제 8) 1부터 10까지의 곱을 구하는 프로그램
a=1
b=1
while a <=10:
    b = a*b
    a+=1
print(b)

#예제9) 이름과 혈액형을 입력 받아 출력하는 프로그램
#???님은 ???형 입니다.

while True:
    name, blood = map(str, input("이름과 혈액형을 입력하세요:").split())

    if blood=="a"or blood=="A":
        print(name,"님은 A형 입니다.")
        break
    elif blood=="b" or blood=="B":
        print(name,"님은 B형입니다.")
        break
    elif blood=="o" or blood=="O":
        print(name,"님은 O형입니다.")
        break
    elif blood=="ab" or blood=="AB"or blood=="aB" or blood=="Ab":
        print(name,"님은 AB형입니다.")
        break
    else:
        continue
'''
