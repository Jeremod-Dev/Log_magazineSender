import hashlib
import sqlite3
from tkinter import filedialog

##############################
# fonction permettant de faire une requete SQL
# Entree: requete
# Sortie: reponse de la requete
##############################
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

##############################
# fonction permettant de recupérer l'ID depuis un mdp
# Entree: mot de passe
# Sortie: ID de l'utilisateur
##############################
def getId(saisi):
    saisiEncoder = hashlib.md5(saisi.encode())
    requete = "Select id from User where mdp = '"+ str(saisiEncoder.hexdigest())+"'"
    return requeteSQL(requete)


##############################
# fonction permettant d'ouvrir une boite de dialogue permettant de choisir le template
# Entree: VIDE
# Sortie: PATH vers le fichier
##############################
def getTemplatePath(): 
    filename = filedialog.askopenfilename(initialdir = ".",title = "Selectionnez votre template template",filetypes = [("Log_Magazine Template", "*.html")]) 
    return filename

##############################
# fonction permettant de recuperer un nom d'utilisateur avec un ID
# Entree: ID
# Sortie: nom d'utilisateur
##############################
def getNameById(id):
    requete = "Select name from User where id = '"+ str(id)+"'"
    return requeteSQL(requete)

##############################
# fonction qui genere le template
# Entree: PATH du template originel, URL PDF, TEXTE a inserer
# Sortie: fichier HTML avec url et texte
##############################
def generatorTemplate(fichier, url, text):
    chaine = ""
    with open(fichier, "r") as fic:
        lines = fic.readlines()
    
    for line in lines:
        chaine += line
    chaineCompleter = chaine.format(url, text)
    with open("4050af11e3cede12a7c250b5f50fcd1c.html", encoding='utf-8', mode='w') as fic2:
        fic2.write(chaineCompleter)


##############################
# fonction permettant de recuperer le code du template d'utilisation
# Entree: VIDE
# Sortie: chaine de caractères
##############################
def getTemplate():
    with open("4050af11e3cede12a7c250b5f50fcd1c.html", encoding='utf-8', mode='r') as fic2:
        lines = fic2.readlines()
        chaine = ""
        for line in lines:
            chaine += line
        return chaine