import pygame
from pygame.locals import *
from powerups import Powerup
import math


class Poison(Powerup):
    def __init__(self, pos, spiel):
        Powerup.__init__(self, pos, spiel, "poison.png")
        self.duration = 0

    def setup(self):
        pass

    def activate(self):
        self.duration = 3

    def update(self):
        if self.duration > 0:
            self.spiel.spieler.hp -= math.pi / 2 # 1
            self.duration -= 1
