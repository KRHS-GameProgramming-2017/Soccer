import pygame, math, sys


pygame.init()




clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height
screen = pygame.display.set_mode(size)


bgColor = r,g,b = 0, 128, 33
bgImage = pygame.image.load("Images/field/fieldfull.png")
bgRect = bgImage.get_rect()







while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
















    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    pygame.display.flip()
    clock.tick(60)
