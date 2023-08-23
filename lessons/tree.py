import turtle as t


def tree(x: float, y: float) -> None:
    t.penup()
    t.goto(x, y)
    t.pendown()
    TRUNK = 100.0
    UP = 90.0
    branch(TRUNK, UP)
    t.update()


def branch(length: float, angle: float) -> None:
    t.setheading(angle)
    t.forward(length)
    if length < 3.0:
        ... # do nothing
    else:
        branch(length * 0.65, angle + 0.25)
        branch(length * 0.6, angle - 20)
    t.setheading(angle + 180.0)
    t.forward(length)

t.tracer(0, 0) # This only updates when you call t.update()
t.speed(0)
tree(0, 0)
t.done()