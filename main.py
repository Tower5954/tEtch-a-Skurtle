from turtle import Turtle, Screen

raph = Turtle()
screen = Screen()


def move_forwards():
    raph.forward(10)


def move_backwards():
    raph.back(10)


def move_anti_clockwise():
    raph.left(10)


def move_clockwise():
    raph.right(10)


def clear():
    raph.clear()
    raph.penup()
    raph.home()
    raph.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_anti_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
