from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for i in range(len(COORDINATES)):
            self.add_block(COORDINATES[i])

    def add_block(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add_block(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles)-1, 0, -1):
            new_x = self.turtles[turtle_num-1].xcor()
            new_y = self.turtles[turtle_num-1].ycor()
            self.turtles[turtle_num].goto(x=new_x, y=new_y)
        self.turtles[0].forward(MOVE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
