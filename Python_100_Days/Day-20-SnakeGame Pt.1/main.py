#main.py
import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


is_game_on = True

turtle.colormode(255)

screen = Screen()
screen.setup(width=800, height=640)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.go_up, "w")
screen.onkey(snake.go_down, "s")
screen.onkey(snake.go_left, "a")
screen.onkey(snake.go_right, "d")

while is_game_on:
    screen.update()
    snake.move()
    time.sleep(0.1)
    scoreboard.update_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score += 1

    if snake.head.xcor() < -395 or \
        snake.head.xcor() > 395 or \
        snake.head.ycor() > 315 or \
        snake.head.ycor() < -315:
        is_game_on = False
        scoreboard.game_over()

    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()


screen.mainloop()
