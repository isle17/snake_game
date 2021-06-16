from turtle import Turtle


class Border(Turtle):
    """Creates a border for the game by using a turtle to draw a square 600 x 600"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(300, 300)
        self.setheading(180)
        self.pendown()
        self.pencolor("white")
        self.hideturtle()
        for i in range(4):
            self.forward(600)
            self.left(90)
