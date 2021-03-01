import pygame
import sys
from pygame.locals import *
import random
import threading

class Gegner(pygame.sprite.Sprite):
    def __init__(self,g_x,g_y,spiel,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/gegner2.png")
        self.spiel = spiel

        #gegnerkoords
        self.g_y = g_y
        self.g_x = g_x
        self.bewegung_in_runde = 2
        self.hp = 10
        self.atk = 2
    
    def setup(self):
        #spielerkoords
        self.y = self.spiel.spieler.y
        self.x = self.spiel.spieler.x


# spieler und gegner koords müssen noch ordentlich importiert werden
    def update(self):
        if self.hp < 1:
            self.spiel.level[g_y][g_x] = ""
    
        if self.y > self.g_y:
            if self.spiel.level[g_y+1][g_x] != "Wand":
                self.g_y = self.g_y +1
        else:
            if self.spiel.level[g_y-1][g_x] != "Wand":
                self.g_y = self.g_y -1

        if self.x > self.g_x:
            if self.spiel.level[g_y][g_x+1] != "Wand":
                self.g_x = self.g_x +1
        else:
            if self.spiel.level[g_y][g_x-1] != "Wand":
                self.g_x = self.g_x -1


        if abs(self.y-self.g_y) == 1 or abs(self.x-self.g_x) == 1:
            #idk
            spiel.spieler.hp = spiel.spieler.hp - self.atk

