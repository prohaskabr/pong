from turtle import Turtle
import random


class Ball(Turtle):
    _x_value = 10
    _y_value = 10

    def __init__(self, height):
        super().__init__()
        self._height = height / 2
        self._height = height / 2
        self.color("white")
        self.shape("circle")
        self.penup()
        self.reset()

    def reset(self):
        self.goto(0, 0)
        self.random_xy()

    def hit_right(self):
        self._x_value = -10

    def hit_left(self):
        self._x_value = 10

    def refresh(self):
        new_x = self.xcor() + self._x_value
        new_y = self.ycor() + self._y_value

        if new_y > self._height or new_y < (self._height * -1):
            self._y_value *= -1

        self.goto(new_x, new_y)

    def random_xy(self):
        x = 1
        y = 1

        if random.randint(1, 100) % 2 == 0:
            x = -1

        if random.randint(1, 100) % 2 == 0:
            y = -1

        self._x_value = 10 * x
        self._y_value = 10 * y
