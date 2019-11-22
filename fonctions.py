import json
import pickle
score = 30
def write(joueur):
    if len(joueur) > 1:
        with open("donnes.py","ab") as fichier:
            ino  = {joueur:score}
            record=pickle.Pickler(fichier)
            print(type(ino))
            record.dump(ino)
            print(ino)
            print(fichier)
            fichier.close()

def recojoueur(joueur):
    with open("donnes.py","rb") as fichier:
        record = pickle.Unpickler(fichier)
        joueur=record.load()
        print(joueur)
        joueur=record.load()
        print(joueur)
