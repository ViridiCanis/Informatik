import pygame
import sys
from pygame.locals import *
import random
import threading

class Spieler(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
        self.bewegung = 2
        self.hp = 10
        self.xp = 0
        self.atk = 5

        def update(self):
            pressed = pygame.key.get_pressed()
            up = pressed[K_UP]
            left = pressed[K_LEFT]
            right = pressed[K_RIGHT]
            down = pressed[K_DOWN]

            if up :
                if bewegung != 0:
                    if y != 15:
                        self.y =self.y +1
                        bewegung = bewegung-1

            if down:
                if bewegung != 0:
                    if y != 0:
                        self.y =self.y-1
                        bewegung = bewegung-1
            
            if left:
                if bewegung != 0:
                    if x != 0:
                        self.x =self.x -1
                        bewegung = bewegung-1
            
            if right:
                if bewegung != 0:
                    if x != 15:
                        self.x =self.x +1
                        bewegung = bewegung-1
