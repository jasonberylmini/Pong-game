from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.title('The Arcade Game!')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.move_down, "Down")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(l_paddle.move_up, "w")

game_is_on =True
while game_is_on:
    time.sleep(ball.movement)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect right paddle miss
    if ball.xcor() > 420:
        ball.reset_position()
        score.l_point()

    # Detect left paddle miss
    if ball.xcor() < -420:
        ball.reset_position()
        score.r_point()

screen.exitonclick()