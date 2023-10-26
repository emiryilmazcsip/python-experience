#Emir Yilmaz
#February, 17, 2023
#Archery Game
import turtle
import random
import math

turtle.speed(50)
turtle.bgcolor("tan")
turtle.penup()
turtle.goto(0, -150)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(150)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -110)
turtle.pendown()
turtle.pencolor("black")
turtle.fillcolor("black")
turtle.begin_fill()
turtle.circle(110)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -70)
turtle.pendown()
turtle.pencolor("purple")
turtle.fillcolor("purple")
turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.pencolor("brown")
turtle.fillcolor("brown")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -30)
turtle.pendown()
turtle.pencolor("yellow")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

i = 0
total = 0
for i in range(3):
    x = random.randint(-150,150)
    y = random.randint(-150,150)
    size = 5
    color = "green"
    turtle.pensize(3)
    turtle.color(color)
    turtle.penup()
    turtle.goto(x-size, y-size)
    turtle.pendown()
    turtle.goto(x+size, y+size)
    turtle.penup()
    turtle.goto(x-size, y+size)
    turtle.pendown()
    turtle.goto(x+size, y-size)
    distance = math.sqrt(x*x+y*y)
    if distance >= 0 and distance <= 30:
        print("You got 9 points")
    elif distance >= 30 and distance <= 50:
        print("You got 7 points")
    elif distance >= 50 and distance <= 70:
        print("You got 5 points")
    elif distance >= 70 and distance <= 110:
        print("You got 3 points")
    elif distance >= 110 and distance <= 150:
        print("You got 1 points")
        total = total + 1
    i = 1 + 1
print(total)









