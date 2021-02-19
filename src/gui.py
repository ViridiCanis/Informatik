import pygame
import os

from logik import Spiel

class GUI:
    def __init__(self):
        pygame.init()
        fenster = pygame.display.set_mode((800, 600))
        fenster.fill((50, 50, 50))
        pygame.display.flip()
        input()

