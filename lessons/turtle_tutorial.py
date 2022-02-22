from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(255)
leo.fillcolor(51, 203, 255)
leo.pencolor("pink")
# pure black is all 0s, pure white is all 255, gray is three of the same number

leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, -60)
leo.pendown()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color(40, 154, 154)
bob.speed(100)

bob.penup()
bob.goto(-150, -60)
bob.pendown()

side_length: float = 300
i: int = 0
while i < 3:
    bob.forward(side_length)
    bob.left(120)
    i += 1

i: int = 0
while i < 20:
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120.5)
    i += 1

done()