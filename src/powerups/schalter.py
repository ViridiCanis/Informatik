import pygame
from pygame.locals import *
from powerups import Powerup
import math


class Schalter(Powerup):
    def __init__(self, pos, spiel):
        Powerup.__init__(self, pos, spiel, "placeholder.png")
        

    def setup(self):
        pass

    def activate(self):
        self.spiel.schalter = not self.spiel.schalter

