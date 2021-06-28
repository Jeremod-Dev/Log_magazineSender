import hashlib
import sqlite3
from sqlite3.dbapi2 import Cursor

def verificationMdp(saisi):
    saisiEncoder = hashlib.md5(saisi.encode())
    connexionBase = sqlite3.connect('data.db')
    curseur = connexionBase.cursor()
    mdp = (saisiEncoder.hexdigest(),)
    try:
        curseur.execute("Select id from User where mdp = ? ", mdp)
        # print(f"L'identifiant de l'utilisateur est: {curseur.fetchone()[0]}")
        id = curseur.fetchone()[0]
        connexionBase.close()
        return id
    except :
        connexionBase.close()
        return -1