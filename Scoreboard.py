import pygame, math

class Scoreboard():
    def __init__(self, pos, side):
     if side == "left":
        self.images = [pygame.image.load("Images/scoreboard/away0.png"),
                       pygame.image.load("Images/scoreboard/away1.png"),
                       pygame.image.load("Images/scoreboard/away2.png"),
                       pygame.image.load("Images/scoreboard/away3.png"),
                       pygame.image.load("Images/scoreboard/away4.png"),
                       pygame.image.load("Images/scoreboard/away5.png")]
     else:
        self.images = [pygame.image.load("Images/scoreboard/home0.png"),
                       pygame.image.load("Images/scoreboard/home1.png"),
                       pygame.image.load("Images/scoreboard/home2.png"),
                       pygame.image.load("Images/scoreboard/home3.png"),
                       pygame.image.load("Images/scoreboard/home4.png"),
                       pygame.image.load("Images/scoreboard/home5.png")]
                       

        self.score = 0
        self.image = self.image[self.score]
        self.rect = pygame.image.rect

