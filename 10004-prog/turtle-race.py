import turtle
import random
import racer
import stadium
import painter


raceLength = 300

_ = stadium.setupStadium(raceLength)
_ = painter.paint(raceLength)


larry = racer.createRacer("green", -(raceLength * 3 / 4))
curly = racer.createRacer("red", 0)
moe = racer.createRacer("blue", +(raceLength * 3 / 4))

min = raceLength / 10
max = raceLength - min

for runner in [larry, curly, moe]:
    n = random.random() * max + min
    runner.sety(n)


turtle.exitonclick()
turtle.mainloop()
turtle.done()
