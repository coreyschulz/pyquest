# ////////////////////////////////////////////////
# Pyquest: How Many Licks 'Till the Visual Novel?
# ITEM CLASSES: BUILD THINGS OTHER THAN WALLS
# ////////////////////////////////////////////////

import pygame, sys
from pygame.locals import *
pygame.init()
pygame.mixer.init()

bocarinasound  = "soundeffects/bocarina.wav"
keysound       = "soundeffects/key.wav"
woodsound      = "soundeffects/wood.wav"
torchsound     = "soundeffects/torch.wav"
icespellsound  = "soundeffects/icespell.wav"
swordsound     = "soundeffects/sword.wav"
shieldsound    = "soundeffects/shield.wav"
bridgesound    = "soundeffects/bridge.wav"

bocarinasprite = "Sprite_Files/bocarina.png"
keysprite1     = "Sprite_Files/bluekey.png"
keysprite2     = "Sprite_Files/greenkey.png"
keysprite3     = "Sprite_Files/redkey.png"
woodsprite     = "Sprite_Files/wood.png"
torchsprite    = "Sprite_Files/torch.png"
icespellsprite = "Sprite_Files/IceSpellOpen.png"
swordspriteup    = "Sprite_Files/sword_up.png"
swordspriteleft  = "Sprite_Files/sword_left.png"
swordspriteright = "Sprite_Files/sword_right.png"
swordspritedown  = "Sprite_Files/sword_down.png"
shieldsprite   = "Sprite_Files/shield.png"
bridgesprite   = "Sprite_Files/wood.png"

class Item(pygame.sprite.Sprite):
    def __init__(self, width, height, itemtype, characterposition, itemposition, surf):

        pygame.sprite.Sprite.__init__(self)


        self.grounddisplay = True
        self.width = width
        self.height = height
        self.surf = surf
        self.itempositionx = itemposition[0]
        self.itempositiony = itemposition[1]
        self.characterpositionx = characterposition[0]
        self.characterpositiony = characterposition[1]
        self.itemtype = itemtype
        self.usedbool = False
        self.pickedup = False

        self.active = True

        self.image = pygame.Surface((width, height), flags=SRCALPHA, depth=32)
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = itemposition[0]
        self.rect.y = itemposition[1]

        self.displaysprite = "nothing.png"
        if self.itemtype == "bocarina":
            self.displaysprite = bocarinasprite
        elif self.itemtype == "key1":
            self.displaysprite = keysprite1
        elif self.itemtype == "key2":
            self.displaysprite = keysprite2
        elif self.itemtype == "key3":
            self.displaysprite = keysprite3
        elif self.itemtype == "wood":
            self.displaysprite = woodsprite
        elif self.itemtype == "torch":
            self.displaysprite = torchsprite
        elif self.itemtype == "icespell":
            self.displaysprite = icespellsprite
        elif self.itemtype == "shield":
            self.displaysprite = shieldsprite
        elif self.itemtype == "bridge":
            self.displaysprite = bridgesprite
        elif self.itemtype == "sword":
            self.displaysprite = swordspriteup

        self.ISprite = pygame.image.load(self.displaysprite).convert_alpha()
        self.ISprite = pygame.transform.scale(self.ISprite, (width, height))
        self.image.blit(self.ISprite, (0, 0))


    def playsound(self):
        if self.itemtype == "bocarina":
            self.soundeffect = pygame.mixer.Sound("soundeffects/bocarina_01.wav")
        if self.itemtype == "key1":
            self.soundeffect = pygame.mixer.Sound(keysound)
        if self.itemtype == "key2":
            self.soundeffect = pygame.mixer.Sound(keysound)
        if self.itemtype == "key3":
            self.soundeffect = pygame.mixer.Sound(keysound)
        if self.itemtype == "wood":
            self.soundeffect = pygame.mixer.Sound(woodsound)
        if self.itemtype == "torch":
            self.soundeffect = pygame.mixer.Sound(torchsound)
        if self.itemtype == "icespell":
            self.soundeffect = pygame.mixer.Sound(icespellsound)
        if self.itemtype == "sword":
            self.soundeffect = pygame.mixer.Sound(swordsound)
        if self.itemtype == "shield":
            self.soundeffect = pygame.mixer.Sound(shieldsound)
        if self.itemtype == "bridge":
            self.soundeffect = pygame.mixer.Sound(bridgesound)
        #if self.usedbool == True and self.pickedup == True:
        self.soundeffect.play()

    def useanimation(self):
        self.itempositionx += 10
        self.itempositiony += 10

    def useswordanimation(self):
        self.itempositionx -= 100
        self.rect.x -= 100

    def resetanimation(self):
        if self.usedbool == False and self.pickedup == True:
            self.itempositionx -= 10
            self.itempositiony -= 10

    def movewithcharacter(self, PPOSITIONX, PPOSITIONY, playerLastFacing):
        if self.pickedup and self.itemtype == "sword":
            if playerLastFacing == "left":
                self.displaysprite = swordspriteleft
                self.itempositionx = PPOSITIONX - 100
                self.itempositiony = PPOSITIONY
                self.rect.x = PPOSITIONX - 100
                self.rect.y = PPOSITIONY
            elif playerLastFacing == "up":
                self.displaysprite = swordspriteup
                self.itempositiony = PPOSITIONY - 100
                self.itempositionx = PPOSITIONX
                self.rect.y = PPOSITIONY - 100
                self.rect.x = PPOSITIONX
            elif playerLastFacing == "right":
                self.displaysprite = swordspriteright
                self.itempositionx = PPOSITIONX + 100
                self.itempositiony = PPOSITIONY
                self.rect.x = PPOSITIONX + 100
                self.rect.y = PPOSITIONY
            elif playerLastFacing == "down":
                self.displaysprite = swordspritedown
                self.itempositiony = PPOSITIONY + 100
                self.itempositionx = PPOSITIONX
                self.rect.y = PPOSITIONY + 100
                self.rect.x = PPOSITIONX
            self.ISprite = pygame.image.load(self.displaysprite).convert_alpha()
            self.ISprite = pygame.transform.scale(self.ISprite, (self.width, self.height))
            self.image.fill((0, 0, 0, 0))
            self.image.blit(self.ISprite, (0, 0))
        elif self.pickedup:
            self.itempositionx = PPOSITIONX
            self.itempositiony = PPOSITIONY
            self.rect.x = PPOSITIONX
            self.rect.y = PPOSITIONY


    def display(self, xOff, yOff):
        if self.active:
            self.surf.blit(self.image, (self.itempositionx - xOff, self.itempositiony - yOff))