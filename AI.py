import pygame, math
from Player import *

class AI(Playerball):
    def __init__(self, side, screensize, ball, size = None):
        Playerball.__init__(self, side, screensize, size)
        self.type = "AI"
        self.ball = ball
        self.noMove = 0;
        self.noMoveMax = 60*.5
        self.atGoal = False
        self.stuck = False
        self.oldpos = [0,0]
        
    def whereBall(self):
        print self.ball.rect.center
    
    def reset(self):
        Playerball.reset(self)
        self.noMove = 0
        self.stuck = False
        
    def checkAtGoal(self):
        width = self.screenSize[0]
        height = self.screenSize[1]
        
        if self.rect.centery < height/2 + 25 and self.rect.centery > height/2 - 25:
            #print "Y at Goal!"
            self.atGoal = True
            
        else:
            self.atGoal = False
            
        
    def go(self):
        self.checkAtGoal()
        if self.oldpos == self.rect.center:
            self.noMove += 1
            #print self.noMove
        else:
            self.oldpos = self.rect.center
            self.noMove = 0
        
        if self.noMove > self.noMoveMax:
            self.stuck = True
            self.noMove = 0
        
        if self.atGoal:
            self.stuck = False
            self.noMove = 0
        
        if self.stuck:
            height = self.screenSize[1]
            if self.rect.centery > height/2:
                direction = "up";
            else:
                direction = "down"
        else:
            direction = self.getDirection()
            #print self.side, direction
        if direction == "up":
            self.speed[0] = 0
            self.speed[1] = -self.maxSpeed
        elif direction == "down":
            self.speed[0] = 0
            self.speed[1] = self.maxSpeed
        elif direction == "right":
            self.speed[0] = self.maxSpeed
            self.speed[1] = 0
        elif direction == "left":
            self.speed[0] = -self.maxSpeed
            self.speed[1] = 0
        elif direction == "up left":
            self.speed[0] = -self.maxSpeed
            self.speed[1] = -self.maxSpeed
        elif direction == "up right":
            self.speed[1] = -self.maxSpeed
            self.speed[0] = self.maxSpeed
        elif direction == "down left":
            self.speed[1] = self.maxSpeed
            self.speed[0] = self.maxSpeed
        elif direction == "down right":
            self.speed[1] = self.maxSpeed
            self.speed[0] = self.maxSpeed
            
        if direction == "stop up":
            self.speed[1] = 0
        elif direction == "stop down":
            self.speed[1] = 0
        elif direction == "stop right":
            self.speed[0] = 0
        elif direction == "stop left":
            self.speed[0] = 0
    
    def getDirection(self):
        width = self.screenSize[0]
        heigth = self.screenSize[1]
        if self.side == "right":
            if self.ball.rect.centerx < width/2-75:
                if self.rect.centery > heigth/2+25:
                    return "up right"
                elif self.rect.centery < heigth/2-25:
                    return "down right"
                else:
                    return "right"
        else:
            if self.ball.rect.x > self.screenSize[0]/2+75:
                if self.rect.centery > heigth/2+25:
                    return "up left"
                elif self.rect.centery < heigth/2-25:
                    return "down left"
                else:
                    return "left"
        
        diffx = self.ball.rect.x - self.rect.x
        diffy = self.ball.rect.y - self.rect.y
        
        if diffx > 10:
            if diffy > 10:
                return "down right"
            elif diffy < -10:
                return "up right"
            else:
                return "right"
        elif diffx < -10:
            if diffy > 5:
                return "down left"
            elif diffy < -10:
                return "up left"
            else: 
                return "left"
        else:
            if diffy > 10:
                return "down"
            elif diffy < -10:
                return "up"
            else:
                return ""
            
