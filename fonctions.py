import json
import pickle

score = 30
def write(joueur):
    if len(joueur) > 1:
        with open("donnes.py","a") as f:
            ino = {joueur:score}
            fichier = open("donnes.py","a")
            fichier.write(json.dumps(ino))
            print(ino)
            print(fichier)
            fichier.close()
