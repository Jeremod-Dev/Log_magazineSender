import hashlib
import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter import filedialog
import time



def requeteSQL(requete):
    connexionBase = sqlite3.connect('data.db')
    curseur = connexionBase.cursor()
    try:
        curseur.execute(requete)
        resultat = curseur.fetchone()[0]
        connexionBase.close()
        return resultat
    except :
        connexionBase.close()
        return -1

def getId(saisi):
    saisiEncoder = hashlib.md5(saisi.encode())
    requete = "Select id from User where mdp = '"+ str(saisiEncoder.hexdigest())+"'"
    print(requete)
    return requeteSQL(requete)

def getTemplatePath(): 
    filename = filedialog.askopenfilename(initialdir = ".",title = "Selectionnez votre template template",filetypes = [("Log_Magazine Template", "*.html")]) 
    print(filename)
    return filename

def getNameById(id):
    requete = "Select name from User where id = '"+ str(id)+"'"
    print(requete)
    return requeteSQL(requete)

def generatorTemplate(fichier, url, text):
    chaine = ""
    print(url, text)
    with open(fichier, "r") as fic:
        lines = fic.readlines()
    
    for line in lines:
        chaine += line
    chaineCompleter = chaine.format(url, text)
    print(chaineCompleter)
    with open("4050af11e3cede12a7c250b5f50fcd1c.html", encoding='utf-8', mode='w') as fic2:
        fic2.write(chaineCompleter)