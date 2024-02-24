from turtle import Turtle

SNEK_SEGMENT_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0


class Snake:
    def __init__(self):
        self.snek_body_seg = []
        self.create_snake_seg()
        self.head = self.snek_body_seg[0]

    def create_snake_seg(self):
        for position in SNEK_SEGMENT_POSITION:
            self.add_body_seg(position)

    def add_body_seg(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.snek_body_seg.append(new_segment)

    def extend_body_seg(self):
        self.add_body_seg(self.snek_body_seg[-1].position())

    def update_body_seg(self):
        for seg in self.snek_body_seg:
            seg.goto(1000, 1000)
        self.snek_body_seg.clear()
        self.create_snake_seg()
        self.head = self.snek_body_seg[0]

    def move(self):
        for body_seg_num in range(len(self.snek_body_seg) - 1, 0, -1):
            new_x_pos = self.snek_body_seg[body_seg_num - 1].xcor()
            new_y_pos = self.snek_body_seg[body_seg_num - 1].ycor()
            self.snek_body_seg[body_seg_num].goto(new_x_pos, new_y_pos)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)

    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT)

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)
