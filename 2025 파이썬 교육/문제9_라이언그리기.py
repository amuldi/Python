import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(15)
t.width(10)
t.fillcolor("orange")

#왼쪽 귀
t.penup()
t.goto(-90, 135)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

#오른쪽 귀
t.penup()
t.goto(90, 135)
t.pendown()
t.begin_fill()
t.circle(40)
t.end_fill()

#얼굴
t.penup()
t.goto(-0, -100)  
t.pendown()
t.begin_fill()
t.circle(150)
t.end_fill()

#왼쪽 눈
t.penup()
t.goto(-65, 50)
t.pendown()
t.begin_fill()
t.circle(5)
t.fillcolor("black")
t.end_fill()

#오른쪽 눈
t.penup()
t.goto(65, 50)
t.pendown()
t.begin_fill()
t.circle(5)
t.fillcolor("black")
t.end_fill()

# 왼쪽 눈썹
t.width(10)
t.penup()
t.goto(-90, 90) 
t.pendown()
t.forward(45)

# 오른쪽 눈썹
t.width(10)
t.penup()
t.goto(45, 90)  
t.pendown()
t.forward(45)

#코
t.penup()
t.goto(-10,-15)
t.pendown()
t.begin_fill()
t.circle(20)
t.fillcolor("white")
t.end_fill()

t.penup()
t.goto(10,-15)
t.pendown()
t.begin_fill()
t.circle(20)
t.fillcolor("white")
t.end_fill()

t.width(12)
t.penup()
t.goto(0, 15)
t.pendown()
t.begin_fill()
t.circle(5)
t.fillcolor("black")
t.end_fill()

t.hideturtle()
turtle.exitonclick()