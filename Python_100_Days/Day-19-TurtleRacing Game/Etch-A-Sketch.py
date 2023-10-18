import turtle
from turtle import Turtle, Screen


def move_forward():
    timmy.forward(20)

def move_backward():
    timmy.backward(20)

def turn_left():
    timmy.setheading(timmy.heading() + 10)

def turn_right():
    timmy.setheading(timmy.heading() - 10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

timmy = Turtle()
turtle.colormode(255)
timmy.speed('fast')
timmy.pensize(2)

screen = Screen()
screen.setup(width=800, height=640)
screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=clear_screen)


screen.mainloop()
