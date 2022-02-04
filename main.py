# SNAKE GAME PROJECT
# divide this  problem into some steps
from food import Foods
from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
import time
s = Screen()
s.bgcolor("black")
s.title("Snake Game")
s.setup(width=600, height=600)
s.tracer(0)  # it will earse the shape util the update fun is called
s.listen()
snake = Snake()
food = Foods()
scoreboard = Scoreboard()
# step 3: - control the snake
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
is_game_on = True
while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move_forward()

    # step4 detect collision with food
    # distance is a method/fun we compare distance of our head of turtle with food
    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.score_increase()

    # step 6: detect collision with wall and tail
    if snake.turtles[0].xcor() > 280 or snake.turtles[0].xcor() < -290 or snake.turtles[0].ycor() > 280 or snake.turtles[0].ycor() < -290:
        scoreboard.game_over()
        is_game_on = False

    # step 8: detect collision with tail
    # if head is collid with any of the segment in the tail:
    for segment in snake.turtles:
        if segment == snake.turtles[0]:
            pass
        elif snake.turtles[0].distance(segment) < 10:
            scoreboard.game_over()
            is_game_on = False

s.exitonclick()
