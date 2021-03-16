import pygame
from pygame.locals import *
from powerups import Powerup


class Attack(Powerup):
    def __init__(self, pos, spiel):
        Powerup.__init__(self, pos, spiel, "Attack.png")

    def setup(self):
        pass

    def activate(self):
        self.spiel.spieler.atk += 3
        self.spiel.level[self.pos[1]][self.pos[0]] = ""

    def update(self):
        pass
