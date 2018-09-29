#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 07:42:40 2018

@author: pengchengliu
"""
import pygame


### constants
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

TYPE_SMALL = 1
TYPE_MEDIUM = 2
TYPE_BIG = 3

#####################################
#         create Bullet class       #
#####################################

### Bullet
# class extends pygame.sprite.Sprite
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, bullet_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10
    
    def move(self):
        self.rect.top -= self.speed
 

#####################################
#         create Player class       #
#####################################

### Player
# class extends pygame.sprite.Sprite       
class Player(pygame.sprite.Sprite):
    
    def __init__(self, plane_img, player_rect, init_pos):
        pygame.sprite.Sprite.__init__(self)
        
        # list for storing player imgs
        self.image = []
        for i in range(len(player_rect)):
            # img.subsurface(rect).convert_aplha() returns sub img
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())

        # init the rect where play is initially
        self.rect = player_rect[0]
        self.rect.topleft = init_pos
        # init player speed
        self.speed = 8
        # init players' bullets 
        self.bullets = pygame.sprite.Group()
        # image index
        self.img_index = 0
        # is knocked
        self.is_hit = False

    # actions: shoot, move up, down, left, right
    def shoot(self, bullet_img):
        # init Bullet class
        bullet = Bullet(bullet_img, self.rect.midtop)
        self.bullets.add(bullet)
    
    def moveUp(self):
        # upper boundry
        if self.rect.top < 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed
    
    def moveDown(self):
        # lower boundry
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed
    
    def moveLeft(self):
        # left boundry
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
        
    def moveRight(self):
        # right boundry
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.right += self.speed
        

#####################################
#         create Enemy class        #
#####################################

### Enemy
# class extends pygame.sprite.Sprite       
class Enemy(pygame.sprite.Sprite):

    def __init__(self, enemy_img, enemy_down_imgs, init_pos): 
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.down_imgs = enemy_down_imgs
        self.speed = 2
        self.down_index = 0
    
    def move(self):
        self.rect.top += self.speed
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    