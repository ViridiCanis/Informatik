from spieler import Spieler
from gegner import Gegner
import pygame
import powerups

class Spiel:
    def __init__(self):
        self.sound = False
        self.level = []
        self.breite = 0
        self.höhe = 0
        self.gewonnen = False
        self.spieler = ""
        self.letztes_level = 0
        self.letztes_level_impl = 18
        self.schalter = False

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
        #if self.schalter == True
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
                    zeile.append(Gegner(x, y, 10, 2, self))
                elif level[y][x] == "g":
                    zeile.append(Gegner(x, y, 80, 1, self, boss=True))
                elif level[y][x] == "w":
                    zeile.append("Wasser")
                elif level[y][x] == "b":
                    zeile.append("BlockLeiter")
                elif level[y][x] == "s":
                    zeile.append(powerups.Schalter((x, y), self))
                elif level[y][x] == "n":
                    zeile.append("Trickwand1")
                elif level[y][x] == "N":
                    zeile.append("Trickwand2")
                elif level[y][x] == "H":
                    zeile.append(powerups.Heal((x, y), self))
                elif level[y][x] == "P":
                    zeile.append(powerups.Poison((x, y), self))
                elif level[y][x] == "A":
                    zeile.append(powerups.Attack((x, y), self))
                else:
                    zeile.append("")
            self.level.append(zeile)
    
    def setup_felder(self): # für alles was Zugriff auf andere Objekte braucht
        for y in range(self.höhe):
            for x in range(self.breite):
                if not isinstance(self.level[y][x], str):
                    self.level[y][x].setup()

