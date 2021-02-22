import pygame
from logik import Spiel

class GUI:
    def __init__(self):
        self.läuft = True
        pygame.init()
        self.fenster = pygame.display.set_mode((1100, 860))
        pygame.display.set_caption("tolles Spiel")

        self.wand_bild = pygame.image.load("images/wand.png")
        self.ziel_bild = pygame.image.load("images/ziel.png")
        self.spiel = Spiel()
        self.lade_level("level1")

        self.loop()

    def lade_level(self, datei):
        self.spiel.lade_level(datei)
        self.feldgröße = 860//max(self.spiel.höhe, self.spiel.breite)
        # -1 damit die Gitterlinien sichtbar bleiben
        self.wand_feld = pygame.transform.scale(self.wand_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.ziel_feld = pygame.transform.scale(self.ziel_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        (sx, sy) = self.spiel.spieler_pos
        self.spiel.level[sy][sx].image = pygame.transform.scale(self.spiel.level[sy][sx].image, 
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
                if self.spiel.level[y][x] == "":
                    pass
                elif self.spiel.level[y][x] == "Wand":
                # +1 zum Zentrieren im Feld, damit die Gitterlinien sichtbar bleiben
                    self.fenster.blit(self.wand_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "Ziel":
                    self.fenster.blit(self.ziel_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                else:
                    self.fenster.blit(self.spiel.level[y][x].image, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))


    def loop(self):
        while self.läuft:
            for ereignis in pygame.event.get():
                if ereignis.type == pygame.QUIT:
                    self.läuft = False
                    break
            
            self.fenster.fill((250, 250, 250))
            self.mal_gitter()
            self.mal_level()

            pygame.display.flip()
