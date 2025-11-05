##pc_class.py
##Mason Norvell
##Fall 2016

##Player Character Class

import pygame
from pygame.locals import *
from random import randint
import pyganim

class player_character(pygame.sprite.Sprite):

    ##class that displays a graphical representation of the player character

    def __init__(self, size, surf, pos, spriteFile):

        ##define values in class
        pygame.sprite.Sprite.__init__(self)

        self.SCALE = 3
        self.leftLook = pygame.image.load('Sprite_Files/Player_Character_left.png')
        pw, ph = self.leftLook.get_size()


        
        self.SURF = surf
        self.POS = pos
        self.SIZE = size
        self.PLAYERSPRITEfile = spriteFile
        self.active = True

        self.moveUp = False
        self.moveDown = False
        self.moveLeft = False
        self.moveRight = False
        self.lastPress = 'down'

        self.image = pygame.Surface((pw * self.SCALE, ph * self.SCALE), flags=SRCALPHA, depth=32)
        self.image.fill((0,0,0,0))
        self.rect = self.image.get_rect()
        self.rect.w = int(self.rect.w * 0.8)
        self.rect.x = pos[0] + int(ph * 1.5)
        self.rect.y = pos[1] + ph


        self.characterSprite = pygame.image.load(self.PLAYERSPRITEfile).convert_alpha()
        self.characterSprite = pygame.transform.scale(self.characterSprite, ((pw * self.SCALE), (ph * self.SCALE)))


        self.leftLook = pygame.image.load('Sprite_Files/Player_Character_left.png')
        self.rightLook = pygame.image.load('Sprite_Files/Player_Character_right.png')
        self.upLook = pygame.image.load('Sprite_Files/Player_Character_up.png')
        self.leftLook = pygame.transform.scale(self.leftLook, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.rightLook = pygame.transform.scale(self.rightLook, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.upLook = pygame.transform.scale(self.upLook, (int(pw * self.SCALE), int(ph * self.SCALE)))



        #self.rect = self.image.get_rect()
        #self.RECT_w = self.rect[0]
        #self.RECT_h = self.rect[1]
        #self.RECT_x, self.RECT_y = (self.rect - self.RECT_w//2, self.rect - self.RECT_h//2)
        #self.moveRECT_x = 0
        #self.moveRECT_y = 0

        self.SPProt = 0
        self.ROT_RATE = 5
        self.MOVE_STEP = 10
        self.NRATE = 2

        self.rotationDIRcc = 0.0
        self.rotationDIRcw = 0.0
        self.spriteROT = 0.0
        #self.RotSPP = pygame.transform.rotate(self.SPPlayer, self.spriteROT)
        self.w, self.h = size, size

        self.x, self.y = (self.POS[0] + self.w//2, self.POS[1] + self.h//2)
        self.move_y = 0
        self.move_x = 0

        self.down1 = pygame.image.load('Sprite_Files/Player_Character_down1.png').convert_alpha()
        self.down2 = pygame.image.load('Sprite_Files/Player_Character_down2.png').convert_alpha()
        self.down1 = pygame.transform.scale(self.down1, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.down2 = pygame.transform.scale(self.down2, (int(pw * self.SCALE), int(ph * self.SCALE)))


        self.walkDownAnimation = pyganim.PygAnimation([(self.down1, 0.3),
                                                       (self.characterSprite, 0.3),
                                                       (self.down2, 0.3),
                                                       (self.characterSprite, 0.3)])

        self.left1 = pygame.image.load('Sprite_Files/Player_Character_left1.png').convert_alpha()
        self.left2 = pygame.image.load('Sprite_Files/Player_Character_left2.png').convert_alpha()
        self.left1 = pygame.transform.scale(self.left1, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.left2 = pygame.transform.scale(self.left2, (int(pw * self.SCALE), int(ph * self.SCALE)))


        self.walkLeftAnimation = pyganim.PygAnimation([(self.left1, 0.3),
                                                       (self.leftLook, 0.3),
                                                       (self.left2, 0.3),
                                                       (self.leftLook, 0.3)])

        self.right1 = pygame.image.load('Sprite_Files/Player_Character_right1.png').convert_alpha()
        self.right2 = pygame.image.load('Sprite_Files/Player_Character_right2.png').convert_alpha()
        self.right1 = pygame.transform.scale(self.right1, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.right2 = pygame.transform.scale(self.right2, (int(pw * self.SCALE), int(ph * self.SCALE)))


        self.walkRightAnimation = pyganim.PygAnimation([(self.right1, 0.3),
                                                        (self.rightLook, 0.3),
                                                        (self.right2, 0.3),
                                                        (self.rightLook, 0.3)])

        self.up1 = pygame.image.load('Sprite_Files/Player_Character_up1.png').convert_alpha()
        self.up2 = pygame.image.load('Sprite_Files/Player_Character_up2.png').convert_alpha()
        self.up1 = pygame.transform.scale(self.up1, (int(pw * self.SCALE), int(ph * self.SCALE)))
        self.up2 = pygame.transform.scale(self.up2, (int(pw * self.SCALE), int(ph * self.SCALE)))


        self.walkUpAnimation = pyganim.PygAnimation([(self.up1, 0.3),
                                                     (self.upLook, 0.3),
                                                     (self.up2, 0.3),
                                                     (self.upLook, 0.3)])
        

    def moveCharacter(self, factor):

        self.walkDownAnimation.play()
        self.walkLeftAnimation.play()
        self.walkRightAnimation.play()
        self.walkUpAnimation.play()

        if self.moveDown == True:
            self.move_y = self.MOVE_STEP * factor
            self.lastPress = 'down'
        if self.moveUp == True:
            self.move_y = -self.MOVE_STEP * factor
            self.lastPress = 'up'
        if self.moveRight == True:
            self.move_x = self.MOVE_STEP * factor
            self.lastPress = 'right'
        if self.moveLeft == True:
            self.move_x = -self.MOVE_STEP * factor
            self.lastPress = 'left'
        if ((self.moveDown == False and self.moveUp == False) or
            (self.moveDown == True and self.moveUp == True)):
            self.move_y = 0
        if ((self.moveRight == False and self.moveLeft == False) or
            (self.moveRight == True and self.moveLeft == True)):
            self.move_x = 0



        self.y += self.move_y
        self.x += self.move_x
        self.rect.x += self.move_x
        self.rect.y += self.move_y

    def display(self, xOff, yOff):

        self.walkDownAnimation.play()
        self.walkLeftAnimation.play()
        self.walkRightAnimation.play()
        self.walkUpAnimation.play()

        if self.active:

            if self.moveDown:
                self.walkDownAnimation.blit(self.SURF, (self.x - xOff, self.y - yOff))
            elif self.moveUp:
                self.walkUpAnimation.blit(self.SURF, (self.x - xOff, self.y - yOff))
            elif self.moveLeft:
                self.walkLeftAnimation.blit(self.SURF, (self.x - xOff, self.y - yOff))
            elif self.moveRight:
                self.walkRightAnimation.blit(self.SURF, (self.x - xOff, self.y - yOff))
            else :
                if self.lastPress == 'down':
                    self.SURF.blit(self.characterSprite, (self.x - xOff, self.y - yOff))
                elif self.lastPress == 'left':
                    self.SURF.blit(self.leftLook, (self.x - xOff, self.y - yOff))
                elif self.lastPress == 'right':
                    self.SURF.blit(self.rightLook, (self.x - xOff, self.y - yOff))
                elif self.lastPress == 'up':
                    self.SURF.blit(self.upLook, (self.x - xOff, self.y - yOff))