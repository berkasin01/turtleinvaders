from turtle import Turtle, Screen
from aliens import Aliens
import random
import time

screen = Screen()
aliens = Aliens()

screen.bgcolor("black")
screen.title("Space Invaders")
screen.screensize(800, 800)
screen.tracer(0)

for i in range(290, 380, 30):
    aliens.create_aliens(i)

game_on = True
while game_on:
    time.sleep(aliens.movement_speed)
    screen.update()
    aliens.move()
    for alien in aliens.all_aliens:
        if alien.pos()[0] > 385:
            aliens.bounce_x()
        elif alien.pos()[0] < -385:
            aliens.bounce_x()




screen.exitonclick()
