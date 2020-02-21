import pygame

pygame.init()

mushroom=pygame.image.load('graphics/mushroom1.png')
speedImg=pygame.image.load('graphics/speed.png')
bonusImg=pygame.image.load('graphics/bonus.png')
shiftImg=pygame.image.load('graphics/shift.png')
obstacleImg=pygame.image.load('graphics/przesz.png')
icon=pygame.image.load('graphics/icon.png')
#32x32
skin1=pygame.image.load('graphics/skin1.png')
skin2=pygame.image.load('graphics/skin2.png')
skin3=pygame.image.load('graphics/skin3.png')
choosenSkin=pygame.image.load('graphics/choosenSkin.png')
#graphics menu
menu1=pygame.image.load('graphics/menu1.png')
#graphics objasnień
classicImg=pygame.image.load('graphics/classic.png')
extendedImg=pygame.image.load('graphics/extended.png')
globalImg=pygame.image.load('graphics/global.png')
globalImg=pygame.image.load('graphics/players.png')
controls1=pygame.image.load('graphics/controls.png')


backgroundTextureList = [pygame.image.load('graphics/background/background3.jpg'),
                         pygame.image.load('graphics/background/background4.jpg'),
                         pygame.image.load('graphics/background/background5.jpg'),
                         pygame.image.load('graphics/background/background6.jpg')]


fruitsTexture = [pygame.image.load('graphics/fruit1.png'),
                 pygame.image.load('graphics/fruit2.png'),
                 pygame.image.load('graphics/fruit3.png'),
                 pygame.image.load('graphics/fruit4.png'),
                 pygame.image.load('graphics/fruit5.png')]