from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

sb = ScoreBoard()

ball = Ball(height=560)
right_p = Paddle(380, 0)
left_p = Paddle(-387, 0)

screen.listen()
screen.onkey(right_p.move_up, "Up")
screen.onkey(right_p.move_down, "Down")
screen.onkey(left_p.move_up, "w")
screen.onkey(left_p.move_down, "s")

while True:
    screen.update()
    ball.refresh()

    if ball.distance(right_p) < 50:
        ball.hit_right()

    if ball.distance(left_p) < 50:
        ball.hit_left()

    if ball.xcor() > 380:
        ball.reset()
        sb.score("L")

    if ball.xcor() < -390:
        ball.reset()
        sb.score("R")

    time.sleep(0.1)
screen.exitonclick()
