from spieler import Spieler
from gegner import Gegner
from objekt import Objekt
import pygame

class Spiel:
    def __init__(self):
        self.level = []
        self.breite = 0
        self.höhe = 0
        self.spieler = ""

    def lade_level(self, levelDatei):
        self.level = []
        with open("level/{}".format(levelDatei), "r") as datei:
            text = datei.read()
            datei.close()
        text = text.split("\n")
        self.breite, self.höhe, züge = [int(x) for x in text[0].split(" ")]
        level = [zeile.split(" ") for zeile in text[1:]]
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
                    zeile.append(Gegner(x, y, self))
                else:
                    zeile.append("")
            self.level.append(zeile)
    """
    def level_win(self, Spieler):
        if Spieler.y == Ziel.y:
             return True
    """         


    
