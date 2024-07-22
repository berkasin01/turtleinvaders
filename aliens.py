from turtle import Turtle
import random


class Aliens:
    def __init__(self):
        self.alien_shapes = ["circle", "triangle", "turtle"]
        self.all_aliens = []
        self.x_vel = 10
        self.y_vel = 10
        self.movement_speed = 0.1

    def create_aliens(self, y_val):
        for i in range(-252, 252, 70):
            alien = Turtle()
            alien.color("green")
            alien.penup()
            alien.setheading(270)
            alien.goto(i, y_val)
            alien.shape(random.choice(self.alien_shapes))
            self.all_aliens.append(alien)

    def move(self):
        for alien in self.all_aliens:
            x = alien.pos()[0]
            y = alien.pos()[1]
            alien.goto(x+self.x_vel, y)

    def bounce_x(self):
        self.x_vel *= -1