import pygame, math, sys

from Ball import *
from Goal import *

pygame.init()




clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height
screen = pygame.display.set_mode(size)


bgColor = r,g,b = 0, 128, 33
bgImage = pygame.image.load("Images/field/fieldfull.png")
bgRect = bgImage.get_rect()

ball = Ball(size, [50,50])
rGoal = Goal("right", size)
lGoal = Goal("left", size)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
















    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    screen.blit(ball.image, ball.rect)
    screen.blit(rGoal.image, rGoal.rect)
    screen.blit(lGoal.image, lGoal.rect)
    pygame.display.flip()
    clock.tick(60)
