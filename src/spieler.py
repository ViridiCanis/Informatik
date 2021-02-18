import pygame
import sys
from pygame.locals import *
import random
import threading

class Spieler(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        bewegung = 2
        hp = 10
        xp = 0

        def bewegen_nord(self):
                pass



        def bewegen_ost(self):
                pass




        def bewegen_süd(self):
                pass




        def bewegen_west(self):
                pass

        def update(self):
            self.rect.x += 5


player = Spieler()

        