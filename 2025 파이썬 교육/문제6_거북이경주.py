from turtle import*
from random import randint

speed(20)
penup()
goto(-140,140)
for step in range(11):
    write(step,align = 'center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)

colors = ["red", "blue", "green", "black", "gray"]
start = [115, 85, 55, 25, -5]
turtles = []

for i in range(5):
    A = Turtle()
    A.color(colors[i])
    A.shape("turtle")
    A.penup()
    A.goto(-160, start[i])
    A.pendown()
    turtles.append(A)

for turn in range(50):
    for A in turtles:
        A.forward(randint(1,7))
    
exitonclick()