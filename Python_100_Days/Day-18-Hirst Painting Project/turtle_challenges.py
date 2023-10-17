import random
import turtle
from turtle import Turtle, Screen

def square():
    for _ in range(4):
        timmy.right(90)
        timmy.forward(100)

def dashed_line():
    for _ in range(10):
        timmy.forward(10)
        timmy.up()
        timmy.forward(10)
        timmy.pendown()

def all_shapes(colors):
    for shape in range(3, 11):
        # print(shape)
        timmy.color(random.choice(colors))
        for side in range(1, shape + 1):
            # print(side)
            timmy.right(360/shape)
            timmy.forward(100)

def random_walk():
    turtle_movements = [timmy.forward, timmy.backward]
    turtle_directions = [timmy.right, timmy.left]
    turtle_angles = [0, 90, 180, 270]

    for _ in range(200):
        timmy.color(random_colors())
        random.choice(turtle_movements)(30)
        random.choice(turtle_directions)(random.choice(turtle_angles))

def spirograph():
    for angle in range(1, 361, 5):
        timmy.color(random_colors())
        timmy.setheading(angle)
        timmy.circle(150)


def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

timmy = Turtle()
turtle.colormode(255)
timmy.speed('fastest')
timmy.pensize(2)

screen = Screen()
screen.setup(width=1280, height=720)
screen.delay(-10)

spirograph()

screen.mainloop()