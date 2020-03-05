import pygame
import time
import random
import os
import re

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

scoreBarHeight = 40
smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)
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
# TODO te zmienne >.<
classicimg = pygame.image.load('graphics/classic.png')
extendedimg = pygame.image.load('graphics/extended.png')
globalimg = pygame.image.load('graphics/global.png')
playersimg = pygame.image.load('graphics/players.png')
sterowanie1 = pygame.image.load('graphics/controls.png')

# ustawienie okna i ikony+ tekst
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Snake- the game")
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


fruitTextureList = [pygame.image.load('graphics/fruit1.png'),
                    pygame.image.load('graphics/fruit2.png'),
                    pygame.image.load('graphics/fruit3.png'),
                    pygame.image.load('graphics/fruit4.png'),
                    pygame.image.load('graphics/fruit5.png')
                    ]


def randomFruitSkin():
    random.seed()
    return fruitTextureList[random.randrange(5)]


def gamePausedScreen():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    gameIntro()
        gameDisplay.blit(menu1, (0, 0))
        showMessageOnScreen("Paused", black, -100, size="large")
        showMessageOnScreen("Nacisnij 'C' by grać dalej", black, 10, size="small")
        showMessageOnScreen("Nacisnij 'Q' by wyjsc do menu", black, 55, size="small")
        pygame.display.update()
        clock.tick(5)


def showActivePowerUps(speed, bonusPoints, shift):
    powerUps = smallFont.render("Aktywne ulepszenia: ", True, black)
    gameDisplay.blit(powerUps, [400, 0])
    if speed:
        gameDisplay.blit(speedImg, [635, 10])
    if bonusPoints:
        gameDisplay.blit(bonusImg, [655, 10])
    if shift:
        gameDisplay.blit(shiftImg, [675, 10])


def showScore(score, position=[0, 0]):
    text = smallFont.render("Wynik: " + str(score), True, black)
    gameDisplay.blit(text, position)


def putTextOnButton(msg, colour, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurf, textRect = createText(msg, colour, size)
    textRect.center = (buttonX + (buttonWidth / 2), buttonY + (buttonHeight / 2))
    gameDisplay.blit(textSurf, textRect)


# do buttonow potrzebne
def createText(text, colour, size):
    if size == "small":
        textSurface = smallFont.render(text, True, colour)
    elif size == "medium":
        textSurface = medFont.render(text, True, colour)
    elif size == "large":
        textSurface = largeFont.render(text, True, colour)
    return textSurface, textSurface.get_rect()


# nazwa
def showMessageOnScreen(msg, colour, y_displace=0, size="small"):
    textSurf, textRect = createText(msg, colour, size)
    textRect.center = (displayWidth / 2), (displayHeight / 2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def button(text, x, y, width, height, inactiveColour, activeColour, action=None, display=False):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if action and display:
            if action == "classic":
                gameDisplay.blit(classicimg, (300, 150))
            elif action == "extended":
                gameDisplay.blit(extendedimg, (300, 150))
            elif action == "global":
                gameDisplay.blit(globalimg, (300, 150))
            elif action == "players":
                gameDisplay.blit(playersimg, (300, 150))
        pygame.draw.rect(gameDisplay, activeColour, (x, y, width, height))
        if click[0] == 1 and action:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "gameIntro":
                gameIntro()
            elif action == "gameTypeMenu":
                gameTypeMenu()
            elif action == "controls":
                controls()
            elif action == "classic":
                gameLoop("classic")
            elif action == "extended":
                gameLoop("extended")
            elif action == "global":
                gameLoop("global")
            elif action == "players":
                gameLoop("players")
            elif action == "skinSelect":
                skinSelect()
            elif action == "green1":
                openAndWrite(1, "gre\n")
            elif action == "red1":
                openAndWrite(1, "red\n")
            elif action == "blue1":
                openAndWrite(1, "blu\n")
            elif action == "green2":
                openAndWrite(2, "gre")
            elif action == "red2":
                openAndWrite(2, "red")
            elif action == "blue2":
                openAndWrite(2, "blu")
    else:
        pygame.draw.rect(gameDisplay, inactiveColour, (x, y, width, height))
    putTextOnButton(text, black, x, y, width, height)


# pygame.display.update()
def skinSelect():
    select = True
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        fileSkin = open("skin.txt", "r")
        line1 = fileSkin.readline()
        line2 = fileSkin.readline()
        fileSkin.close()

        if line1 == "gre\n":
            gameDisplay.blit(choosenSkin, (165, 125))
        elif line1 == "red\n":
            gameDisplay.blit(choosenSkin, (390, 125))
        elif line1 == "blu\n":
            gameDisplay.blit(choosenSkin, (615, 125))

        if line2 == "gre":
            gameDisplay.blit(choosenSkin, (165, 275))
        elif line2 == "red":
            gameDisplay.blit(choosenSkin, (390, 275))
        elif line2 == "blu":
            gameDisplay.blit(choosenSkin, (615, 275))

        showMessageOnScreen("Wybierz skina węża", black, -275, "medium")
        showMessageOnScreen("Singleplayer", black, -200, "small")
        button("Ziel/Czer", 100, 150, 150, 50, green, lightGreen, action="green1")
        button("Czer/czarny", 325, 150, 150, 50, red, lightRed, action="red1")
        button("Nieb/Zółty", 550, 150, 150, 50, blue, changeBlue, action="blue1")
        showMessageOnScreen("Multiplayer", black, -50, "small")
        button("Ziel/Czer", 100, 300, 150, 50, green, lightGreen, action="green2")
        button("Czer/czarny", 325, 300, 150, 50, red, lightRed, action="red2")
        button("Nieb/Zółty", 550, 300, 150, 50, blue, changeBlue, action="blue2")
        gameDisplay.blit(skin1, (145, 400))
        gameDisplay.blit(skin2, (370, 400))
        gameDisplay.blit(skin3, (595, 400))

        button("Powrót", 275, 525, 250, 50, red, lightRed, action="gameTypeMenu")

        pygame.display.update()
        clock.tick(15)


def gameTypeMenu():
    gameTypeMenuActive = True
    while gameTypeMenuActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        showMessageOnScreen("Wybierz rodzaj rozgrywki", black, -250, "medium")
        button("Klasyczny", 20, 150, 250, 50, yellow, changeYellow, action="classic", display=True)
        button("Rozbudowany", 20, 225, 250, 50, green, lightGreen, action="extended", display=True)
        button("Global", 20, 300, 250, 50, blue, changeBlue, action="global", display=True)
        button("Dla dwóch graczy", 20, 375, 250, 50, orange, changeOrange, action="players", display=True)
        button("Wybor skina", 20, 450, 250, 50, violet, changeViolet, action="skinSelect")
        button("Powrót", 20, 525, 250, 50, red, lightRed, action="gameIntro")

        pygame.display.update()
        clock.tick(15)


def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(menu1, (0, 0))
        showMessageOnScreen("Snake", green, -200, "large")

        button("Graj", 275, 200, 250, 50, green, lightGreen, action="gameTypeMenu")
        button("Zasady i sterowanie", 275, 300, 250, 50, grey, light_grey, action="controls")
        button("Wyjscie", 275, 400, 250, 50, red, lightRed, action="quit")

        pygame.display.update()
        clock.tick(15)


def controls():
    controlsActive = True
    while controlsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.blit(sterowanie1, (0, 0))
        button("Powrót", 525, 525, 250, 50, red, lightRed, action="gameIntro")

        pygame.display.update()
        clock.tick(15)


def getSkin(number):
    fileWithSkin = open("skin.txt", "r")
    while number > 0:
        line = fileWithSkin.readline()
        number = number - 1
    fileWithSkin.close()
    if re.match("gre", line):
        return [pygame.image.load('graphics/head1.png'), pygame.image.load('graphics/body1.png')]
    elif re.match("red", line):
        return [pygame.image.load('graphics/head2.png'), pygame.image.load('graphics/body2.png')]
    elif re.match("blu", line):
        return [pygame.image.load('graphics/head3.png'), pygame.image.load('graphics/body3.png')]


def randFruitPosition():
    X = round(random.randrange(0, displayWidth - blockSize) / 20.0) * 20.0
    Y = scoreBarHeight + round(random.randrange(0, displayHeight - scoreBarHeight - blockSize) / 20.0) * 20.0
    return [X, Y]


def checkBorder(snake, displayWidth, displayHeight, scoreBarHeight):
    if snake.leadX >= displayWidth or snake.leadX < 0 or snake.leadY >= displayHeight or snake.leadY < scoreBarHeight:
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

        if self.direction == "right":
            head = pygame.transform.rotate(self.headImg, 270)
        if self.direction == "left":
            head = pygame.transform.rotate(self.headImg, 90)
        if self.direction == "up":
            head = self.headImg
        if self.direction == "down":
            head = pygame.transform.rotate(self.headImg, 180)

        gameDisplay.blit(head, (self.snakeList[-1][0], self.snakeList[-1][1]))

        # part = [X,Y]
        for part in self.snakeList[:-1]:
            gameDisplay.blit(self.bodyImg, (part[0], part[1]))

    def checkSnakeLength(self):
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList[0]

    def checkHeadOverlapsBody(self):
        for eachSegment in self.snakeList[:-1]:
            if eachSegment == [self.leadX, self.leadY]:
                return True

    def getHead(self):
        return [self.leadX, self.leadY]


def randObstaclePosition():
    X = round(random.randrange(blockSize, displayWidth - blockSize - blockSize) / 20.0) * 20.0
    Y = scoreBarHeight + round(
        random.randrange(blockSize, displayHeight - scoreBarHeight - blockSize - blockSize) / 20.0) * 20.0
    return [X, Y]


def endGameScreen(gameType, text="Przegrałeś"):
    showMessageOnScreen(text, white, y_displace=-50, size="large")
    button("Jeszcze raz!", 275, 350, 250, 50, green, lightGreen, action=gameType)
    button("Do menu głównego", 275, 450, 250, 50, red, lightRed, action="gameIntro")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            gameOver = False
            return gameOver, gameExit


def handleInput(snake1, controlsKeys1, snake2=None, controlKeys2=None):
    leftKey1, rightKey1, upKey1, downKey1 = controlsKeys1
    if snake2 is not None:
        leftKey2, rightKey2, upKey2, downKey2 = controlKeys2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == leftKey1:
                if snake1.direction != "right":
                    snake1.setDirection("left")
                    snake1.setChange(-blockSize, 0)
            elif event.key == rightKey1:
                if snake1.direction != "left":
                    snake1.setDirection("right")
                    snake1.setChange(blockSize, 0)
            elif event.key == upKey1:
                if snake1.direction != "down":
                    snake1.setDirection("up")
                    snake1.setChange(0, -blockSize)
            elif event.key == downKey1:
                if snake1.direction != "up":
                    snake1.setDirection("down")
                    snake1.setChange(0, blockSize)
            elif event.key == pygame.K_p:
                gamePausedScreen()
            if snake2 is not None:
                if event.key == leftKey2:
                    if snake2.direction != "right":
                        snake2.setDirection("left")
                        snake2.setChange(-blockSize, 0)
                elif event.key == rightKey2:
                    if snake2.direction != "left":
                        snake2.setDirection("right")
                        snake2.setChange(blockSize, 0)
                elif event.key == upKey2:
                    if snake2.direction != "down":
                        snake2.setDirection("up")
                        snake2.setChange(0, -blockSize)
                elif event.key == downKey2:
                    if snake2.direction != "up":
                        snake2.setDirection("down")
                        snake2.setChange(0, blockSize)
                elif event.key == pygame.K_p:
                    gamePausedScreen()


def openAndWrite(player, text):
    newFile = open("skinTMP.txt", "w+")
    openedFile = open("skin.txt", "r+")

    line1 = openedFile.readline()
    line2 = openedFile.readline()
    if player == 1:
        newFile.write(text)
        newFile.write(line2)
    elif player == 2:
        newFile.write(line1)
        newFile.write(text)
    openedFile.close()
    newFile.close()
    os.remove("skin.txt")
    os.rename("skinTMP.txt", "skin.txt")


def classic():
    skin = getSkin(1)
    snake = Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
    fruitPosition = randFruitPosition()
    background = backgroundTextureRandom()

    getNewFruit = True
    gameExit = False
    gameOver = False

    player1Score = 0

    while not gameExit:
        while gameOver:

            snake.setChange(0, 0)
            try:
                gameOver, gameExit = endGameScreen("classic")
            except TypeError:
                pass

        try:
            gameExit = handleInput(snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
        except TypeError:
            pass

        if getNewFruit:
            img = randomFruitSkin()
            getNewFruit = False

        gameDisplay.blit(background, (0, 0))
        gameDisplay.blit(img, fruitPosition)
        snake.move()
        snake.checkSnakeLength()
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(player1Score)

        pygame.display.update()

        gameOver = checkBorder(snake, displayWidth, displayHeight, scoreBarHeight) or snake.checkHeadOverlapsBody()

        if [snake.leadX, snake.leadY] == fruitPosition:
            fruitPosition = randFruitPosition()

            while fruitPosition in snake.snakeList:
                fruitPosition = randFruitPosition()

            snake.snakeLength += 1
            player1Score += 10
            getNewFruit = True

        clock.tick(FPS)

    pygame.quit()
    quit()


def extended(gameMode="extended"):
    lastMushroom = time.time()
    isMushroomPresent = False

    lastObstacle = time.time()
    isObstaclePresent = False

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
    skin = getSkin(1)
    snake = Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
    player1Score = 0

    for index in range(0, 3):
        fruitPosition = randFruitPosition()
        while fruitPosition in objectList:
            fruitPosition = randFruitPosition()
        objectList[index] = fruitPosition

    while not gameExit:
        while gameOver:

            snake.setChange(0, 0)
            try:
                gameOver, gameExit = endGameScreen(gameMode)
            except TypeError:
                pass

        try:
            if not shiftActive:
                gameExit = handleInput(snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
            else:
                gameExit = handleInput(snake, [pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w])
        except TypeError:
            pass

        # Checking PowerUps
        if speedActive:
            if (time.time() - timeSinceSpeedPickup) > speedDuration:
                FPS = 7
                speedActive = False
            else:
                FPS = 14
        else:
            FPS = 7

        if shiftActive:
            if (time.time() - timeSinceShiftPickup) > shiftDuration:
                shiftActive = False

        if bonusPointsActive:
            if time.time() - timeSinceBonusPointsPickup > bonusPointsDuration:
                bonusPointsActive = False
                bonus = 0
            else:
                bonus = 5
        else:
            bonus = 0

        # Placing objects
        if time.time() - lastMushroom > 10 and not isMushroomPresent:
            mushroomPosition = randFruitPosition()
            while mushroomPosition in snake.snakeList or mushroomPosition in objectList:
                mushroomPosition = randFruitPosition()
            objectList[3] = mushroomPosition
            isMushroomPresent = True

        if time.time() - lastObstacle > 5 and not isObstaclePresent:
            obstaclePosition = randObstaclePosition()
            while obstaclePosition in snake.snakeList or obstaclePosition in objectList:
                obstaclePosition = randObstaclePosition()
            objectList[4] = obstaclePosition
            isObstaclePresent = True

        if time.time() - lastPowerUp > 3 and not isPowerUpPresent:
            powerupNumber = random.randrange(3)
            if powerupNumber == 0:
                powerupimg = speedImg
            elif powerupNumber == 1:
                powerupimg = bonusImg
            elif powerupNumber == 2:
                powerupimg = shiftImg
            powerUpPosition = randFruitPosition()
            while powerUpPosition in snake.snakeList or powerUpPosition in objectList:
                powerUpPosition = randFruitPosition()
            objectList[5] = powerUpPosition
            isPowerUpPresent = True

        # Showing object on the screen
        gameDisplay.blit(background, (0, 0))
        snake.move()
        snake.checkSnakeLength()

        for index in range(0, 3):
            gameDisplay.blit(fruitSkin[index], objectList[index])

        if isMushroomPresent:
            gameDisplay.blit(mushroom, objectList[3])

        if isObstaclePresent:
            gameDisplay.blit(obstacleImg, objectList[4])

        if isPowerUpPresent:
            gameDisplay.blit(powerupimg, objectList[5])

        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(player1Score)
        showActivePowerUps(speedActive, bonusPointsActive, shiftActive)  # wyswietlanie bonusa
        pygame.display.update()

        # Eating the Fruit & other objects
        for index in range(0, 3):
            if [snake.leadX, snake.leadY] == objectList[index]:
                fruitPosition = randFruitPosition()
                while fruitPosition in snake.snakeList or fruitPosition in objectList:
                    fruitPosition = randFruitPosition()
                objectList[index] = fruitPosition
                snake.snakeLength += 1
                player1Score += 10 + bonus
                fruitSkin[index] = randomFruitSkin()

        if isMushroomPresent:
            if [snake.leadX, snake.leadY] == objectList[3]:
                isMushroomPresent = False
                player1Score -= 5
                snake.snakeLength -= 1
                lastMushroom = time.time()
                if snake.snakeLength <= 2:
                    gameOver = True

        if isObstaclePresent:
            if [snake.leadX, snake.leadY] == objectList[4]:
                gameOver = True

        if isPowerUpPresent:
            if [snake.leadX, snake.leadY] == objectList[5]:
                isPowerUpPresent = False
                lastPowerUp = time.time()
                if powerupimg == speedImg:
                    speedActive = True
                    timeSinceSpeedPickup = time.time()
                elif powerupimg == bonusImg:
                    bonusPointsActive = True
                    timeSinceBonusPointsPickup = time.time()
                elif powerupimg == shiftImg:
                    shiftActive = True
                    timeSinceShiftPickup = time.time()

        if isObstaclePresent:
            obstacleNeighbourList = []
            obstaclePositionX, obstaclePositionY = obstaclePosition
            for eachSegment in snake.snakeList:
                if eachSegment == [obstaclePositionX - blockSize, obstaclePositionY - blockSize]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX, obstaclePositionY - blockSize]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX + blockSize, obstaclePositionY - blockSize]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX - blockSize, obstaclePositionY]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX + blockSize, obstaclePositionY]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX - blockSize, obstaclePositionY + blockSize]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX, obstaclePositionY + blockSize]:
                    obstacleNeighbourList.append(True)
                if eachSegment == [obstaclePositionX + blockSize, obstaclePositionY + blockSize]:
                    obstacleNeighbourList.append(True)
            if all(obstacleNeighbourList) and len(obstacleNeighbourList) == 8:
                player1Score += 50
                isObstaclePresent = False
                lastObstacle = time.time()
            obstacleNeighbourList = []

        # GameOver Conditions
        if gameMode == "extended":
            gameOver = checkBorder(snake, displayWidth, displayHeight,
                                   scoreBarHeight) or snake.checkHeadOverlapsBody() or gameOver  # last one form
            # hiting the obstacle
        elif gameMode == "global":
            if snake.leadX == displayWidth:
                snake.leadX = -blockSize
            elif snake.leadX == 0 - blockSize:
                snake.leadX = displayWidth
            elif snake.leadY == displayHeight:
                snake.leadY = -blockSize + scoreBarHeight
            elif snake.leadY < 0 + scoreBarHeight:
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

    skin1 = getSkin(1)
    skin2 = getSkin(2)
    background = backgroundTextureRandom()

    snake = Snake(0, 2 * blockSize + 3 * blockSize, skin1[0], skin1[1])
    snake2 = Snake(displayWidth - blockSize, displayHeight - 3 * blockSize, skin2[0], skin2[1], "left")
    snake2.xChange = -blockSize

    fruitList = [None, None, None]
    fruitSkin = [randomFruitSkin(), randomFruitSkin(), randomFruitSkin()]

    for index in range(0, 3):
        fruitPosition = randFruitPosition()
        while fruitPosition in fruitList:
            fruitPosition = randFruitPosition()
        fruitList[index] = fruitPosition

    # ---

    while not gameExit:
        while gameOver or timeLeft < 0:
            snake.setChange(0, 0)
            snake2.setChange(0, 0)
            try:
                if gameOver:
                    if player1Fault:
                        gameOver, gameExit = endGameScreen("players", "Wygrywa gracz nr.2")
                    else:
                        gameOver, gameExit = endGameScreen("players", "Wygrywa gracz nr.1")
                elif timeLeft < 0:
                    if player1Score > player2Score:
                        gameOver, gameExit = endGameScreen("players", "Wygrywa gracz nr.1")
                    elif player1Score < player2Score:
                        gameOver, gameExit = endGameScreen("players", "Wygrywa gracz nr.2")
                    else:
                        gameOver, gameExit = endGameScreen("players", "Remis")
            except TypeError:
                pass

        try:
            gameExit = handleInput(snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], snake2,
                                   [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]) or gameExit
        except TypeError:
            pass

        if checkBorder(snake, displayWidth, displayHeight, scoreBarHeight):
            gameOver = True
            player1Fault = True

        if checkBorder(snake2, displayWidth, displayHeight, scoreBarHeight):
            gameOver = True

        gameDisplay.blit(background, (0, 0))
        snake.move()
        snake2.move()
        # TODO opisy ang funkcji

        for index in range(0, 3):
            gameDisplay.blit(fruitSkin[index], fruitList[index])

        snake.checkSnakeLength()
        snake2.checkSnakeLength()
        gameDisplay.fill(grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(player1Score)
        showScore(player2Score, [650, 0])

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
        showMessageOnScreen("Pozostaly czas: " + str(timeLeft), black, - 280)
        pygame.display.update()

        for index in range(0, 3):
            if snake.getHead() == fruitList[index]:
                fruitPosition = randFruitPosition()
                while (
                        fruitPosition in snake.snakeList or fruitPosition in snake2.snakeList or fruitPosition in fruitList):
                    fruitPosition = randFruitPosition()
                fruitList[index] = fruitPosition
                snake.snakeLength += 1
                player1Score += 10
                fruitSkin[index] = randomFruitSkin()

        for index in range(0, 3):
            if snake2.getHead() == fruitList[index]:
                fruitPosition = randFruitPosition()
                while (
                        fruitPosition in snake.snakeList or fruitPosition in snake2.snakeList or fruitPosition in fruitList):
                    fruitPosition = randFruitPosition()
                fruitList[index] = fruitPosition
                snake2.snakeLength += 1
                player2Score += 10
                fruitSkin[index] = randomFruitSkin()

        clock.tick(FPS)

    pygame.quit()
    quit()


# penbackground gry
def gameLoop(gameMode):
    if gameMode == "classic":
        classic()
    elif gameMode == "extended":
        extended()
    elif gameMode == "global":
        extended("global")
    elif gameMode == "players":
        players()


gameIntro()
