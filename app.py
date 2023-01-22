import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

cor = 0
for i in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.setx(-cor)
    cor += 20

screen.exitonclick()
