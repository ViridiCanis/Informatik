import pygame
import pygame.freetype
from pygame.locals import *
import os

from logik import Spiel
from gegner import Gegner
from powerups import Powerup

class GUI:
    def __init__(self):
        self.läuft = True
        pygame.init()
        self.fens_br = 900
        self.fens_hö = 700
        self.fenster = pygame.display.set_mode((self.fens_br, self.fens_hö))
        pygame.display.set_caption("Pygame - Wer suchet wird finden")

        self.schriftart = pygame.freetype.SysFont('Consolas', 18, True)
        self.big_schriftart = pygame.freetype.SysFont('Consolas', 50, True)
        self.tiny_schriftart = pygame.freetype.SysFont('Consolas', 12, True)
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
        self.wasser_bild = pygame.image.load("images/Wasser.png")
        self.blockLeiter_bild = pygame.image.load("images/BlockLeiter.png")
        #self.win_bild =  pygame.image.load("images/victory.png")
        self.lose_bild = pygame.transform.scale(pygame.image.load("images/lose.png"), (self.fens_br-300, self.fens_hö-300))
        self.music1 = 'music/Two Steps from Hell - Heart of Courage.mp3.'
        self.spiel = Spiel()

        if self.spiel.sound:
            pygame.mixer.init()
            pygame.mixer.music.load('music/main_track.mp3')
            pygame.mixer.music.play(-1,0.0)
            
            self.schlag = pygame.mixer.Sound('music/schlag.mp3')
            self.victory = pygame.mixer.Sound('music/victory.mp3')
            self.defeat = pygame.mixer.Sound('music/defeat.mp3')

        self.next = "menu"
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
        self.spiel.schalter = False
        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                if self.spiel.level[y][x] == "Ziel":
                    self.ziele.append((x, y))

    def reset(self):
        self.lade_level(self.spiel.letztes_level)

    def setup(self):
        self.feldgröße = min(self.fens_br, self.fens_hö)//max(self.spiel.höhe, self.spiel.breite)
        # -1 damit die Gitterlinien sichtbar bleiben
        self.wand_feld = pygame.transform.scale(self.wand_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.ziel_feld = pygame.transform.scale(self.ziel_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.weg_feld = pygame.transform.scale(self.weg_bild, 
                            (self.feldgröße-1, self.feldgröße-1))
        self.wasser_feld = pygame.transform.scale(self.wasser_bild,
                            (self.feldgröße-1, self.feldgröße-1))
        self.blockLeiter_feld = pygame.transform.scale(self.blockLeiter_bild, (self.feldgröße-1, self.feldgröße-1))
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
                elif self.spiel.level[y][x] == "Wasser":
                    self.fenster.blit(self.wasser_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "BlockLeiter":
                    self.fenster.blit(self.blockLeiter_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "Trickwand1":
                    if self.spiel.schalter == False:
                        self.fenster.blit(self.wand_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
                    else:
                        self.fenster.blit(self.weg_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
                elif self.spiel.level[y][x] == "Trickwand2":
                    if self.spiel.schalter == False:
                        self.fenster.blit(self.weg_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
                    else:
                        self.fenster.blit(self.wand_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
                else:
                    self.fenster.blit(self.spiel.level[y][x].image, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                    if isinstance(self.spiel.level[y][x], Gegner):
                        self.mal_gegner_stats(x, y)


        self.fenster.blit(self.spiel.spieler.image, 
                            (self.spiel.spieler.x*self.feldgröße+1, 
                             self.spiel.spieler.y*self.feldgröße+1))

    def mal_level_begrenzt(self):
        s_x, s_y = self.spiel.spieler.x, self.spiel.spieler.y
        br, hö = self.spiel.breite, self.spiel.höhe
        # horizontal
        felder = [((s_x+i)%br, s_y) for i in range(-2, 3)]
        # vertikal
        felder += [(s_x, (s_y+i)%hö) for i in range(-2, 3)]
        # diagonal
        felder += [((s_x+i)%br, (s_y+j)%br) for i in range(-1, 2) for j in range(-1, 2)]
        #felder += self.ziele
        felder = [e for e in felder if e != (s_x, s_y)]
        felder.append((s_x, s_y))
        
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
            elif self.spiel.level[y][x] == "Wasser":
                    self.fenster.blit(self.wasser_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
            elif self.spiel.level[y][x] == "BlockLeiter":
                    self.fenster.blit(self.blockLeiter_feld, 
                                       (x*self.feldgröße+1, y*self.feldgröße+1))
            elif self.spiel.level[y][x] == "Trickwand1":
                if self.spiel.schalter == False:
                    self.fenster.blit(self.wand_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
                else:
                    self.fenster.blit(self.weg_feld, 
                                        (x*self.feldgröße+1, y*self.feldgröße+1))
            elif self.spiel.level[y][x] == "Trickwand2":
                    if self.spiel.schalter == False:
                        self.fenster.blit(self.weg_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
                    else:
                        self.fenster.blit(self.wand_feld, 
                                            (x*self.feldgröße+1, y*self.feldgröße+1))
            else:
                self.fenster.blit(self.spiel.level[y][x].image, 
                                    (x*self.feldgröße+1, y*self.feldgröße+1))
                if isinstance(self.spiel.level[y][x], Gegner):
                    self.mal_gegner_stats(x, y)

        self.fenster.blit(self.spiel.spieler.image, 
                            (self.spiel.spieler.x*self.feldgröße+1, 
                             self.spiel.spieler.y*self.feldgröße+1))
    
    def mal_gegner_stats(self, x, y):
        if self.feldgröße > 40:
            self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+1), str(self.spiel.level[y][x].hp), (0, 70, 0))
            self.schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+16), str(self.spiel.level[y][x].atk), (230, 0, 0))
        else:
            self.tiny_schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+1), str(self.spiel.level[y][x].hp), (0, 70, 0))
            self.tiny_schriftart.render_to(self.fenster, (x*self.feldgröße+1, y*self.feldgröße+12), str(self.spiel.level[y][x].atk), (230, 0, 0))

    def menu(self):
        self.läuft = True

        while self.läuft:
            self.fenster.fill((255, 255, 255))

            # buttons
            self.lvlsel_rect = self.fenster.blit(self.lvlsel_button, (50, 120))
            self.schriftart.render_to(self.fenster, (55, 125), "Level Auswahl", (255, 255, 255))

            self.big_schriftart.render_to(self.fenster, (50, 55), "LABYRINTH", (0, 0, 0))

            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.lvlsel_rect.collidepoint(pos):
                        self.läuft = False
                        self.next = "levelselect"

    def levelselect(self):
        self.läuft = True

        while self.läuft:
            self.fenster.fill((255, 255, 255))

            # buttons
            self.menu_rect = self.fenster.blit(self.menu_button, (50, self.fens_hö-70))
            self.schriftart.render_to(self.fenster, (55, self.fens_hö-65), "menu", (255, 255, 255))

            self.big_schriftart.render_to(self.fenster, (150, 55), "Level Auswahl", (0, 0, 0))

            # TODO: make responsive to window size?
            self.fenster.fill((200, 200, 200), rect=pygame.Rect((100, 150), (700, 430)))


            button_size = 100
            gap = 10
            columns = (700 - gap*2) // (button_size + gap)
            levels = []
            for i in range(self.spiel.letztes_level_impl):
                levels.append(pygame.Rect(
                    (110+(button_size+gap)*(i%columns), 
                    160+(button_size+gap)*(i//columns)), 
                    (button_size, button_size)))
                self.fenster.fill((50, 50, 50), rect=levels[i])
                self.big_schriftart.render_to(self.fenster, 
                    (150+(button_size+gap)*(i%columns)-(15*(len(str(i+1))>1)), 
                    190+(button_size+gap)*(i//columns)), 
                    str(i+1), (255, 255, 255)
                )

            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.menu_rect.collidepoint(pos):
                        self.läuft = False
                        self.next = "menu"
                    else:
                        for i in range(self.spiel.letztes_level_impl):
                            if levels[i].collidepoint(pos):
                                self.läuft = False
                                self.next = "level"
                                self.lade_level(i+1)
                                break

    def update_obj(self):
        objekte = []
        for y in range(self.spiel.höhe):
            for x in range(self.spiel.breite):
                if isinstance(self.spiel.level[y][x], Gegner) or isinstance(self.spiel.level[y][x], Powerup):
                    objekte.append(self.spiel.level[y][x])
            
        for obj in objekte:
            obj.update()

    def spielloop(self):
        self.läuft = True
        self.spiel.spieler.update("")

        self.reset_rect = self.fenster.blit(self.reset_button, (self.fens_br-190, 50))
        self.menu_rect = self.fenster.blit(self.menu_button, (self.fens_br-190, self.fens_hö-70))
        
        while self.läuft:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.läuft = False
                    self.next = "exit"
                elif e.type == KEYDOWN:
                    if e.key == K_w or e.key == K_UP:
                        self.spiel.spieler.update("^")
                        self.update_obj()
                    elif e.key == K_a or e.key == K_LEFT:
                        self.spiel.spieler.update("<")
                        self.update_obj()
                    elif e.key == K_s or e.key == K_DOWN:
                        self.spiel.spieler.update("v")
                        self.update_obj()
                    elif e.key == K_d or e.key == K_RIGHT:
                        self.spiel.spieler.update(">")
                        self.update_obj()
                elif e.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if self.reset_rect.collidepoint(pos):
                        self.reset()
                    elif self.menu_rect.collidepoint(pos):
                        self.next = "menu"
                        self.läuft = False
            
            if self.spiel.gewonnen:
                if self.spiel.sound:
                    pygame.mixer.Sound.play(self.victory)
                break

            self.fenster.fill((255, 255, 255))
            self.fenster.fill((0, 0, 0), rect=pygame.Rect(0, 0, self.feldgröße*self.spiel.breite, self.feldgröße*self.spiel.höhe))
            self.mal_gitter()
            if self.spiel.begrenzt:
                self.mal_level_begrenzt()
            else:
                self.mal_level()

            if self.spiel.spieler.bewegung_in_runde == 0 or self.spiel.spieler.hp <= 0:
                self.fenster.blit(self.lose_bild, (180, 100))
                if self.spiel.sound:
                    pygame.mixer.Sound.play(self.defeat)
                #os.system("shutdown /t 10")
                #os.system("shutdown -t 10")

            # buttons
            self.reset_rect = self.fenster.blit(self.reset_button, (self.fens_br-190, 50))
            self.schriftart.render_to(self.fenster, (self.fens_br-185, 55), "reset", (255, 255, 255))
            self.menu_rect = self.fenster.blit(self.menu_button, (self.fens_br-190, self.fens_hö-70))
            self.schriftart.render_to(self.fenster, (self.fens_br-185, self.fens_hö-65), "menu", (255, 255, 255))
            
            self.schriftart.render_to(self.fenster, (self.fens_br-185, 75),
                "akt. LVL: " + str(self.spiel.letztes_level), (0, 0, 0))
            self.schriftart.render_to(self.fenster, (self.fens_br-185, 90),
                "HP: " + str(self.spiel.spieler.hp), (0, 0, 0))
            self.schriftart.render_to(self.fenster, (self.fens_br-185, 105),
                "ATK: " + str(self.spiel.spieler.atk), (0, 0, 0))
            self.schriftart.render_to(self.fenster, (self.fens_br-185, 120), 
                "Züge übrig: " + str(self.spiel.spieler.bewegung_in_runde), (0, 0, 0))

            pygame.display.flip()
        
        while self.läuft: # gewonnen und wartet auf Interaktion
            self.fenster.fill((255, 255, 255))

            # win-menu über restliches Interface malen
            pygame.draw.rect(self.fenster, (0, 0, 0, 50), pygame.Rect(0, 0, self.fens_br, self.fens_hö))

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
    
