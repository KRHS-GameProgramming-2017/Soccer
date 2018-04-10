import pygame, math, sys

from Ball import *
from PolarBall import *
from Goal import *
from Player import *
from Scoreboard import *
from Button import *
pygame.init()




clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height
screen = pygame.display.set_mode(size)
bgColor = r,g,b = 0, 128, 33
bgImage = pygame.image.load("Images/field/fieldfull.png")
bgRect = bgImage.get_rect()





ball = PolarBall(size, [45,45])
rGoal = Goal("right", size)
lGoal = Goal("left", size) 
p1= Playerball("right", size, [70,70])
p2= Playerball("left", size, [70,70])
rScore = Scoreboard([width/2+50, 25], "right")
lScore = Scoreboard([width/2-50, 25], "left")
sButton= Button([width/4,height/2], "single")
mButton= Button([(width/4)*3, height/2], "else")

mode = "menu"
so = False
mo = False
while True:
    bgImage = pygame.image.load("Images/Screens/MENU.png")
    bgRect = bgImage.get_rect()
    while mode == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                so = sButton.mouseOver(event.pos)
                mo = mButton.mouseOver(event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                if so:
                    mode = "count down"
                    rScore.pointreset()
                    lScore.pointreset()
                    p1= Playerball("right", size, [70,70])
                    p2= AI("left", size, ball, [70,70])
                if mo:
                    mode = "count down"
                    rScore.pointreset()
                    lScore.pointreset()
                    p1= Playerball("right", size, [70,70])
                    p2= Playerball("left", size, [70,70])
        
                
                
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(sButton.image, sButton.rect)
        screen.blit(mButton.image, mButton.rect)
        pygame.display.flip()
        clock.tick(60)
    bgImage = pygame.image.load("Images/field/fieldfull.png")
    bgRect = bgImage.get_rect()
    count = 0;
    countDown = pygame.image.load("Images/field/three.png")
    countDownRect = countDown.get_rect(center = [width/2, height/2])
    countDownTime = 30
    while mode == "count down" :
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        count += 1
        if count == countDownTime:
            countDown = pygame.image.load("Images/field/two.png")
            countDownRect = countDown.get_rect(center = [width/2, height/2])
        if count == countDownTime*2:
            countDown = pygame.image.load("Images/field/one.png")
            countDownRect = countDown.get_rect(center = [width/2, height/2])
        if count == countDownTime*3:
            countDown = pygame.image.load("Images/field/Go.png")
            countDownRect = countDown.get_rect(center = [width/2
            , height/2])
        if count == countDownTime*4:
            mode = "game"
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(ball.image, ball.rect)
        screen.blit(rGoal.image, rGoal.rect)
        screen.blit(lGoal.image, lGoal.rect)
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(rScore.image, rScore.rect)
        screen.blit(lScore.image, lScore.rect)
        screen.blit(countDown, countDownRect)
        pygame.display.flip()
        clock.tick(60)
    while mode == "game" :
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    p1.go("up")
                if event.key == pygame.K_DOWN:
                    p1.go("down")
                if event.key == pygame.K_LEFT: 
                    p1.go("left")
                if event.key == pygame.K_RIGHT: 
                    p1.go("right")
                if event.key == pygame.K_w:
                    p2.go("up")
                if event.key == pygame.K_s:
                    p2.go("down")
                if event.key == pygame.K_a:    
                    p2.go("left")
                if event.key == pygame.K_d:  
                    p2.go("right")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP: 
                    p1.go("stop up")
                if event.key == pygame.K_DOWN: 
                    p1.go("stop down")
                if event.key == pygame.K_LEFT: 
                    p1.go("stop left")
                if event.key == pygame.K_RIGHT: 
                    p1.go("stop right")
                if event.key == pygame.K_w:
                    p2.go("stop up")
                if event.key == pygame.K_s:
                    p2.go("stop down")
                if event.key == pygame.K_a: 
                    p2.go("stop left")
                if event.key == pygame.K_d:   
                    p2.go("stop right")    
        
        p1.move()
        p1.wallBounce()
        p2.move()
        p2.wallBounce()
        
        ball.move()
        ball.wallBounce(size)
        ball.playerBounce(p1)
        ball.playerBounce(p2)
        
        if ball.bounceGoal(lGoal, size):
            p1.reset()
            p2.reset()
            ball.reset()
            if rScore.pointadd():
                mode = "home win"
            else:
                mode = "count down"
                
            #if rScore > (5):
            
        if ball.bounceGoal(rGoal, size):
            p1.reset()
            p2.reset()
            ball.reset()
            if lScore.pointadd():
                mode = "away win"
            else:
                mode = "count down"

                
                
            #if lScore > (5):
              
            
            

        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(ball.image, ball.rect)
        screen.blit(rGoal.image, rGoal.rect)
        screen.blit(lGoal.image, lGoal.rect)
        screen.blit(p1.image, p1.rect)
        screen.blit(p2.image, p2.rect)
        screen.blit(rScore.image, rScore.rect)
        screen.blit(lScore.image, lScore.rect)
        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
        
    bgImage = pygame.image.load("Images/Screens/home win.png")
    bgRect = bgImage.get_rect()
    while mode == "home win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                mode = "menu"
        
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
    
    bgImage = pygame.image.load("Images/Screens/away win.png")
    bgRect = bgImage.get_rect()
    while mode == "away win":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                mode = "menu"
        
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
