from turtle import Turtle, Screen
from aliens import Aliens
from middleshape import MidShape
from playership import PlayerShip
import random
import time

screen = Screen()
aliens = Aliens()
midshape = MidShape()
player_ship = PlayerShip()

screen.bgcolor("black")
screen.title("Space Invaders")
screen.screensize(800, 800)
screen.tracer(0)
screen.listen()
screen.onkey(player_ship.move_right, "Right")
screen.onkey(player_ship.move_left, "Left")

for i in range(290, 380, 30):
    aliens.create_aliens(i)

midshape.create_shape()

previous_num_aliens = len(aliens.all_aliens)
alien_projectile_probability = 10

game_on = True
while game_on:
    time.sleep(aliens.movement_speed)
    aliens.move()

    if random.randint(0, 10) == 2:
        player_x = player_ship.main_ship.pos()[0]
        player_y = player_ship.main_ship.pos()[1]
        player_ship.main_projectiles(player_x, player_y)

    player_ship.move_projectile()

    project_aliens = []
    for alien in aliens.all_aliens:
        if alien.pos()[0] > 385 or alien.pos()[0] < -385:
            aliens.bounce_x()
        if alien.pos()[1] == 290:
            project_aliens.append(alien)

    if random.randint(0, alien_projectile_probability) == 4 and project_aliens:
        pick_alien = random.choice(project_aliens)
        pro_alien_x = pick_alien.pos()[0]
        pro_alien_y = pick_alien.pos()[1]
        aliens.spawn_projectiles(pro_alien_x, pro_alien_y)

    aliens.projectile_move()

    for project in aliens.all_projectiles[:]:
        if project.pos()[1] < -380:
            project.clear()
            project.hideturtle()
            aliens.all_projectiles.remove(project)
        else:
            for mid in midshape.all_midshape[:]:
                if project.distance(mid) < 20:
                    project.clear()
                    project.hideturtle()
                    try:
                        aliens.all_projectiles.remove(project)
                    except ValueError:
                        pass
                    mid.clear()
                    mid.hideturtle()
                    midshape.all_midshape.remove(mid)

    for po in player_ship.player_projectiles[:]:
        for alien in aliens.all_aliens[:]:
            if po.distance(alien) < 20:
                alien.clear()
                alien.hideturtle()
                aliens.all_aliens.remove(alien)
                po.clear()
                po.hideturtle()
                try:
                    player_ship.player_projectiles.remove(po)
                except ValueError:
                    pass

        for mid in midshape.all_midshape[:]:
            if po.distance(mid) < 20:
                po.clear()
                po.hideturtle()
                try:
                    player_ship.player_projectiles.remove(po)
                except ValueError:
                    pass
                mid.clear()
                mid.hideturtle()
                midshape.all_midshape.remove(mid)

    for ko in aliens.all_projectiles:
        if ko.distance(player_ship.main_ship) < 20:
            player_ship.lives -= 1

    current_num_aliens = len(aliens.all_aliens)
    if current_num_aliens < previous_num_aliens:
        if aliens.x_vel > 0:
            aliens.x_vel += 2
        else:
            aliens.x_vel -= 2
        alien_projectile_probability = max(1, alien_projectile_probability - 1)
        previous_num_aliens = current_num_aliens

    if player_ship.lives == 0:
        game_on = False

    print(f"Lives: {player_ship.lives}, Number of Aliens: {current_num_aliens}, Alien Speed: {aliens.x_vel}")

    screen.update()

screen.exitonclick()
