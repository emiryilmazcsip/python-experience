#Emir Yilmaz
#March 27, 2023
#Turtle Race!
import turtle
import random
turtle.speed(9)
turtle.penup()
turtle.goto(-150, 150)
for line in range(15):
  turtle.write(line, align='center')
  turtle.right(90)
  for rep in range(8):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    turtle.forward(10)
  turtle.penup()
  turtle.backward(160)
  turtle.left(90)
  turtle.forward(20)
pancakes = turtle.Turtle()
pancakes.shape("turtle")
pancakes.color("red")
pancakes.penup()
pancakes.goto(-170,120)
pancakes.pendown()
woofles = turtle.Turtle()
woofles.shape("turtle")
woofles.color("blue")
woofles.penup()
woofles.goto(-170,90)
woofles.pendown()
sushi = turtle.Turtle()
sushi.shape("turtle")
sushi.color("green")
sushi.penup()
sushi.goto(-170,60)
sushi.pendown()
pizza = turtle.Turtle()
pizza.shape("turtle")
pizza.color("yellow")
pizza.penup()
pizza.goto(-170,30)
pizza.pendown()
while pancakes.xcor() <= 130 and woofles.xcor() <=130 and sushi.xcor() <= 130 and pizza.xcor() <= 130:
  pancakes.forward(random.randint(1,5))
  woofles.forward(random.randint(1,5))
  sushi.forward(random.randint(1,5))
  pizza.forward(random.randint(1,5))
if (pancakes.xcor() >= 130):
  print("Pancake is the Winner!!!")
elif (woofles.xcor() >= 130):
  print("Woofles is the Winner!!!")
elif (sushi.xcor() >= 130):
  print("Sushi is the Winner!!!")
elif (pizza.xcor() >=130):
  print("Pizza is the Winner!!!")
