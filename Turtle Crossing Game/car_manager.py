from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 4) == 1:  # Adjust the frequency of car creation as needed
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_cor = random.randint(-200, 200)

            # Checks to see if there is a gap of at least 20 between the cars
            if self.all_cars:
                last_car_y = self.all_cars[-1].ycor()
                if y_cor - last_car_y < 20:  # Check for a gap of 20 between cars
                    y_cor = random.randint(-200, 200)

            new_car.goto(280, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
