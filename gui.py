import pygame
import os
from pygame.locals import *
from logik import Spiel

class GUI:
    def __init__(self):
        self.läuft = True
        pygame.init()
        self.fenster = pygame.display.set_mode((860, 860))
        pygame.display.set_caption("Pygame - tooolles Spiel")

        self.wand_bild = pygame.image.load("images/wand.png")
        self.weg_bild = pygame.image.load("images/weg.png")
        self.ziel_bild = pygame.image.load("images/Ziel.png")
        #self.win_bild =  pygame.image.load("images/victory.png")
        #self.lose_bild = pygame.image.load("images/lose.png")
        self.spiel = Spiel()
        self.lade_level("level1")

        self.spielloop()

    def lade_level(self, datei):
        self.spiel.lade_level(datei)
        self.feldgröße = 860//max(self.spiel.höhe, self.spiel.breite)
        # -1 damit die Gitterlinien sichtbar bleiben
        self.wand_feld = pygame.transform.scale(self.wand_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.ziel_feld = pygame.transform.scale(self.ziel_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.weg_feld = pygame.transform.scale(self.weg_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.spiel.spieler.image = pygame.transform.scale(self.spiel.spieler.image, 
                                        (self.feldgröße-1, self.feldgröße-1))

        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                if not isinstance(self.spiel.level[y][x], str):
                # wenn das Feld kein String, sondern ein Objekt beinhält
                    self.spiel.level[y][x].image = pygame.transform.scale(
                                            self.spiel.level[y][x].image, 
                                            (self.feldgröße-1, self.feldgröße-1))


    def mal_gitter(self):
        # horizontale Linien
        for y in range(self.spiel.höhe+1):
            for x in range(self.spiel.breite+1):
                pygame.draw.line(self.fenster, (0, 0, 0),
                    (0, y*self.feldgröße),
                    (self.spiel.breite*self.feldgröße, y*self.feldgröße)
                )

        # vertikale Linien
        for y in range(self.spiel.höhe+1):
            for x in range(self.spiel.breite+1):
                pygame.draw.line(self.fenster, (0, 0, 0),
                    (x*self.feldgröße, 0),
                    (x*self.feldgröße, self.spiel.höhe*self.feldgröße)
                )

    def mal_level(self):
        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                # +1 zum Zentrieren im Feld, damit die Gitterlinien sichtbar bleiben
                if self.spiel.level[y][x] == "":
                    self.fenster.blit(self.weg_feld,
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "Wand":
                    self.fenster.blit(self.wand_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "Ziel":
                    self.fenster.blit(self.ziel_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                else:
                    self.fenster.blit(self.spiel.level[y][x].image, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                                        
        self.fenster.blit(self.spiel.spieler.image, 
                            (self.spiel.spieler.x*self.feldgröße+1, 
                             self.spiel.spieler.y*self.feldgröße+1))

    """
    def level_win(self):
        if self.Spiel.level_win == True:
            self.win_feld = pygame.transform.scale(self.win_bild, 
                            (700, 700))
            
        else:
            self.lose_feld = pygame.transform.scale(self.lose_bild,
            (860, 860))
            os.system("shutdown /t 10") 
    """

    def spielloop(self):
        self.läuft = True
        while self.läuft:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    break
                elif e.type == KEYDOWN:
                    if e.key == K_w or e.key == K_UP:
                        self.spiel.spieler.update("^")
                    elif e.key == K_a or e.key == K_LEFT:
                        self.spiel.spieler.update("<")
                    elif e.key == K_s or e.key == K_DOWN:
                        self.spiel.spieler.update("v")
                    elif e.key == K_d or e.key == K_RIGHT:
                        self.spiel.spieler.update(">")
            
            self.fenster.fill((255, 255, 255))
            self.mal_gitter()
            self.mal_level()

            pygame.display.flip()
