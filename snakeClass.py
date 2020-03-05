import pygame


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

    def move(self, display):
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

        display.blit(head, (self.snakeList[-1][0], self.snakeList[-1][1]))

        # part = [X,Y]
        for part in self.snakeList[:-1]:
            display.blit(self.bodyImg, (part[0], part[1]))

    def checkSnakeLength(self):
        if len(self.snakeList) > self.snakeLength:
            del self.snakeList[0]

    def checkHeadOverlapsBody(self):
        for eachSegment in self.snakeList[:-1]:
            if eachSegment == [self.leadX, self.leadY]:
                return True

    def getHead(self):
        return [self.leadX, self.leadY]
