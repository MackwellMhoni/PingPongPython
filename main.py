from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball((0, 0))

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "W")
screen.onkey(left_paddle.paddle_down, "S")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()




screen.exitonclick()