'''
날짜 : 6월 29일
이름 : 박상혁
실습 내용 : 리스트
'''
'''
#ex1) 학과를 나타내는 리스트
major = ["물리학과", "수학과", "소프트웨어", "기계공학"]
print(major)
print(major[0])
print(major[1:3])
print(major[2:])
print(major[:4])

#ex2) 계절을 나타내는 리스트
seasons = []
print(seasons)
seasons.append("봄")
print(seasons)
seasons.pop()
print(seasons)
seasons.append("여름")
print(seasons)
seasons.append("겨울")
print(seasons)
seasons.insert(1,"가을")
print(seasons)
seasons.reverse()
print(seasons)
seasons.sort()
print(seasons)

#ex3) 정수 5개가 있는 리스트
num=[1,2,3,4,5]
del(num[4])
print(num)
print(len(num))
num[0] = 5
print(num)

#ex4) 좌석 예매 프로그램
seat=[0,0,0,0,0,0,0,0,0,0]

while True:
    a=input("좌석을 예약하시겠습니까?[YES/NO]")
    if a == "YES" or a == "yes":
        pick = int(input("원하는 좌석을 선택하세요: 1번~10번"))
        if pick <= 10 and pick>=1:
            if (seat[pick-1])==0:
                 seat[pick-1]=1
                 print(pick,"번 좌석이 예매되었습니다.")
                 seat[pick-1] = 1
                 print("-----------------------")
                 print(seat)
                 print("-----------------------")
            else:
                print("이미 예약된 좌석입니다.")
        else:
            pass
    elif a == "NO" or a == "no":
        print("좌석예매를 종료합니다.")
        break
    else:
        continue
'''
#ex5) 소프트웨어적 사고 성적을 입력 받아 합을 구하는 프로그램
#음수가 입력되면 반복문이 종료
sum = 0
while True:
    score = int(input("성적 입력:"))
    if score >= 0: 
        sum += score
    else:
        break
print(sum)
