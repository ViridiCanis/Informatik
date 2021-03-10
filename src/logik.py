from spieler import Spieler
from gegner import Gegner
from objekt import Objekt
import pygame

class Spiel:
    def __init__(self):
        self.level = []
        self.breite = 0
        self.höhe = 0
        self.gewonnen = False
        self.spieler = ""
        self.letztes_level = 0
        self.letztes_level_impl = 3

    def lade_level(self, level):
        self.gewonnen = False
        self.letztes_level = level
        levelDatei = "level" + str(level)
        self.level = []
        with open("level/{}".format(levelDatei), "r") as datei:
            text = datei.read()
            datei.close()
        text = text.split("\n")
        self.breite, self.höhe, züge, self.begrenzt = [int(x) for x in text[0].split(" ")]
        self.begrenzt = self.begrenzt == 1
        level = [zeile.split(" ") for zeile in text[1:]]
        gid = 0
        for y in range(self.höhe):
            zeile = []
            for x in range(self.breite):
                if level[y][x] == "W":
                    zeile.append("Wand")
                elif level[y][x] == "S":
                    self.spieler = Spieler(x, y, züge, self)
                    zeile.append("")
                elif level[y][x] == "Z":
                    zeile.append("Ziel")
                elif level[y][x] == "G":
                    zeile.append(Gegner(x, y, self, id=gid))
                    gid += 1
                else:
                    zeile.append("")
            self.level.append(zeile)
    
    def setup_felder(self): # für alles was Zugriff auf andere Objekte braucht
        for y in range(self.höhe):
            for x in range(self.breite):
                if not isinstance(self.level[y][x], str):
                    self.level[y][x].setup()

