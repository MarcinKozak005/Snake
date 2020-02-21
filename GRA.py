import pygame
import time
import random

import coloursAndFonts as CAF
import images as GFX

pygame.init()


displayHeight=600
displayWidth=800
blockSize=20
direction="right"
direction2="right"
scoreBarHeight=40
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption("Wunsz rzeczny, bardzo CAF.blueezpieczny")
pygame.display.set_icon(GFX.icon)
FPS=7
clock=pygame.time.Clock()



def chooseBackgroundTexture():
    numer_background=random.randrange(4)
    return GFX.backgroundTextureList[numer_background]


def chooseFruitTexture():
    numer=random.randrange(5)
    return GFX.fruitsTexture[numer]


#definicja snake'a ?
def snake(blockSize, snakeList,headImg,bodyImg):
    if(direction=="right"):
        head=pygame.transform.rotate(headImg,270)
    if(direction=="left"):
        head=pygame.transform.rotate(headImg,90)
    if(direction=="up"):
        head=headImg
    if(direction=="down"):
        head=pygame.transform.rotate(headImg,180)
    
    gameDisplay.blit(head,(snakeList[-1][0],snakeList[-1][1]))
    
    for XiY in snakeList[:-1]:
        gameDisplay.blit(bodyImg,(XiY[0],XiY[1]))

def snake2(blockSize, snakeList2,headImg2,bodyImg2):
    if(direction2=="right"):
        head2=pygame.transform.rotate(headImg2,270)
    if(direction2=="left"):
        head2=pygame.transform.rotate(headImg2,90)
    if(direction2=="up"):
        head2=headImg2
    if(direction2=="down"):
        head2=pygame.transform.rotate(headImg2,180)
    
    gameDisplay.blit(head2,(snakeList2[-1][0],snakeList2[-1][1]))
    
    for XiY in snakeList2[:-1]:
        gameDisplay.blit(bodyImg2,(XiY[0],XiY[1]))

   

def pause():
    paused=True
    while(paused==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
            if(event.type==pygame.KEYDOWN):
                if(event.key==pygame.K_c):
                    paused=False
                elif(event.key==pygame.K_q):
                    gameIntro()
        gameDisplay.blit(GFX.menu1,(0,0))
        messageToScreen("Paused",CAF.black,-100,size="large")
        messageToScreen("Nacisnij 'C' by grać dalej",CAF.black,10,size="small")
        messageToScreen("Nacisnij 'Q' by wyjsc do menu",CAF.black,55,size="small")
        pygame.display.update()
        clock.tick(5)
        

#wyswiebackgroundnie w rogu
def powerUps(speed,bonusPoints,shift):
    powery=CAF.smallFont.render("Aktywne ulepszenia: ",True,CAF.black)
    gameDisplay.blit(powery,[400,0])
    if(speed==True):
        gameDisplay.blit(GFX.speedImg,[635,10])
    if(bonusPoints==True):
        gameDisplay.blit(GFX.bonusImg,[655,10])
    if(shift==True):
        gameDisplay.blit(GFX.shiftImg,[675,10])


#wyswiebackgroundnie score'a
def score(score):
    text=CAF.smallFont.render("Wynik: "+str(score),True,CAF.black)
    gameDisplay.blit(text,[0,0])

def score2(score):
    text=CAF.smallFont.render("Wynik: "+str(score),True,CAF.black)
    gameDisplay.blit(text,[650,0])

#jak nazwa mowi
def textToButton(msg,colour,buttonX, buttonY, buttonWidth,buttonHeight,size="small"):
    textSurf,textRect=textObjects(msg,colour,size)
    textRect.center=((buttonX+(buttonWidth/2),buttonY+(buttonHeight/2)))
    gameDisplay.blit(textSurf,textRect)

#do buttonow potrzebne
def textObjects(text,colour,size):
    if(size=="small"):
        textSurface=CAF.smallFont.render(text,True,colour)
    elif(size=="medium"):
        textSurface=CAF.medFont.render(text,True,colour)
    elif(size=="large"):
        textSurface=CAF.largeFont.render(text,True,colour)
    return textSurface,textSurface.get_rect()
    
#nazwa
def messageToScreen(msg,colour,yDisplace=0,size="small"):
    textSurf,textRect=textObjects(msg,colour,size)
    textRect.center=(displayWidth/2),(displayHeight/2)+yDisplace
    gameDisplay.blit(textSurf,textRect)


#guziki
def button(text,x,y,width,height,inactiveColour,activeColour,action=None,action2=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if(x+width>cur[0]>x and y+height>cur[1]>y):
        if(action2 != None):
            if(action2=="classic"):
                gameDisplay.blit(GFX.classicImg,(300,150))
            elif(action2=="extended"):
                gameDisplay.blit(GFX.extendedImg,(300,150))
            elif(action2=="global"):
                gameDisplay.blit(GFX.globalImg,(300,150))
            elif(action2=="players"):
                gameDisplay.blit(GFX.globalImg,(300,150))
        pygame.draw.rect(gameDisplay,activeColour,(x,y,width,height))
        if(click[0]==1 and action!=None):
            if(action=="quit"):
                pygame.quit()
                quit()
            if(action=="intro"):
                gameIntro()
            if(action=="intro1"):
                subGameMenu()
            if(action=="controls"):
                controls()
            if(action=="play"):
                subGameMenu()
            if(action=="classic"):
                gameLoop("classic")
            if(action=="rozbud"):
                gameLoop("rozbud")
            if(action=="global"):
                gameLoop("global")
            if(action=="multi"):
                gameLoop("players")
            if(action=="skins"):
                chooseSkin()
            if(action=="greenAction1"):
                GFX.skin1=open("GFX.skin1.txt","r+")
                GFX.skin1.write("CAF.green")
                skin1.close()
            if(action=="redAction1"):
                GFX.skin1=open("GFX.skin1.txt","r+")
                GFX.skin1.write("CAF.red")
                skin1.close()
            if(action=="blueAction1"):
                GFX.skin1=open("GFX.skin1.txt","r+")
                GFX.skin1.write("CAF.blue")
                skin1.close()
            if(action=="greenAction2"):
                GFX.skin2=open("GFX.skin2.txt","r+")
                GFX.skin2.write("CAF.green")
                GFX.skin2.close()
            if(action=="redAction2"):
                GFX.skin2=open("GFX.skin2.txt","r+")
                GFX.skin2.write("CAF.red")
                GFX.skin2.close()
            if(action=="blueAction2"):
                GFX.skin2=open("GFX.skin2.txt","r+")
                GFX.skin2.write("CAF.blue")
                GFX.skin2.close()
            if(action=="no"):
                paused=False
                
            
    else:
        pygame.draw.rect(gameDisplay,inactiveColour,(x,y,width,height))
    
    textToButton(text,CAF.black,x,y,width,height)
    
#pygame.display.update()
def chooseSkin():
    selected=True
    while(selected==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        
        
        gameDisplay.fill(CAF.white)
        plik_GFX.skin1=open("GFX.skin1.txt","r")
        dane=plik_GFX.skin1.read()
        if(dane=="green"):
            gameDisplay.blit(GFX.choosenSkin,(165,125))
        elif(dane=="red"):
            gameDisplay.blit(GFX.choosenSkin,(390,125))
        elif(dane=="blue"):
            gameDisplay.blit(GFX.choosenSkin,(615,125))
        plik_skin1.close()
        
        
        plik_GFX.skin2=open("GFX.skin2.txt","r")
        dane=plik_GFX.skin2.read()
        if(dane=="green"):
            gameDisplay.blit(GFX.choosenSkin,(165,275))
        elif(dane=="red"):
            gameDisplay.blit(GFX.choosenSkin,(390,275))
        elif(dane=="blue"):
            gameDisplay.blit(GFX.choosenSkin,(615,275))
        plik_GFX.skin2.close()
        
        
        
        
        
        messageToScreen("Wybierz skina węża",CAF.black,-275,"medium")
        messageToScreen("Singleplayer",CAF.black,-200,"small")
        button("zielony/czerwony",100,150,150,50,CAF.green,CAF.lightGreen,action="CAF.greenAction1")
        button("czerwony/czarny",325,150,150,50,CAF.red,CAF.lightRed,action="CAF.redAction1")
        button("niebieski/zółty",550,150,150,50,CAF.blue,CAF.changeBlue,action="CAF.blueAction1")
        messageToScreen("Multiplayer",CAF.black,-50,"small")
        button("zielony/czerwony",100,300,150,50,CAF.green,CAF.lightGreen,action="CAF.greenAction2")
        button("czerwony/czarny",325,300,150,50,CAF.red,CAF.lightRed,action="CAF.redAction2")
        button("niebieski/zółty",550,300,150,50,CAF.blue,CAF.changeBlue,action="CAF.blueAction2")
        gameDisplay.blit(GFX.skin1,(145,400))
        gameDisplay.blit(GFX.skin2,(370,400))
        gameDisplay.blit(GFX.skin3,(595,400))
                
        button("Powrót",275,525,250,50,CAF.red,CAF.lightRed,action="intro1")
        
        pygame.display.update()
        clock.tick(15)
    
def subGameMenu():
    gmenu=True
    while(gmenu==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()

        
        gameDisplay.fill(CAF.white)
        messageToScreen("Wybierz rodzaj rozgrywki",CAF.black,-250,"medium")
        button("Klasyczny",20,150,250,50,CAF.yellow,CAF.changeYellow,action="classic",action2="classic")
        button("extended",20,225,250,50,CAF.green,CAF.lightGreen,action="rozbud",action2="extended")
        button("Global",20,300,250,50,CAF.blue,CAF.changeBlue,action="global",action2="global")
        button("Dla dwóch graczy",20,375,250,50,CAF.orange,CAF.changeOrange,action="multi",action2="players")
        button("Wybór skina",20,450,250,50,CAF.violet,CAF.changeViolet,action="skins")
        button("Powrót",20,525,250,50,CAF.red,CAF.lightRed,action="intro")
        
        pygame.display.update()
        clock.tick(15)

def gameIntro():
    intro=True
    while(intro==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        
        gameDisplay.blit(GFX.menu1,(0,0))
        messageToScreen("Snake",CAF.green,-200,"large")
        
        #buttonY
        button("Graj",275,200,250,50,CAF.green,CAF.lightGreen,action="play")
        button("Zasady i controls",275,300,250,50,CAF.grey,CAF.lightGrey,action="controls")
        button("Wyjscie",275,400,250,50,CAF.red,CAF.lightRed,action="quit")
        
        pygame.display.update()
        clock.tick(15)

def controls():
    controls=True
    while(controls==True):
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                pygame.quit()
                quit()
        
    
        gameDisplay.blit(GFX.controls1,(0,0))
        button("Powrót",525,525,250,50,CAF.red,CAF.lightRed,action="intro")
        
        pygame.display.update()
        clock.tick(15)


def classic():
    global direction
    direction="right"
    randFruits=True
    gameExit=False
    gameOver=False
    leadX=displayWidth/2
    leadY=displayHeight/2
    leadXChange=20
    leadYChange=0
    
    snakeList=[]
    snakeLength=3
    score1=0
    
    skin1=open("skin1.txt","r")
    line1=skin1.readline()
    if(line1=="green"):
        headImg=pygame.image.load('graphics/head1.png')
        bodyImg=pygame.image.load('graphics/body1.png')
    elif(line1=="red"):
        headImg=pygame.image.load('graphics/head2.png')
        bodyImg=pygame.image.load('graphics/body2.png')
    elif(line1=="blue"):
        headImg=pygame.image.load('graphics/head3.png')
        bodyImg=pygame.image.load('graphics/body3.png')
    skin1.close()
    
    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    
    background=chooseBackgroundTexture()
       
    
    while(gameExit != True):
        while(gameOver==True):
            leadXChange=0
            leadYChange=0
            messageToScreen("Przegrałes",CAF.white,yDisplace=-50,size="large")
            button("Jeszcze raz!",275,350,250,50,CAF.green,CAF.lightGreen,action="classic")
            button("Do menu głównego",275,450,250,50,CAF.red,CAF.lightRed,action="intro")
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    gameExit=True
                    gameOver=False
    
                        
        for event in pygame.event.get():
            if(event.type== pygame.QUIT):
                gameExit=True
            if(event.type==pygame.KEYDOWN):
                if(event.key == pygame.K_a):
                    if(direction!="right"):
                        direction="left"
                        leadXChange=-blockSize
                        leadYChange=0
                elif(event.key==pygame.K_d):
                    if(direction!="left"):                        
                        direction="right"
                        leadXChange=blockSize
                        leadYChange=0
                elif(event.key == pygame.K_w):
                    if(direction!="down"):
                        direction="up"
                        leadYChange=-blockSize
                        leadXChange=0
                elif(event.key==pygame.K_s):
                    if(direction!="up"):
                        direction="down"
                        leadYChange=blockSize
                        leadXChange=0
                elif(event.key==pygame.K_p):
                    pause()
                    
        leadX+=leadXChange
        leadY+=leadYChange
        
        if(leadX>=displayWidth or leadX<0 or leadY>=displayHeight or leadY<scoreBarHeight):
            gameOver=True
        
        gameDisplay.blit(background,(0,0))

        if(randFruits==True):
            img=chooseFruitTexture()
            randFruits=False
            
        gameDisplay.blit(img,(randAppleX,randAppleY))
                   

        snakeHead=[]
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        snake(blockSize,snakeList,headImg,bodyImg)
        gameDisplay.fill(CAF.grey,rect=[0,0,displayWidth,scoreBarHeight])
        
        if(len(snakeList)>snakeLength):
            del snakeList[0]
            
        for eachSegment in snakeList[:-1]:
            if(eachSegment==snakeHead):
                gameOver=True
        
        
        score(score1)
        pygame.display.update()
        
        if(leadX==randAppleX and leadY==randAppleY):
            randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple=[randAppleX,randAppleY]
            
            keepChecking=True
            newElement=False
            while(keepChecking==True):
                checked=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple):
                        #print("ala")
                        newElement=True
                        break
                    else:
                        checked+=1
                if(checked==len(snakeList)):
                    keepChecking=False
                if(newElement==True):
                    newElement=False
                    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple=[randAppleX,randAppleY]
                 
            snakeLength+=1
            score1+=10
            randFruits=True
    
        clock.tick(FPS)

    pygame.quit()
    quit()



def extended(gameMode="rozbud"):
    passingBorder=1
    #potrzebne do losowania skina pierwszych jeblek~cos takiego to powyzsze
    random2=True
    random3=True
    timeGFX.mushroom=time.time()
    isGFX.mushroom=False
    timeObstacle=time.time()
    isObstacle=False
    timePowerUp=time.time()
    isPowerUp=False
    #czas przyspieszenia jest nizej
    speed=False
    bonusPoints=False
    shift=False
    speedCooldown=7
    bonusCooldown=10
    shiftCooldown=7
    timeToSpawnPowerUp=3
    #byl_GFX.mushroom=False
    appleList=[]
    global direction
    direction="right"
    #losowac_skin_Fruits=True
    gameExit=False
    gameOver=False
    leadX=displayWidth/2
    leadY=displayHeight/2
    leadXChange=20
    leadYChange=0
    
    snakeList=[]
    snakeLength=3
    score1=0
    
    #losowanie background
    background=chooseBackgroundTexture()
    
    skin1=open("skin1.txt","r")
    line1=skin1.readline()
    if(line1=="green"):
        headImg=pygame.image.load('graphics/head1.png')
        bodyImg=pygame.image.load('graphics/body1.png')
    elif(line1=="red"):
        headImg=pygame.image.load('graphics/head2.png')
        bodyImg=pygame.image.load('graphics/body2.png')
    elif(line1=="blue"):
        headImg=pygame.image.load('graphics/head3.png')
        bodyImg=pygame.image.load('graphics/body3.png')
    skin1.close()
    
    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple=[randAppleX,randAppleY]
    appleList.append(placeApple)
    
    randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY2= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple2=[randAppleX2,randAppleY2]    
    
    #sprawdza czy sie powtarza z applelist
    while(random2==True):
        checkedRandom2=0
        for eachElem in appleList[:]:
            if(placeApple2==eachElem):
                break
            else:
                checkedRandom2+=1
        if(checkedRandom2==len(appleList)):
            random2=False
            appleList.append(placeApple2)
        randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
        randAppleY2= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
        placeApple2=[randAppleX2,randAppleY2]
    
    randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY3= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple3=[randAppleX3,randAppleY3]
    
    #sprawdza czy sie powtarza z applelist
    while(random3==True):
        checkedRandom3=0
        for eachElem in appleList[:]:
            if(placeApple3==eachElem):
                break
            else:
                checkedRandom3+=1
        if(checkedRandom3==len(appleList)):
            random3=False
            appleList.append(placeApple3)
        randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
        randAppleY3= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
        placeApple3=[randAppleX3,randAppleY3]


    while(gameExit != True):
        while(gameOver==True):
            #brak poruszenia po koncu gry
            leadXChange=0
            leadYChange=0
            messageToScreen("Przegrałes",CAF.white,yDisplace=-50,size="large")
            button("Jeszcze raz!",275,350,250,50,CAF.green,CAF.lightGreen,action=gameMode)
            button("Do menu głównego",275,450,250,50,CAF.red,CAF.lightRed,action="intro")
            pygame.display.update()
            
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    gameExit=True
                    gameOver=False          
                        
        if(speed==True):
            endOfSpeed=time.time()-timeSpeed
            if(endOfSpeed>speedCooldown):
                FPS=7
                speed=False
            else:
                FPS=14
        else:
            FPS=7
            
        if(shift==True):
            endOfShift=time.time()-timeShift
            if(endOfShift>shiftCooldown):
                shift=False
            
        for event in pygame.event.get():
            if(event.type== pygame.QUIT):
                gameExit=True
            if(event.type==pygame.KEYDOWN):
                if(shift==False):
                    if(event.key == pygame.K_a):
                        if(direction!="right"):
                            direction="left"
                            leadXChange=-blockSize
                            leadYChange=0
                    elif(event.key==pygame.K_d):
                        if(direction!="left"):                        
                            direction="right"
                            leadXChange=blockSize
                            leadYChange=0
                    elif(event.key == pygame.K_w):
                        if(direction!="down"):
                            direction="up"
                            leadYChange=-blockSize
                            leadXChange=0
                    elif(event.key==pygame.K_s):
                        if(direction!="up"):
                            direction="down"
                            leadYChange=blockSize
                            leadXChange=0
                    elif(event.key==pygame.K_p):
                        pause()
                elif(shift==True):
                    if(event.key == pygame.K_a):
                        if(direction!="left"):
                            direction="right"
                            leadXChange=blockSize
                            leadYChange=0
                    elif(event.key==pygame.K_d):
                        if(direction!="right"):                        
                            direction="left"
                            leadXChange=-blockSize
                            leadYChange=0
                    elif(event.key == pygame.K_w):
                        if(direction!="up"):
                            direction="down"
                            leadYChange=blockSize
                            leadXChange=0
                    elif(event.key==pygame.K_s):
                        if(direction!="down"):
                            direction="up"
                            leadYChange=-blockSize
                            leadXChange=0
                    elif(event.key==pygame.K_p):
                        pause()
                    
        leadX+=leadXChange
        leadY+=leadYChange
        
        #wyjscie poza plansze
        if(gameMode=="rozbud"):
            if(leadX>=displayWidth or leadX<0 or leadY>=displayHeight or leadY<scoreBarHeight):
                gameOver=True
        elif(gameMode=="global"):
            if(leadX==displayWidth):
                leadX=0
            elif(leadX==0-blockSize):
                leadX=displayWidth
            elif(leadY==displayHeight):
                leadY=0+scoreBarHeight
            elif(leadY<0+scoreBarHeight):
                leadY=displayHeight
        
        gameDisplay.blit(background,(0,0))            
            
        if(passingBorder==1):
            appleimg=pygame.image.load('graphics/fruit1.png')
            appleimg2=pygame.image.load('graphics/fruit2.png')
            appleimg3=pygame.image.load('graphics/fruit3.png')
            passingBorder=2
            
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        gameDisplay.blit(appleimg2,(randAppleX2,randAppleY2))
        gameDisplay.blit(appleimg3,(randAppleX3,randAppleY3))
                
        
        
        
        #ustawianie GFX.mushrooma i losowanie jego wspolrzednych
        koniecGFX.mushroom=time.time()-timeGFX.mushroom
        if(koniecGFX.mushroom>10 and isGFX.mushroom==False):
            #if(byl_GFX.mushroom==False):
            randGFX.mushroomX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randGFX.mushroomY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0 
            placeGFX.mushroom=[randGFX.mushroomX,randGFX.mushroomY]
            #sprawdzanie GFX.mushroomka na snake i fruitek
            keepChecking_M=True
            randNewElementM=False
            while(keepChecking_M==True):
                
                checked_snake=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeGFX.mushroom):
                        print("MnaS")
                        randNewElementM=True
                        break
                    else:
                        checked_snake+=1
                            
                checked_apple=0    
                if(randNewElementM==False):
                    for eachElem in appleList[:]:
                        if(eachElem==placeGFX.mushroom):
                            print("MnaO")
                            randNewElementM=True
                            break
                        else:
                            checked_apple+=1
                            
                if(isObstacle==True and randNewElementM==False):
                    if(placeGFX.mushroom==placePrzesz):
                        randNewElementM=True
                        
                if(isPowerUp==True and randNewElementM==False):
                    if(placeGFX.mushroom==placePower):
                        randNewElementM=True
                            
                if(checked_snake==len(snakeList) and checked_apple==len(appleList) and randNewElementM==False):
                    keepChecking_M=False
                        
                if(randNewElementM==True):
                    randNewElementM=False
                    randGFX.mushroomX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randGFX.mushroomY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0 
                    placeGFX.mushroom=[randGFX.mushroomX,randGFX.mushroomY]
            isGFX.mushroom=True
            
        if(isGFX.mushroom==True):
            gameDisplay.blit(GFX.mushroom,(randGFX.mushroomX,randGFX.mushroomY))

          
        #przeszkoda
        koniecPrzeszkoda=time.time()-timeObstacle
        if(koniecPrzeszkoda>5 and isObstacle==False):
            #podwojne blocksize aby dalo sie okrazyc
            randObstacleX= round(random.randrange(blockSize,displayWidth-blockSize-blockSize)/20.0)*20.0
            randObstacleY= scoreBarHeight+ round(random.randrange(blockSize,displayHeight-scoreBarHeight-blockSize-blockSize)/20.0)*20.0
            placePrzesz=[randObstacleX,randObstacleY]
            
            keepChecking_snakeP=True
            randomNewElementP=False
            while(keepChecking_snakeP==True):
                
                checked=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placePrzesz):
                        print("PnaS")
                        randomNewElementP=True
                        break
                    else:
                        checked+=1
                        
                #checked_apple=0    
                if(randomNewElementP==False):
                    for eachElem in appleList[:]:
                        if(eachElem==placePrzesz):
                            print("PnaO")
                            randomNewElementP=True
                            break
                        #else:
                            #checked_apple+=1
                        
                if(isGFX.mushroom==True and randomNewElementP==False):
                    if(placePrzesz==placeGFX.mushroom):
                        randomNewElementP=True
                
                if(isPowerUp==True and randomNewElementP==False):
                    if(placePrzesz==placePower):
                        randomNewElementP=True
                        
                        
                if(checked==len(snakeList) and randomNewElementP==False):
                    keepChecking_snakeP=False
                    
                if(randomNewElementP==True):
                    randomNewElementP=False
                    randObstacleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randObstacleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placePrzesz=[randObstacleX,randObstacleY]

            isObstacle=True
            
        
        
        #powerup        
        koniecpowerup=time.time()-timePowerUp
        if(koniecpowerup>timeToSpawnPowerUp and isPowerUp==False):
            
            numer_power=random.randrange(3)
            if(numer_power==0):
                powerupimg=GFX.speedImg
            elif(numer_power==1):
                powerupimg=GFX.bonusImg
            elif(numer_power==2):
                powerupimg=GFX.shiftImg
                
            randPowerX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randPowerY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0 
            placePower=[randPowerX,randPowerY]
            #sprawdzanie powera na snake i fruitek
            keepChecking_PU=True
            randomNewElementPU=False
            
            while(keepChecking_PU==True):
                
                checked_snake=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placePower):
                        print("PUnaS")
                        randomNewElementPU=True
                        break
                    else:
                        checked_snake+=1
                            
                checked_apple=0    
                if(randomNewElementPU==False):
                    for eachElem in appleList[:]:
                        if(eachElem==placePower):
                            print("PUnaO")
                            randomNewElementPU=True
                            break
                        else:
                            checked_apple+=1
                            
                if(isObstacle==True and randomNewElementPU==False):
                    if(placePower==placePrzesz):
                        randomNewElementPU=True
                        
                if(isGFX.mushroom==True and randomNewElementPU==False):
                    if(placePower==placeGFX.mushroom):
                        randomNewElementPU=True
                            
                if(checked_snake==len(snakeList) and checked_apple==len(appleList) and randomNewElementPU==False):
                    keepChecking_PU=False
                        
                if(randomNewElementPU==True):
                    randomNewElementPU=False
                    randPowerX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randPowerY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0 
                    placePower=[randPowerX,randPowerY]
            isPowerUp=True
            
        if(isPowerUp==True):
            gameDisplay.blit(powerupimg,(randPowerX,randPowerY))

        
        snakeHead=[]
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        snake(blockSize,snakeList,headImg,bodyImg)
        
        #wyswiebackgroundnie przeszkody po snaku-wazniejsza
        if(isObstacle==True):
            gameDisplay.blit(GFX.obstacleImg,(randObstacleX,randObstacleY))
        
        
        #Gorne menu
        gameDisplay.fill(CAF.grey,rect=[0,0,displayWidth,scoreBarHeight])
        
        if(len(snakeList)>snakeLength):
            del snakeList[0]
            
        #czy wjechal sam w siebie
        for eachSegment in snakeList[:-1]:
            if(eachSegment==snakeHead):
                gameOver=True
        
        
        score(score1)
        powerUps(speed,bonusPoints,shift)
        pygame.display.update()
        
        if(bonusPoints==True):
            koniecbonuspoints=time.time()-czasbonuspoints
            if(koniecbonuspoints>bonusCooldown):
                bonusPoints=False
                bonus=0
            else:
                bonus=5
        else:
            bonus=0
            
        
        
        #zjadanie jabluszka1
        if(leadX==randAppleX and leadY==randAppleY):
            randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple=[randAppleX,randAppleY]
            
            keepCheckingSnakeO=True
            randomNewElementO=False
            while(keepCheckingSnakeO==True):
                
                checked=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple):
                        print("ala")
                        randomNewElementO=True
                        break
                    else:
                        checked+=1
                        
                if(isGFX.mushroom==True):
                    if(placeApple==placeGFX.mushroom):
                        randomNewElementO=True
                        
                if(isObstacle==True and randomNewElementO==False):
                    if(placeApple==placePrzesz):
                        randomNewElementO=True
                        
                if(isPowerUp==True and randomNewElementO==False):
                    if(placeApple==placePower):
                        randomNewElementO=True
                
                if(placeApple==placeApple2 or placeApple==placeApple3):
                    randomNewElementO=True
                        
                        
                if(checked==len(snakeList) and randomNewElementO==False):
                    keepCheckingSnakeO=False
                    
                if(randomNewElementO==True):
                    randomNewElementO=False
                    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple=[randAppleX,randAppleY]
            appleList.pop(0)
            appleList.insert(0,[randAppleX,randAppleY])
            snakeLength+=1
            score1+=10+bonus
            appleimg=chooseFruitTexture()
            
        
        #zjadanie jabloszka 2
        if(leadX==randAppleX2 and leadY==randAppleY2):
            randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple2=[randAppleX2,randAppleY2]
            
            keepCheckingSnakeO2=True
            randomNewElementO2=False
            while(keepCheckingSnakeO2==True):
                
                checked2=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple2):
                        print("ala")
                        randomNewElementO2=True
                        break
                    else:
                        checked2+=1
                        
                if(isGFX.mushroom==True and randomNewElementO2==False):
                    if(placeApple2==placeGFX.mushroom):
                        randomNewElementO2=True
                        
                if(isObstacle==True and randomNewElementO2==False):
                    if(placeApple2==placePrzesz):
                        randomNewElementO2=True
                        
                if(isPowerUp==True and randomNewElementO2==False):
                    if(placeApple2==placePower):
                        randomNewElementO2=True
                        
                if(placeApple2==placeApple or placeApple2==placeApple3):
                    randomNewElementO2=True
                        
                        
                if(checked2==len(snakeList) and randomNewElementO2==False):
                    keepCheckingSnakeO2=False
                    
                if(randomNewElementO2==True):
                    randomNewElementO2=False
                    randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple2=[randAppleX2,randAppleY2]
            appleList.pop(1)
            appleList.insert(1,[randAppleX2,randAppleY2])
            snakeLength+=1
            score1+=10+bonus
            appleimg2=chooseFruitTexture()
        
        
        
        #zjadanie jabluszka3
        if(leadX==randAppleX3 and leadY==randAppleY3):
            randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple3=[randAppleX3,randAppleY3]
            
            keepCheckingSnakeO3=True
            randomNewElementO3=False
            while(keepCheckingSnakeO3==True):
                
                checked3=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple3):
                        print("ala")
                        randomNewElementO3=True
                        break
                    else:
                        checked3+=1
                        
                if(isGFX.mushroom==True):
                    if(placeApple3==placeGFX.mushroom):
                        randomNewElementO3=True
                        
                if(isObstacle==True and randomNewElementO3==False):
                    if(placeApple3==placePrzesz):
                        randomNewElementO3=True
                        
                if(isPowerUp==True and randomNewElementO3==False):
                    if(placeApple3==placePower):
                        randomNewElementO3=True
                    
                if(placeApple3==placeApple or placeApple3==placeApple2):
                    randomNewElementO3=True
                        
                        
                if(checked3==len(snakeList) and randomNewElementO3==False):
                    keepCheckingSnakeO3=False
                    
                if(randomNewElementO3==True):
                    randomNewElementO3=False
                    randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple3=[randAppleX3,randAppleY3]
            appleList.pop(2)
            appleList.insert(2,[randAppleX3,randAppleY3])
            snakeLength+=1
            score1+=10+bonus
            appleimg3=chooseFruitTexture()
        
        
        
        #zjadanie GFX.mushrooma
        if(isGFX.mushroom==True):
            if(leadX==randGFX.mushroomX and leadY==randGFX.mushroomY):
                isGFX.mushroom=False
                score1-=5
                snakeLength-=1
                timeGFX.mushroom=time.time()
                if(snakeLength<=2):
                    gameOver=True
        
        #"zjadanie" przeszkody
        if(isObstacle==True):
            if(leadX==randObstacleX and leadY==randObstacleY):
                gameOver=True
                
                
        #zjadanie powerupa
        if(isPowerUp==True):
            if(leadX==randPowerX and leadY==randPowerY):
                isPowerUp=False
                timePowerUp=time.time()
                if(powerupimg==GFX.speedImg):
                    speed=True
                    timeSpeed=time.time()
                elif(powerupimg==GFX.bonusImg):
                    bonusPoints=True
                    czasbonuspoints=time.time()
                elif(powerupimg==GFX.shiftImg):
                    shift=True
                    timeShift=time.time()
        
        
        #okrazenie przeszkody
        if(isObstacle==True):
            P1=False
            P2=False
            P3=False
            P4=False
            P5=False
            P6=False
            P7=False
            P8=False
            
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX-blockSize,randObstacleY-blockSize]):
                    P1=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX,randObstacleY-blockSize]):
                    P2=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX+blockSize,randObstacleY-blockSize]):
                    P3=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX-blockSize,randObstacleY]):
                    P4=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX+blockSize,randObstacleY]):
                    P5=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX-blockSize,randObstacleY+blockSize]):
                    P6=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX,randObstacleY+blockSize]):
                    P7=True
            for eachSegment in snakeList[:]:
                if(eachSegment==[randObstacleX+blockSize,randObstacleY+blockSize]):
                    P8=True
            if(P1==True and P2==True and P3==True and P4==True and P5==True and P6==True and P7==True and P8==True):
                score1+=50
                isObstacle=False
                timeObstacle=time.time()
            
        clock.tick(FPS)
    
 
    pygame.quit()
    quit()
    
    
def players():
    czas=time.clock()
    gameTime=60
    elapsedTime=time.clock()-czas
    timeLeft=gameTime-elapsedTime
    FPS=7
    passingBorder=1
    #potrzebne do losowania skina pierwszych jeblek~cos takiego to powyzsze
    random2=True
    random3=True
    appleList=[]
    global direction
    direction="right"
    #losowac_skin_Fruits=True
    gameExit=False
    gameOver=False
    leadX=0
    leadY=40+3*blockSize
    leadXChange=20
    leadYChange=0
    
    snakeList=[]
    snakeLength=3
    score1=0
    
    
    global direction2
    direction2="left"
    leadX2=displayWidth-blockSize
    leadY2=displayHeight-3*blockSize
    leadXChange2=-20
    leadYChange2=0
    
    snakeList2=[]
    snakeLength2=3
    score2p=0
    
    skin1=open("skin1.txt","r")
    line1=skin1.readline()
    if(line1=="green"):
        headImg=pygame.image.load('graphics/head1.png')
        bodyImg=pygame.image.load('graphics/body1.png')
    elif(line1=="red"):
        headImg=pygame.image.load('graphics/head2.png')
        bodyImg=pygame.image.load('graphics/body2.png')
    elif(line1=="blue"):
        headImg=pygame.image.load('graphics/head3.png')
        bodyImg=pygame.image.load('graphics/body3.png')
    skin1.close()
    
    
    skin2=open("skin2.txt","r")
    linia2=skin2.readline()
    if(linia2=="green"):
        headImg2=pygame.image.load('graphics/head1.png')
        bodyImg2=pygame.image.load('graphics/body1.png')
    elif(linia2=="red"):
        headImg2=pygame.image.load('graphics/head2.png')
        bodyImg2=pygame.image.load('graphics/body2.png')
    elif(linia2=="blue"):
        headImg2=pygame.image.load('graphics/head3.png')
        bodyImg2=pygame.image.load('graphics/body3.png')
    skin2.close()
    
    
    
    """
    numer_background=random.randrange(2)
    if(numer_background==0):
        background=pygame.image.load('background1.png')
    elif(numer_background==1):
        background=pygame.image.load('background2.png')
    """
    background=chooseBackgroundTexture()
    
    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple=[randAppleX,randAppleY]
    appleList.append(placeApple)
    
    randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY2= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple2=[randAppleX2,randAppleY2]    
    
    #sprawdza czy sie powtarza z applelist
    while(random2==True):
        checkedRandom2=0
        for eachElem in appleList[:]:
            if(placeApple2==eachElem):
                break
            else:
                checkedRandom2+=1
        if(checkedRandom2==len(appleList)):
            random2=False
            appleList.append(placeApple2)
        randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
        randAppleY2= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
        placeApple2=[randAppleX2,randAppleY2]
    
    randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
    randAppleY3= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
    placeApple3=[randAppleX3,randAppleY3]
    
    #sprawdza czy sie powtarza z applelist
    while(random3==True):
        checkedRandom3=0
        for eachElem in appleList[:]:
            if(placeApple3==eachElem):
                break
            else:
                checkedRandom3+=1
        if(checkedRandom3==len(appleList)):
            random3=False
            appleList.append(placeApple3)
        randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
        randAppleY3= scoreBarHeight+round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
        placeApple3=[randAppleX3,randAppleY3]
    
    

    while(gameExit != True):
        while(gameOver==True or timeLeft<0):
            #brak poruszenia po koncu gry
            leadXChange=0
            leadYChange=0
            if(gameOver==True):
                if(gameOverCausedBy==1):
                    messageToScreen("Wygrywa gracz nr.2",CAF.white,yDisplace=-50,size="large")
                    button("Jeszcze raz!",275,350,250,50,CAF.green,CAF.lightGreen,action="multi")
                    button("Do menu głównego",275,450,250,50,CAF.red,CAF.lightRed,action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if(event.type==pygame.QUIT):
                            gameExit=True
                            gameOver=False
                elif(gameOverCausedBy==2):
                    messageToScreen("Wygrywa gracz nr.1",CAF.white,yDisplace=-50,size="large")
                    button("Jeszcze raz!",275,350,250,50,CAF.green,CAF.lightGreen,action="multi")
                    button("Do menu głównego",275,450,250,50,CAF.red,CAF.lightRed,action="intro")
                    pygame.display.update()
                    for event in pygame.event.get():
                        if(event.type==pygame.QUIT):
                            gameExit=True
                            gameOver=False
            elif(timeLeft<0):
                if(score1>score2p):
                    messageToScreen("Wygrywa gracz nr.1",CAF.white,yDisplace=-50,size="large")
                elif(score1<score2p):
                    messageToScreen("Wygrywa gracz nr.2",CAF.white,yDisplace=-50,size="large")
                else:
                    messageToScreen("Remis",CAF.white,yDisplace=-50,size="large")
                button("Jeszcze raz!",275,350,250,50,CAF.green,CAF.lightGreen,action="multi")
                button("Do menu głównego",275,450,250,50,CAF.red,CAF.lightRed,action="intro")
                pygame.display.update()
                for event in pygame.event.get():
                    if(event.type==pygame.QUIT):
                        gameExit=True
                        gameOver=False
        #######################

        for event in pygame.event.get():
            if(event.type== pygame.QUIT):
                gameExit=True
            if(event.type==pygame.KEYDOWN):
                    if(event.key == pygame.K_a):
                        if(direction!="right"):
                            direction="left"
                            leadXChange=-blockSize
                            leadYChange=0
                    elif(event.key==pygame.K_d):
                        if(direction!="left"):                        
                            direction="right"
                            leadXChange=blockSize
                            leadYChange=0
                    elif(event.key == pygame.K_w):
                        if(direction!="down"):
                            direction="up"
                            leadYChange=-blockSize
                            leadXChange=0
                    elif(event.key==pygame.K_s):
                        if(direction!="up"):
                            direction="down"
                            leadYChange=blockSize
                            leadXChange=0
                     
                    
                    if(event.key == pygame.K_LEFT):
                        if(direction2!="right"):
                            direction2="left"
                            leadXChange2=-blockSize
                            leadYChange2=0
                    elif(event.key==pygame.K_RIGHT):
                        if(direction2!="left"):                        
                            direction2="right"
                            leadXChange2=blockSize
                            leadYChange2=0
                    elif(event.key == pygame.K_UP):
                        if(direction2!="down"):
                            direction2="up"
                            leadYChange2=-blockSize
                            leadXChange2=0
                    elif(event.key==pygame.K_DOWN):
                        if(direction2!="up"):
                            direction2="down"
                            leadYChange2=blockSize
                            leadXChange2=0
                            
  
                            
                    elif(event.key==pygame.K_p):
                        pause()
                    
        leadX+=leadXChange
        leadY+=leadYChange
        
        leadX2+=leadXChange2
        leadY2+=leadYChange2
        
        #wyjscie poza plansze
        if(leadX>=displayWidth or leadX<0 or leadY>=displayHeight or leadY<scoreBarHeight):
            gameOver=True
            gameOverCausedBy=1
        
        if(leadX2>=displayWidth or leadX2<0 or leadY2>=displayHeight or leadY2<scoreBarHeight):
            gameOver=True
            gameOverCausedBy=2
            
        
        gameDisplay.blit(background,(0,0))
            
        if(passingBorder==1):
            appleimg=pygame.image.load('graphics/fruit1.png')
            appleimg2=pygame.image.load('graphics/fruit2.png')
            appleimg3=pygame.image.load('graphics/fruit3.png')
            passingBorder=2
            
        gameDisplay.blit(appleimg,(randAppleX,randAppleY))
        gameDisplay.blit(appleimg2,(randAppleX2,randAppleY2))
        gameDisplay.blit(appleimg3,(randAppleX3,randAppleY3))
                
        
        
        snakeHead=[]
        snakeHead.append(leadX)
        snakeHead.append(leadY)
        snakeList.append(snakeHead)
        snake(blockSize,snakeList,headImg,bodyImg)
        
        
        snakeHead2=[]
        snakeHead2.append(leadX2)
        snakeHead2.append(leadY2)
        snakeList2.append(snakeHead2)
        snake2(blockSize,snakeList2,headImg2,bodyImg2)
        #ZAKOŃCZYŁEM TU!
        
        
        
        #Gorne menu
        gameDisplay.fill(CAF.grey,rect=[0,0,displayWidth,scoreBarHeight])
        
        if(len(snakeList)>snakeLength):
            del snakeList[0]
        
        if(len(snakeList2)>snakeLength2):
            del snakeList2[0]
        
        #czy wjechal sam w siebie
        for eachSegment in snakeList[:-1]:
            if(eachSegment==snakeHead):
                gameOver=True
                gameOverCausedBy=1
        
        for eachSegment in snakeList2[:-1]:
            if(eachSegment==snakeHead2):
                gameOver=True
                gameOverCausedBy=2
                
        for eachSegment in snakeList2[:-1]:
            if(eachSegment==snakeHead):
                gameOver=True
                gameOverCausedBy=1
                
        for eachSegment in snakeList[:-1]:
            if(eachSegment==snakeHead2):
                gameOver=True
                gameOverCausedBy=2
        
        
        
        score(score1)
        score2(score2p)
        elapsedTime=time.clock()-czas
        timeLeft=gameTime-elapsedTime
        timeLeft=round(timeLeft,2)
        messageToScreen("Pozostaly czas: "+str(timeLeft),CAF.black,-280)
        pygame.display.update()
        

        
        
        #zjadanie jabluszka1
        if(leadX==randAppleX and leadY==randAppleY):
            randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple=[randAppleX,randAppleY]
            
            keepCheckingSnakeO=True
            randomNewElementO=False
            while(keepCheckingSnakeO==True):
                
                checked=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple):
                        print("ala")
                        randomNewElementO=True
                        break
                    else:
                        checked+=1
                        
                checked2=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple):
                        print("ala")
                        randomNewElementO=True
                        break
                    else:
                        checked2+=1

                if(placeApple==placeApple2 or placeApple==placeApple3):
                    randomNewElementO=True

                if(checked==len(snakeList) and randomNewElementO==False):
                    keepCheckingSnakeO=False
                    
                if(randomNewElementO==True):
                    randomNewElementO=False
                    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple=[randAppleX,randAppleY]
            appleList.pop(0)
            appleList.insert(0,[randAppleX,randAppleY])
            snakeLength+=1
            score1+=10
            appleimg=chooseFruitTexture()
            #losowac_skin_Fruits=True
        
        
        #zjadanie jabloszka 2
        if(leadX==randAppleX2 and leadY==randAppleY2):
            randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple2=[randAppleX2,randAppleY2]
            
            keepCheckingSnakeO2=True
            randomNewElementO2=False
            while(keepCheckingSnakeO2==True):
                
                checked2=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple2):
                        print("ala")
                        randomNewElementO2=True
                        break
                    else:
                        checked2+=1
                        
                checked21=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple2):
                        print("ala")
                        randomNewElementO2=True
                        break
                    else:
                        checked21+=1
                        
                if(placeApple2==placeApple or placeApple2==placeApple3):
                    randomNewElementO2=True

                if(checked2==len(snakeList) and randomNewElementO2==False):
                    keepCheckingSnakeO2=False
                    
                if(randomNewElementO2==True):
                    randomNewElementO2=False
                    randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple2=[randAppleX2,randAppleY2]
            appleList.pop(1)
            appleList.insert(1,[randAppleX2,randAppleY2])
            snakeLength+=1
            score1+=10
            appleimg2=chooseFruitTexture()

       
        #zjadanie jabluszka3
        if(leadX==randAppleX3 and leadY==randAppleY3):
            randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple3=[randAppleX3,randAppleY3]
            
            keepCheckingSnakeO3=True
            randomNewElementO3=False
            while(keepCheckingSnakeO3==True):
                
                checked3=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple3):
                        print("ala")
                        randomNewElementO3=True
                        break
                    else:
                        checked3+=1
                        
                checked32=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple3):
                        print("ala")
                        randomNewElementO3=True
                        break
                    else:
                        checked32+=1
                    
                if(placeApple3==placeApple or placeApple3==placeApple2):
                    randomNewElementO3=True
                        
                        
                if(checked3==len(snakeList) and randomNewElementO3==False):
                    keepCheckingSnakeO3=False
                    
                if(randomNewElementO3==True):
                    randomNewElementO3=False
                    randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple3=[randAppleX3,randAppleY3]
            appleList.pop(2)
            appleList.insert(2,[randAppleX3,randAppleY3])
            snakeLength+=1
            score1+=10
            appleimg3=chooseFruitTexture()
        
       #dla drugiego weża:
       #zjadanie jabluszka1
        if(leadX2==randAppleX and leadY2==randAppleY):
            randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple=[randAppleX,randAppleY]
            
            keepCheckingSnakeO=True
            randomNewElementO=False
            while(keepCheckingSnakeO==True):
                
                checked=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple):
                        print("ala")
                        randomNewElementO=True
                        break
                    else:
                        checked+=1
                        
                checked1=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple):
                        print("ala")
                        randomNewElementO=True
                        break
                    else:
                        checked1+=1

                if(placeApple==placeApple2 or placeApple==placeApple3):
                    randomNewElementO=True

                if(checked==len(snakeList2) and randomNewElementO==False):
                    keepCheckingSnakeO=False
                    
                if(randomNewElementO==True):
                    randomNewElementO=False
                    randAppleX= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple=[randAppleX,randAppleY]
            appleList.pop(0)
            appleList.insert(0,[randAppleX,randAppleY])
            snakeLength2+=1
            score2p+=10
            appleimg=chooseFruitTexture()
            #losowac_skin_Fruits=True
            
        
        #zjadanie jabloszka 2
        if(leadX2==randAppleX2 and leadY2==randAppleY2):
            randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple2=[randAppleX2,randAppleY2]
            
            keepCheckingSnakeO2=True
            randomNewElementO2=False
            while(keepCheckingSnakeO2==True):
                
                checked2=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple2):
                        print("ala")
                        randomNewElementO2=True
                        break
                    else:
                        checked2+=1
                        
                checked21=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple2):
                        print("ala")
                        randomNewElementO2=True
                        break
                    else:
                        checked21+=1
                        
                if(placeApple2==placeApple or placeApple2==placeApple3):
                    randomNewElementO2=True

                if(checked2==len(snakeList2) and randomNewElementO2==False):
                    keepCheckingSnakeO2=False
                    
                if(randomNewElementO2==True):
                    randomNewElementO2=False
                    randAppleX2= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY2= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple2=[randAppleX2,randAppleY2]
            appleList.pop(1)
            appleList.insert(1,[randAppleX2,randAppleY2])
            snakeLength2+=1
            score2p+=10
            appleimg2=chooseFruitTexture()
        
        
        
        #zjadanie jabluszka3
        if(leadX2==randAppleX3 and leadY2==randAppleY3):
            randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
            randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
            placeApple3=[randAppleX3,randAppleY3]
            
            keepCheckingSnakeO3=True
            randomNewElementO3=False
            while(keepCheckingSnakeO3==True):
                
                checked3=0
                for eachSegment in snakeList2[:]:
                    if(eachSegment==placeApple3):
                        print("ala")
                        randomNewElementO3=True
                        break
                    else:
                        checked3+=1
                        
                checked31=0
                for eachSegment in snakeList[:]:
                    if(eachSegment==placeApple3):
                        print("ala")
                        randomNewElementO3=True
                        break
                    else:
                        checked31+=1
                        
                    
                if(placeApple3==placeApple or placeApple3==placeApple2):
                    randomNewElementO3=True
                        
                        
                if(checked3==len(snakeList2) and randomNewElementO3==False):
                    keepCheckingSnakeO3=False
                    
                if(randomNewElementO3==True):
                    randomNewElementO3=False
                    randAppleX3= round(random.randrange(0,displayWidth-blockSize)/20.0)*20.0
                    randAppleY3= scoreBarHeight+ round(random.randrange(0,displayHeight-scoreBarHeight-blockSize)/20.0)*20.0
                    placeApple3=[randAppleX3,randAppleY3]
            appleList.pop(2)
            appleList.insert(2,[randAppleX3,randAppleY3])
            snakeLength2+=1
            score2p+=10
            appleimg3=chooseFruitTexture()
                            
            
        clock.tick(FPS)

    pygame.quit()
    quit()
    
#penbackground gry
def gameLoop(gameMode,pierwszego="CAF.green",drugiego="CAF.red"): #tu były te CAF.greenony
    
    if(gameMode=="rozbud"):
        extended()
    elif(gameMode=="classic"):
        classic()
    elif(gameMode=="global"):
        extended("global")
    elif(gameMode=="players"):
        players()
    


gameIntro()
