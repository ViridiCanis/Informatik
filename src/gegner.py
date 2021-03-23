import pygame
import sys
from pygame.locals import *
import random
import threading
import math


class Gegner(pygame.sprite.Sprite):
    bild = pygame.image.load('images/gegner.png')
    bild2 = pygame.image.load('images/gegner2.png')
    def __init__(
        self,
        g_x,
        g_y,
        hp,
        atk,
        spiel,
        boss = False,
        id = 0
    ):
        pygame.sprite.Sprite.__init__(self)
        self.spiel = spiel

        if boss:
            self.image = Gegner.bild
        else:
            self.image = Gegner.bild2

        #gegnerkoords
        self.g_y = g_y
        self.g_x = g_x
        self.bewegung_in_runde = 1
        self.hp = hp
        self.atk = atk
        self.id = id

    def setup(self):
        pass

    def update(self):
        if self.hp < 1:
            self.spiel.level[self.g_y][self.g_x] = ""

        s_x, s_y = self.spiel.spieler.x, self.spiel.spieler.y
        d = abs(self.g_x - s_x) + abs(self.g_y - s_y)
        if d > 1:
            if s_y > self.g_y and self.spiel.level[self.g_y + 1][self.g_x] == "":
                self.spiel.level[self.g_y + 1][self.g_x] = self
                self.spiel.level[self.g_y][self.g_x] = ""
                self.g_y = self.g_y + 1
            elif s_y < self.g_y and self.spiel.level[self.g_y - 1][self.g_x] == "":
                self.spiel.level[self.g_y - 1][self.g_x] = self
                self.spiel.level[self.g_y][self.g_x] = ""
                self.g_y = self.g_y - 1
            elif s_x > self.g_x and self.spiel.level[self.g_y][self.g_x + 1] == "":
                self.spiel.level[self.g_y][self.g_x + 1] = self
                self.spiel.level[self.g_y][self.g_x] = ""
                self.g_x = self.g_x + 1
            elif s_x < self.g_x and self.spiel.level[self.g_y][self.g_x - 1] == "":
                self.spiel.level[self.g_y][self.g_x - 1] = self
                self.spiel.level[self.g_y][self.g_x] = ""
                self.g_x = self.g_x - 1
        else: # neben dem Spieler => Angriff
            if s_y > self.g_y:
                self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk
            elif s_y < self.g_y:
                self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk
            elif s_x > self.g_x:
                self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk
            elif s_x < self.g_x:
                self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk

        #if abs(s_y - self.g_y) == 1 or abs(s_x - self.g_x) == 1:
            #idk
            #self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk
            #self.hp = self.hp - self.spiel.spieler.atk
