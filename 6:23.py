'''
날짜 : 6월 23일
작성자 : 박상혁
실습 내용 : 변수, 입출력 함수
'''
#변수, 표준출력합수
'''
변수 : 데이터를 저장하는 임시 공간
변수 사용법 : 변수명 = 값
ex) age = 23
!대입 연산자 : 오른쪽에 있는 값을 왼쪽 변수에 대입한다.
ex) blood_type = "B"

!!!표준 출력함수 : print()
1)문자열 출력
print('출력하고자하는 문자열')

2)변수에 저장된 값 출력
print(변수이름)

3) 변수에 저장된 값 + 문자 출력
print(변수명,"출력하고자 하는 문자열")


#ex1) 국민대학교 문자열 출력하자
print('국민대학교')

#ex2) univ변수에 저장된 값 출력하자
univ = "국민대학교"
print(univ)

#ex3) 나이를 변수에 저장한 후 출력하는 프로그램
#(출력 결과 예시 : ??살 입니다.)
age = 23
print(str(age)+"살 입니다.") #str() : 숫자를 문자열 형태로 변환하는 함수

#표준 입력 함수 : input()

#ex4) 이름을 입력받아 출력하자.
name = input('이름을 입력하세요:')
print(name)

#ex5) 나이를 입력받아 출력하는 프로그램
#(??살 입니다.)
age = input('나이를 입력하세요:')
print(str(age)+'살 입니다')

#ex6) 정수 2개를 입력받아 함을 구하는 프로그램
#(두수의 합은 ??입니다)

a = int(input("두 수를 입력하세요"))
b = int(input())
c = a+b
print("두 수의 합은", str(c)+"입니다.")
'''

# 실습 예제
#ex7) 이름과 혈액형을 입력받아 출력하는 프로그램
name = input("이름을 입력하세요:")
blood_type = input("혈액형을 입력하세요:")
print(str(name)+"님은", str(blood_type)+"형 입니다.")

#ex8) 학교이름과 학년을 입력받아 출력하는 프로그램
school_name = input("학교이름을 입력하세요:")
grade = input("학년을 입력하세요:")
print(str(school_name), str(grade)+"학년 입니다.")

#ex9) 두 정수를 입력받아 곱을 구하는 문제
num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세"))
num3 = num1 * num2
print(str(num1)+"과", str(num2)+"의 곱은", str(num3)+"입니다")


