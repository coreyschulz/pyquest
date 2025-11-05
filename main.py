##################################################
# PYQUEST: HOW MANY LICKS 'TILL THE VISUAL NOVEL?
# main.py
# Corey Schulz
# Fall 2016
##################################################
import pygame, sys
from pygame.locals import *
from pc_class import player_character
from wall_class import buildWall
from ItemClasses import Item
from stationary_item_class import stationaryItem
from EnemyClass import Enemy
##from squareClass import Square
from random import randrange

##Initialize Pygame
pygame.init()
pygame.mixer.init()
FPSCLOCK = pygame.time.Clock()

##Establish some variables
FPS = 120
DWIDTH = 1280
DHEIGHT = 720
DISPLAYSURF= pygame.display.set_mode((DWIDTH, DHEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('Pyventure alpha 1.000003 handicapped edition+')
BGIMAGE = pygame.image.load("Sprite_Files/stonefloor.png")
BGIMAGE = pygame.transform.scale(BGIMAGE, (128, 128))
CONTROLSIMAGE = pygame.image.load("Sprite_Files/Controls.png")
CONTROLSIMAGE = pygame.transform.scale(CONTROLSIMAGE, (901, 231))
BGCOLOR = (200,190,255)
PURPLE = (100, 10, 175)
DISPLAYSURF.fill(BGCOLOR)

PLAYERSIZE = 100
PLAYERX = DWIDTH//2
PLAYERY = DHEIGHT//2
PLAYERSPRITEFILE = 'Sprite_Files/Player_Character_down.png'

playerList = pygame.sprite.Group()
wallList = pygame.sprite.Group()
itemList = pygame.sprite.Group()
sItemList = pygame.sprite.Group()
enemyList = pygame.sprite.Group()

##Instantiate Player
PLAYER = player_character(PLAYERSIZE, DISPLAYSURF, (PLAYERX, PLAYERY), PLAYERSPRITEFILE)

##Wall Variables
WALLTHICKNESS = 100
WALLSPRITE = "Sprite_Files/Wall.png"

##Instantiate Walls
def instantiateWalls(wall_file, wList, offSetx, offSety):
    tempFile = open(wall_file, "r")

    for line in tempFile:
        tempList = line.split(',')
        tempx = int(tempList[0])
        tempy = int(tempList[1])
        tempw = int(tempList[2])
        temph = int(tempList[3])
        wList.append(buildWall(tempw, temph, DISPLAYSURF, (tempx + offSetx, tempy + offSety), WALLSPRITE))

def chooseItem(item):
    if item == 'wood':
        wood.active = True
        wood.pickedup = True
    elif item == 'stick':
        wood.pickedup = True
    elif item == 'bocarina':
        bocarina.pickedup = True
    elif item == 'redkey':
        redkey.pickedup = True
    elif item == 'bluekey':
        bluekey.pickedup = True
    elif item == 'greenkey':
        greenkey.pickedup = True
    elif item == 'shield':
        shield.pickedup = True
    elif item == 'icespell':
        icespell.pickedup = True
    elif item == 'sword':
        sword.pickedup = True


#INSTANTIATE ROOMS
C1 = []
instantiateWalls("Wall_Files/C1.txt", C1, 0, (-2040))
D4 = []
instantiateWalls("Wall_Files/D4.txt", D4, 1240, (-2040))
A5 = []
instantiateWalls("Wall_Files/A5.txt", A5, -(2480), (-1360))
B5 = []
instantiateWalls("Wall_Files/B5.txt", B5, (-1240), (-1360))
C5 = []
instantiateWalls("Wall_Files/C5.txt", C5, 0, (-1360))
D5 = []
instantiateWalls("Wall_Files/D5.txt", D5, 1240, (-1360))
B6 = []
instantiateWalls("Wall_Files/B6.txt", B6, (-1240), (-680))
C6 = []
instantiateWalls("Wall_Files/C6.txt", C6, 0, (-680))
D6 = []
instantiateWalls("Wall_Files/D6.txt", D6, 1240, (-680))
E6 = []
instantiateWalls("Wall_Files/E6.txt", E6, 2480, (-680))
B7 = []
instantiateWalls("Wall_Files/B7.txt", B7, (-1240), 0)
C7 = []
instantiateWalls("Wall_Files/C7.txt", C7, 0, 0)

ROOMLIST = [C1,D4,A5,B5,C5,D5,B6,C6,D6,E6,B7,C7]

##Instantiate Items

woodPile = stationaryItem(100, 100, DISPLAYSURF, (40,-780), "Sprite_Files/woodpile.png")
bocarina = Item(50, 50, "bocarina", (PLAYER.x, PLAYER.y), (590, -100), DISPLAYSURF)
brazier = stationaryItem(100, 100, DISPLAYSURF,(40, -1320), "Sprite_Files/LitBrazier1.png")
wood = Item(100, 100, "wood", (PLAYER.x, PLAYER.y), (40, -780), DISPLAYSURF)
torch = Item(100, 100, "torch", (PLAYER.x, PLAYER.y), (40, -1320), DISPLAYSURF)
bluekey = Item(50, 50, "key1", (PLAYER.x, PLAYER.y), (-2370, -1050), DISPLAYSURF)
greenkey = Item(50, 50, "key2", (PLAYER.x, PLAYER.y), (3530, -380), DISPLAYSURF)
redkey = Item(50, 50, "key3", (PLAYER.x, PLAYER.y), (-440, 480), DISPLAYSURF)
shield = Item(100, 100, "shield", (PLAYER.x, PLAYER.y), (-930, 470), DISPLAYSURF)
icespell = Item(100, 100, "icespell", (PLAYER.x, PLAYER.y), (1840, -1750), DISPLAYSURF)
sword = Item(100, 100, "sword", (PLAYER.x, PLAYER.y), (-330, -800), DISPLAYSURF)
darkness = stationaryItem(1240, 720, DISPLAYSURF,(-1240, -1360), "Sprite_Files/darkness.png")
brazier2 = stationaryItem(100, 100, DISPLAYSURF, (-1200, -780), "Sprite_Files/UnlitBrazier.png")
floor = stationaryItem(0, 0, DISPLAYSURF, (128, 128), "Sprite_Files/stonefloor.png")
lava = stationaryItem(1200, 300, DISPLAYSURF, (-1200, -400), "Sprite_Files/LavaLong.png")
door = stationaryItem(178, 202, DISPLAYSURF, (542, -1360), "Sprite_Files/Door.png")
chains = stationaryItem(178, 202, DISPLAYSURF, (542, -1360), "Sprite_Files/Chains.png")
redlock = stationaryItem(178, 202, DISPLAYSURF, (542, -1360), "Sprite_Files/redlock.png")
bluelock = stationaryItem(178, 202, DISPLAYSURF, (542, -1360), "Sprite_Files/bluelock.png")
greenlock = stationaryItem(178, 202, DISPLAYSURF, (542, -1360), "Sprite_Files/greenlock.png")
vines = stationaryItem(258, 101, DISPLAYSURF, (1742, -1360), "Sprite_Files/Vines.png")
pit = stationaryItem(893,514, DISPLAYSURF, (1496, -168), "Sprite_Files/Pit.png")


ITEMLIST = [bocarina,wood, torch, bluekey, greenkey, redkey, shield, icespell, sword]
SITEMLIST = [woodPile, brazier, brazier2, lava, door, chains, redlock, bluelock, greenlock, vines, pit]

##Instantiate Enemies

enemy1 = Enemy(100, 100, "genericenemy", (-2170, -1050), DISPLAYSURF)
shieldEnemy = Enemy(200, 200, "shieldenemy", (1770, -300), DISPLAYSURF)
dragon = Enemy(400,400, "dragon", (600, -2000), DISPLAYSURF)


ENEMYLIST = [enemy1, shieldEnemy, dragon]

##Add objects to respective lists
playerList.add(PLAYER)
for room in ROOMLIST:
    wallList.add(room)
for item in ITEMLIST:
    itemList.add(item)
for item in SITEMLIST:
    sItemList.add(item)
for enemy in ENEMYLIST:
    enemyList.add(enemy)


def drawFloorTiles(tile):
    for x in range(10):
        for y in range(6):
            DISPLAYSURF.blit(tile, (x*128,y*128))
#################################################### VISUAL NOVEL STUFF

from dialogue2 import *

pygame.init() # Initializes pygame for the program and computer

##COLORS
GREY      = (150, 150, 150)
WHITE     = (255, 255, 255)
ORANGE    = (255, 100, 100)
LTBLUE    = (100, 100, 255)
TEAL      = (20, 200, 200)
PURPLE    = (200, 20, 200)
DARKBLUE  = (18, 52, 86)
TRUMPRED  = (199, 34, 57)
CRORANGE  = (246, 138, 39)
LGREEN    = (78, 185, 72)
FFPINK    = (152, 96, 94)
BLACK     = (1, 1, 1)
TRANSP    = (0, 0, 0, 0)
YELLOW    = (249, 249, 85)
PMBLUE    = (173, 225, 243)

pygame.mixer.init()
vnbgm = pygame.mixer.Sound('soundeffects/winter_wind.wav')
windnoise = pygame.mixer.Sound("soundeffects/wind_sound.wav")
bossfight = pygame.mixer.Sound("soundeffects/boss_fight.wav")
bocarinanoise = pygame.mixer.Sound("soundeffects/bocarina_01.wav")
maintheme = pygame.mixer.Sound("soundeffects/main_theme.wav")
bosstheme = pygame.mixer.Sound("soundeffects/boss_fight.wav")

# Set up the window

DISPLAYWIDTH = DWIDTH
DISPLAYHEIGHT = DHEIGHT
DISPLAYSURF= pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption('Pyquest: Story Mode SIDE STORY I: NOT THE DLC BATH SCENE WE WERE HOPING FOR')
BGCOLOR = CRORANGE
TRANSPARENTCOLOR = (0, 0, 0, 0)
DISPLAYSURF.fill(BGCOLOR)



##TRANSURF INSTANTIATE - TEXT SURFACE && CHARA
##CHARA >> BOX >> TEXT RENDER ORDER


DBOXH = int(DISPLAYHEIGHT / 4)

TRANSURF =  pygame.Surface((DISPLAYWIDTH, DISPLAYHEIGHT), flags=SRCALPHA, depth=32)
BGSURF =      pygame.Surface((DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH), flags=SRCALPHA, depth=32)
DRAWSURF = pygame.Surface((DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH), flags=SRCALPHA, depth=32)

TRANSURF.fill(TRANSP)
BGSURF.fill(LTBLUE)

##SPRITES, BGs
VillageDay = 'Sprite_Files/day_village_FILLER.jpg'
PROTAGSPRITE = 'Sprite_Files/protag_FILLER.png'
BPROTAGSPRITE = 'Sprite_Files/protag_BOCARINA.png'
VILLAGERSPRITE = 'Sprite_Files/villager_FILLER.png'
VillageNight = 'Sprite_Files/night_village_FILLER.jpg'
TREESPRITE = 'Sprite_Files/tree_FILLER.png'
FINALBG2 = "Sprite_Files/finalbg2.PNG"
FINALBG1 = "Sprite_Files/finalbg1.png"
VILLAGERSCALE = 2
TREESCALE = .3

FINALBG2IMAGE = pygame.image.load(FINALBG2).convert()
FINALBG1IMAGE = pygame.image.load(FINALBG1).convert()
BGimage = pygame.image.load(VillageDay).convert()
BGimage2 = pygame.image.load(VillageNight).convert()
PROTAG = pygame.image.load(PROTAGSPRITE).convert_alpha()
BPROTAG = pygame.image.load(BPROTAGSPRITE).convert_alpha()
VILLAGER = pygame.image.load(VILLAGERSPRITE).convert_alpha()
TREE = pygame.image.load(TREESPRITE).convert_alpha()
VW, VH = VILLAGER.get_size()
TW, TH = TREE.get_size()
VILLAGER = pygame.transform.scale(VILLAGER, (int(VW * VILLAGERSCALE), int(VH * VILLAGERSCALE*1.02)))
TREE = pygame.transform.scale(TREE, (int(TW * TREESCALE), int(TH * TREESCALE)))
BGimage = pygame.transform.scale(BGimage, (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH))
BGimage2 = pygame.transform.scale(BGimage2, (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH))
FINALBG2IMAGE = pygame.transform.scale(FINALBG2IMAGE, (DISPLAYWIDTH, DISPLAYHEIGHT))
FINALBG1IMAGE = pygame.transform.scale(FINALBG1IMAGE, (DISPLAYWIDTH, DISPLAYHEIGHT))

def updateName(counter):
    characterName = str(DIALOGUE[counter][0])
    return characterName

def updateTextLn1(counter):
    dialogueTextLn1 =str( DIALOGUE[counter][1])
    return dialogueTextLn1

def updateTextLn2(counter):
    dialogueTextLn2 = str(DIALOGUE[counter][2])
    return dialogueTextLn2


###################################################### END VISUAL NOVEL STUFF

def main():
##############################VISUAL NOVEL STUFF
    visualnovel = False
    counter = 0
    pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
    displaybool = True
    characterName = "PYQUEST: INTERLUDE STORY"
    dialogueTextLn1 = "An epic conclusion to an epic story! It all ends... here and now!"
    dialogueTextLn2 = "(PROTAG just transformed into an anime girl!)"
    dialogueFont = pygame.font.Font("Chivo-Regular.ttf", 25)
    charaFont = pygame.font.Font("Chivo-Bold.otf", 70)
    CHARASURF = charaFont.render(characterName, True, WHITE, None)
    DIALOGUESURF = dialogueFont.render(dialogueTextLn1, True, BLACK, None)
    DIALOGUESURF2 = dialogueFont.render(dialogueTextLn2, True, BLACK, None)
    pygame.draw.rect(DRAWSURF, BLACK, Rect((0, 0), (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH)))
    TRANSURF.blit(CHARASURF, (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
    TRANSURF.blit(DIALOGUESURF, (int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11)))
    TRANSURF.blit(DIALOGUESURF2, (int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185)))
    BGSURF.blit(BGimage, (0, 0))
    BGSURF.blit(PROTAG, (0, 0))
    BGSURF.blit(VILLAGER, (int(DISPLAYHEIGHT * .9), int(DISPLAYHEIGHT / 10)))
    pygame.draw.rect(BGSURF, BLACK, Rect((0, 0), (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH)))
    windnoiseplay = False
    bocarinanoiseplay = False
    bossfightplay = False
    vnbgmplay = False

#############################END VISUAL NOVEL STUFF

###############Gameplay Variables
    maintheme.play(-1)
    gameplay = True
    wood.active = False
    torch.active = False
    sword.active = False
    brazierlit = False
    chains.rect.y += 200
    shieldEnemy.rect.y += 20

    pit.rect.w -=256
    pit.rect.x += 128
    pit.rect.y += 100

    bossTheme = False
    mainthemeplay = True

#################Main Game Loop
    while gameplay is True:


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN:

                if event.key == K_DOWN:
                    PLAYER.moveDown = True
                if event.key == K_UP:
                    PLAYER.moveUp = True
                if event.key == K_RIGHT:
                    PLAYER.moveRight = True
                if event.key == K_LEFT:
                    PLAYER.moveLeft = True


                PLAYER.moveCharacter(1)
                if colliding():
                    PLAYER.moveCharacter(-1)


            elif event.type == KEYUP:

                if event.key == K_DOWN:
                    PLAYER.moveDown = False
                if event.key == K_UP:
                    PLAYER.moveUp = False
                if event.key == K_RIGHT:
                    PLAYER.moveRight = False
                if event.key == K_LEFT:
                    PLAYER.moveLeft = False
                if event.key == K_z:
                    print(itemcolliding())
                    if 'wood' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        wood.active = True
                        wood.pickedup = True
                    elif 'stick' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        wood.pickedup = True
                    elif 'bocarina' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        bocarina.pickedup = True
                    elif 'redkey' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        redkey.pickedup = True
                    elif 'bluekey' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        bluekey.pickedup = True
                    elif 'greenkey' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        greenkey.pickedup = True
                    elif 'shield' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        shield.pickedup = True
                    elif 'icespell' in itemcolliding() and len(itemcolliding()) == 1:
                        for item in itemList:
                            item.pickedup = False
                        icespell.pickedup = True
                    elif 'sword' in itemcolliding() and len(itemcolliding()) == 1 and sword.active == True:
                        for item in itemList:
                            item.pickedup = False
                        sword.pickedup = True
                    elif len(itemcolliding()) > 1:
                        for item in itemList:
                            item.pickedup = False
                        chooseItem(itemcolliding()[0])

                if event.key == K_x:
                    for item in itemList:
                        item.pickedup = False
                    torch.active = False
                if event.key == K_SPACE:
                    for item in itemList:
                        if item.pickedup:
                            item.playsound()
                            item.useanimation()
                    if ('brazier' in itemcolliding()) and wood.pickedup:
                        wood.active = False
                        torch.active = True
                        torch.pickedup = True
                    if 'brazier2' in itemcolliding() and torch.pickedup:
                        brazier2.changeSprite("Sprite_Files/LitBrazier1.png")
                        brazierlit = True
                    if xOff == -1240 and yOff == -680 and icespell.pickedup:
                        lava.changeSprite("Sprite_Files/LavaLongCold.png")
                        lava.rect.w = 0
                        lava.rect.h = 0
                    if ('door' in itemcolliding()) and bluekey.pickedup:
                        print('blue')
                        bluelock.active = False
                        bluekey.active = False
                        bluekey.pickedup = False
                        bluekey.rect.y = 2000
                    if ('door' in itemcolliding()) and greenkey.pickedup:
                        print('green')
                        greenlock.active = False
                        greenkey.active = False
                        greenkey.pickedup = False
                        greenkey.rect.y = 2000
                    if ('door' in itemcolliding()) and redkey.pickedup:
                        print('red')
                        redlock.active = False
                        redkey.active = False
                        redkey.pickedup = False
                        redkey.rect.y = 2000
                    if yOff == -2040 and xOff == 0 and bocarina.pickedup:
                        gameplay = False
                        visualnovel = True
                        bossfight.stop()
                        bocarina.soundeffect.stop()



        if colliding():
            PLAYER.moveDown = False
            PLAYER.moveUp = False
            PLAYER.moveRight = False
            PLAYER.moveLeft = False


        if PLAYER.x > 0 and PLAYER.x < 1260:
            xOff = 0
        elif PLAYER.x >= 1260 and PLAYER.x < 2480:
            xOff = 1240
        elif PLAYER.x >= 2480 and PLAYER.x < 3720:
            xOff = 2480
        elif PLAYER.x <= 0 and PLAYER.x > -1240:
            xOff = -1240
            if torch.pickedup or brazierlit:
                darkness.active = False
                sword.active = True
            else:
                darkness.active = True
                sword.active = False
            enemy1.x = -2170
            enemy1.y = -1050
        elif PLAYER.x <= -1240 and PLAYER.x > -2480:
            xOff = -2480
            if enemy1.active:
                enemy1.moveToPlayer(PLAYER.x, PLAYER.y, False)



        if PLAYER.y > 0 and PLAYER.y < 720:
            yOff = 0
        elif PLAYER.y > -680:
            yOff = -680
        elif PLAYER.y > -1360:
            yOff = -1360
        elif PLAYER.y > -2040:
            yOff = -2040
        elif PLAYER.y > -2720:
            yOff = -2720

        if xOff == 1240 and yOff == -680 and shieldEnemy.active:
            shieldEnemy.moveToPlayer(PLAYER.x, PLAYER.y, False)
        elif xOff == 1240 and yOff == -1360 and shieldEnemy.active:
            shieldEnemy.x = 1770
            shieldEnemy.y = -300
            shieldEnemy.rect.x = 1770
            shieldEnemy.rect.y = -300

        if yOff == -2040 and xOff == 0:
            if bossTheme == False:
                maintheme.stop()
                bossfight.play(-1)
                bossTheme = True
                mainthemeplay = False
        else:
            if mainthemeplay == False:
                bossfight.stop()
                maintheme.play(-1)
                bossTheme = False
                mainthemeplay = True


        DISPLAYSURF.fill(BGCOLOR)
        drawFloorTiles(BGIMAGE)
        DISPLAYSURF.blit(CONTROLSIMAGE, (200 - xOff, 100- yOff))
        #floor.display(xOff, yOff)
        for wall in wallList:
            wall.display(xOff, yOff)
        for x in SITEMLIST:
            x.display(xOff, yOff)
            x.movewithcharacter(PLAYER.x, PLAYER.y, PLAYER.lastPress)
        for x in enemyList:
            x.display(xOff, yOff)
        #for item in itemList:
            #item.display(xOff, yOff)
        PLAYER.moveCharacter(1)

        if redlock.active == False and bluelock.active == False and greenlock.active == False:
            door.active = False
            chains.active = False

        # if pygame.sprite.groupcollide(playerList, wallList, False, False):
        if colliding():
            PLAYER.moveCharacter(-1)

        if "hit1" in itemcolliding():
            print('hit1')
            sword.playsound()
            enemy1.active = False
            enemy1.rect.y = 2000
        if "enemy1" in itemcolliding():
            if enemy1.active and shield.pickedup == False:
                PLAYER.x = 500
                PLAYER.y = 500
                PLAYER.rect.x = PLAYER.x
                PLAYER.rect.y = PLAYER.y
            elif enemy1.active and shield.pickedup:
                enemy.moveToPlayer(PLAYER.x, PLAYER.y, True)
        if "shieldEnemy" in itemcolliding():
            if shieldEnemy.active and shield.pickedup == False:
                PLAYER.x = 500
                PLAYER.y = 500
                PLAYER.rect.x = PLAYER.x
                PLAYER.rect.y = PLAYER.y
            elif shieldEnemy.active and shield.pickedup:
                shieldEnemy.moveToPlayer(PLAYER.x, PLAYER.y, True)
        if "dragon" in itemcolliding():
            PLAYER.x = 500
            PLAYER.y = 500
            PLAYER.rect.x = PLAYER.x
            PLAYER.rect.y = PLAYER.y
        if "vines" in itemcolliding():
            vines.active = False
            vines.rect.y = 2000
            sword.playsound()
        if "pit" in itemcolliding():
            shieldEnemy.active = False
            shieldEnemy.rect.y = 2000
        PLAYER.display(xOff, yOff)

        for x in itemList:
            x.display(xOff, yOff)
            x.movewithcharacter(PLAYER.x, PLAYER.y, PLAYER.lastPress)
        darkness.display(xOff, yOff)
        
        FPSCLOCK.tick(FPS)
        
        pygame.display.update()


######################VISUAL NOVEL LOOP

    while visualnovel:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.blit(TRANSURF, (0, 0))
        DISPLAYSURF.blit(BGSURF, (0, 0))

        if counter == 0:
            if windnoiseplay == False:
                windnoise.play(-1)
                windnoiseplay = True
        if counter == 4:
            windnoise.stop()
            if bossfightplay == False:
                bossfight.play(-1)
                bossfightplay = True
        if counter == 13:
            bossfight.stop()
            if bocarinanoiseplay == False:
                bocarinanoise.play()
                bocarinanoiseplay = True
        if counter == 19:
            if vnbgmplay == False:
                vnbgm.play(-1)
                vnbgmplay = True

        if event.type == KEYDOWN:
            # displaybool = True
            if event.key == K_SPACE or event.key == K_n or event.key == K_y:
                if displaybool == True:
                    if counter <= 9:  ##PROTAG, alive dragon. No P_bocarina.
                        BGSURF.blit(FINALBG1IMAGE, (0, 0))  ##CHANGE to INTERLUDE 1
                        BGSURF.blit(PROTAG, (0, 0))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False


                    elif counter <= 13:  ##PROTAG, alive dragon. P_BOCARINA
                        BGSURF.blit(FINALBG1IMAGE, (0, 0))  ##CHANGE to INTERLUDE 1
                        BGSURF.blit(BPROTAG, (0, 0))  ##CHANGE to P_BOCARINA
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 18:  ##PROTAG, dead dragon. No P_bocarina.
                        BGSURF.blit(FINALBG2IMAGE, (0, 0))  ##CHANGE to INTERLUDE 2
                        BGSURF.blit(PROTAG, (0, 0))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 3 + 20:
                        pygame.draw.rect(BGSURF, BLACK, Rect((0, 0), (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 25 + 20:
                        BGSURF.blit(BGimage, (0, 0))
                        BGSURF.blit(PROTAG, (0, 0))
                        BGSURF.blit(VILLAGER, (int(DISPLAYHEIGHT * .9), int(DISPLAYHEIGHT / 10)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False
                    elif counter <= 28 + 20:
                        BGSURF.blit(BGimage, (0, 0))
                        BGSURF.blit(PROTAG, (int(DISPLAYWIDTH * .4), 0))
                        BGSURF.blit(VILLAGER, (int(DISPLAYHEIGHT * .9), int(DISPLAYHEIGHT / 10)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False
                    elif counter <= 36 + 20:
                        BGSURF.blit(BGimage, (0, 0))
                        BGSURF.blit(PROTAG, (0, 0))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 52 + 20:
                        BGSURF.blit(BGimage, (0, 0))
                        BGSURF.blit(PROTAG, (0, 0))
                        pygame.draw.rect(BGSURF, BLACK, Rect((0, 0), (DISPLAYWIDTH, DISPLAYHEIGHT - DBOXH)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 58 + 20:
                        BGSURF.blit(BGimage2, (0, 0))
                        BGSURF.blit(TREE, (int(DISPLAYWIDTH * .55), 0))
                        BGSURF.blit(PROTAG, (0, 0))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False
                    elif counter <= 61 + 20:
                        BGSURF.blit(BGimage2, (0, 0))
                        BGSURF.blit(TREE, (int(DISPLAYWIDTH * .55), 0))
                        BGSURF.blit(PROTAG, ((int(DISPLAYWIDTH * .4), 0)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

                    elif counter <= 62 + 20:
                        BGSURF.blit(BGimage2, (0, 0))
                        BGSURF.blit(PROTAG, ((int(DISPLAYWIDTH * .4), 0)))
                        pygame.draw.rect(TRANSURF, PMBLUE, Rect((0, DISPLAYHEIGHT - DBOXH), (DISPLAYWIDTH, DBOXH)))
                        CHARASURF = charaFont.render(DIALOGUE[counter][0], True, WHITE, None)
                        DIALOGUESURF = dialogueFont.render(DIALOGUE[counter][1], True, BLACK, None)
                        DIALOGUESURF2 = dialogueFont.render(DIALOGUE[counter][2], True, BLACK, None)
                        TRANSURF.blit(DIALOGUESURF,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .11))))
                        TRANSURF.blit(DIALOGUESURF2,
                                      ((int(DISPLAYHEIGHT * .03125), DISPLAYHEIGHT - DBOXH + int(DISPLAYHEIGHT * .185))))
                        TRANSURF.blit(CHARASURF,
                                      (int(DISPLAYHEIGHT * .00625), DISPLAYHEIGHT - DBOXH - (DISPLAYHEIGHT / 80)))
                        counter += 1
                        displaybool = False

        if event.type == KEYUP:
            variableTester = 0
            displaybool = True

        pygame.display.update()


def colliding():

    for wall in wallList:
        if wall.active and pygame.sprite.collide_rect(PLAYER, wall):
            return True
    if lava.active and pygame.sprite.collide_rect(PLAYER, lava):
        return True
    if door.active and pygame.sprite.collide_rect(PLAYER, door):
        return True
    if vines.active and pygame.sprite.collide_rect(PLAYER, vines):
        return True
    if pit.active and pygame.sprite.collide_rect(PLAYER, pit):
        return True
    return False

def itemcolliding():
    tempHitList = []
    if pygame.sprite.collide_rect(PLAYER, woodPile):
        tempHitList.append("wood")
    if pygame.sprite.collide_rect(PLAYER, bocarina):
        tempHitList.append("bocarina")
    if pygame.sprite.collide_rect(PLAYER, wood) and wood.active:
        tempHitList.append("stick")
    if pygame.sprite.collide_rect(PLAYER, redkey):
        tempHitList.append("redkey")
    if pygame.sprite.collide_rect(PLAYER, bluekey):
        tempHitList.append("bluekey")
    if pygame.sprite.collide_rect(PLAYER, greenkey):
        tempHitList.append("greenkey")
    if pygame.sprite.collide_rect(PLAYER, shield):
        tempHitList.append("shield")
    if pygame.sprite.collide_rect(PLAYER, icespell):
        tempHitList.append("icespell")
    if pygame.sprite.collide_rect(PLAYER, sword) and sword.pickedup == False:
        tempHitList.append("sword")
    if pygame.sprite.collide_rect(shieldEnemy, pit):
        tempHitList.append("pit")
    if pygame.sprite.collide_rect(PLAYER, brazier):
        tempHitList.append("brazier")
    if pygame.sprite.collide_rect(PLAYER, chains):
        tempHitList.append("door")
    if pygame.sprite.collide_rect(PLAYER, brazier2):
        tempHitList.append("brazier2")
    if pygame.sprite.collide_rect(PLAYER, enemy1):
        tempHitList.append("enemy1")
    if pygame.sprite.collide_rect(PLAYER, shieldEnemy):
        tempHitList.append("shieldEnemy")
    if pygame.sprite.collide_rect(sword, enemy1):
        tempHitList.append("hit1")
    if pygame.sprite.collide_rect(PLAYER, lava):
        tempHitList.append("lava")
    if pygame.sprite.collide_rect(sword, vines):
        tempHitList.append("vines")
    if pygame.sprite.collide_rect(PLAYER, dragon):
        tempHitList.append("dragon")
    return tempHitList


if __name__ == '__main__': main()
