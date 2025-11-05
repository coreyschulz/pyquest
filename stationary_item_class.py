##stationary_item_class.py
##Mason Norvell
##Fall 2016

import pygame
from pygame.locals import *
from random import randint
import pyganim

class stationaryItem(pygame.sprite.Sprite):

    #Class that creates a stationary item

    def __init__(self, width, height, surf, pos, spriteFile):

        pygame.sprite.Sprite.__init__(self)

        self.WIDTH = width
        self.HEIGHT = height
        self.SURF = surf
        self.POS = pos
        self.SPRITEfile = spriteFile

        self.image = pygame.Surface((width, height), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.active = True
        self.pickedup = False

        self.SSprite = pygame.image.load(self.SPRITEfile).convert_alpha()
        self.SSprite = pygame.transform.scale(self.SSprite, (self.WIDTH, self.HEIGHT))
        self.image.blit(self.SSprite, (0, 0))

        self.x = pos[0]
        self.y = pos[1]

        if spriteFile == "Sprite_Files/LitBrazier1.png" or spriteFile == "Sprite_Files/UnlitBrazier.png":
            self.flame1 = pygame.image.load("Sprite_Files/LitBrazier1.png")
            self.flame1 = pygame.transform.scale(self.flame1, (width, height))
            self.flame2 = pygame.image.load("Sprite_Files/LitBrazier2.png")
            self.flame2 = pygame.transform.scale(self.flame2, (width, height))
            self.flame3 = pygame.image.load("Sprite_Files/LitBrazier3.png")
            self.flame3 = pygame.transform.scale(self.flame3, (width, height))

            self.flameAnim = pyganim.PygAnimation([(self.flame1, 0.2),
                                                   (self.flame2, 0.2),
                                                   (self.flame3, 0.2)])


    def movewithcharacter(self, x, y, p):
        pass

    def changeSprite(self, new_sprite):
        self.SPRITEfile = new_sprite
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.SSprite = pygame.image.load(new_sprite).convert_alpha()
        self.SSprite = pygame.transform.scale(self.SSprite, (self.WIDTH, self.HEIGHT))
        self.image.blit(self.SSprite, (0, 0))

    def display(self, xOff, yOff):

        if self.SPRITEfile == "Sprite_Files/LitBrazier1.png" and self.active:
            self.flameAnim.play()
            self.flameAnim.blit(self.SURF, (self.x - xOff, self.y - yOff))
        elif self.active:
            self.SURF.blit(self.image, (self.x - xOff, self.y - yOff))
