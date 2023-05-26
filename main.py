from turtle import Turtle, Screen
from myturtle import MyTurtle
from rangeencars import rangeen
import random
from Scoreboard import ScoreBoard

speed = 2
level = 1

def game():
    myscreen = Screen()
    myscreen.bgcolor('white')
    myscreen.tracer(0)
    cars = []
    for x in range(1000):
        gaadi = rangeen()
        #gaadi.speed(random.randint(1,3))
        cars.append(gaadi)

    trutle = MyTurtle()

    global speed
    global level

    myscreen.setup(800,800)
    scoreboard = ScoreBoard(level)

    is_game_on = True
    while is_game_on:
        
        myscreen.update()
        for car in cars:
            car.backward(speed)
            if car.distance(trutle)<15:
                is_game_on = False
                print("You have lost")
        if trutle.ycor()>250:
            speed = speed +1
            level = level + 1
            myscreen.clear()
            game()

        myscreen.onkeypress(trutle.moveupwards,"Up")
        myscreen.onkeypress(trutle.movebackwards,"Down")
        myscreen.listen()


    myscreen.mainloop()
game()
