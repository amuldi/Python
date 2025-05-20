print(1) #int
print(1.1) # float

print(1+1)
print(1+1)
print(2-1)
print(1*1)
print(2/2)

import math
print(math.sqrt(4)) #제곱근
print(math.pow(4,2)) #제곱

import random
print(random.random()) # 랜덤한 값 생성

print("Hello world") #문자열 
print('''Hello
world''') #''' 줄바꿈
print("'1'+'1'",'1'+'1')
print("Hello world"*100)
print(len("Hello world")) #갯수 새기
print('Hello world'.replace('world','universe')) #문자 치환

students = ["andy", "sihun", "jiwoo"] #문자형 리스트
grades = [1,2,4] #숫자형 리스트
print(students[1]) 
print(len(students),len(grades))

print(min(grades)) #촤솟값 구하기
print(max(grades)) #최댓값 
print(sum(grades)) #합계

import statistics #통계
print(statistics.mean(grades)) #평균값 구하기

print(random.choice(students)) #랜덥뽑기

name = input("이름을 입력하세요 : ") #입력받기

age = int(input("나이를 입력하세요 : ")) #정수 입력밥기
print(age,"살",name ,"님")
