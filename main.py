import pygame, math, sys

from Ball import *
from Goal import *
from Player import *

pygame.init()




clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height
screen = pygame.display.set_mode(size)


bgColor = r,g,b = 0, 128, 33
bgImage = pygame.image.load("Images/field/fieldfull.png")
bgRect = bgImage.get_rect()

ball = Ball(size, [40,40])
rGoal = Goal("right", size)
lGoal = Goal("left", size) 
p1= Playerball("right", size, [70,70])
p2= Playerball("left", size, [70,70])





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
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
    p1.wallBounce(size)
    p2.move()
    p2.wallBounce(size)

    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(ball.image, ball.rect)
    screen.blit(rGoal.image, rGoal.rect)
    screen.blit(lGoal.image, lGoal.rect)
    screen.blit(p1.image, p1.rect)
    screen.blit(p2.image, p2.rect)
    pygame.display.flip()
    clock.tick(60)
    print clock.get_fps()
