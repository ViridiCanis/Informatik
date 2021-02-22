import pygame
import sys
from pygame.locals import *
import random
import threading

class Gegner(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()

        self.bewegung = 2
        self.hp = 10
        self.atk = 2
