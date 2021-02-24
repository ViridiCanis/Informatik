import pygame
import sys
from pygame.locals import *
import random
import threading

class Spieler(pygame.sprite.Sprite):
    def __init__(self, x, y, züge, spiel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png")
        self.y = y
        self.x = x
        self.bewegung_in_runde = züge
        self.hp = 10
        #self.xp = 0
        self.atk = 5
        self.spiel = spiel

    def update(self, direction):
        x, y = self.x, self.y
        if direction == "^" :
            if self.bewegung_in_runde != 0:
                if self.spiel.level[y-1][x] != "Wand":
                    self.y =self.y - 1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                

        if direction == "v":
            if self.bewegung_in_runde != 0:
                if self.spiel.level[y+1][x] != "Wand":
                    self.y =self.y + 1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                
        
        if direction == "<":
            if self.bewegung_in_runde != 0:
                if self.spiel.level[y][x-1] != "Wand":
                    self.x =self.x -1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
               
        if direction == ">":
            if self.bewegung_in_runde != 0:
                if self.spiel.level[y][x+1] != "Wand":
                    self.x =self.x +1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                

    def __str__(self):
        return "Spieler"
        