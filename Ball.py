import pygame, math

class Ball():
    def __init__(self,  screenSize, size=None):
        self.image = pygame.image.load("Images/ball/Soccerball.png")
        if size:
            self.image=pygame.transform.scale(self.image,size)
        self.rect = self.image.get_rect(center=[screenSize[0]/2, screenSize[1]/2])
        self.radius=self.rect.width/2
        self.speed = [0,0]
        self.maxSpeed = 10
        self.boostedSpeed = 13
    
      
    def wallBounce(self,size):
        width=size[0]
        height=size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
     
    def playerBounce(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.dist(other.rect.center)<self.radius+other.radius:
                    self.speed[0]=-self.speed[0]
                    self.speed[1]=-self.speed[1]
                    
    def dist(self,pt):
        x1=self.rect.center[0]
        y1=self.rect.center[1]
        x2=pt[0]
        y2=pt[1]
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
        
        
        
        
        
        
        
        
        
        
        
        
        
