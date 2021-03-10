import pygame
import pygame.freetype
from pygame.locals import *
# import os

from logik import Spiel
from gegner import Gegner

class GUI:
    def __init__(self):
        self.läuft = True
        pygame.init()
        self.fenster = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Pygame - tooolles Spiel")

        self.schriftart = pygame.freetype.SysFont('Consolas', 18, True)
        self.big_schriftart = pygame.freetype.SysFont('Consolas', 50, True)
        self.reset_button = pygame.Surface((95, 20))
        self.reset_button.fill((50, 50, 50))
        self.next_button = pygame.Surface((160, 20))
        self.next_button.fill((50, 50, 50))
        self.lvlsel_button = pygame.Surface((150, 20))
        self.lvlsel_button.fill((50, 50, 50))
        self.lvl_button = pygame.Surface((30, 30))
        self.lvl_button.fill((50, 50, 50))
        self.menu_button = pygame.Surface((70, 20))
        self.menu_button.fill((50, 50, 50))

        self.wand_bild = pygame.image.load("images/wand.png")
        self.weg_bild = pygame.image.load("images/weg.png")
        self.ziel_bild = pygame.image.load("images/Ziel.png")
        #self.win_bild =  pygame.image.load("images/victory.png")
        #self.lose_bild = pygame.image.load("images/lose.png")
        self.spiel = Spiel()

        self.next = "menu"
        self.lade_level(1)
        while self.next != "exit":
            if self.next == "level":
                self.spielloop()
            elif self.next == "menu":
                self.menu()
            elif self.next == "levelselect":
                self.levelselect()
    
    def lade_level(self, level):
        self.spiel.lade_level(level)
        self.setup()
        self.spiel.setup_felder()
        self.ziele = []
        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                if self.spiel.level[y][x] == "Ziel":
                    self.ziele.append((x, y))

    def reset(self):
        self.spiel.lade_level(self.spiel.letztes_level)
        self.setup()

    def setup(self):
        self.feldgröße = 700//max(self.spiel.höhe, self.spiel.breite)
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
                    if isinstance(self.spiel.level[y][x], Gegner):
                        self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+1), str(self.spiel.level[y][x].id), (0, 0, 0))
                        self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+16), str(self.spiel.level[y][x].hp), (0, 200, 0))
                        self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+31), str(self.spiel.level[y][x].atk), (255, 0, 0))

        self.fenster.blit(self.spiel.spieler.image, 
                            (self.spiel.spieler.x*self.feldgröße+1, 
                             self.spiel.spieler.y*self.feldgröße+1))

    def mal_level_begrenzt(self):
        s_x, s_y = self.spiel.spieler.x, self.spiel.spieler.y
        br, hö = self.spiel.breite, self.spiel.höhe
        felder = [
            (s_x, s_y),
            ((s_x-1)%br, s_y),
            ((s_x+1)%br, s_y),
            (s_x, (s_y-1)%hö),
            (s_x, (s_y+1)%hö)
        ] + self.ziele
        
        for feld in felder:
            # +1 zum Zentrieren im Feld, damit die Gitterlinien sichtbar bleiben
            x, y = feld
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
                if isinstance(self.spiel.level[y][x], Gegner):
                    self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+1), str(self.spiel.level[y][x].id), (0, 0, 0))
                    self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+16), str(self.spiel.level[y][x].hp), (0, 200, 0))
                    self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+31), str(self.spiel.level[y][x].atk), (255, 0, 0))

        self.fenster.blit(self.spiel.spieler.image, 
                            (self.spiel.spieler.x*self.feldgröße+1, 
                             self.spiel.spieler.y*self.feldgröße+1))

    def menu(self):
        self.läuft = True
        while self.läuft:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.lvlsel_rect.collidepoint(pos):
                        self.läuft = False
                        self.next = "levelselect"

            self.fenster.fill((255, 255, 255))

            # buttons
            self.lvlsel_rect = self.fenster.blit(self.lvlsel_button, (50, 120))
            self.schriftart.render_to(self.fenster, (55, 125), "Level Auswahl", (255, 255, 255))

            self.big_schriftart.render_to(self.fenster, (50, 55), "SUPER SPIEL", (0, 0, 0))

            pygame.display.flip()
    
    def levelselect(self):
        self.läuft = True
        while not self.spiel.gewonnen and self.läuft:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.menu_rect.collidepoint(pos):
                        self.läuft = False
                        self.next = "menu"

            self.fenster.fill((255, 255, 255))

            self.fenster.fill((200, 200, 200), rect=pygame.Rect((100, 150), (700, 430)))
            # buttons
            self.menu_rect = self.fenster.blit(self.menu_button, (50, 630))
            self.schriftart.render_to(self.fenster, (55, 635), "menu", (255, 255, 255))

            self.big_schriftart.render_to(self.fenster, (150, 55), "Level Auswahl", (0, 0, 0))

            pygame.display.flip()

    def update_gegner(self):
        gegner = []
        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                if isinstance(self.spiel.level[y][x], Gegner):
                    gegner.append(self.spiel.level[y][x])
            
        for geg in gegner:
            geg.update()

    def spielloop(self):
        self.läuft = True     
        while not self.spiel.gewonnen and self.läuft:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == KEYDOWN:
                    if e.key == K_w or e.key == K_UP:
                        self.spiel.spieler.update("^")
                        self.update_gegner()
                    elif e.key == K_a or e.key == K_LEFT:
                        self.spiel.spieler.update("<")
                        self.update_gegner()
                    elif e.key == K_s or e.key == K_DOWN:
                        self.spiel.spieler.update("v")
                        self.update_gegner()
                    elif e.key == K_d or e.key == K_RIGHT:
                        self.spiel.spieler.update(">")
                        self.update_gegner()
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.reset_rect.collidepoint(pos):
                        self.reset()
                    elif self.menu_rect.collidepoint(pos):
                        self.next = "menu"
                        self.läuft = False

            self.fenster.fill((255, 255, 255))
            self.fenster.fill((0, 0, 0), rect=pygame.Rect(0, 0, self.feldgröße*self.spiel.breite, self.feldgröße*self.spiel.höhe))
            self.mal_gitter()
            if self.spiel.begrenzt:
                self.mal_level_begrenzt()
            else:
                self.mal_level()

            if self.spiel.spieler.bewegung_in_runde == 0:
                self.big_schriftart.render_to(self.fenster, (100, 100), "keine", (255, 200, 200))
                self.big_schriftart.render_to(self.fenster, (100, 150), "Züge übrig", (255, 200, 200))

            # buttons
            self.reset_rect = self.fenster.blit(self.reset_button, (710, 50))
            self.schriftart.render_to(self.fenster, (715, 55), "reset", (255, 255, 255))
            self.menu_rect = self.fenster.blit(self.menu_button, (710, 630))
            self.schriftart.render_to(self.fenster, (715, 635), "menu", (255, 255, 255))

            self.schriftart.render_to(self.fenster, (715, 75), 
                "Züge übrig: " + str(self.spiel.spieler.bewegung_in_runde), (255, 0, 0))
            self.schriftart.render_to(self.fenster, (715, 90),
                "HP: " + str(self.spiel.spieler.hp), (255, 0, 0))
            self.schriftart.render_to(self.fenster, (715, 105),
                "ATK: " + str(self.spiel.spieler.atk), (255, 0, 0))

            pygame.display.flip()
        
        while self.läuft: # gewonnen und wartet auf Interaktion
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.reset_rect.collidepoint(pos):
                        self.reset()
                        self.läuft = False
                    elif self.spiel.letztes_level < self.spiel.letztes_level_impl and self.next_rect.collidepoint(pos):
                        self.lade_level(self.spiel.letztes_level+1)
                        self.läuft = False
                    elif self.menu_rect.collidepoint(pos):
                        self.next = "menu"
                        self.läuft = False
            self.fenster.fill((255, 255, 255))

            # win-menu über restliches Interface malen
            pygame.draw.rect(self.fenster, (0, 0, 0, 50), pygame.Rect(0, 0, 700, 700))

            self.schriftart.render_to(self.fenster, (250, 300), "Level geschafft", (255, 255, 255))

            # buttons
            if self.spiel.letztes_level < self.spiel.letztes_level_impl:
                self.next_rect = self.fenster.blit(self.next_button, (170, 400))
                self.schriftart.render_to(self.fenster, (175, 405), "Nächstes Level", (255, 255, 255))
                self.reset_rect = self.fenster.blit(self.reset_button, (380, 400))
                self.schriftart.render_to(self.fenster, (385, 405), "neustart", (255, 255, 255))
            else:
                self.reset_rect = self.fenster.blit(self.reset_button, (290, 400))
                self.schriftart.render_to(self.fenster, (295, 405), "neustart", (255, 255, 255))

            self.menu_rect = self.fenster.blit(self.menu_button, (290, 450))
            self.schriftart.render_to(self.fenster, (295, 455), "menu", (255, 255, 255))

            pygame.display.flip()
