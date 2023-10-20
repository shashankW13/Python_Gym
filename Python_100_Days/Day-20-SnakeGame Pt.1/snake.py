#snake.py
from turtle import Turtle

INITIAL_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = {'x': 0, 'y': 0}
class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for _ in range(INITIAL_SEGMENTS):
            self.add_segment(POSITIONS)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position['x'], position['y'])
        position['x'] -= 20
        self.snake_segments.append(new_segment)

    def extend(self):
        last_position = self.snake_segments[-1].position()
        self.add_segment({'x': last_position[0], 'y': last_position[1]})

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment - 1].xcor()
            new_y = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



