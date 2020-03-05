import pygame
import time
import random
import os
import re

# Begin: Own modules
import colours
import images
import snakeClass
# End: Own modules

pygame.init()

displayHeight = 600
displayWidth = 800
blockSize = 20

scoreBarHeight = 40
smallFont = pygame.font.SysFont("comicsansms", 25)
medFont = pygame.font.SysFont("comicsansms", 50)
largeFont = pygame.font.SysFont("comicsansms", 80)
smallFontSize = 25

gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Snake- the game")
pygame.display.set_icon(images.iconIMG)

FPS = 7
clock = pygame.time.Clock()


# Begin: Game Screens
def gameIntroScreen(display):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(images.menuIMG, (0, 0))
        showMessageOnScreen(display, "Snake", colours.green, -200, "large")

        button(display, "Graj", 275, 200, 250, 50, colours.green, colours.lightGreen, action="gameTypeMenu")
        button(display, "Zasady i sterowanie", 275, 300, 250, 50, colours.grey, colours.lightGrey, action="controls")
        button(display, "Wyjscie", 275, 400, 250, 50, colours.red, colours.lightRed, action="quit")

        pygame.display.update()
        clock.tick(15)


def gameTypeMenuScreen(display):
    gameTypeMenuActive = True
    while gameTypeMenuActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(colours.white)
        showMessageOnScreen(display, "Wybierz rodzaj rozgrywki", colours.black, -250, "medium")
        button(display, "Klasyczny", 20, 150, 250, 50, colours.yellow, colours.changeYellow, action="classic",
               display=True)
        button(display, "Rozbudowany", 20, 225, 250, 50, colours.green, colours.lightGreen, action="extended",
               display=True)
        button(display, "Global", 20, 300, 250, 50, colours.blue, colours.changeBlue, action="global", display=True)
        button(display, "Dla dwóch graczy", 20, 375, 250, 50, colours.orange, colours.changeOrange, action="players",
               display=True)
        button(display, "Wybor skina", 20, 450, 250, 50, colours.violet, colours.changeViolet, action="skinSelect")
        button(display, "Powrót", 20, 525, 250, 50, colours.red, colours.lightRed, action="gameIntro")

        pygame.display.update()
        clock.tick(15)


def controlsScreen(display):
    controlsActive = True
    while controlsActive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.blit(images.controlsIMG, (0, 0))
        button(display, "Powrót", 525, 525, 250, 50, colours.red, colours.lightRed, action="gameIntro")

        pygame.display.update()
        clock.tick(15)


def skinSelectScreen(display):
    select = True
    while select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(colours.white)
        fileSkin = open("skin.txt", "r")
        line1 = fileSkin.readline()
        line2 = fileSkin.readline()
        fileSkin.close()

        if line1 == "gre\n":
            display.blit(images.pointingArrowIMG, (165, 125))
        elif line1 == "red\n":
            display.blit(images.pointingArrowIMG, (390, 125))
        elif line1 == "blu\n":
            display.blit(images.pointingArrowIMG, (615, 125))

        if line2 == "gre":
            display.blit(images.pointingArrowIMG, (165, 275))
        elif line2 == "red":
            display.blit(images.pointingArrowIMG, (390, 275))
        elif line2 == "blu":
            display.blit(images.pointingArrowIMG, (615, 275))

        showMessageOnScreen(display, "Wybierz skina węża", colours.black, -275, "medium")
        showMessageOnScreen(display, "Singleplayer", colours.black, -200, "small")
        button(display, "Ziel/Czer", 100, 150, 150, 50, colours.green, colours.lightGreen, action="green1")
        button(display, "Czer/czarny", 325, 150, 150, 50, colours.red, colours.lightRed, action="red1")
        button(display, "Nieb/Zółty", 550, 150, 150, 50, colours.blue, colours.changeBlue, action="blue1")
        showMessageOnScreen(display, "Multiplayer", colours.black, -50, "small")
        button(display, "Ziel/Czer", 100, 300, 150, 50, colours.green, colours.lightGreen, action="green2")
        button(display, "Czer/czarny", 325, 300, 150, 50, colours.red, colours.lightRed, action="red2")
        button(display, "Nieb/Zółty", 550, 300, 150, 50, colours.blue, colours.changeBlue, action="blue2")
        display.blit(images.skin1IMG, (145, 400))
        display.blit(images.skin2IMG, (370, 400))
        display.blit(images.skin3IMG, (595, 400))

        button(display, "Powrót", 275, 525, 250, 50, colours.red, colours.lightRed, action="gameTypeMenu")

        pygame.display.update()
        clock.tick(15)


def gamePausedScreen(display):
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
                    gameIntroScreen(display)
        display.blit(images.menuIMG, (0, 0))
        showMessageOnScreen(display, "Paused", colours.black, -100, size="large")
        showMessageOnScreen(display, "Nacisnij 'C' by grać dalej", colours.black, 10, size="small")
        showMessageOnScreen(display, "Nacisnij 'Q' by wyjsc do menu", colours.black, 55, size="small")
        pygame.display.update()
        clock.tick(5)


def endGameScreen(display, gameType, text="Przegrałeś"):
    showMessageOnScreen(display, text, colours.white, yDisplace=-50, size="large")
    button(display, "Jeszcze raz!", 275, 350, 250, 50, colours.green, colours.lightGreen, action=gameType)
    button(display, "Do menu głównego", 275, 450, 250, 50, colours.red, colours.lightRed, action="gameIntro")
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
            gameOver = False
            return gameOver, gameExit
# End: Game Screens


# Begin: View Modification
def showActivePowerUps(display, speed, bonusPoints, shift):
    powerUps = smallFont.render("Aktywne ulepszenia: ", True, colours.black)
    display.blit(powerUps, [400, 0])
    if speed:
        display.blit(images.speedIMG, [635, 10])
    if bonusPoints:
        display.blit(images.bonusIMG, [655, 10])
    if shift:
        display.blit(images.shiftIMG, [675, 10])


def showMessageOnScreen(display, msg, colour, yDisplace=0, size="small"):
    textSurf, textRect = createText(msg, colour, size)
    textRect.center = (displayWidth / 2), (displayHeight / 2) + yDisplace
    display.blit(textSurf, textRect)


def showScore(display, score, position=[0, 0]):
    text = smallFont.render("Wynik: " + str(score), True, colours.black)
    display.blit(text, position)


def button(theDisplay, text, x, y, width, height, inactiveColour, activeColour, action=None, display=False):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        if action and display:
            if action == "classic":
                theDisplay.blit(images.classicGameDescriptionIMG, (300, 150))
            elif action == "extended":
                theDisplay.blit(images.extendedGameDescriptionIMG, (300, 150))
            elif action == "global":
                theDisplay.blit(images.globalGameDescriptionIMG, (300, 150))
            elif action == "players":
                theDisplay.blit(images.playersGameDescriptionIMG, (300, 150))
        pygame.draw.rect(theDisplay, activeColour, (x, y, width, height))
        if click[0] == 1 and action:
            if action == "quit":
                pygame.quit()
                quit()
            elif action == "gameIntro":
                gameIntroScreen(theDisplay)
            elif action == "gameTypeMenu":
                gameTypeMenuScreen(theDisplay)
            elif action == "controls":
                controlsScreen(theDisplay)
            elif action == "classic":
                gameLoopGame(theDisplay, "classic")
            elif action == "extended":
                gameLoopGame(theDisplay, "extended")
            elif action == "global":
                gameLoopGame(theDisplay, "global")
            elif action == "players":
                gameLoopGame(theDisplay, "players")
            elif action == "skinSelect":
                skinSelectScreen(theDisplay)
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
        pygame.draw.rect(theDisplay, inactiveColour, (x, y, width, height))
    putTextOnButton(theDisplay, text, colours.black, x, y, width, height)


def putTextOnButton(display, msg, colour, buttonX, buttonY, buttonWidth, buttonHeight, size="small"):
    textSurf, textRect = createText(msg, colour, size)
    textRect.center = (buttonX + (buttonWidth / 2), buttonY + (buttonHeight / 2))
    display.blit(textSurf, textRect)


def createText(text, colour, size):
    if size == "small":
        textSurface = smallFont.render(text, True, colour)
    elif size == "medium":
        textSurface = medFont.render(text, True, colour)
    elif size == "large":
        textSurface = largeFont.render(text, True, colour)
    return textSurface, textSurface.get_rect()
# End: View Modification


# Begin: Utility Functions
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


def randObstaclePosition():
    X = round(random.randrange(blockSize, displayWidth - blockSize - blockSize) / 20.0) * 20.0
    Y = scoreBarHeight + round(
        random.randrange(blockSize, displayHeight - scoreBarHeight - blockSize - blockSize) / 20.0) * 20.0
    return [X, Y]


def checkBorder(snake, displayWidth, displayHeight, scoreBarHeight):
    if snake.leadX >= displayWidth or snake.leadX < 0 or snake.leadY >= displayHeight or snake.leadY < scoreBarHeight:
        return True
    return False


def handleInput(display, snake1, controlsKeys1, snake2=None, controlKeys2=None):
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
                gamePausedScreen(display)
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
                    gamePausedScreen(display)
# End: Utility Functions


# Begin: Game Modes
def classicGame(display):
    skin = getSkin(1)
    snake = snakeClass.Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
    fruitPosition = randFruitPosition()
    background = images.backgroundTextureRandom()

    getNewFruit = True
    gameExit = False
    gameOver = False

    player1Score = 0

    while not gameExit:
        while gameOver:

            snake.setChange(0, 0)
            try:
                gameOver, gameExit = endGameScreen(display, "classic")
            except TypeError:
                pass

        try:
            gameExit = handleInput(display, snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
        except TypeError:
            pass

        if getNewFruit:
            img = images.randomFruitSkin()
            getNewFruit = False

        display.blit(background, (0, 0))
        display.blit(img, fruitPosition)
        snake.move(display)
        snake.checkSnakeLength()
        display.fill(colours.grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(display, player1Score)

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


def extendedGame(display, gameMode="extended"):
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
    fruitSkin = [images.randomFruitSkin(), images.randomFruitSkin(), images.randomFruitSkin()]

    gameExit = False
    gameOver = False
    background = images.backgroundTextureRandom()
    skin = getSkin(1)
    snake = snakeClass.Snake(displayWidth / 2, displayHeight / 2, skin[0], skin[1])
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
                gameOver, gameExit = endGameScreen(display, gameMode)
            except TypeError:
                pass

        try:
            if not shiftActive:
                gameExit = handleInput(display, snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s])
            else:
                gameExit = handleInput(display, snake, [pygame.K_d, pygame.K_a, pygame.K_s, pygame.K_w])
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
                powerupimg = images.speedIMG
            elif powerupNumber == 1:
                powerupimg = images.bonusIMG
            elif powerupNumber == 2:
                powerupimg = images.shiftIMG
            powerUpPosition = randFruitPosition()
            while powerUpPosition in snake.snakeList or powerUpPosition in objectList:
                powerUpPosition = randFruitPosition()
            objectList[5] = powerUpPosition
            isPowerUpPresent = True

        # Showing object on the screen
        display.blit(background, (0, 0))
        snake.move(display)
        snake.checkSnakeLength()

        for index in range(0, 3):
            display.blit(fruitSkin[index], objectList[index])

        if isMushroomPresent:
            display.blit(images.mushroomIMG, objectList[3])

        if isObstaclePresent:
            display.blit(images.obstacleIMG, objectList[4])

        if isPowerUpPresent:
            display.blit(powerupimg, objectList[5])

        display.fill(colours.grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(display, player1Score)
        showActivePowerUps(display, speedActive, bonusPointsActive, shiftActive)  # wyswietlanie bonusa
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
                fruitSkin[index] = images.randomFruitSkin()

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
                if powerupimg == images.speedIMG:
                    speedActive = True
                    timeSinceSpeedPickup = time.time()
                elif powerupimg == images.bonusIMG:
                    bonusPointsActive = True
                    timeSinceBonusPointsPickup = time.time()
                elif powerupimg == images.shiftIMG:
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
            gameOver = snake.checkHeadOverlapsBody() or gameOver

        clock.tick(FPS)
    pygame.quit()
    quit()


def playersGame(display):
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
    background = images.backgroundTextureRandom()

    snake = snakeClass.Snake(0, 2 * blockSize + 3 * blockSize, skin1[0], skin1[1])
    snake2 = snakeClass.Snake(displayWidth - blockSize, displayHeight - 3 * blockSize, skin2[0], skin2[1], "left")
    snake2.xChange = -blockSize

    fruitList = [None, None, None]
    fruitSkin = [images.randomFruitSkin(), images.randomFruitSkin(), images.randomFruitSkin()]

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
                        gameOver, gameExit = endGameScreen(display, "players", "Wygrywa gracz nr.2")
                    else:
                        gameOver, gameExit = endGameScreen(display, "players", "Wygrywa gracz nr.1")
                elif timeLeft < 0:
                    if player1Score > player2Score:
                        gameOver, gameExit = endGameScreen(display, "players", "Wygrywa gracz nr.1")
                    elif player1Score < player2Score:
                        gameOver, gameExit = endGameScreen(display, "players", "Wygrywa gracz nr.2")
                    else:
                        gameOver, gameExit = endGameScreen(display, "players", "Remis")
            except TypeError:
                pass

        try:
            gameExit = handleInput(display, snake, [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s], snake2,
                                   [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]) or gameExit
        except TypeError:
            pass

        if checkBorder(snake, displayWidth, displayHeight, scoreBarHeight):
            gameOver = True
            player1Fault = True

        if checkBorder(snake2, displayWidth, displayHeight, scoreBarHeight):
            gameOver = True

        display.blit(background, (0, 0))
        snake.move(display)
        snake2.move(display)
        # TODO opisy ang funkcji

        for index in range(0, 3):
            display.blit(fruitSkin[index], fruitList[index])

        snake.checkSnakeLength()
        snake2.checkSnakeLength()
        display.fill(colours.grey, rect=[0, 0, displayWidth, scoreBarHeight])
        showScore(display, player1Score)
        showScore(display, player2Score, [650, 0])

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
        showMessageOnScreen(display, "Pozostaly czas: " + str(timeLeft), colours.black, - 280)
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
                fruitSkin[index] = images.randomFruitSkin()

        for index in range(0, 3):
            if snake2.getHead() == fruitList[index]:
                fruitPosition = randFruitPosition()
                while fruitPosition in snake.snakeList or fruitPosition in snake2.snakeList or fruitPosition in fruitList:
                    fruitPosition = randFruitPosition()
                fruitList[index] = fruitPosition
                snake2.snakeLength += 1
                player2Score += 10
                fruitSkin[index] = images.randomFruitSkin()

        clock.tick(FPS)

    pygame.quit()
    quit()


def gameLoopGame(display, gameMode):
    if gameMode == "classic":
        classicGame(display)
    elif gameMode == "extended":
        extendedGame(display)
    elif gameMode == "global":
        extendedGame(display, "global")
    elif gameMode == "players":
        playersGame(display)


# End: Game Modes
gameIntroScreen(gameDisplay)
