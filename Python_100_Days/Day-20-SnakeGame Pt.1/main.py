#main.py
import turtle
from turtle import Turtle, Screen
import time
from snake import Snake


is_game_on = True

turtle.colormode(255)

screen = Screen()
screen.setup(width=800, height=640)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

new_snake = Snake()
screen.listen()

screen.onkey(new_snake.go_up, "w")
screen.onkey(new_snake.go_down, "s")
screen.onkey(new_snake.go_left, "a")
screen.onkey(new_snake.go_right, "d")


while is_game_on:
    screen.update()
    new_snake.move()
    time.sleep(0.1)




screen.mainloop()
