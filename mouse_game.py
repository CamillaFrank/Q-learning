import pygame as pg
import numpy as np
import time
pg.init()

stage = pg.image.load("stage.png")

mouse_img = pg.image.load("mouse.png")
cheese_img = pg.image.load("cheese.png")
cat_img = pg.image.load("cat.png")

stage_w,stage_h = stage.get_size()
L = 70

stage = pg.transform.scale(stage,(stage_w*L,stage_h*L))

mouse_img = pg.transform.scale(mouse_img,(L,L))
cheese_img = pg.transform.scale(cheese_img,(L,L))
cat_img = pg.transform.scale(cat_img,(L,L))

screen = pg.display.set_mode((stage_w * L,stage_h * L))
screen.blit(stage,(0,0))

pg.display.flip()
cats = []
player = ()

qtab = np.zeros((stage_w,stage_h,4))
actionlist = ['Left','Right','Up','Down']

########### Functions #############

def reward(player,player_old,target,is_trapped,snack):
    old_dist = np.aboslute(old_pos - target)
    new_dist = np.aboslute(new_pos - target)

    if is_trapped:
        Reward = -100
    elif snack:
        Reward = 100
    elif new_dist < old_dist:
        Reward = 1
    else:
        Reward = -1
    
    return Reward
    





for c in range (stage_w):
    for r in range (stage_h):
        tile = screen.get_at((c*L, r*L))[:3]
        if tile == (236,28,36):
            cats.append((c,r))
        elif tile == (255,242,0):
            cheese = (c,r)
        elif tile == (185,122,86):
            player = (c,r)
            player_start = (c,r)
            

running = True
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_UP:
                if player[1] != 0:
                    player = (player[0],player[1] - 1)
            elif event.key == pg.K_DOWN:
                if player[1] != stage_h - 1:
                    player = (player[0],player[1] + 1)
            elif event.key == pg.K_LEFT:
                if player[0] != 0:
                    player = (player[0] - 1,player[1])
            elif event.key == pg.K_RIGHT:
                if player[0] != stage_w - 1:
                    player = (player[0] + 1,player[1])


    keys = pg.key.get_pressed()

    screen.fill((252,252,252))

    screen.blit(cheese_img,(cheese[0]*L,cheese[1]*L))

    for cat in cats:
        screen.blit(cat_img,(cat[0]*L,cat[1]*L))

    screen.blit(mouse_img,(player[0]*L,player[1]*L))

    if player in cats:
        trapped = True
        #player = player_start
    if player == cheese:
        snack = True

    #Calc reward

    pg.display.flip()

    time.sleep(0.1)