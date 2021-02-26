import pygame
import sys
from pygame.locals import *
import random
import threading
from gegner import Gegner

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
        if self.bewegung_in_runde != 0:

            if direction == "^" :
                if isinstance(self.spiel.level[y-1][x], Gegner):
                    self.spiel.level[y-1][x].hp = self.spiel.level[y-1][x].hp - self.atk
                elif self.spiel.level[y-1][x] != "Wand":
                    self.y =self.y - 1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                    if self.spiel.level[y][x] == "Ziel":
                      self.spiel.gewonnen = True
                    

            if direction == "v":
                if isinstance(self.spiel.level[y+1][x], Gegner):
                    self.spiel.level[y+1][x].hp = self.spiel.level[y+1][x].hp - self.atk
                elif self.spiel.level[y+1][x] != "Wand":
                    self.y =self.y + 1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                    if self.spiel.level[y][x] == "Ziel":
                        self.spiel.gewonnen = True
                    
            
            if direction == "<":
                if isinstance(self.spiel.level[y][x-1], Gegner):
                    self.spiel.level[y][x-1].hp = self.spiel.level[y][x-1].hp - self.atk
                elif self.spiel.level[y][x-1] != "Wand":
                    self.x =self.x -1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                    if self.spiel.level[y][x] == "Ziel":
                        self.spiel.gewonnen = True
                  
            if direction == ">":
                if isinstance(self.spiel.level[y][x+1], Gegner):
                    self.spiel.level[y][x+1].hp = self.spiel.level[y][x+1].hp - self.atk
                elif self.spiel.level[y][x+1] != "Wand":
                    self.x =self.x +1
                    self.bewegung_in_runde = self.bewegung_in_runde-1
                    if self.spiel.level[y][x] == "Ziel":
                        self.spiel.gewonnen = True
        else:   
            print("keine Züge übrig")
                

    def __str__(self):
        return "Spieler"
        