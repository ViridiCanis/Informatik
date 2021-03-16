import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, pos, spiel, bilddatei):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/{}".format(bilddatei))
        self.spiel = spiel
        self.pos = pos

    def activate(self):
        pass

    def update(self):
        pass