from turtle import Turtle, Screen
import random


class Aliens:
    def __init__(self):
        self.alien_shapes = ["circle", "triangle", "turtle"]
        self.all_aliens = []
        self.x_vel = 10
        self.y_vel = 10
        self.projectile_vel = 20
        self.all_projectiles = []
        self.projectile_spawn_rate = 2
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
            alien.setx(x + self.x_vel)  # Move alien based on x_vel

    def spawn_projectiles(self, x_val, y_val):
        projectile = Turtle()
        projectile.penup()
        projectile.color("green")
        projectile.shape("square")
        projectile.shapesize(0.1, 0.5)
        projectile.setheading(270)
        projectile.goto(x_val, y_val)
        self.all_projectiles.append(projectile)

    def projectile_move(self):
        for projectile in self.all_projectiles:
            y = projectile.pos()[1]
            projectile.sety(y - self.projectile_vel)

    def bounce_x(self):
        self.x_vel *= -1
