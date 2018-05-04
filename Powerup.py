import pygame, math, random


class Powerup():
    def __init__(self, kind, screenSize, size= None):
        self.kind=kind
        if self.kind=="fastball":
            self.image=pygame.image.load("Images/ball/PowerUp.png")
        
        if size:
            self.image=pygame.transform.scale(self.image,size)
        
        self.rect = self.image.get_rect()
        self.radius=self.rect.width/2
        pos = [screenSize[0]/2 , random.randint(50+self.radius, screenSize[1]-self.radius)]
        self.rect = self.image.get_rect(center = pos)
        
            
            
            
            



















