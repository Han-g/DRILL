import turtle

def run_turtle(deg, dist = 50):
    turtle.setheading(deg)
    turtle.forward(dist)
    turtle.stamp()

def move_up():
    run_turtle(90)
    print('UP')

def move_left():
    run_turtle(180)
    print('LEFT')

def move_down():
    run_turtle(-90)
    print('DOWN')

def move_right():
    run_turtle(0)
    print('RIGHT')

def finish():
    turtle.bye()

turtle.shape('turtle')

turtle.onkey(move_up, 'w')
turtle.onkey(move_left, 'a')
turtle.onkey(move_down, 's')
turtle.onkey(move_right, 'd')

turtle.onkey(finish,'Escape')
turtle.listen()
turtle.mainloop()
