import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, pos, spiel, bild):
        pygame.sprite.Sprite.__init__(self)
        self.image = bild
        self.spiel = spiel
        self.pos = pos

    def activate(self):
        pass

    def update(self):
        pass