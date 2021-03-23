import pygame
from pygame.locals import *
from powerups import Powerup


class Heal(Powerup):
    bild = pygame.image.load('images/Heal.png')
    def __init__(self, pos, spiel):
        Powerup.__init__(self, pos, spiel, Heal.bild)

    def setup(self):
        pass

    def activate(self):
        self.spiel.spieler.hp += 5
        self.spiel.level[self.pos[1]][self.pos[0]] = ""

    def update(self):
        pass
