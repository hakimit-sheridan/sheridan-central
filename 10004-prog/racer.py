import turtle


def createRacer(colour: str, x: float):
    t = turtle.Turtle(shape="turtle", visible=False)
    speed = t.speed()
    t.speed(0)
    t.color(colour)
    t.up()
    t.left(90)
    t.setx(x)
    t.showturtle()
    t.speed(speed)
    return t
