from pygame import * 
init()
from math import *
from random import *

window_size = (1000,1000)

window = display.set_mode(window_size)

display.set_caption("Agar.io")

clock = time.Clock()

my_player = [0,0,20]
player_speed = 15

class Food:
    def __init__(self,x,y,r,c):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
    def check_collision(self,player_x,player_y,player_r):
        dx = self.x - player_x
        dy = self.y - player_y
        return hypot(dx,dy) <= self.r + player_r

eats = [Food(randint(-2000,2000),randint(-2000,2000),10,(randint(0,255),randint(0,255),randint(0,255))) for _ in range (300) ] 

running = True
while  running:
    window.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            running = False

    scale = max(0.3,min(50/my_player[2],1.5))

    to_remove = []
    for eat in eats:
        if eat.check_collision(my_player[0],my_player[1],my_player[2]):
            to_remove.append(eat)
            my_player[2] += int(eat.r * 0.2)
        else:
            sx = int((eat.x-my_player[0])*scale +500)
            sy = int((eat.y-my_player[1])*scale +500)
            draw.circle(window,eat.c,(sx,sy),int(eat.r * scale))

    draw.circle(window,(0,255,0,),(500,500),int(my_player[2] * scale))

    for eat in to_remove:
        eats.remove(eat)

    display.update()

    keys = key.get_pressed()
    if keys [K_w]:
        my_player[1] -= player_speed
    if keys [K_s]:
        my_player[1] += player_speed
    if keys [K_a]:
        my_player[0] -= player_speed
    if keys [K_d]:
        my_player[0] += player_speed


    clock.tick(60)







