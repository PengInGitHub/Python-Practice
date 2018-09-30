#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 07:42:40 2018

@author: pengchengliu
"""

import pygame
from Role import *
from pygame.locals import *
import random
from sys import exit

# the principals of 2D game
# in each round of the main loop (infinite loop):
# draw the images of objects in corresponding locations
# the animation effects root from the change of locatins of images
# knocking or crashing of obejcts are defined as the collision of img rects

# make use of pygame.sprite.Sprite class
# Sprite represent a single movable obj, it has Surface & Rect two objs



##############################
#      set up the screen     #
##############################       

# init the game
pygame.init()
# set screen
screen = pygame.display.set_mode((480, 800))
# set caption
pygame.display.set_caption('Shoot Game')

# background graph
background = pygame.image.load('PythonShootGame/resources/image/background.png').convert()
# background graph of game over
game_over = pygame.image.load('PythonShootGame/resources/image/gameover.png')

#####################################
#      set up the sound effects     #
#####################################

bullet_sound = pygame.mixer.Sound('PythonShootGame/resources/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('PythonShootGame/resources/sound/enemy1_down.wav')
game_over_sound = pygame.mixer.Sound('PythonShootGame/resources/sound/game_over.wav')

bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)

pygame.mixer.music.load('PythonShootGame/resources/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)


##############################
#      set up the player     #
##############################

# all the images we need are in the resources/image folder

# all the objects in this game such as player(air plane), bullet, enemy ...
# are surface objects in the context of Pygame

# in this way, in order to init these objects we could get the images 

# plane graph
plane_img = pygame.image.load('PythonShootGame/resources/image/shoot.png')

# this image has a lot of resources, we need to set parameters on the img
# by using subsurface(), in order to for example draw a beautiful air plane

# init a list to store player parameters
player_rect = []
# img the player was fine
player_rect.append(pygame.Rect(165, 360, 102, 126))
# img the player was knocked
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))

# init player
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)


##############################
#      set up the bullet     #
##############################

bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

##############################
#      set up the enemy      #
##############################

# choose a typy of enemy from the chart
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)

# imgs of enemies got knocked down
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 697, 57, 43)))

# enemies group defined as sprite.Group
# when they are alive
enemies1 = pygame.sprite.Group()
# when they got shoot
enemies_down = pygame.sprite.Group()


##########################################
#      the main logic of the game        #
##########################################

score = 0
clock = pygame.time.Clock()
# shoot_frequency is used to control the frequency of bullet shooting
shoot_frequency, enemy_frequency = 0, 0
player_down_index = 16
# flag to control the running of game
Running = True


while Running:
    
    # set FPS Frame Per Second as 60
    clock.tick(60)
    
    ##############################
    #   handel bullet frequency  #
    ##############################
    
    # shoot and control the frequency of shooting    
    # bullet should keep on coming out of the player while the player is alive
    # generate and control the frequency of bullet
    
    # if player is safe and sound
    # make a shooting every 15 times of iteration!
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            bullet_sound.play()
            player.shoot(bullet_img)

        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0
 
    ##############################
    #    let the bullets fly     #
    ##############################    
    
    for bullet in player.bullets:
        # bullet moves at a steady spped
        bullet.move()
        
        # remove bullet if it is out of screen
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)

    ##############################
    #    handel enemy frequency  #
    ##############################
    
    # generate enemies with certain frequency
    # every 50 iterations generate an enemy
    if enemy_frequency % 50 == 0:
        # at random position
        enemy1_pos = [random.randint(0, SCREEN_WIDTH-enemy1_rect.width), 0]
        # init an enemy
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    
    # control frequency
    enemy_frequency += 1
    if enemy_frequency >= 100:
        enemy_frequency = 0
       
    ##############################
    #    let the enemies move    #
    ##############################  

    
    # let the enemy move
    for enemy in enemies1:
        # move the air plane
        enemy.move()
        
        # remove enemy if it is out of screen
        if enemy.rect.top < 0:
            enemies1.remove(enemy)
 
    # enemy crashed with player or got knocked
        
    # handle the effects when enemy and player crashed
    # crash is defined as collide_circle(obj1, obj2) == True
    # collision test
    if pygame.sprite.collide_circle(enemy, player):
        # add enemy to enemies_down
        enemies_down.add(enemy)
        # remove enemy from alive enemies
        enemies1.remove(enemy)
        # set knocked flag to True
        player.is_hit = True
        # game over
        game_over_sound.play()
        break
    
    
    # handle the effects when enemy is knocked (collide(enemy, bullet))
    # add to knocked-down enemies
    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy_down in enemies1_down:
         enemies_down.add(enemy_down)
    
    ###################################
    #    draw objects on the screen   #
    ###################################
    
    # draw background
    screen.fill(0)
    screen.blit(background, (0,0))

    # draw player
    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        # modify the img_index to generate animation effects
        player.img_index = shoot_frequency // 8
    else:
        # player got shoot, change img via img_index
        player.img_index = player_down_index // 8
        screen.blit(player.img[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 47:
            Running = False
        
    # make animation effects when enemy is knocked down
    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            enemy1_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 1000
            continue

        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)
        enemy_down.down_index += 1
        
    # draw bullets and enemies on screen
    player.bullets.draw(screen)
    enemies1.draw(screen)

    # draw scores
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)
    
   # update screen
    pygame.display.update()
   
    # quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    ################################
    #         event listener       #
    ################################
    
    # handel keyboard
    # to control the move of player's plane
    
    # get key pressed
    key_pressed = pygame.key.get_pressed()
    
    # move the air plane
    if not player.is_hit:
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()

        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()

        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()

        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()


# draw score text
font = pygame.font.Font(None, 48)
text = font.render('Score: '+str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(game_over, (0,0))
screen.blit(text, text_rect)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()



































