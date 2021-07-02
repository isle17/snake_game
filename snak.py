from turtle import Turtle, Screen


class Snak:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        # Originally I was using self.tail to check if the snake hit its own tail but it was
        # not working is this because it is in the initialization of the code and never gets changed?
        self.tail = self.segments[1:]

    def create_snake(self):
        x_origin = 0
        for i in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            self.segments.append(segment)
        for seg in self.segments:
            seg.setx(x_origin)
            x_origin -= 20

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        snake_length = len(self.segments)-1
        last_segment_x_cor = self.segments[snake_length].xcor()
        last_segment_y_cor = self.segments[snake_length].ycor()
        segment.setpos(last_segment_x_cor, last_segment_y_cor)
        self.segments.append(segment)
