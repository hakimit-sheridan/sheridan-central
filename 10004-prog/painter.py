import turtle


def paint(raceLength: int):
    painter = turtle.Turtle(visible=False)

    painter.speed(0)
    painter.up()
    painter.forward(raceLength)
    painter.left(90)
    painter.forward(raceLength)
    painter.down()

    for _ in range(4):
        painter.left(90)
        painter.forward(raceLength * 2)

    painter.hideturtle()
    return painter
