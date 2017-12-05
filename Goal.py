import pygame, math

class Goal():
    def __init__(self, side, screenSize, size=None):
        self.image = pygame.image.load("Images/goal/Goal.png")
        yOffset = 0;  #fudge factor to fix goals not quite center
        if size:
            self.image=pygame.transform.scale(self.image,size)
        if side == "left":
            pos = [0, screenSize[1]/2+yOffset]
            print "left", pos
            self.rect = self.image.get_rect(midleft=pos)
        else: 
            pos = [screenSize[0], screenSize[1]/2+yOffset]
            print "right", pos
            self.rect = self.image.get_rect(midright=pos)
        
