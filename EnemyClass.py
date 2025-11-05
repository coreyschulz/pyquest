# ///////////////////////////////////////////////////////
# Pyquest: How Many Licks 'Till the Visual Novel?
# ENEMY CLASS: LET'S MAKE A CASUAL GAME WITH NO COMABT
# ///////////////////////////////////////////////////////

import pygame, sys
from pygame.locals import *
pygame.init()
pygame.mixer.init()
from random import randint

genericenemy = "Sprite_Files/EnemyRight.png"
dragon = "Sprite_Files/dragon.png"
shieldenemy = "Sprite_Files/EnemyShield.png"



class Enemy(pygame.sprite.Sprite):
    def __init__(self, width, height, enemytype, position, surf):

        pygame.sprite.Sprite.__init__(self)

        self.x = position[0]
        self.y = position[1]
        self.WIDTH = width
        self.HEIGHT = height
        self.surf = surf
        self.active = True
        self.enemytype = enemytype
        self.SPRITEfile = enemytype

        self.image = pygame.Surface((width, height), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

        if self.enemytype == "dragon":
            self.SPRITEfile = dragon
        if self.enemytype == "genericenemy":
            self.SPRITEfile = genericenemy
        if self.enemytype == "shieldenemy":
            self.SPRITEfile = shieldenemy

        self.ESprite = pygame.image.load(self.SPRITEfile).convert_alpha()
        self.ESprite = pygame.transform.scale(self.ESprite, (self.WIDTH, self.HEIGHT))
        self.image.blit(self.ESprite, (0, 0))

    def moveToPlayer(self, PLAYERPOSX, PLAYERPOSY, isShield):
        if isShield == False and self.enemytype == "genericenemy":
            if self.x > PLAYERPOSX:
                self.x -= randint(5,20)
                self.rect.x = self.x
            if self.x < PLAYERPOSX:
                self.x += randint(5,20)
                self.rect.x = self.x
            if self.y < PLAYERPOSY:
                self.y += randint(5,20)
                self.rect.y = self.y
            if self.y > PLAYERPOSY:
                self.y -= randint(5,20)
                self.rect.y = self.y
        elif isShield == False and self.enemytype == "shieldenemy":
            if self.y < PLAYERPOSY:
                self.y += randint(1,5)
                self.rect.y = self.y
            if self.y > PLAYERPOSY:
                self.y -= randint(1,5)
                self.rect.y = self.y
        elif isShield:
            self.y += 50


    def display(self, xOff, yOff):
        if self.active:
            self.surf.blit(self.image, (self.x - xOff, self.y - yOff))
