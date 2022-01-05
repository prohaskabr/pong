from turtle import Turtle


class Paddle(Turtle):
    _step = 15

    def __init__(self, position_x, position_y):
        super().__init__()
        self.penup()
        self.goto(position_x, position_y)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.shape("square")
        self.color("white")

    def move_up(self):
        max_height = 260
        new_y = self.ycor() + self._step
        if new_y < max_height:
            self.goto(self.xcor(), new_y)

    def move_down(self):
        min_height = -250
        new_y = self.ycor() - self._step
        if new_y > min_height:
            self.goto(self.xcor(), new_y)
