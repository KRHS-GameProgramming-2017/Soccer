import pygame, math

class Button():
    def __init__(self, pos, name):
        if name == "single":
            self.images = [pygame.image.load("Images/button/singleplayer.png"),
                           pygame.image.load("Images/button/mouseover2.png")]
        else:
            self.images = [pygame.image.load("Images/button/multiplayer.png"),
                           pygame.image.load("Images/button/Mousover.png")]
                                
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = pos)
        
    def mouseOver(self, pt):
        if self.rect.right > pt[0] and self.rect.left < pt[0]:
            if self.rect.bottom > pt[1] and self.rect.top < pt[1]:
                self.image = self.images[1]
                return True
        self.image = self.images[0]
        return False
                           
                           
                           
                           
                           
                           
                           
                           
