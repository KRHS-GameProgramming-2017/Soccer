import pygame, math

class playerball();
 def __init__(self, side, screenSize, size=None):
        self.side = side
        if self.side == "right":
            self.image = pygame.image.load("Images/player/player1.png")
        else:
            self.image = pygame.image.load("Images/player/player2.png")
        if size:
            self.image=pygame.transform.scale(self.image,size)
        
        if self.side == "right":
            self.rect = self.image.get_rect(center=[screenSize[0]*.85, screenSize[1]/2])
        else:
            self.rect = self.image.get_rect(center=[screenSize[0]*.15, screenSize[1]/2])
            
        self.radius=self.rect.width/2
        self.speed = [0,0]
        self.maxSpeed = 10
        self.boostedSpeed = 13
        self.borderSize = 10
        self.endSize = 33
        self.centerSize = 12/2
        
def wallBounce(self,size):
        width=size[0]
        height=size[1]
        
        if self.side == "right":
            if self.rect.left < width/2+self.centerSize or self.rect.right > width-endSize:
                self.speed[0] = -self.speed[0]
        else:
            if self.rect.left < self.endSize or self.rect.right > width/2-self.centersize:
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
