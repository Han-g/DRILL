import turtle

temp = 6

turtle.penup()
turtle.goto(0,200)
while(temp > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(180)
    temp = temp - 1

temp = 6

turtle.penup()
turtle.goto(0,200)
turtle.right(90)
while(temp > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(180)
    temp = temp - 1
