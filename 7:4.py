'''
날짜 : 7월 4일
작성자 : 박상혁
실습 내용 : 딕셔너리, 함수

#ex1) 정보를 나타내는 딕셔너리 생성
info = {"학과":"나노전자물리학과", "학번":"20201916","이름":"박상혁"}
print(info)
del(info["학번"])
print(info)
info["연락처"] = "010-0000-0000"
print(info)
info["학과"]="소프트웨어"
print(info)

print(info.get("이름"))
print(info["이름"])
print(list(info.keys()))
print(list(info.values()))
print("연락처" in info)
print("이름" in info)

#ex2) 영한사전 딕셔너리 생성

1) 항목 3개 생성
2)항목 하나 추가
3)항목 하나 삭제
4)항목 하나 수정
5)키로 값 접근
6)모든 키 반환
7)모든 값 반환

note = {"사과":"apple", "가방":"bag", "컴퓨터":"computer"}
note["노란색"]="yellow"
del(note["컴퓨터"])
note["가방"]="가방"
print(note["사과"])
print(note.keys())
print(note.values())

#ex3) 함수 이름을 출력하는 함수
def univ():
    print("국민대학교")
univ()

#ex4) 거듭제곱을 출력하는 함수(반환값이 없는 경우)
def square(num):
    print(num**num)
square(4)

#ex5) 정수의 거듭제곱을 계산하는 함수(반환값이 있는 출력)
def square(num):
    return num**num
print(square(4))

#ex6) 이름을 입력받아 이름을 출력하는 함수(반환값이 없는 경우)
def func(name):
    print(name)
name=input("이름을 입력하세요:")
func(name)


#ex7) 두 정수를 입력받아 합을 구하는 함수(반환값 있는 경우)
a= int(input())
b= int(input())
def sum(a, b):
    return a+b
print(sum(a,b))
'''
