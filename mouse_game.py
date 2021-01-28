import pygame as pg
import numpy as np
import random
import time
pg.init()

stage = pg.image.load("stage.png")

mouse_img = pg.image.load("mouse.png")
cheese_img = pg.image.load("cheese.png")
cat_img = pg.image.load("cat.png")

stage_w,stage_h = stage.get_size()
L = 40
stage = pg.transform.scale(stage,(stage_w*L,stage_h*L))

mouse_img = pg.transform.scale(mouse_img,(L,L))
cheese_img = pg.transform.scale(cheese_img,(L,L))
cat_img = pg.transform.scale(cat_img,(L,L))

screen = pg.display.set_mode((stage_w * L,stage_h * L))
screen.blit(stage,(0,0))

pg.display.flip()
cats = []
player = ()
snack = False
trapped = False
border = False

epsilon = 1.0
epsilondecay = 0.00005
discount = 0.9
lrate = 0.2

old_player = (0,0)

t = 1
vel = [1,0.5,0.1]

route = []

qtab = np.zeros((stage_w,stage_h,4))
actionlist = ['Up','Down','Left','Right']

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
            

########### Functions #############

def reward(new_pos,old_pos,target,is_trapped,snack,route):
    global qtab,lrate,discount
    if is_trapped:
        for i,m in enumerate(route):
            R = -100 * (i+1/len(route))
            qtab[int(m[0]), int(m[1]), m[2]] =  qtab[int(m[0]), int(m[1]), m[2]] + lrate*(R + (discount**i)*(np.max(qtab[int(m[0]), int(m[1])] -  qtab[int(m[0]), int(m[1]), m[2]])))
    elif snack:
        for i,m in enumerate(route):
            R = 100000 * (i+1/len(route))
            qtab[int(m[0]), int(m[1]), m[2]] =  qtab[int(m[0]), int(m[1]), m[2]] + lrate*(R + (discount**i)*(np.max(qtab[int(m[0]), int(m[1])] -  qtab[int(m[0]), int(m[1]), m[2]])))
    
def action(qtable):
    global epsilon
    global player
    chance = random.uniform(0,1)
    deciding = True
    border = False
    if chance < epsilon:
        while deciding:
            choice = random.randrange(len(actionlist))
            if actionlist[choice] == 'Up' and player[1] != 0:
                player = (player[0],player[1] - 1)
                deciding = False

            elif actionlist[choice] == 'Down' and player[1] != stage_h - 1:
                player = (player[0],player[1] + 1)
                deciding = False

            elif actionlist[choice] == 'Left' and player[0] != 0:
                player = (player[0] - 1,player[1])
                deciding = False

            elif actionlist[choice] == 'Right' and player[0] != stage_w - 1:
                player = (player[0] + 1,player[1])
                deciding = False
    else:
        
        choice = np.argmax(qtable[player[0], player[1]])
        if actionlist[choice] == 'Up':
            if player[1] != 0:
                player = (player[0],player[1] - 1)
            else:
                border = True
            

        elif actionlist[choice] == 'Down':
            if player[1] != stage_h - 1:
                player = (player[0],player[1] + 1)
            else:
                border = True
            
            
        elif actionlist[choice] == 'Left':
            if player[0] != 0:
                player = (player[0] - 1,player[1])
            else:
                border = True
                

        elif actionlist[choice] == 'Right':
            if player[0] != stage_w - 1:
                player = (player[0] + 1,player[1])
            else:
                border = True
                
    epsilon = epsilon - epsilondecay
    return choice,border



############ Program ##############
running = True
while running:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            elif event.key == pg.K_PLUS:
                if t < len(vel):
                    t = t + 1
            elif event.key == pg.K_MINUS:
                if t > 0:
                    t = t - 1



    keys = pg.key.get_pressed()

    old_player = player[:]
    choice,border = action(qtab)
    route.append([old_player[0],old_player[1],choice])

    screen.fill((252,252,252))

    screen.blit(cheese_img,(cheese[0]*L,cheese[1]*L))

    for cat in cats:
        screen.blit(cat_img,(cat[0]*L,cat[1]*L))

    screen.blit(mouse_img,(player[0]*L,player[1]*L))

    if player in cats:
        trapped = True
    if player == cheese:
        snack = True

    if border:
        qtab[int(old_player[0]), int(old_player[1]), choice] = qtab[int(old_player[0]), int(old_player[1]), choice] + (-10*10**10)

    if trapped or snack:
        R = reward(player,old_player,cheese,trapped,snack,route)
        player = player_start
        snack = False
        trapped = False
        route = []
        

    pg.display.flip()
    print(player, qtab[player])
    print('______________________________________________________')
    if t != len(vel):
        time.sleep(vel[t])
#test