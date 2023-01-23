from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()

screen.onkey(key="w", fun=snake.up)
screen.onkey(key="a", fun=snake.left)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="s", fun=snake.down)


game_on = True

while game_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.snake_head.distance(food) < 15:
        food.refresh()

screen.exitonclick()
