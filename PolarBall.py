import pygame, math, random
from Ball import Ball

class PolarBall(Ball):
    def __init__(self,  screenSize, size=None):
        Ball.__init__(self, screenSize, size)
        self.angle = 0
        self.totalSpeed = 0;
        self.screenSize = screenSize
        
    def move(self):
        self.convertSpeed()
        self.rect.move_ip(self.speed)
        
    def wallBounce(self,size):
        width=size[0]
        height=size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.angle = 360 - self.angle
            self.move()
        elif self.rect.top < 0 or self.rect.bottom > height:
            self.angle = 180 - self.angle
            self.move()
            
        if self.rect.top < 0:
            self.rect.top = 1
        if self.rect.bottom > height:
            self.rect.bottom = height - 1
        if self.rect.left < 0:
            self.rect.left = 1
        if self.rect.right > width:
            self.rect.right = width - 1
            
    def reset(self): 
        self.rect = self.image.get_rect(center=[ self.screenSize[0]/2,  self.screenSize[1]/2])
        #self.rect = self.image.get_rect(center=[ self.screenSize[0]/3*2,  self.screenSize[1]/2])
        self.totalSpeed = 0
        #print
        #print
    
    def playerBounce(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.dist(other.rect.center)<self.radius+other.radius:
                    if other.powerup == "fastball":
                        self.totalSpeed = self.boostedSpeed
                    else:
                        self.totalSpeed = self.normalSpeed
                    self.maxSpeed = self.totalSpeed
                    self.setAngle(other.rect.center)
                    self.angle += random.randint(-5, 5)
                    #print self.angle
                    self.move()
                    return True
        return False
        
    def setAngle(self, pt):
        diffX = float(self.rect.centerx - pt[0])
        diffY = float(self.rect.centery - pt[1])
        #if diffY == 0:
            #if diffX < 0:
                #self.angle = 90
            #else:
                #self.angle = 270
        #elif diffX == 0:
            #if diffY < 0:
                #self.angle = 180
            #else:
                #self.angle = 0
        #else:
        self.angle = -math.degrees(math.atan2(diffY,diffX))-90
                
    
    def convertSpeed(self):
        self.angle %= 360 #remainder keeps us bound 0 -> 360
        if self.totalSpeed == 0:
            self.speed = [0,0]
        elif self.angle == 0:
            self.speed = [0, -self.maxSpeed]
        elif 0 < self.angle < 90:
            x = math.sin(math.radians(self.angle))*-self.maxSpeed
            y = math.cos(math.radians(self.angle))*-self.maxSpeed
            self.speed = [x, y]
        elif self.angle == 90:
            self.speed = [-self.maxSpeed, 0]
        elif 90 < self.angle < 180:
            x = math.sin(math.radians(self.angle))*-self.maxSpeed
            y = math.cos(math.radians(self.angle))*-self.maxSpeed
            self.speed = [x, y]
        elif self.angle == 180:
            self.speed = [0, self.maxSpeed]
        elif 180 < self.angle < 270:
            x = math.sin(math.radians(self.angle))*-self.maxSpeed
            y = math.cos(math.radians(self.angle))*-self.maxSpeed
            self.speed = [x, y]
        elif self.angle == 270:
            self.speed = [self.maxSpeed, 0]
        elif 270 < self.angle < 360:
            x = math.sin(math.radians(self.angle))*-self.maxSpeed
            y = math.cos(math.radians(self.angle))*-self.maxSpeed
            self.speed = [x, y]
    
        
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    width = 1000
    height = 700
    size = width, height
    screen = pygame.display.set_mode(size)
    bgColor = r,g,b = 0, 128, 33
    bgImage = pygame.image.load("Images/field/fieldfull.png")
    bgRect = bgImage.get_rect()

    ball = PolarBall(size, [60,60])
    ball.angle = 45
    ball.totalSpeed = 20
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
        ball.move()
        ball.wallBounce(size)
        #print ball.angle
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
