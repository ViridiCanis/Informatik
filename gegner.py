import pygame
import sys
from pygame.locals import *
import random
import threading

class Gegner(pygame.sprite.Sprite):
    def __init__(self, x, y, spiel,):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/gegner2.png")
        self.spiel = spiel
        #spielerkoords
        self.y = y
        self.x = x
        #gegnerkoords
        self.g_y = 0
        self.g_x = 0
        self.bewegung_in_runde = 2
        self.hp = 10
        self.atk = 2


# spieler und gegner koords müssen noch ordentlich importiert werden
    def update(self):
        """
            Fehlermeldungen: x und y sind nicht bekannt
        """
        if self.y > self.g_y:
            if self.spiel.level[y+1][x] != "Wand":
                self.g_y = self.g_y +1
        else:
            if self.spiel.level[y-1][x] != "Wand":
                self.g_y = self.g_y -1

        if self.x > self.g_x:
            if self.spiel.level[y][x+1] != "Wand":
                self.g_x = self.g_x +1
        else:
            if self.spiel.level[y][x-1] != "Wand":
                self.g_x = self.g_x -1


        if abs(self.y-self.g_y) == 1 or abs(self.x-self.g_x) == 1:
            #idk
            self.spiel.spieler.hp = self.spiel.spieler.hp - self.atk
            


            


        
            
            
            
    def __str__(self):
        return "Gegner"
        