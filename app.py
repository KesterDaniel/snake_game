from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_on = True

while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
