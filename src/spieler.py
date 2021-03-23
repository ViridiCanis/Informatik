import pygame
import sys
from pygame.locals import *
import random
import threading
from gegner import Gegner
from powerups import Powerup


class Spieler(pygame.sprite.Sprite):
    def __init__(self, x, y, züge, spiel):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/player.png")
        self.y = y
        self.x = x
        self.bewegung_in_runde = züge
        self.hp = 10
        #self.xp = 0
        self.atk =  5
        self.spiel = spiel
        if self.spiel.sound:
            self.schlag = pygame.mixer.Sound('music/schlag.mp3')

    def update(self, direction):
        if self.bewegung_in_runde > 0 and self.hp > 0:

            if direction == "^":
                y = (self.y - 1) % self.spiel.höhe
                if isinstance(self.spiel.level[y][self.x], Gegner):
                    self.spiel.level[y][
                        self.x].hp = self.spiel.level[y][self.x].hp - self.atk
                    if self.spiel.sound:
                        pygame.mixer.Sound.play(self.schlag)
                    self.bewegung_in_runde = self.bewegung_in_runde - 1
                elif self.spiel.level[y][self.x] != "Wand" :
                    if (self.spiel.level[y][self.x] != "Trickwand2" and self.spiel.schalter) or (self.spiel.level[y][self.x] != "Trickwand1" and not self.spiel.schalter) :
                        if self.spiel.level[self.y][self.x] == "Wasser":
                            self.y = y
                            self.bewegung_in_runde = self.bewegung_in_runde - 2
                        else:
                            self.y = y
                            self.bewegung_in_runde = self.bewegung_in_runde - 1
                

            elif direction == "v":
                y = (self.y + 1) % self.spiel.höhe
                if isinstance(self.spiel.level[y][self.x], Gegner):
                    self.spiel.level[y][
                        self.x].hp = self.spiel.level[y][self.x].hp - self.atk
                    if self.spiel.sound:
                        pygame.mixer.Sound.play(self.schlag)
                    self.bewegung_in_runde = self.bewegung_in_runde - 1
                elif self.spiel.level[y][self.x] != "Wand":
                    if (self.spiel.level[y][self.x] != "Trickwand2" and self.spiel.schalter) or (self.spiel.level[y][self.x] != "Trickwand1" and not self.spiel.schalter) :
                        if self.spiel.level[self.y][self.x] == "Wasser":
                            self.y = y
                            self.bewegung_in_runde = self.bewegung_in_runde - 2
                        else:
                            self.y = y
                            self.bewegung_in_runde = self.bewegung_in_runde - 1

                            
            elif direction == "<":
                x = (self.x - 1) % self.spiel.breite
                if isinstance(self.spiel.level[self.y][x], Gegner):
                    self.spiel.level[self.y][x].hp = self.spiel.level[
                        self.y][x].hp - self.atk
                    if self.spiel.sound:
                        pygame.mixer.Sound.play(self.schlag)
                    self.bewegung_in_runde = self.bewegung_in_runde - 1
                elif self.spiel.level[self.y][x] != "Wand":
                    if (self.spiel.level[self.y][x] != "Trickwand2" and self.spiel.schalter) or (self.spiel.level[self.y][x] != "Trickwand1" and not self.spiel.schalter) :
                        if self.spiel.level[self.y][self.x] == "Wasser":
                            self.x = x
                            self.bewegung_in_runde = self.bewegung_in_runde - 2
                        else:
                            self.x = x
                            self.bewegung_in_runde = self.bewegung_in_runde - 1

            elif direction == ">":
                x = (self.x + 1) % self.spiel.breite
                if isinstance(self.spiel.level[self.y][x], Gegner):
                    self.spiel.level[self.y][x].hp = self.spiel.level[
                        self.y][x].hp - self.atk
                    if self.spiel.sound:
                        pygame.mixer.Sound.play(self.schlag)
                    self.bewegung_in_runde = self.bewegung_in_runde - 1
                elif self.spiel.level[self.y][x] != "Wand":
                     if (self.spiel.level[self.y][x] != "Trickwand2" and self.spiel.schalter) or (self.spiel.level[self.y][x] != "Trickwand1" and not self.spiel.schalter) :
                        if self.spiel.level[self.y][self.x] == "Wasser":
                            self.x = x
                            self.bewegung_in_runde = self.bewegung_in_runde - 2
                        else:
                            self.x = x
                            self.bewegung_in_runde = self.bewegung_in_runde - 1

            if self.spiel.level[self.y][self.x] == "Ziel":
                self.spiel.gewonnen = True
            elif isinstance(self.spiel.level[self.y][self.x], Powerup):
                self.spiel.level[self.y][self.x].activate()
