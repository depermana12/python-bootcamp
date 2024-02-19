from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def forward():
    timmy.forward(20)

def backward():
    timmy.backward(50)

def turn_left():
    timmy.left(5)

def turn_right():
    timmy.right(5)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(clear_screen, "c")


screen.exitonclick()
