import hashlib
import sqlite3
from tkinter import filedialog



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
    return requeteSQL(requete)

def getTemplatePath(): 
    filename = filedialog.askopenfilename(initialdir = ".",title = "Selectionnez votre template template",filetypes = [("Log_Magazine Template", "*.html")]) 
    return filename

def getNameById(id):
    requete = "Select name from User where id = '"+ str(id)+"'"
    return requeteSQL(requete)

def generatorTemplate(fichier, url, text):
    chaine = ""
    with open(fichier, "r") as fic:
        lines = fic.readlines()
    
    for line in lines:
        chaine += line
    chaineCompleter = chaine.format(url, text)
    with open("4050af11e3cede12a7c250b5f50fcd1c.html", encoding='utf-8', mode='w') as fic2:
        fic2.write(chaineCompleter)

def getTemplate():
    with open("4050af11e3cede12a7c250b5f50fcd1c.html", encoding='utf-8', mode='r') as fic2:
        lines = fic2.readlines()
        chaine = ""
        for line in lines:
            chaine += line
        return chaine