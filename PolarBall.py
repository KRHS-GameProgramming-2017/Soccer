import pygame, math
from Ball import Ball

class PolarBall(Ball):
    def __init__(self,  screenSize, size=None):
        Ball.__init__(self, screenSize, size)
        angle = 0
        totalSpeed = 0;
        
    def move(self):
        self.convertSpeed()
        self.rect.move_ip(self.speed)
        
    def wallBounce(self,size):
        width=size[0]
        height=size[1]
        
        if self.rect.left < 0 or self.rect.right > width:
            self.angle -= 180
        elif self.rect.top < 0 or self.rect.bottom > height:
            self.angle -= 180
     
        
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
    ball.totalSpeed = 7
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
        ball.move()
        ball.wallBounce(size)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        screen.blit(ball.image, ball.rect)
        pygame.display.flip()
        clock.tick(60)
        
        
        
        
        
        
        
        
        
        
        
