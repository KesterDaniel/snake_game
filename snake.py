from turtle import Turtle
X_COORDINATES = [-0, -20, -40]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for cor in X_COORDINATES:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.setx(cor)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def left(self):
        if self.snake_head.heading() == 90:
            self.snake_head.left(90)
        elif self.snake_head.heading() == 270:
            self.snake_head.right(90)

    def right(self):
        if self.snake_head.heading() == 90:
            self.snake_head.right(90)
        elif self.snake_head.heading() == 270:
            self.snake_head.left(90)

    def down(self):
        if self.snake_head.heading() == 180:
            self.snake_head.left(90)
        elif self.snake_head.heading() == 0:
            self.snake_head.right(90)


