"""Drawing a beautiful picture of the Wilson Library with turtles.

I broke up complex functions in multiple places. I resued the window function in the arch function. I also broke up the tree function into the leaves and the trunk.
I used functions that were not in the tutorial, such as the circle function and the write function.
I used the random integer function to make my trees of varying heights.
I have 5 repeating components in my scene.
"""

__author__ = "730309871"

from turtle import Turtle, colormode, done

from random import randint

# helper functions


def rectangle(turtle: Turtle, side_one: float, side_two: float) -> None:
    """Makes a filled in rectangle."""
    turtle.pendown()
    turtle.begin_fill()
    i: int = 0
    while i < 2:
        turtle.forward(side_one)
        turtle.left(90)
        turtle.forward(side_two)
        turtle.left(90)
        i += 1
    turtle.end_fill()


def line(turtle: Turtle, x: float, y: float, a: float, b: float) -> None:
    """Draws a line from one point to another."""
    # turtle.penup()
    # turtle.setpos(x, y)
    # turtle.pendown()
    travel(turtle, x, y)
    turtle.goto(a, b)


def travel(turtle: Turtle, x: float, y: float) -> None:
    """Saves a tiny amount of space in moving a turtle from one place to another."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


# drawing functions

def column(turtle: Turtle, x: float, y: float, width: int, height: int) -> None:
    """Makes a column."""
    travel(turtle, x, y)
    turtle.setheading(180.0)
    rectangle(turtle, width, height)


def window(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Makes a normal, four pane window."""
    travel(turtle, x, y)
    turtle.setheading(180.0)
    rectangle(turtle, width, height)
    i: int = 0
    while i < 2:
        rectangle(turtle, width / 2, height / 2)
        travel(turtle, x - width / 2, y)
        rectangle(turtle, width / 2, height / 2)
        y = y - height / 2
        travel(turtle, x, y)
        i += 1


def arch(turtle: Turtle, x: float, y: float, width: int, height: int) -> None:
    """Makes an arched window using the window function."""
    window(turtle, x, y, width, height)
    turtle.begin_fill()
    turtle.setheading(90.0)
    travel(turtle, x, y)
    turtle.circle(width / 2, 180)
    turtle.setheading(180.0)
    travel(turtle, x, y)
    turtle.end_fill()


def door(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Makes the front doors of the library."""
    travel(turtle, x, y)
    turtle.color("brown")
    rectangle(turtle, width, height)


def tree_leaves(turtle: Turtle, x: float, y: float, height: float, width: float) -> None:
    """A function that makes the tree leaves."""
    turtle.color(67, 143, 21)
    turtle.begin_fill()
    line(turtle, x, y, x + width, y)
    line(turtle, x + width, y, x + width / 2, y + height)
    line(turtle, x + width / 2, y + height, x, y)
    turtle.end_fill()


def tree_trunk(turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """The trunk of the tree."""
    turtle.color(130, 112, 110)
    travel(turtle, x, y)
    turtle.setheading(180.0)
    rectangle(turtle, width, height)


def tree(turtle: Turtle, x: float, y: float, a: int, b: int, width: float) -> None:
    """A function to make beautiful trees of varying height and constant width."""
    height: int = randint(a, b)
    tree_trunk(turtle, x + 3 * width / 5, y, width / 5, 20)
    tree_leaves(turtle, x, y, height, width)
    

def main() -> None:
    """The main function."""
    bob: Turtle = Turtle()
    bob.speed(50)
    travel(bob, -300, -200)
    colormode(255)
    # quad
    bob.color(49, 154, 38)
    rectangle(bob, 600, 200)
    # sky
    travel(bob, -300, 0)
    bob.color(191, 253, 255)
    rectangle(bob, 600, 300)
    # building
    bob.color(238, 240, 220)
    travel(bob, -260, 0)
    rectangle(bob, 520, 200)
    # dome
    travel(bob, 75, 200)
    bob.left(90)
    bob.begin_fill()
    bob.circle(75, 180)
    # triangle
    bob.pencolor("black")
    line(bob, 80, 200, 0, 225)
    line(bob, 0, 225, -80, 200)
    line(bob, -80, 200, 80, 200)
    bob.end_fill()
    # name plate?
    travel(bob, -80, 200)
    rectangle(bob, 30, 160)
    travel(bob, -69, 180)
    bob.write("LOUIS ROUND WILSON LIBRARY", font=('times new roman', 7, 'normal'))
    # windows
    window_x: int = -220
    window_y: int = 75
    travel(bob, window_x, window_y)
    bob.pencolor("white")
    bob.color("black")
    window_counter: int = 0
    while window_counter < 16:
        bob.pencolor("white")
        if window_counter < 8:
            window(bob, window_x, window_y, 20, 40)
        else:
            arch(bob, window_x, window_y, 20, 40)
        if window_counter == 3:
            window_x += 220
        elif window_counter == 7:
            window_x -= 460
            window_y += 70
        elif window_counter == 11:
            window_x += 220
        else:
            window_x += 40
        travel(bob, window_x, window_y)
        window_counter += 1
    # windows and doors between the columns
    i = 0
    door_x: int = 36
    door_y: int = 160
    while i < 3:
        bob.color("black")
        bob.pencolor("white")
        arch(bob, door_x, door_y, 14, 40)
        door(bob, door_x, door_y - 100, 14, 40)
        door_x -= 29
        i += 1
    # stairs
    bob.pencolor("black")
    bob.fillcolor(229, 231, 216)
    travel(bob, 80, 20)
    bob.setheading(180.0)
    rectangle(bob, 160, 20)
    # columns
    i = 0
    x_coord: int = 80
    while i < 6:
        column(bob, x_coord, 170, 15, 150)
        x_coord -= 29
        i += 1
    # trees
    i = 0
    tree_x: int = -250
    while i < 6:
        tree(bob, tree_x, 20, 100, 210, 40)
        if i == 2:
            tree_x += 240
        else:
            tree_x += 55
        i += 1
    bob.hideturtle()
    done()


if __name__ == "__main__":
    main()