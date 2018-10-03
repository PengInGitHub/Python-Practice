#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 22:22:35 2018

@author: pengchengliu
"""
# resource
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python
# http://blog.jobbole.com/46308/

import math
######################################
#    Step 3: Let The Bunny Move      #
######################################
# let the bunny respond to key presses
# detect key presses by using 

def listen_key_press(event, keys):
    # key down
    if event.type == pygame.KEYDOWN:
        if event.key == K_w or event.key == K_UP:
            keys[0] = True
        elif event.key == K_a or event.key == K_LEFT:
            keys[1] = True
        elif event.key == K_s or event.key == K_DOWN:
            keys[2] = True            
        elif event.key == K_d or event.key == K_RIGHT:
            keys[3] = True        
    # key realeased
    if event.type == pygame.KEYUP:
        if event.key == K_w or event.key == K_UP:
            keys[0] = False
        elif event.key == K_a or event.key == K_LEFT:
            keys[1] = False
        elif event.key == K_s or event.key == K_DOWN:
            keys[2] = False            
        elif event.key == K_d or event.key == K_RIGHT:
            keys[3] = False 

def bunny_move(keys, playerpos):
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5


#####################################
#    Step 4: Turning The Bunny      #
#####################################
# set player rotation and position
def get_angle(position, playerpos):
    y_diff = position[1] - (playerpos[1]+32)
    x_diff = position[0] - (playerpos[0]+26)
    return math.atan2(y_diff, x_diff)

def get_rot_degree(angle):
    return 360 - angle*57.29
def rotate_bunny(playerpos, screen):
    # get mouse position
    position = pygame.mouse.get_pos()
    angle = get_angle(position, playerpos)
    #convert angle from radians to degree
    
    playerrot = pygame.transform.rotate(player, get_rot_degree(angle))
    new_x = playerpos[0] - playerrot.get_rect().width/2
    new_y = playerpos[1] - playerrot.get_rect().height/2
    playerpos_new = (new_x, new_y)
    screen.blit(playerrot, playerpos_new)
    return playerpos_new
        
###############################
#    Step 5: Banny Shoot      #
###############################
def shoot(event, arrows, playerpos_new):
    if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()
        angle = get_angle(position, playerpos_new)
        arrows.append([angle, playerpos_new[0]+32, playerpos_new[1]+32])
    
def draw_arrow(arrow, arrows):
    for bullet in arrows:
        # index: current index of arrow
        # speed: constant speed of the flying arrow
        index, speed = 0, 10
        # velocity in two directions
        velx, vely = math.cos(bullet[0])*speed, math.sin(bullet[0])*speed
        # change location of x and y
        bullet[1] += velx
        bullet[2] += vely
        # arrow is not inside the screen
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 640:
            # remove current arrow, the following arrow will replace
            arrows.pop(bullet)
        else: 
            # calculate next arrow            
            index += 1
            for projectile in arrows:
                arrow_new = pygame.transform.rotate(arrow, get_rot_degree(projectile[0]))
                screen.blit(arrow_new, (projectile[1], projectile[2]))
        
    
###############################
#    Step 1: Hello Bunny      #
###############################

# 1. import library
import pygame
from pygame.locals import *

# 2. init the game
pygame.init()
width, height = 640,480
screen = pygame.display.set_mode((width, height))
# key array to follow the actions of WASD
keys = [False, False, False, False]
# where the programm draws the player
playerpos = [100, 100]
# track performance: [num of arrows fired, num of badgers hit]
# track arrows
acc, arrows = [0,0], []

# 3. load images
player = pygame.image.load('resources/image/bunny.png')
grass = pygame.image.load('resources/image/grass.png')
castle = pygame.image.load('resources/image/castle.png')
arrow = pygame.image.load('resources/image/bullet.png')

# 4. infinite loop
while 1:
    # 5. clear the screen before drawing it again
    screen.fill(0)
    # add background and castle
    # draw background in a loop
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass, (x*200, y*150))
    # draw four castles
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))

    # 6. draw the screen elements, get new player position
    # 6.1 Set player position and rotation
    playerpos_new = rotate_bunny(playerpos, screen)
    # 6.2 Draw arrows
    draw_arrow(arrow, arrows)
    # 7. update the screen
    pygame.display.flip()
    # 8. listen to the signal to quit
    for event in pygame.event.get():
        # if quit
        if event.type == pygame.QUIT:
            # then quit
            pygame.quit()
            exit(0)
        listen_key_press(event, keys)
        shoot(event, arrows, playerpos_new)
    bunny_move(keys, playerpos)

###############################
#    Step 2: Add Scenery      #
###############################



            


 

















