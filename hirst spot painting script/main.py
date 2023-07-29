import turtle
import turtle as turtle_module
import random

tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
turtle.colormode(255)
color_list = [(1, 31, 31), (52, 17, 17), (219, 106, 106), (9, 160, 160), (242, 69, 69), (150, 39, 39), (215, 64, 64),
              (164, 32, 32), (158, 24, 24), (157, 102, 102), (11, 32, 32)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
