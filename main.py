from turtle import Screen, Turtle
import time
from snak import Snak
from food import Food
from scoreboad import Scoreboard
from border import Border

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes Eat Apples")
screen.tracer(0)


snake = Snak()
food = Food()

border = Border()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

score = 0
# continue_playing = "y"

# while continue_playing == "y":
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    snake.move()

    # Detect if the snake ate the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.add_segment()

    # for
    # if snake.tail.distance(snake.head) < 15:
    #     game_is_on = False
    #     scoreboard.game_over()

    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()
    # continue_playing = input("Play Again? Type 'y' for Yes or 'n' to exit")

print(snake.tail)
screen.exitonclick()
