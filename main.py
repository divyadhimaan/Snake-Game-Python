from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
SPEED_LEVELS = [0.1, 0.07, 0.05]

snake = Snake()
food = Food()
scores = Scoreboard()

level = int(screen.textinput(title="LEVEL", prompt="Choose a Level. (EASY -> 0 / MEDIUM -> 1 / HARD -> 2): "))

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(SPEED_LEVELS[level])
    # time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        scores.update_scores()
        snake.extend()

    # Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scores.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            scores.game_over()
            game_is_on = False

screen.exitonclick()
