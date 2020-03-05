import random

import pygame

mushroomIMG = pygame.image.load('graphics/mushroom.png')
speedIMG = pygame.image.load('graphics/speed.png')
bonusIMG = pygame.image.load('graphics/bonus.png')
shiftIMG = pygame.image.load('graphics/shift.png')
obstacleIMG = pygame.image.load('graphics/obstacle.png')
iconIMG = pygame.image.load('graphics/icon.png')
skin1IMG = pygame.image.load('graphics/skin1.png')
skin2IMG = pygame.image.load('graphics/skin2.png')
skin3IMG = pygame.image.load('graphics/skin3.png')
pointingArrowIMG = pygame.image.load('graphics/pointingArrow.png')

menuIMG = pygame.image.load('graphics/menu1.png')
controlsIMG = pygame.image.load('graphics/controls.png')
classicGameDescriptionIMG = pygame.image.load('graphics/classicDescription.png')
extendedGameDescriptionIMG = pygame.image.load('graphics/extendedDescription.png')
globalGameDescriptionIMG = pygame.image.load('graphics/globalDescription.png')
playersGameDescriptionIMG = pygame.image.load('graphics/playersDescription.png')

fruitTextureList = [pygame.image.load('graphics/fruit1.png'),
                    pygame.image.load('graphics/fruit2.png'),
                    pygame.image.load('graphics/fruit3.png'),
                    pygame.image.load('graphics/fruit4.png'),
                    pygame.image.load('graphics/fruit5.png')
                    ]

backgroundTextureList = [pygame.image.load('graphics/background/background1.png'),
                         pygame.image.load('graphics/background/background2.png')]


def backgroundTextureRandom():
    randomNumber = random.randrange(2)
    return backgroundTextureList[randomNumber]


def randomFruitSkin():
    random.seed()
    return fruitTextureList[random.randrange(5)]
