from spieler import Spieler
# from gegner import Gegner
from objekt import Objekt
import pygame

class Spiel:
    def __init__(self):
        self.level = []
        self.breite = 0
        self.höhe = 0
        self.spieler_pos = (0, 0)

    def lade_level(self, levelDatei):
        self.level = []
        with open("level/{}".format(levelDatei), "r") as datei:
            text = datei.read()
            datei.close()
        text = text.split("\n")
        self.breite, self.höhe = [int(x) for x in text[0].split(" ")]
        level = [zeile.split(" ") for zeile in text[1:]]
        print(self.höhe, self.breite)
        print(len(level), len(level[1]))
        for y in range(self.höhe):
            zeile = []
            for x in range(self.breite):
                if level[y][x] == "W":
                    zeile.append("Wand")
                elif level[y][x] == "S":
                    zeile.append(Spieler(x, y))
                    self.spieler_pos = (x, y)
                elif level[y][x] == "Z":
                    zeile.append("Ziel")
                else:
                    zeile.append("")
            self.level.append(zeile)
    
    def spieler_bewegt(self):
        while self.level != []:
            if spieler.up:
                if self.level[spieler.y + 1][spieler.x] == "W":
                    print ("Durch Wand ist dämlich")
                elif self.level[spieler.y + 1][spieler.x] == "Z":
                    self.level[spieler.y + 1][spieler.x]
                    print ("Ziel erreicht") 
                else:
                    self.level[spieler.y + 1][spieler.x]
            elif spieler.down:
                if self.level[spieler.y - 1][spieler.x] == "W":
                    print ("Durch Wand ist dämlich")
                elif self.level[spieler.y - 1][spieler.x] == "Z":
                    self.level[spieler.y - 1][spieler.x]
                    print ("Ziel erreicht") 
                else:
                    self.level[spieler.y - 1][spieler.x]
            elif spieler.right:
                if self.level[spieler.y][spieler.x + 1] == "W":
                    print ("Durch Wand ist dämlich")
                elif self.level[spieler.y][spieler.x + 1] == "Z":
                    self.level[spieler.y][spieler.x + 1]
                    print ("Ziel erreicht") 
                else:
                    self.level[spieler.y][spieler.x + 1]
            else:
                if self.level[spieler.y][spieler.x - 1] == "W":
                    print ("Durch Wand ist dämlich")
                elif self.level[spieler.y][spieler.x - 1] == "Z":
                    self.level[spieler.y][spieler.x - 1]
                    print ("Ziel erreicht") 
                else:
                    self.level[spieler.y][spieler.x - 1]

  