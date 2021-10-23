from turtle import Screen , Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(height=600 , width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
#to turn off animation
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    #to turn on animation
    screen.update()
    time.sleep(0.1)
    snake.move()

   #Detect collision with food
    if snake.head.distance(food) < 15 :
       food.refresh()
       snake.extend()
       scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 287 or snake.head.xcor() < -287 or snake.head.ycor() > 287 or snake.head.ycor() < -287:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail
    for segment in snake.seg:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) <10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()