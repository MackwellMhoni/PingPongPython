from turtle import Screen, Turtle
from Paddle import Paddle
from ball import Ball
import time
from score import score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball((0,0))
score = score()

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "w")
screen.onkey(left_paddle.paddle_down, "s")


game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect y-axis collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_on_y()

    # Detect paddle collision
    if ball.distance(right_paddle) < 50 and ball.xcor() < 340 or ball.distance(left_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_on_x()

    if ball.xcor() > 380:
        ball.resetGame()
        score.leftPoint()

    if ball.xcor() < -380:
        ball.resetGame()
        score.rightPoint()



screen.exitonclick()