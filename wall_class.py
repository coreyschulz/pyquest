##wall_class.py
##Mason Norvell
##Fall 2016

##Wall Class

import pygame
from pygame.locals import *
from random import randint

class buildWall(pygame.sprite.Sprite):

    #Class that creates a grapic wall

    def __init__(self, width, height, surf, pos, spriteFile):

        pygame.sprite.Sprite.__init__(self)

        self.WIDTH = width
        self.HEIGHT = height
        self.SURF = surf
        self.POS = pos
        self.WALLSPRITEfile = spriteFile

        self.active = True

        self.image = pygame.Surface((width, height), flags=SRCALPHA, depth=32)
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.wallSprite = pygame.image.load(self.WALLSPRITEfile).convert_alpha()
        self.wallSprite = pygame.transform.scale(self.wallSprite, (self.WIDTH, self.HEIGHT))
        self.image.blit(self.wallSprite, (0,0))

        self.x = pos[0]
        self.y = pos[1]

    def display(self, xOff, yOff):

        if self.active:

            self.SURF.blit(self.image, (self.x - xOff, self.y - yOff))