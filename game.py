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
def randomFruitSkin():
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
def showActivePowerUps(przyspieszenie, bonus_points, shift):
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


def getSkin(file="skin1.txt"):
    fileWithSkin = open(file, "r")
    line = fileWithSkin.readline()
    fileWithSkin.close()
    if (line == "ziel"):
        return (pygame.image.load('graphics/head1.png'), pygame.image.load('graphics/body1.png'))
    elif (line == "czer"):
        return (pygame.image.load('graphics/head2.png'), pygame.image.load('graphics/body2.png'))
    elif (line == "nieb"):
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
    def __init__(self, leadX, leadY, headImg, bodyImg, direction="right"):
        self.direction = direction
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

    def getHead(self):
        return [self.leadX,self.leadY]


def randObstaclePosition():
    X = round(random.randrange(blockSize, displayWidth - blockSize - blockSize) / 20.0) * 20.0
    Y = scoreBarHeight + round(
        random.randrange(blockSize, displayHeight - scoreBarHeight - blockSize - blockSize) / 20.0) * 20.0
    return [X, Y]

def classic():
    skin = getSkin()
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

            #TODO funkcja od tego ?
            message_to_screen("Przegrałes", white, y_displace=-50, size="large")
            button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="classic")
            button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
            pygame.display.update()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    gameExit = True
                    gameOver = False

        #TODO funkcja od tego?
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
            img = randomFruitSkin()
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
    lastMushroom = time.time()
    isMushroomPresent = False

    lastObstacle = time.time()
    isObstacePresent = False

    lastPowerUp = time.time()
    isPowerUpPresent = False

    speedActive = False
    speedDuration = 7
    timeSinceSpeedPickup = time.time()

    bonusPointsActive = False
    bonusPointsDuration = 10
    timeSinceBonusPointsPickup = time.time()

    shiftActive = False
    shiftDuration = 7
    timeSinceShiftPickup = time.time()

    objectList = 6 * [None]  # Fruit,Fruit,Fruit,Mushroom,Obstacle,PowerUp
    fruitSkin = [randomFruitSkin(), randomFruitSkin(), randomFruitSkin()]

    gameExit = False
    gameOver = False
    background = backgroundTextureRandom()
    skin = getSkin()
    snake = Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
    player1Score = 0

    for index in range(0, 3):
        fruitPosition = randFruitPosition()
        while (fruitPosition in objectList):
            fruitPosition = randFruitPosition()
        objectList[index] = fruitPosition

    while (gameExit != True):
        while (gameOver == True):
            snake.setChange(0, 0)

            # TODO funkcja od tego ?
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
                if (shiftActive == False):
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
                elif (shiftActive == True):
                    if (event.key == pygame.K_a):
                        if (snake.direction != "left"):
                            snake.setDirection("right")
                            snake.setChange(blockSize, 0)
                    elif (event.key == pygame.K_d):
                        if (snake.direction != "right"):
                            snake.setDirection("left")
                            snake.setChange(-blockSize, 0)
                    elif (event.key == pygame.K_w):
                        if (snake.direction != "up"):
                            snake.setDirection("down")
                            snake.setChange(0, blockSize)
                    elif (event.key == pygame.K_s):
                        if (snake.direction != "down"):
                            snake.setDirection("up")
                            snake.setChange(0, -blockSize)
                    elif (event.key == pygame.K_p):
                        pause()

        # Checking PowerUps
        if (speedActive == True):
            if ((time.time() - timeSinceSpeedPickup) > speedDuration):
                FPS = 7
                speedActive = False
            else:
                FPS = 14
        else:
            FPS = 7

        if (shiftActive == True):
            if ((time.time() - timeSinceShiftPickup) > shiftDuration):
                shiftActive = False

        if (bonusPointsActive == True):
            if (time.time() - timeSinceBonusPointsPickup > bonusPointsDuration):
                bonusPointsActive = False
                bonus = 0
            else:
                bonus = 5
        else:
            bonus = 0

        # Placing objects
        if (time.time() - lastMushroom > 10 and isMushroomPresent == False):
            mushroomPosition = randFruitPosition()
            while (mushroomPosition in snake.snakeList or mushroomPosition in objectList):
                mushroomPosition = randFruitPosition()
            objectList[3] = mushroomPosition
            isMushroomPresent = True

        if (time.time() - lastObstacle > 5 and isObstacePresent == False):
            obstaclePosition = randObstaclePosition()
            while (obstaclePosition in snake.snakeList or obstaclePosition in objectList):
                obstaclePosition = randObstaclePosition()
            objectList[4] = obstaclePosition
            isObstacePresent = True

        if (time.time() - lastPowerUp > 3 and isPowerUpPresent == False):
            powerupNumber = random.randrange(3)
            if (powerupNumber == 0):
                powerupimg = speedImg
            elif (powerupNumber == 1):
                powerupimg = bonusImg
            elif (powerupNumber == 2):
                powerupimg = shiftImg
            powerUpPosition = randFruitPosition()
            while (powerUpPosition in snake.snakeList or powerUpPosition in objectList):
                powerUpPosition = randFruitPosition()
            objectList[5] = powerUpPosition
            isPowerUpPresent = True

        #Showing object on the screen
        gameDisplay.blit(background, (0, 0))
        snake.move()
        snake.checkSnakeLength()

        for index in range(0, 3):
            gameDisplay.blit(fruitSkin[index], objectList[index])

        if (isMushroomPresent == True):
            gameDisplay.blit(mushroom, objectList[3])

        if (isObstacePresent == True):
            gameDisplay.blit(obstacleImg, objectList[4])

        if (isPowerUpPresent == True):
            gameDisplay.blit(powerupimg, objectList[5])

        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        score(player1Score)
        showActivePowerUps(speedActive, bonusPointsActive, shiftActive)  # wyswietlanie bonusa
        pygame.display.update()

        # Eating the Fruit & other objects
        for index in range(0, 3):
            if ([snake.leadX, snake.leadY] == objectList[index]):
                fruitPosition = randFruitPosition()
                while (fruitPosition in snake.snakeList or fruitPosition in objectList):
                    fruitPosition = randFruitPosition()
                objectList[index] = fruitPosition
                snake.snakeLength += 1
                player1Score += 10 + bonus
                fruitSkin[index] = randomFruitSkin()

        if (isMushroomPresent == True):
            if ([snake.leadX, snake.leadY] == objectList[3]):
                isMushroomPresent = False
                player1Score -= 5
                snake.snakeLength -= 1
                lastMushroom = time.time()
                if (snake.snakeLength <= 2):
                    gameOver = True

        if (isObstacePresent == True):
            if ([snake.leadX, snake.leadY] == objectList[4]):
                gameOver = True

        if (isPowerUpPresent == True):
            if ([snake.leadX, snake.leadY] == objectList[5]):
                isPowerUpPresent = False
                lastPowerUp = time.time()
                if (powerupimg == speedImg):
                    speedActive = True
                    timeSinceSpeedPickup = time.time()
                elif (powerupimg == bonusImg):
                    bonusPointsActive = True
                    timeSinceBonusPointsPickup = time.time()
                elif (powerupimg == shiftImg):
                    shiftActive = True
                    timeSinceShiftPickup = time.time()

        if (isObstacePresent == True):
            obstacleNeighbourList = []
            obstaclePositionX, obstaclePositionY = obstaclePosition
            for eachSegment in snake.snakeList:
                if (eachSegment == [obstaclePositionX - blockSize, obstaclePositionY - blockSize]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX, obstaclePositionY - blockSize]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX + blockSize, obstaclePositionY - blockSize]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX - blockSize, obstaclePositionY]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX + blockSize, obstaclePositionY]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX - blockSize, obstaclePositionY + blockSize]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX, obstaclePositionY + blockSize]):
                    obstacleNeighbourList.append(True)
                if (eachSegment == [obstaclePositionX + blockSize, obstaclePositionY + blockSize]):
                    obstacleNeighbourList.append(True)
            if (all(obstacleNeighbourList) and len(obstacleNeighbourList) == 8):
                player1Score += 50
                isObstacePresent = False
                lastObstacle = time.time()
            obstacleNeighbourList = []

        # GameOver Conditions
        if (tryb == "rozbud"):
            gameOver = checkBorder(snake, displayWidth, displayHeight,scoreBarHeight) or snake.checkHeadOverlapsBody() or gameOver #last one form hiting the obstacle
        elif (tryb == "global"):
            if (snake.leadX == displayWidth):
                snake.leadX = -blockSize
            elif (snake.leadX == 0 - blockSize):
                snake.leadX = displayWidth
            elif (snake.leadY == displayHeight):
                snake.leadY = -blockSize + scoreBarHeight
            elif (snake.leadY < 0 + scoreBarHeight):
                snake.leadY = displayHeight
            gameOver = snake.checkHeadOverlapsBody()

        clock.tick(FPS)
    pygame.quit()
    quit()

def players():
    gameBeginning = time.time()
    gameDuration = 60
    timeElapsed = time.time() - gameBeginning
    timeLeft = gameDuration - timeElapsed

    FPS = 7
    gameExit = False
    gameOver = False

    player1Fault = False

    player1Score = 0
    player2Score = 0

    skin1 = getSkin()
    skin2 = getSkin("skin2.txt")
    background = backgroundTextureRandom()

    snake = Snake(0,2*blockSize + 3 * blockSize, skin1[0],skin1[1])
    snake2 = Snake(displayWidth - blockSize,displayHeight - 3 * blockSize,skin2[0],skin2[1], "left")
    snake2.xChange = -blockSize

    fruitList = [None, None, None]
    fruitSkin = [randomFruitSkin(), randomFruitSkin(), randomFruitSkin()]

    for index in range(0, 3):
        fruitPosition = randFruitPosition()
        while (fruitPosition in fruitList):
            fruitPosition = randFruitPosition()
        fruitList[index] = fruitPosition

# ---

    while (gameExit != True):
        while (gameOver == True or timeLeft < 0):
            snake.setChange(0, 0)
            snake2.setChange(0, 0)
            if (gameOver == True):
                if (player1Fault):
                    #TODO do funkcji
                    message_to_screen("Wygrywa gracz nr.2", white, y_displace=-50, size="large")
                    button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="multi")
                    button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            gameExit = True
                            gameOver = False
                else:
                    message_to_screen("Wygrywa gracz nr.1", white, y_displace=-50, size="large")
                    button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action="multi")
                    button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT):
                            gameExit = True
                            gameOver = False
            elif (timeLeft < 0):
                if (player1Score > player2Score):
                    message_to_screen("Wygrywa gracz nr.1", white, y_displace=-50, size="large")
                elif (player1Score < player2Score):
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

                if (event.key == pygame.K_LEFT):
                    if (snake2.direction != "right"):
                        snake2.setDirection("left")
                        snake2.setChange(-blockSize, 0)
                elif (event.key == pygame.K_RIGHT):
                    if (snake2.direction != "left"):
                        snake2.setDirection("right")
                        snake2.setChange(blockSize, 0)
                elif (event.key == pygame.K_UP):
                    if (snake2.direction != "down"):
                        snake2.setDirection("up")
                        snake2.setChange(0, -blockSize)
                elif (event.key == pygame.K_DOWN):
                    if (snake2.direction != "up"):
                        snake2.setDirection("down")
                        snake2.setChange(0, blockSize)
                elif (event.key == pygame.K_p):
                    pause()

        if (checkBorder(snake,displayWidth,displayHeight,scoreBarHeight)):
            gameOver = True
            player1Fault = True

        if (checkBorder(snake2,displayWidth,displayHeight,scoreBarHeight)):
            gameOver = True

        gameDisplay.blit(background, (0, 0))
        snake.move()
        snake2.move()
        #TODO opisy ang funkcji

        for index in range(0, 3):
            gameDisplay.blit(fruitSkin[index], fruitList[index])

        snake.checkSnakeLength()
        snake2.checkSnakeLength()
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        score(player1Score)
        score2(player2Score)

        # czy wjechal sam w siebie
        if snake.checkHeadOverlapsBody():
            gameOver = True
            player1Fault = True

        if snake2.checkHeadOverlapsBody():
            gameOver = True

        for eachSegment in snake2.snakeList:
            if eachSegment == snake.getHead():
                gameOver = True
                player1Fault = True

        for eachSegment in snake.snakeList:
            if eachSegment == snake2.getHead():
                gameOver = True

        timeElapsed = time.time() - gameBeginning
        timeLeft = gameDuration - timeElapsed
        timeLeft = round(timeLeft, 2)
        message_to_screen("Pozostaly czas: " + str(timeLeft), black, - 280)
        pygame.display.update()

        for index in range(0, 3):
            if (snake.getHead() == fruitList[index]):
                fruitPosition = randFruitPosition()
                while (fruitPosition in snake.snakeList or fruitPosition in snake2.snakeList or fruitPosition in fruitList):
                    fruitPosition = randFruitPosition()
                fruitList[index] = fruitPosition
                snake.snakeLength += 1
                player1Score += 10
                fruitSkin[index] = randomFruitSkin()

        for index in range(0, 3):
            if (snake2.getHead() == fruitList[index]):
                fruitPosition = randFruitPosition()
                while (fruitPosition in snake.snakeList or fruitPosition in snake2.snakeList or fruitPosition in fruitList):
                    fruitPosition = randFruitPosition()
                fruitList[index] = fruitPosition
                snake2.snakeLength += 1
                player2Score += 10
                fruitSkin[index] = randomFruitSkin()

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
