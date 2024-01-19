import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(500,400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the game? Enter a color: ")
all_turtle = []
colors = ['red', 'yellow', 'green', 'blue', 'magenta', 'cyan', 'white''']
y_position = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    # goto method helps to move the turtle
    new_turtle.goto(x=-250, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 250:
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The winning color is {winning_color}")
            else:
                print(f"You lost! The winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
screen.exitonclick()