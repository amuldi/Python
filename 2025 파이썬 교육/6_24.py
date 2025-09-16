#함수
#인수-매개변수
#함수: get_sum, 매개변수: start, end 인수: 1,10
#def get_sum(start,end): 
#    sum = 0
#    for i in range(start,end+1):
#        sum = sum +i
#    return sum
#print(get_sum(1,10))
#print(get_sum(1,20))

#random
#import random
#print(random.randint(0,10)) # 인수(0~10)사이의 랜덤한 값 출력
#print(random.randrange(0,10,2)) # step(2)만큼 띄운 값(짝수) 중 하나가 출력

#random-주사위
#import random
#dice1 = random.randint(1,6)
#dice2 = random.randint(1,6)
#dice_sum = dice1+dice2
#print("1번 주사위:",dice1)
#print("2번 주사위:",dice2)
#print("합:",dice_sum)

#거북이
#import turtle
#window = turtle.Screen() 
#window.bgcolor("lightgreen")
#t=turtle.Turtle()
#t.shape("turtle")
#t.color("blue")
#colors = ["yellow","red","purple","blue"]
#for c in colors :
#    t.color(c)
#    t.forward(200)
#    t.left(90)

#거북이_육각형
#import turtle
#polygon = turtle.Turtle()
#num_sides = 6
#side_length = 70
#angle = 360.0/num_sides
#for i in range(num_sides):
#    polygon.forward(side_length)
#    polygon.right(angle)
#turtle.exitonclick()

#거북이-경주
#from turtle import* #import* : 한꺼번에 모든 클래스, 함수등 가져오기
#from random import randint
#speed(12)
#penup()
#goto(-140,140)
#for step in range(11):
#    write(step,align = 'center')
#    right(90)
#    forward(10)
#    pendown()
#    forward(150)
#    penup()
#    backward(160)
#    left(90)
#    forward(20)
#A = Turtle()
#A.color("red")
#A.shape("turtle")
#A.penup()
#A.goto(-160,100)
#A.pendown()
#for turn in range(50):
#    A.forward(randint(1,5))
#exitonclick() #클릭으로 나가기

#3과 5의 배수
#total = 0
#for i in range(1, 1000):  
#    if i % 3 == 0: #3의 배수
#        total += i
#    elif i % 5 == 0: #5의 배수
#        total += i
#print("총합:", total)







