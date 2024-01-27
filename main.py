import time
from turtle import Turtle, Screen
import random
import tkinter

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
print(user_bet)
colors = ["red", "orange", "purple", "blue", "yellow", "green"]
y_poistions = [-70, -40, -10, 20, 80, 50]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_poistions[turtle_index])
    all_turtles.append(new_turtle)
is_on = False
if user_bet:
    is_on = True

while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            win_color = turtle.pencolor()

            if win_color == user_bet:
                print(f"You have won. The winning turtle is {win_color}")
            else:
                print(f"You lose. The winning turtle color is {win_color}")

        distance = random.randint(0, 10)
        turtle.forward(distance)

draw_colors = set(turtle.pencolor() for turtle in all_turtles)
if len(draw_colors) == 1:
    print("The race is a draw!")
screen.bye()
