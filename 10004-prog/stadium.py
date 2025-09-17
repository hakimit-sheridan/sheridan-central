import turtle


def setupStadium(raceLength: int):
    stadium = turtle.Screen()
    stadium.bgcolor("lightgreen")
    stadium.screensize(raceLength * 2, raceLength * 2)
    return stadium
