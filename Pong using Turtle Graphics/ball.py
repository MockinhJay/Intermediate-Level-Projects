from turtle import Turtle
import random

signs = [-1, 1]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction_x = random.choice(signs)
        self.direction_y = random.choice(signs)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + 18 * self.direction_x
        new_y = self.ycor() + 18 * self.direction_y
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.direction_x *= -1
        self.direction_y *= -1
