from turtle import Turtle

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 15
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.up()
        segment.setpos(position)
        self.segments.append(segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)

    def reset(self):

        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


