import random
import turtle
from turtle import Turtle, Screen

color_list = [(202, 109, 166), (152, 47, 73), (170, 41, 153),
              (222, 138, 202), (53, 124, 93), (135, 22, 32)]

def hirst_spot_painting():
    timmy.hideturtle()
    y_pos = -200
    x_pos = -200
    timmy.penup()
    timmy.setposition(x_pos, y_pos)
    timmy.pendown()
    for x in range(10):
        y_pos += 50
        for y in range(10):
            random_colors = random.choice(color_list)
            timmy.pendown()
            timmy.dot(20, random_colors)
            timmy.penup()
            timmy.forward(50)
        timmy.setposition(x_pos, y_pos)


timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')
timmy.pensize(2)

screen = Screen()
screen.setup(width=1280, height=720)


hirst_spot_painting()

screen.mainloop()


