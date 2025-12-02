from turtle import Screen, Turtle
from Paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Paddle((0, 0))

ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)

screen.listen()
screen.onkey(right_paddle.paddle_up, "Up")
screen.onkey(right_paddle.paddle_down, "Down")
screen.onkey(left_paddle.paddle_up, "W")
screen.onkey(left_paddle.paddle_down, "S")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()