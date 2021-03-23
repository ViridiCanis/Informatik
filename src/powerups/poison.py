import pygame
from pygame.locals import *
from powerups import Powerup
import math


class Poison(Powerup):
    bild = pygame.image.load('images/poison.png')
    def __init__(self, pos, spiel):
        Powerup.__init__(self, pos, spiel, Poison.bild)
        self.duration = 0

    def setup(self):
        pass

    def activate(self):
        self.duration = 3

    def update(self):
        if self.duration > 0:
            self.spiel.spieler.hp -= 1
            self.duration -= 1
