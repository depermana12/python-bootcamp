from turtle import Turtle

SNEK_SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snek_body_seg = []
        self.create_snake_seg()

    def create_snake_seg(self):
        for position in SNEK_SEGMENT_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.snek_body_seg.append(new_segment)

    def move(self):
        for body_seg_num in range(len(self.snek_body_seg) - 1, 0, -1):
            new_x_pos = self.snek_body_seg[body_seg_num - 1].xcor()
            new_y_pos = self.snek_body_seg[body_seg_num - 1].ycor()
            self.snek_body_seg[body_seg_num].goto(new_x_pos, new_y_pos)
        self.snek_body_seg[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snek_body_seg[0].setheading(90)

    def down(self):
        self.snek_body_seg[0].setheading(270)

    def left(self):
        self.snek_body_seg[0].setheading(180)

    def right(self):
        self.snek_body_seg[0].setheading(0)
