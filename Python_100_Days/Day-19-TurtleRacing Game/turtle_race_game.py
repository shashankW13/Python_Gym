import random
import turtle
from turtle import Turtle, Screen

def setup_start_line(turtles):
    ...

turtle.colormode(255)

colors = ['green', 'red', 'blue', 'yellow', 'black', 'purple', 'pink']
turtle_list = []
initial_pos = {'x': -300, 'y': -240}
is_race_on = False
user_bet = ''

screen = Screen()
screen.setup(width=800, height=640)
screen.delay(1)
screen.listen()

for color in colors:
    turtle_color = color
    new_turtle = Turtle(shape='turtle')
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.color(turtle_color)
    new_turtle.goto(initial_pos['x'], initial_pos['y'])
    initial_pos['y'] += 80
    turtle_list.append(new_turtle)

print(turtle_list)



while user_bet not in colors:
    user_bet = screen.textinput(title='Make your bet',
                     prompt='Which turtle will win the race? Enter the color: ')

if user_bet.lower() in colors:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        random_distance = random.randint(0, 50)
        turtle.forward(random_distance)

        if turtle.xcor() > (screen.window_width()/2 - 20):
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The winning turtle is {winning_color}')
            else:
                print(f'You lost! The winning turtle is {winning_color}')
            break

screen.mainloop()
