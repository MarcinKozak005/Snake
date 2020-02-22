import pygame
import time
import random

pygame.init()

# COLOURS
white = (255, 255, 255)
black = (0, 0, 0)

red = (205, 0, 0)
lightRed = (255, 0, 0)

green = (0, 155, 0)
lightGreen = (0, 255, 0)

yellow = (255, 255, 0)
changeYellow = (252, 239, 3)

blue = (54, 5, 250)
changeBlue = (0, 128, 255)

violet = (245, 12, 222)
changeViolet = (170, 6, 154)

orange = (255, 128, 0)
changeOrange = (236, 58, 21)

grey = (200, 200, 200)
light_grey = (250, 250, 250)
# COLOURS end

displayHeight = 600
displayWidth = 800
blockSize = 20
direction = "right"
direction2 = "right"

scoreBarHeight = 40
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)
smallFontSize = 25

# graphics
mushroom = pygame.image.load('graphics/mushroom.png')
speedImg = pygame.image.load('graphics/speed.png')
bonusImg = pygame.image.load('graphics/bonus.png')
shiftImg = pygame.image.load('graphics/shift.png')
obstacleImg = pygame.image.load('graphics/przesz.png')
icon = pygame.image.load('graphics/icon.png')
# 32x32
skin1 = pygame.image.load('graphics/skin1.png')
skin2 = pygame.image.load('graphics/skin2.png')
skin3 = pygame.image.load('graphics/skin3.png')
choosenSkin = pygame.image.load('graphics/choosenSkin.png')
# graphics menu
menu1 = pygame.image.load('graphics/menu1.png')
# graphics objasnień
classicimg = pygame.image.load('graphics/classic.png')
extendedimg = pygame.image.load('graphics/extended.png')
globalimg = pygame.image.load('graphics/global.png')
playersimg = pygame.image.load('graphics/players.png')
sterowanie1 = pygame.image.load('graphics/controls.png')

# ustawienie okna i ikony+ tekst
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Wunsz rzeczny, bardzo niebezpieczny")
pygame.display.set_icon(icon)

FPS = 7
clock = pygame.time.Clock()

backgroundTextureList = [pygame.image.load('graphics/background/background3.jpg'),
                         pygame.image.load('graphics/background/background4.jpg'),
                         pygame.image.load('graphics/background/background5.jpg'),
                         pygame.image.load('graphics/background/background6.jpg')]


def backgroundTextureRandom():
    randomNumber = random.randrange(4)
    return backgroundTextureList[randomNumber]


# losowanie skina fruitka
def fruits_skin_rand():
    random.seed()
    numer = random.randrange(5)
    if (numer == 0):
        fruitsimg = pygame.image.load('graphics/fruit1.png')
    elif (numer == 1):
        fruitsimg = pygame.image.load('graphics/fruit2.png')
    elif (numer == 2):
        fruitsimg = pygame.image.load('graphics/fruit3.png')
    elif (numer == 3):
        fruitsimg = pygame.image.load('graphics/fruit4.png')
    elif (numer == 4):
        fruitsimg = pygame.image.load('graphics/fruit5.png')
    return fruitsimg


# definicja snake'a ?
def snake(blockSize, snakelist, headimg, bodyimg):
    if (direction == "right"):
        head = pygame.transform.rotate(headimg, 270)
    if (direction == "left"):
        head = pygame.transform.rotate(headimg, 90)
    if (direction == "up"):
        head = headimg
    if (direction == "down"):
        head = pygame.transform.rotate(headimg, 180)

    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))

    for XiY in snakelist[:-1]:
        gameDisplay.blit(bodyimg, (XiY[0], XiY[1]))


def snake2(blockSize, snakelist2, headimg2, bodyimg2):
    if (direction2 == "right"):
        head2 = pygame.transform.rotate(headimg2, 270)
    if (direction2 == "left"):
        head2 = pygame.transform.rotate(headimg2, 90)
    if (direction2 == "up"):
        head2 = headimg2
    if (direction2 == "down"):
        head2 = pygame.transform.rotate(headimg2, 180)

    gameDisplay.blit(head2, (snakelist2[-1][0], snakelist2[-1][1]))

    for XiY in snakelist2[:-1]:
        # pygame.draw.rect(gameDisplay,green, [XiY[0],XiY[1],blockSize,blockSize])
        gameDisplay.blit(bodyimg2, (XiY[0], XiY[1]))


def pause():
    paused = True
    while (paused == True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_c):
                    paused = False
                elif (event.key == pygame.K_q):
                    game_intro()
        gameDisplay.blit(menu1, (0, 0))
        message_to_screen("Paused", black, -100, size="large")
        message_to_screen("Nacisnij 'C' by grać dalej", black, 10, size="small")
        message_to_screen("Nacisnij 'Q' by wyjsc do menu", black, 55, size="small")
        pygame.display.update()
        clock.tick(5)


# wyswiebackgroundnie w rogu
def powerups(przyspieszenie, bonus_points, shift):
    powery = smallfont.render("Aktywne ulepszenia: ", True, black)
    gameDisplay.blit(powery, [400, 0])
    if (przyspieszenie == True):
        gameDisplay.blit(speedImg, [635, 10])
    if (bonus_points == True):
        gameDisplay.blit(bonusImg, [655, 10])
    if (shift == True):
        gameDisplay.blit(shiftImg, [675, 10])


# wyswiebackgroundnie score'a
def score(score):
    text = smallfont.render("Wynik: " + str(score), True, black)
    gameDisplay.blit(text, [0, 0])


def score2(score):
    text = smallfont.render("Wynik: " + str(score), True, black)
    gameDisplay.blit(text, [650, 0])


# jak nazwa mowi
def text_to_button(msg, colour, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = ((buttonx + (buttonwidth / 2), buttony + (buttonheight / 2)))
    gameDisplay.blit(textSurf, textRect)


# do buttonow potrzebne
def text_objects(text, colour, size):
    if (size == "small"):
        textSurface = smallfont.render(text, True, colour)
    elif (size == "medium"):
        textSurface = medfont.render(text, True, colour)
    elif (size == "large"):
        textSurface = largefont.render(text, True, colour)
    return textSurface, textSurface.get_rect()


# nazwa
def message_to_screen(msg, colour, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, colour, size)
    textRect.center = (displayWidth / 2), (displayHeight / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


# guziki
def button(text, x, y, width, height, inactive_colour, active_colour, action=None, action2=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + width > cur[0] > x and y + height > cur[1] > y):
        if (action2 != None):
            if (action2 == "classic"):
                gameDisplay.blit(classicimg, (300, 150))
            elif (action2 == "extended"):
                gameDisplay.blit(extendedimg, (300, 150))
            elif (action2 == "global"):
                gameDisplay.blit(globalimg, (300, 150))
            elif (action2 == "players"):
                gameDisplay.blit(playersimg, (300, 150))
        pygame.draw.rect(gameDisplay, active_colour, (x, y, width, height))
        if (click[0] == 1 and action != None):
            if (action == "quit"):
                pygame.quit()
                quit()
            if (action == "intro"):
                game_intro()
            if (action == "intro1"):
                sub_game_menu()
            if (action == "controls"):
                sterowanie()
            if (action == "play"):
                sub_game_menu()
            if (action == "classic"):
                gameLoop("classic")
            if (action == "rozbud"):
                gameLoop("rozbud")
            if (action == "global"):
                gameLoop("global")
            if (action == "multi"):
                gameLoop("players")
            if (action == "skins"):
                wybor_skina()
            if (action == "zielony1"):
                skin1 = open("skin1.txt", "r+")
                skin1.write("ziel")
                skin1.close()
            if (action == "czerwony1"):
                skin1 = open("skin1.txt", "r+")
                skin1.write("czer")
                skin1.close()
            if (action == "niebieski1"):
                skin1 = open("skin1.txt", "r+")
                skin1.write("nieb")
                skin1.close()
            if (action == "zielony2"):
                skin2 = open("skin2.txt", "r+")
                skin2.write("ziel")
                skin2.close()
            if (action == "czerwony2"):
                skin2 = open("skin2.txt", "r+")
                skin2.write("czer")
                skin2.close()
            if (action == "niebieski2"):
                skin2 = open("skin2.txt", "r+")
                skin2.write("nieb")
                skin2.close()
            if (action == "no"):
                paused = False


    else:
        pygame.draw.rect(gameDisplay, inactive_colour, (x, y, width, height))

    text_to_button(text, black, x, y, width, height)


# pygame.display.update()
def wybor_skina():
    wybor = True
    while (wybor == True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        plik_skin1 = open("skin1.txt", "r")
        dane = plik_skin1.read()
        if (dane == "ziel"):
            gameDisplay.blit(choosenSkin, (165, 125))
        elif (dane == "czer"):
            gameDisplay.blit(choosenSkin, (390, 125))
        elif (dane == "nieb"):
            gameDisplay.blit(choosenSkin, (615, 125))
        plik_skin1.close()

        plik_skin2 = open("skin2.txt", "r")
        dane = plik_skin2.read()
        if (dane == "ziel"):
            gameDisplay.blit(choosenSkin, (165, 275))
        elif (dane == "czer"):
            gameDisplay.blit(choosenSkin, (390, 275))
        elif (dane == "nieb"):
            gameDisplay.blit(choosenSkin, (615, 275))
        plik_skin2.close()

        message_to_screen("Wybierz skina węża", black, -275, "medium")
        message_to_screen("Singleplayer", black, -200, "small")
        button("Ziel/Czer", 100, 150, 150, 50, green, lightGreen, action="zielony1")
        button("Czer/czarny", 325, 150, 150, 50, red, lightRed, action="czerwony1")
        button("Nieb/Zółty", 550, 150, 150, 50, blue, changeBlue, action="niebieski1")
        message_to_screen("Multiplayer", black, -50, "small")
        button("Ziel/Czer", 100, 300, 150, 50, green, lightGreen, action="zielony2")
        button("Czer/czarny", 325, 300, 150, 50, red, lightRed, action="czerwony2")
        button("Nieb/Zółty", 550, 300, 150, 50, blue, changeBlue, action="niebieski2")
        gameDisplay.blit(skin1, (145, 400))
        gameDisplay.blit(skin2, (370, 400))
        gameDisplay.blit(skin3, (595, 400))

        button("Powrót", 275, 525, 250, 50, red, lightRed, action="intro1")

        pygame.display.update()
        clock.tick(15)


def sub_game_menu():
    gmenu = True
    while (gmenu == True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("Wybierz rodzaj rozgrywki", black, -250, "medium")
        button("Klasyczny", 20, 150, 250, 50, yellow, changeYellow, action="classic", action2="classic")
        button("Rozbudowany", 20, 225, 250, 50, green, lightGreen, action="rozbud", action2="extended")
        button("Global", 20, 300, 250, 50, blue, changeBlue, action="global", action2="global")
        button("Dla dwóch graczy", 20, 375, 250, 50, orange, changeOrange, action="multi", action2="players")
        button("Wybor skina", 20, 450, 250, 50, violet, changeViolet, action="skins")
        button("Powrót", 20, 525, 250, 50, red, lightRed, action="intro")

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True
    while (intro == True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        gameDisplay.blit(menu1, (0, 0))
        message_to_screen("Snake", green, -200, "large")

        # BUTTONY
        button("Graj", 275, 200, 250, 50, green, lightGreen, action="play")
        button("Zasady i sterowanie", 275, 300, 250, 50, grey, light_grey, action="controls")
        button("Wyjscie", 275, 400, 250, 50, red, lightRed, action="quit")

        pygame.display.update()
        clock.tick(15)


def sterowanie():
    sterowanie = True
    while (sterowanie == True):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

        gameDisplay.blit(sterowanie1, (0, 0))
        button("Powrót", 525, 525, 250, 50, red, lightRed, action="intro")

        pygame.display.update()
        clock.tick(15)


def getSkinOne():
    skin1 = open("skin1.txt", "r")
    linia1 = skin1.readline()
    skin1.close()
    if (linia1 == "ziel"):
        return (pygame.image.load('graphics/head1.png'), pygame.image.load('graphics/body1.png'))
    elif (linia1 == "czer"):
        return (pygame.image.load('graphics/head2.png'), pygame.image.load('graphics/body2.png'))
    elif (linia1 == "nieb"):
        return (pygame.image.load('graphics/head3.png'), pygame.image.load('graphics/body3.png'))


def randFruitPosition():
    X = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    Y = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    return [X, Y]


def checkBorder(snake, displayWidth, displayHeight, scoreBarHeight):
    if (snake.leadX >= displayWidth or snake.leadX < 0 or snake.leadY >= displayHeight or snake.leadY < scoreBarHeight):
        return True
    return False


class Snake:
    def __init__(self, leadX, leadY, headImg, bodyImg):
        self.direction = "right"
        self.leadX = leadX
        self.leadY = leadY
        self.xChange = 20
        self.yChange = 0
        self.snakeList = []
        self.snakeList.append([self.leadX, self.leadY])
        self.snakeLength = 3
        self.headImg = headImg
        self.bodyImg = bodyImg

    def setChange(self, X, Y):
        self.xChange = X
        self.yChange = Y

    def setDirection(self, newDirection):
        self.direction = newDirection

    def move(self):
        self.leadX += self.xChange
        self.leadY += self.yChange

        self.snakeList.append([self.leadX, self.leadY])

        if (self.direction == "right"):
            head = pygame.transform.rotate(self.headImg, 270)
        if (self.direction == "left"):
            head = pygame.transform.rotate(self.headImg, 90)
        if (self.direction == "up"):
            head = self.headImg
        if (self.direction == "down"):
            head = pygame.transform.rotate(self.headImg, 180)

        gameDisplay.blit(head, (self.snakeList[-1][0], self.snakeList[-1][1]))

        # part = [X,Y]
        for part in self.snakeList[:-1]:
            gameDisplay.blit(self.bodyImg, (part[0], part[1]))

    def checkSnakeLength(self):
        if (len(self.snakeList) > self.snakeLength):
            del self.snakeList[0]

    def checkHeadOverlapsBody(self):
        for eachSegment in self.snakeList[:-1]:
            if (eachSegment == [self.leadX, self.leadY]):
                return True


def classic():
    skin = getSkinOne()
    snake = Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
    fruitPosition = randFruitPosition()
    background = backgroundTextureRandom()

    getNewFruit = True
    gameExit = False
    gameOver = False

    player1Score = 0

    while (gameExit != True):
        while (gameOver == True):
            snake.setChange(0, 0)

            message_to_screen("Przegrałes", white, y_displace=-50, size="large")
            button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="classic")
            button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
            pygame.display.update()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    gameExit = True
                    gameOver = False

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):
                    if (snake.direction != "right"):
                        snake.setDirection("left")
                        snake.setChange(-blockSize, 0)
                elif (event.key == pygame.K_d):
                    if (snake.direction != "left"):
                        snake.setDirection("right")
                        snake.setChange(blockSize, 0)
                elif (event.key == pygame.K_w):
                    if (snake.direction != "down"):
                        snake.setDirection("up")
                        snake.setChange(0, -blockSize)
                elif (event.key == pygame.K_s):
                    if (snake.direction != "up"):
                        snake.setDirection("down")
                        snake.setChange(0, blockSize)
                elif (event.key == pygame.K_p):
                    pause()

        if (getNewFruit == True):
            img = fruits_skin_rand()
            getNewFruit = False

        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(img, fruitPosition)
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        score(player1Score)
        snake.move()
        snake.checkSnakeLength()
        pygame.display.update()

        gameOver = checkBorder(snake, displayWidth, displayHeight, scoreBarHeight) or snake.checkHeadOverlapsBody()

        if ([snake.leadX, snake.leadY] == fruitPosition):
            fruitPosition = randFruitPosition()

            while (fruitPosition in snake.snakeList):
                fruitPosition = randFruitPosition()

            snake.snakeLength += 1
            player1Score += 10
            getNewFruit = True

        clock.tick(FPS)

    pygame.quit()
    quit()


def extended(tryb="rozbud"):
    przejscie = 1
    # potrzebne do losowania skina pierwszych jeblek~cos takiego to powyzsze
    losuj2 = True
    losuj3 = True
    czasmushroom = time.time()
    jest_mushroom = False
    czasPrzeszkoda = time.time()
    jest_przeszkoda = False
    czaspowerup = time.time()
    jest_powerup = False
    # czas przyspieszenia jest nizej
    przyspieszenie = False
    bonus_points = False
    shift = False
    czas_tr_speed = 7
    czas_tr_bonus = 10
    czas_tr_shift = 7
    czas_spawn_power = 3
    # byl_mushroom=False
    apple_list = []
    global direction
    direction = "right"
    # losowac_skin_Fruits=True
    gameExit = False
    gameOver = False
    lead_x = displayWidth / 2
    lead_y = displayHeight / 2
    lead_x_change = 20
    lead_y_change = 0

    snakelist = []
    snakeLength = 3
    score1 = 0

    # losowanie background
    background = backgroundTextureRandom()

    skin1 = open("skin1.txt", "r")
    linia1 = skin1.readline()
    if (linia1 == "ziel"):
        headimg = pygame.image.load('graphics/head1.png')
        bodyimg = pygame.image.load('graphics/body1.png')
    elif (linia1 == "czer"):
        headimg = pygame.image.load('graphics/head2.png')
        bodyimg = pygame.image.load('graphics/body2.png')
    elif (linia1 == "nieb"):
        headimg = pygame.image.load('graphics/head3.png')
        bodyimg = pygame.image.load('graphics/body3.png')
    skin1.close()

    randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple = [randAppleX, randAppleY]
    apple_list.append(placeApple)

    randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY2 = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple2 = [randAppleX2, randAppleY2]

    # sprawdza czy sie powtarza z applelist
    while (losuj2 == True):
        checked_losuj2 = 0
        for eachElem in apple_list[:]:
            if (placeApple2 == eachElem):
                break
            else:
                checked_losuj2 += 1
        if (checked_losuj2 == len(apple_list)):
            losuj2 = False
            apple_list.append(placeApple2)
        randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
        randAppleY2 = scoreBarHeight + round(
            random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
        placeApple2 = [randAppleX2, randAppleY2]

    randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY3 = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple3 = [randAppleX3, randAppleY3]

    # sprawdza czy sie powtarza z applelist
    while (losuj3 == True):
        checked_losuj3 = 0
        for eachElem in apple_list[:]:
            if (placeApple3 == eachElem):
                break
            else:
                checked_losuj3 += 1
        if (checked_losuj3 == len(apple_list)):
            losuj3 = False
            apple_list.append(placeApple3)
        randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
        randAppleY3 = scoreBarHeight + round(
            random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
        placeApple3 = [randAppleX3, randAppleY3]

    while (gameExit != True):
        while (gameOver == True):
            # brak poruszenia po koncu gry
            lead_x_change = 0
            lead_y_change = 0
            message_to_screen("Przegrałes", white, y_displace=-50, size="large")
            button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action=tryb)
            button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
            pygame.display.update()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    gameExit = True
                    gameOver = False

        if (przyspieszenie == True):
            koniecprzyspieszenia = time.time() - czasprzyspieszenie
            if (koniecprzyspieszenia > czas_tr_speed):
                FPS = 7
                przyspieszenie = False
            else:
                FPS = 14
        else:
            FPS = 7

        if (shift == True):
            koniecshift = time.time() - czasshift
            if (koniecshift > czas_tr_shift):
                shift = False

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True
            if (event.type == pygame.KEYDOWN):
                if (shift == False):
                    if (event.key == pygame.K_a):
                        if (direction != "right"):
                            direction = "left"
                            lead_x_change = -blockSize
                            lead_y_change = 0
                    elif (event.key == pygame.K_d):
                        if (direction != "left"):
                            direction = "right"
                            lead_x_change = blockSize
                            lead_y_change = 0
                    elif (event.key == pygame.K_w):
                        if (direction != "down"):
                            direction = "up"
                            lead_y_change = -blockSize
                            lead_x_change = 0
                    elif (event.key == pygame.K_s):
                        if (direction != "up"):
                            direction = "down"
                            lead_y_change = blockSize
                            lead_x_change = 0
                    elif (event.key == pygame.K_p):
                        pause()
                elif (shift == True):
                    if (event.key == pygame.K_a):
                        if (direction != "left"):
                            direction = "right"
                            lead_x_change = blockSize
                            lead_y_change = 0
                    elif (event.key == pygame.K_d):
                        if (direction != "right"):
                            direction = "left"
                            lead_x_change = -blockSize
                            lead_y_change = 0
                    elif (event.key == pygame.K_w):
                        if (direction != "up"):
                            direction = "down"
                            lead_y_change = blockSize
                            lead_x_change = 0
                    elif (event.key == pygame.K_s):
                        if (direction != "down"):
                            direction = "up"
                            lead_y_change = -blockSize
                            lead_x_change = 0
                    elif (event.key == pygame.K_p):
                        pause()

        lead_x += lead_x_change
        lead_y += lead_y_change

        # wyjscie poza plansze
        if (tryb == "rozbud"):
            if (lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < scoreBarHeight):
                gameOver = True
        elif (tryb == "global"):
            if (lead_x == displayWidth):
                lead_x = 0
            elif (lead_x == 0 - blockSize):
                lead_x = displayWidth
            elif (lead_y == displayHeight):
                lead_y = 0 + scoreBarHeight
            elif (lead_y < 0 + scoreBarHeight):
                lead_y = displayHeight

        gameDisplay.blit(background, (0, 0))

        if (przejscie == 1):
            appleimg = pygame.image.load('graphics/fruit1.png')
            appleimg2 = pygame.image.load('graphics/fruit2.png')
            appleimg3 = pygame.image.load('graphics/fruit3.png')
            przejscie = 2

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        gameDisplay.blit(appleimg2, (randAppleX2, randAppleY2))
        gameDisplay.blit(appleimg3, (randAppleX3, randAppleY3))

        # ustawianie mushrooma i losowanie jego wspolrzednych
        koniecmushroom = time.time() - czasmushroom
        if (koniecmushroom > 10 and jest_mushroom == False):
            # if(byl_mushroom==False):
            randmushroomX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randmushroomY = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placemushroom = [randmushroomX, randmushroomY]
            # sprawdzanie mushroomka na snake i fruitek
            sprawdzaj_M = True
            losuj_noweM = False
            while (sprawdzaj_M == True):

                checked_snake = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placemushroom):
                        print("MnaS")
                        losuj_noweM = True
                        break
                    else:
                        checked_snake += 1

                checked_apple = 0
                if (losuj_noweM == False):
                    for eachElem in apple_list[:]:
                        if (eachElem == placemushroom):
                            print("MnaO")
                            losuj_noweM = True
                            break
                        else:
                            checked_apple += 1

                if (jest_przeszkoda == True and losuj_noweM == False):
                    if (placemushroom == placePrzesz):
                        losuj_noweM = True

                if (jest_powerup == True and losuj_noweM == False):
                    if (placemushroom == placePower):
                        losuj_noweM = True

                if (checked_snake == len(snakelist) and checked_apple == len(apple_list) and losuj_noweM == False):
                    sprawdzaj_M = False

                if (losuj_noweM == True):
                    losuj_noweM = False
                    randmushroomX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randmushroomY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placemushroom = [randmushroomX, randmushroomY]
            jest_mushroom = True

        if (jest_mushroom == True):
            gameDisplay.blit(mushroom, (randmushroomX, randmushroomY))

        # przeszkoda
        koniecPrzeszkoda = time.time() - czasPrzeszkoda
        if (koniecPrzeszkoda > 5 and jest_przeszkoda == False):
            # podwojne blocksize aby dalo sie okrazyc
            randPrzeszX = round(random.randrange(blockSize, displayWidth - blockSize - blockSize) / 20.0) * 20.0
            randPrzeszY = scoreBarHeight + round(
                random.randrange(blockSize, displayHeight - scoreBarHeight - blockSize - blockSize) / 20.0) * 20.0
            placePrzesz = [randPrzeszX, randPrzeszY]

            sprawdzaj_snakeP = True
            losuj_noweP = False
            while (sprawdzaj_snakeP == True):

                checked = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placePrzesz):
                        print("PnaS")
                        losuj_noweP = True
                        break
                    else:
                        checked += 1

                # checked_apple=0
                if (losuj_noweP == False):
                    for eachElem in apple_list[:]:
                        if (eachElem == placePrzesz):
                            print("PnaO")
                            losuj_noweP = True
                            break
                        # else:
                        # checked_apple+=1

                if (jest_mushroom == True and losuj_noweP == False):
                    if (placePrzesz == placemushroom):
                        losuj_noweP = True

                if (jest_powerup == True and losuj_noweP == False):
                    if (placePrzesz == placePower):
                        losuj_noweP = True

                if (checked == len(snakelist) and losuj_noweP == False):
                    sprawdzaj_snakeP = False

                if (losuj_noweP == True):
                    losuj_noweP = False
                    randPrzeszX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randPrzeszY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placePrzesz = [randPrzeszX, randPrzeszY]

            jest_przeszkoda = True

        # powerup
        koniecpowerup = time.time() - czaspowerup
        if (koniecpowerup > czas_spawn_power and jest_powerup == False):

            numer_power = random.randrange(3)
            if (numer_power == 0):
                powerupimg = speedImg
            elif (numer_power == 1):
                powerupimg = bonusImg
            elif (numer_power == 2):
                powerupimg = shiftImg

            randPowerX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randPowerY = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placePower = [randPowerX, randPowerY]
            # sprawdzanie powera na snake i fruitek
            sprawdzaj_PU = True
            losuj_nowePU = False

            while (sprawdzaj_PU == True):

                checked_snake = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placePower):
                        print("PUnaS")
                        losuj_nowePU = True
                        break
                    else:
                        checked_snake += 1

                checked_apple = 0
                if (losuj_nowePU == False):
                    for eachElem in apple_list[:]:
                        if (eachElem == placePower):
                            print("PUnaO")
                            losuj_nowePU = True
                            break
                        else:
                            checked_apple += 1

                if (jest_przeszkoda == True and losuj_nowePU == False):
                    if (placePower == placePrzesz):
                        losuj_nowePU = True

                if (jest_mushroom == True and losuj_nowePU == False):
                    if (placePower == placemushroom):
                        losuj_nowePU = True

                if (checked_snake == len(snakelist) and checked_apple == len(apple_list) and losuj_nowePU == False):
                    sprawdzaj_PU = False

                if (losuj_nowePU == True):
                    losuj_nowePU = False
                    randPowerX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randPowerY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placePower = [randPowerX, randPowerY]
            jest_powerup = True

        if (jest_powerup == True):
            gameDisplay.blit(powerupimg, (randPowerX, randPowerY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(blockSize, snakelist, headimg, bodyimg)

        # wyswiebackgroundnie przeszkody po snaku-wazniejsza
        if (jest_przeszkoda == True):
            gameDisplay.blit(obstacleImg, (randPrzeszX, randPrzeszY))

        # Gorne menu
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])

        if (len(snakelist) > snakeLength):
            del snakelist[0]

        # czy wjechal sam w siebie
        for eachSegment in snakelist[:-1]:
            if (eachSegment == snakehead):
                gameOver = True

        score(score1)
        powerups(przyspieszenie, bonus_points, shift)
        pygame.display.update()

        if (bonus_points == True):
            koniecbonuspoints = time.time() - czasbonuspoints
            if (koniecbonuspoints > czas_tr_bonus):
                bonus_points = False
                bonus = 0
            else:
                bonus = 5
        else:
            bonus = 0

        # zjadanie jabluszka1
        if (lead_x == randAppleX and lead_y == randAppleY):
            randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple = [randAppleX, randAppleY]

            sprawdzaj_snakeO = True
            losuj_noweO = False
            while (sprawdzaj_snakeO == True):

                checked = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple):
                        print("ala")
                        losuj_noweO = True
                        break
                    else:
                        checked += 1

                if (jest_mushroom == True):
                    if (placeApple == placemushroom):
                        losuj_noweO = True

                if (jest_przeszkoda == True and losuj_noweO == False):
                    if (placeApple == placePrzesz):
                        losuj_noweO = True

                if (jest_powerup == True and losuj_noweO == False):
                    if (placeApple == placePower):
                        losuj_noweO = True

                if (placeApple == placeApple2 or placeApple == placeApple3):
                    losuj_noweO = True

                if (checked == len(snakelist) and losuj_noweO == False):
                    sprawdzaj_snakeO = False

                if (losuj_noweO == True):
                    losuj_noweO = False
                    randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple = [randAppleX, randAppleY]
            apple_list.pop(0)
            apple_list.insert(0, [randAppleX, randAppleY])
            snakeLength += 1
            score1 += 10 + bonus
            appleimg = fruits_skin_rand()

        # zjadanie jabloszka 2
        if (lead_x == randAppleX2 and lead_y == randAppleY2):
            randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY2 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple2 = [randAppleX2, randAppleY2]

            sprawdzaj_snakeO2 = True
            losuj_noweO2 = False
            while (sprawdzaj_snakeO2 == True):

                checked2 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple2):
                        print("ala")
                        losuj_noweO2 = True
                        break
                    else:
                        checked2 += 1

                if (jest_mushroom == True and losuj_noweO2 == False):
                    if (placeApple2 == placemushroom):
                        losuj_noweO2 = True

                if (jest_przeszkoda == True and losuj_noweO2 == False):
                    if (placeApple2 == placePrzesz):
                        losuj_noweO2 = True

                if (jest_powerup == True and losuj_noweO2 == False):
                    if (placeApple2 == placePower):
                        losuj_noweO2 = True

                if (placeApple2 == placeApple or placeApple2 == placeApple3):
                    losuj_noweO2 = True

                if (checked2 == len(snakelist) and losuj_noweO2 == False):
                    sprawdzaj_snakeO2 = False

                if (losuj_noweO2 == True):
                    losuj_noweO2 = False
                    randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY2 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple2 = [randAppleX2, randAppleY2]
            apple_list.pop(1)
            apple_list.insert(1, [randAppleX2, randAppleY2])
            snakeLength += 1
            score1 += 10 + bonus
            appleimg2 = fruits_skin_rand()

        # zjadanie jabluszka3
        if (lead_x == randAppleX3 and lead_y == randAppleY3):
            randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY3 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple3 = [randAppleX3, randAppleY3]

            sprawdzaj_snakeO3 = True
            losuj_noweO3 = False
            while (sprawdzaj_snakeO3 == True):

                checked3 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple3):
                        print("ala")
                        losuj_noweO3 = True
                        break
                    else:
                        checked3 += 1

                if (jest_mushroom == True):
                    if (placeApple3 == placemushroom):
                        losuj_noweO3 = True

                if (jest_przeszkoda == True and losuj_noweO3 == False):
                    if (placeApple3 == placePrzesz):
                        losuj_noweO3 = True

                if (jest_powerup == True and losuj_noweO3 == False):
                    if (placeApple3 == placePower):
                        losuj_noweO3 = True

                if (placeApple3 == placeApple or placeApple3 == placeApple2):
                    losuj_noweO3 = True

                if (checked3 == len(snakelist) and losuj_noweO3 == False):
                    sprawdzaj_snakeO3 = False

                if (losuj_noweO3 == True):
                    losuj_noweO3 = False
                    randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY3 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple3 = [randAppleX3, randAppleY3]
            apple_list.pop(2)
            apple_list.insert(2, [randAppleX3, randAppleY3])
            snakeLength += 1
            score1 += 10 + bonus
            appleimg3 = fruits_skin_rand()

        # zjadanie mushrooma
        if (jest_mushroom == True):
            if (lead_x == randmushroomX and lead_y == randmushroomY):
                jest_mushroom = False
                score1 -= 5
                snakeLength -= 1
                czasmushroom = time.time()
                if (snakeLength <= 2):
                    gameOver = True

        # "zjadanie" przeszkody
        if (jest_przeszkoda == True):
            if (lead_x == randPrzeszX and lead_y == randPrzeszY):
                gameOver = True

        # zjadanie powerupa
        if (jest_powerup == True):
            if (lead_x == randPowerX and lead_y == randPowerY):
                jest_powerup = False
                czaspowerup = time.time()
                if (powerupimg == speedImg):
                    przyspieszenie = True
                    czasprzyspieszenie = time.time()
                elif (powerupimg == bonusImg):
                    bonus_points = True
                    czasbonuspoints = time.time()
                elif (powerupimg == shiftImg):
                    shift = True
                    czasshift = time.time()

        # okrazenie przeszkody
        if (jest_przeszkoda == True):
            P1 = False
            P2 = False
            P3 = False
            P4 = False
            P5 = False
            P6 = False
            P7 = False
            P8 = False

            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX - blockSize, randPrzeszY - blockSize]):
                    P1 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX, randPrzeszY - blockSize]):
                    P2 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX + blockSize, randPrzeszY - blockSize]):
                    P3 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX - blockSize, randPrzeszY]):
                    P4 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX + blockSize, randPrzeszY]):
                    P5 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX - blockSize, randPrzeszY + blockSize]):
                    P6 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX, randPrzeszY + blockSize]):
                    P7 = True
            for eachSegment in snakelist[:]:
                if (eachSegment == [randPrzeszX + blockSize, randPrzeszY + blockSize]):
                    P8 = True
            if (
                    P1 == True and P2 == True and P3 == True and P4 == True and P5 == True and P6 == True and P7 == True and P8 == True):
                score1 += 50
                jest_przeszkoda = False
                czasPrzeszkoda = time.time()

        clock.tick(FPS)

    pygame.quit()
    quit()


def players():
    czas = time.clock()
    czas_rozgrywki = 60
    uplynelo_czas = time.clock() - czas
    pozostaly_czas = czas_rozgrywki - uplynelo_czas
    FPS = 7
    przejscie = 1
    # potrzebne do losowania skina pierwszych jeblek~cos takiego to powyzsze
    losuj2 = True
    losuj3 = True
    apple_list = []
    global direction
    direction = "right"
    # losowac_skin_Fruits=True
    gameExit = False
    gameOver = False
    lead_x = 0
    lead_y = 40 + 3 * blockSize
    lead_x_change = 20
    lead_y_change = 0

    snakelist = []
    snakeLength = 3
    score1 = 0

    global direction2
    direction2 = "left"
    lead_x2 = displayWidth - blockSize
    lead_y2 = displayHeight - 3 * blockSize
    lead_x_change2 = -20
    lead_y_change2 = 0

    snakelist2 = []
    snakeLength2 = 3
    score2p = 0

    skin1 = open("skin1.txt", "r")
    linia1 = skin1.readline()
    if (linia1 == "ziel"):
        headimg = pygame.image.load('graphics/head1.png')
        bodyimg = pygame.image.load('graphics/body1.png')
    elif (linia1 == "czer"):
        headimg = pygame.image.load('graphics/head2.png')
        bodyimg = pygame.image.load('graphics/body2.png')
    elif (linia1 == "nieb"):
        headimg = pygame.image.load('graphics/head3.png')
        bodyimg = pygame.image.load('graphics/body3.png')
    skin1.close()

    skin2 = open("skin2.txt", "r")
    linia2 = skin2.readline()
    if (linia2 == "ziel"):
        headimg2 = pygame.image.load('graphics/head1.png')
        bodyimg2 = pygame.image.load('graphics/body1.png')
    elif (linia2 == "czer"):
        headimg2 = pygame.image.load('graphics/head2.png')
        bodyimg2 = pygame.image.load('graphics/body2.png')
    elif (linia2 == "nieb"):
        headimg2 = pygame.image.load('graphics/head3.png')
        bodyimg2 = pygame.image.load('graphics/body3.png')
    skin2.close()

    """
    randomNumber=random.randrange(2)
    if(randomNumber==0):
        background=pygame.image.load('background1.png')
    elif(randomNumber==1):
        background=pygame.image.load('background2.png')
    """
    background = backgroundTextureRandom()

    randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple = [randAppleX, randAppleY]
    apple_list.append(placeApple)

    randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY2 = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple2 = [randAppleX2, randAppleY2]

    # sprawdza czy sie powtarza z applelist
    while (losuj2 == True):
        checked_losuj2 = 0
        for eachElem in apple_list[:]:
            if (placeApple2 == eachElem):
                break
            else:
                checked_losuj2 += 1
        if (checked_losuj2 == len(apple_list)):
            losuj2 = False
            apple_list.append(placeApple2)
        randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
        randAppleY2 = scoreBarHeight + round(
            random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
        placeApple2 = [randAppleX2, randAppleY2]

    randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    randAppleY3 = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    placeApple3 = [randAppleX3, randAppleY3]

    # sprawdza czy sie powtarza z applelist
    while (losuj3 == True):
        checked_losuj3 = 0
        for eachElem in apple_list[:]:
            if (placeApple3 == eachElem):
                break
            else:
                checked_losuj3 += 1
        if (checked_losuj3 == len(apple_list)):
            losuj3 = False
            apple_list.append(placeApple3)
        randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
        randAppleY3 = scoreBarHeight + round(
            random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
        placeApple3 = [randAppleX3, randAppleY3]

    while (gameExit != True):
        while (gameOver == True or pozostaly_czas < 0):
            # brak poruszenia po koncu gry
            lead_x_change = 0
            lead_y_change = 0
            if (gameOver == True):
                if (winny == 1):
                    message_to_screen("Wygrywa gracz nr.2", white, y_displace=-50, size="large")
                    button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="multi")
                    button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            gameExit = True
                            gameOver = False
                elif (winny == 2):
                    message_to_screen("Wygrywa gracz nr.1", white, y_displace=-50, size="large")
                    button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="multi")
                    button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            gameExit = True
                            gameOver = False
            elif (pozostaly_czas < 0):
                if (score1 > score2p):
                    message_to_screen("Wygrywa gracz nr.1", white, y_displace=-50, size="large")
                elif (score1 < score2p):
                    message_to_screen("Wygrywa gracz nr.2", white, y_displace=-50, size="large")
                else:
                    message_to_screen("Remis", white, y_displace=-50, size="large")
                button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="multi")
                button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
                pygame.display.update()
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT):
                        gameExit = True
                        gameOver = False
        #######################

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_a):
                    if (direction != "right"):
                        direction = "left"
                        lead_x_change = -blockSize
                        lead_y_change = 0
                elif (event.key == pygame.K_d):
                    if (direction != "left"):
                        direction = "right"
                        lead_x_change = blockSize
                        lead_y_change = 0
                elif (event.key == pygame.K_w):
                    if (direction != "down"):
                        direction = "up"
                        lead_y_change = -blockSize
                        lead_x_change = 0
                elif (event.key == pygame.K_s):
                    if (direction != "up"):
                        direction = "down"
                        lead_y_change = blockSize
                        lead_x_change = 0

                if (event.key == pygame.K_LEFT):
                    if (direction2 != "right"):
                        direction2 = "left"
                        lead_x_change2 = -blockSize
                        lead_y_change2 = 0
                elif (event.key == pygame.K_RIGHT):
                    if (direction2 != "left"):
                        direction2 = "right"
                        lead_x_change2 = blockSize
                        lead_y_change2 = 0
                elif (event.key == pygame.K_UP):
                    if (direction2 != "down"):
                        direction2 = "up"
                        lead_y_change2 = -blockSize
                        lead_x_change2 = 0
                elif (event.key == pygame.K_DOWN):
                    if (direction2 != "up"):
                        direction2 = "down"
                        lead_y_change2 = blockSize
                        lead_x_change2 = 0



                elif (event.key == pygame.K_p):
                    pause()

        lead_x += lead_x_change
        lead_y += lead_y_change

        lead_x2 += lead_x_change2
        lead_y2 += lead_y_change2

        # wyjscie poza plansze
        if (lead_x >= displayWidth or lead_x < 0 or lead_y >= displayHeight or lead_y < scoreBarHeight):
            gameOver = True
            winny = 1

        if (lead_x2 >= displayWidth or lead_x2 < 0 or lead_y2 >= displayHeight or lead_y2 < scoreBarHeight):
            gameOver = True
            winny = 2

        gameDisplay.blit(background, (0, 0))

        if (przejscie == 1):
            appleimg = pygame.image.load('graphics/fruit1.png')
            appleimg2 = pygame.image.load('graphics/fruit2.png')
            appleimg3 = pygame.image.load('graphics/fruit3.png')
            przejscie = 2

        gameDisplay.blit(appleimg, (randAppleX, randAppleY))
        gameDisplay.blit(appleimg2, (randAppleX2, randAppleY2))
        gameDisplay.blit(appleimg3, (randAppleX3, randAppleY3))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(blockSize, snakelist, headimg, bodyimg)

        snakehead2 = []
        snakehead2.append(lead_x2)
        snakehead2.append(lead_y2)
        snakelist2.append(snakehead2)
        snake2(blockSize, snakelist2, headimg2, bodyimg2)
        # ZAKOŃCZYŁEM TU!

        # Gorne menu
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])

        if (len(snakelist) > snakeLength):
            del snakelist[0]

        if (len(snakelist2) > snakeLength2):
            del snakelist2[0]

        # czy wjechal sam w siebie
        for eachSegment in snakelist[:-1]:
            if (eachSegment == snakehead):
                gameOver = True
                winny = 1

        for eachSegment in snakelist2[:-1]:
            if (eachSegment == snakehead2):
                gameOver = True
                winny = 2

        for eachSegment in snakelist2[:-1]:
            if (eachSegment == snakehead):
                gameOver = True
                winny = 1

        for eachSegment in snakelist[:-1]:
            if (eachSegment == snakehead2):
                gameOver = True
                winny = 2

        score(score1)
        score2(score2p)
        uplynelo_czas = time.clock() - czas
        pozostaly_czas = czas_rozgrywki - uplynelo_czas
        pozostaly_czas = round(pozostaly_czas, 2)
        message_to_screen("Pozostaly czas: " + str(pozostaly_czas), black, -280)
        pygame.display.update()

        # zjadanie jabluszka1
        if (lead_x == randAppleX and lead_y == randAppleY):
            randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple = [randAppleX, randAppleY]

            sprawdzaj_snakeO = True
            losuj_noweO = False
            while (sprawdzaj_snakeO == True):

                checked = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple):
                        print("ala")
                        losuj_noweO = True
                        break
                    else:
                        checked += 1

                checked2 = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple):
                        print("ala")
                        losuj_noweO = True
                        break
                    else:
                        checked2 += 1

                if (placeApple == placeApple2 or placeApple == placeApple3):
                    losuj_noweO = True

                if (checked == len(snakelist) and losuj_noweO == False):
                    sprawdzaj_snakeO = False

                if (losuj_noweO == True):
                    losuj_noweO = False
                    randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple = [randAppleX, randAppleY]
            apple_list.pop(0)
            apple_list.insert(0, [randAppleX, randAppleY])
            snakeLength += 1
            score1 += 10
            appleimg = fruits_skin_rand()
            # losowac_skin_Fruits=True

        # zjadanie jabloszka 2
        if (lead_x == randAppleX2 and lead_y == randAppleY2):
            randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY2 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple2 = [randAppleX2, randAppleY2]

            sprawdzaj_snakeO2 = True
            losuj_noweO2 = False
            while (sprawdzaj_snakeO2 == True):

                checked2 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple2):
                        print("ala")
                        losuj_noweO2 = True
                        break
                    else:
                        checked2 += 1

                checked21 = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple2):
                        print("ala")
                        losuj_noweO2 = True
                        break
                    else:
                        checked21 += 1

                if (placeApple2 == placeApple or placeApple2 == placeApple3):
                    losuj_noweO2 = True

                if (checked2 == len(snakelist) and losuj_noweO2 == False):
                    sprawdzaj_snakeO2 = False

                if (losuj_noweO2 == True):
                    losuj_noweO2 = False
                    randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY2 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple2 = [randAppleX2, randAppleY2]
            apple_list.pop(1)
            apple_list.insert(1, [randAppleX2, randAppleY2])
            snakeLength += 1
            score1 += 10
            appleimg2 = fruits_skin_rand()

        # zjadanie jabluszka3
        if (lead_x == randAppleX3 and lead_y == randAppleY3):
            randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY3 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple3 = [randAppleX3, randAppleY3]

            sprawdzaj_snakeO3 = True
            losuj_noweO3 = False
            while (sprawdzaj_snakeO3 == True):

                checked3 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple3):
                        print("ala")
                        losuj_noweO3 = True
                        break
                    else:
                        checked3 += 1

                checked32 = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple3):
                        print("ala")
                        losuj_noweO3 = True
                        break
                    else:
                        checked32 += 1

                if (placeApple3 == placeApple or placeApple3 == placeApple2):
                    losuj_noweO3 = True

                if (checked3 == len(snakelist) and losuj_noweO3 == False):
                    sprawdzaj_snakeO3 = False

                if (losuj_noweO3 == True):
                    losuj_noweO3 = False
                    randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY3 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple3 = [randAppleX3, randAppleY3]
            apple_list.pop(2)
            apple_list.insert(2, [randAppleX3, randAppleY3])
            snakeLength += 1
            score1 += 10
            appleimg3 = fruits_skin_rand()

        # dla drugiego weża:
        # zjadanie jabluszka1
        if (lead_x2 == randAppleX and lead_y2 == randAppleY):
            randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple = [randAppleX, randAppleY]

            sprawdzaj_snakeO = True
            losuj_noweO = False
            while (sprawdzaj_snakeO == True):

                checked = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple):
                        print("ala")
                        losuj_noweO = True
                        break
                    else:
                        checked += 1

                checked1 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple):
                        print("ala")
                        losuj_noweO = True
                        break
                    else:
                        checked1 += 1

                if (placeApple == placeApple2 or placeApple == placeApple3):
                    losuj_noweO = True

                if (checked == len(snakelist2) and losuj_noweO == False):
                    sprawdzaj_snakeO = False

                if (losuj_noweO == True):
                    losuj_noweO = False
                    randAppleX = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple = [randAppleX, randAppleY]
            apple_list.pop(0)
            apple_list.insert(0, [randAppleX, randAppleY])
            snakeLength2 += 1
            score2p += 10
            appleimg = fruits_skin_rand()
            # losowac_skin_Fruits=True

        # zjadanie jabloszka 2
        if (lead_x2 == randAppleX2 and lead_y2 == randAppleY2):
            randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY2 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple2 = [randAppleX2, randAppleY2]

            sprawdzaj_snakeO2 = True
            losuj_noweO2 = False
            while (sprawdzaj_snakeO2 == True):

                checked2 = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple2):
                        print("ala")
                        losuj_noweO2 = True
                        break
                    else:
                        checked2 += 1

                checked21 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple2):
                        print("ala")
                        losuj_noweO2 = True
                        break
                    else:
                        checked21 += 1

                if (placeApple2 == placeApple or placeApple2 == placeApple3):
                    losuj_noweO2 = True

                if (checked2 == len(snakelist2) and losuj_noweO2 == False):
                    sprawdzaj_snakeO2 = False

                if (losuj_noweO2 == True):
                    losuj_noweO2 = False
                    randAppleX2 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY2 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple2 = [randAppleX2, randAppleY2]
            apple_list.pop(1)
            apple_list.insert(1, [randAppleX2, randAppleY2])
            snakeLength2 += 1
            score2p += 10
            appleimg2 = fruits_skin_rand()

        # zjadanie jabluszka3
        if (lead_x2 == randAppleX3 and lead_y2 == randAppleY3):
            randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
            randAppleY3 = scoreBarHeight + round(
                random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
            placeApple3 = [randAppleX3, randAppleY3]

            sprawdzaj_snakeO3 = True
            losuj_noweO3 = False
            while (sprawdzaj_snakeO3 == True):

                checked3 = 0
                for eachSegment in snakelist2[:]:
                    if (eachSegment == placeApple3):
                        print("ala")
                        losuj_noweO3 = True
                        break
                    else:
                        checked3 += 1

                checked31 = 0
                for eachSegment in snakelist[:]:
                    if (eachSegment == placeApple3):
                        print("ala")
                        losuj_noweO3 = True
                        break
                    else:
                        checked31 += 1

                if (placeApple3 == placeApple or placeApple3 == placeApple2):
                    losuj_noweO3 = True

                if (checked3 == len(snakelist2) and losuj_noweO3 == False):
                    sprawdzaj_snakeO3 = False

                if (losuj_noweO3 == True):
                    losuj_noweO3 = False
                    randAppleX3 = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
                    randAppleY3 = scoreBarHeight + round(
                        random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
                    placeApple3 = [randAppleX3, randAppleY3]
            apple_list.pop(2)
            apple_list.insert(2, [randAppleX3, randAppleY3])
            snakeLength2 += 1
            score2p += 10
            appleimg3 = fruits_skin_rand()

        clock.tick(FPS)

    pygame.quit()
    quit()


# penbackground gry
def gameLoop(tryb, pierwszego="zielony", drugiego="czerwony"):
    if (tryb == "rozbud"):
        extended()
    elif (tryb == "classic"):
        classic()
    elif (tryb == "global"):
        extended("global")
    elif (tryb == "players"):
        players()


game_intro()
