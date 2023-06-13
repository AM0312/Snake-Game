from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_on = True
while game_on:
    screen.update()
    time.sleep(0.075)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    if (snake.turtles[0].xcor() > 290) or (snake.turtles[0].xcor() < -290) or (snake.turtles[0].ycor() > 290) or (snake.turtles[0].ycor() < -290):
        game_on = False
        score_board.game_over()

    for turtle in snake.turtles[1:]:
        if snake.turtles[0].distance(turtle) < 10:
            game_on = False
            score_board.game_over()

screen.exitonclick()
