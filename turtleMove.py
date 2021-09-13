import turtle

x,y = turtle.position()
turtle.pendown()

def move_f():
    turtle.setheading(90)
    turtle.forward(50)

def move_l():
    turtle.setheading(180)
    turtle.forward(50)

def move_b():
    turtle.setheading(-90)
    turtle.forward(50)

def move_r():
    turtle.setheading(0)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.onkey(move_f, 'w')
turtle.onkey(move_l, 'a')
turtle.onkey(move_b, 's')
turtle.onkey(move_r, 'd')

turtle.onkey(restart,'Escape')
turtle.listen()
