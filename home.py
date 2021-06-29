from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import os
import constante as const
import enginer
import pyperclip
import time

class Application:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title(const.TITRE)
        self.fenetre.geometry(str(const.ECRAN_X) +"x"+ str(const.ECRAN_Y) +"+150+100")
        self.fenetre.resizable(False, False)
        self.fenetre.config(background=const.FOND)
        self.fenetre.iconbitmap("logo.ico")
        self.idUser = -1

        # Page de connexion
        self.fontTitre = ("Arial",30,"bold")
        self.homePageZone = Frame(self.fenetre, background=const.FOND,width=const.ECRAN_X, height=const.ECRAN_Y)
        self.lbLogMagazine = ttk.Label(self.homePageZone, text="LOG_MAGAZINE",foreground=const.MAJENTA,background=const.FOND, font=self.fontTitre)
        self.eMdp = Entry(self.homePageZone, show="*")
        self.ErreurMdp = ttk.Label(self.homePageZone, foreground="red", background=const.FOND)

        # Page de template
        self.fontClassique = ("Arial",11)
        self.createurPageZone = Frame(self.fenetre, background=const.FOND,width=const.ECRAN_X, height=const.ECRAN_Y)
        self.lbLogMagazineCreateur = ttk.Label(self.createurPageZone, text="LOG_MAGAZINE",foreground=const.MAJENTA,background=const.FOND, font=self.fontTitre)
        self.lbPathTemplate = ttk.Label(self.createurPageZone,foreground=const.MAJENTA,background=const.FOND)
        self.path = str()
        self.lbUtilisateur = ttk.Label(self.createurPageZone)
        self.ErreurTemplate = ttk.Label(self.createurPageZone, foreground="red", background=const.FOND)

    def verificationMdp(self):
        if (self.verificationExistenceMdp()):
            self.ErreurMdp.config(text="")
            self.createurPage()
        else:
            self.ErreurMdp.config(text="Mot de passe incorrect")
            self.ErreurMdp.place(x=const.ECRAN_X/2-50, y=220)

    def verificationExistenceMdp(self):
        self.idUser = enginer.getId(self.eMdp.get())
        return self.idUser !=-1

    def homePage(self):
        self.lbLogMagazine.place(x=const.ECRAN_X/2-150, y=150)
        self.homePageZone.place(x=0,y=0)
        self.eMdp.place(x=const.ECRAN_X/2, y=250)
        lbMdp = ttk.Label(self.homePageZone, text="Mot de Passe",foreground="black",background=const.FOND, font=self.fontClassique)
        lbMdp.place(x=const.ECRAN_X/2-120, y=250)
        self.eMdp.config(font=self.fontClassique)
        btnValider = Button(self.homePageZone, text="Connexion",foreground=const.MAJENTA, background="white", width=25, command=self.verificationMdp)
        btnValider.place(x=542 ,y=372)
        btnVersion = Button(self.homePageZone, text=const.SOUSTITRE+" - "+const.VERSION,foreground=const.MAJENTA, background=const.FOND, width=25,relief=FLAT, command=self.detailApp)
        btnVersion.place(x=10 ,y=const.ECRAN_Y-30)
        

        self.fenetre.mainloop()

    def getTemplate(self):
        self.path = str(enginer.getTemplatePath())
        self.lbPathTemplate.config(text=self.path)

    def detailApp(self):
        fen = Toplevel()
        fen.geometry("300x250+250+250")
        fen.title("Détails application")
        lbinfo = ttk.Label(fen,text="Ce logiciel a été développé à des fins \nnon commerciale et offert au Log_Magazine. \n \nTous droits réservés (c) - Jérémy DRON \n version courante: "+const.VERSION+"\n\nlien vers le projet: \nhttps://github.com/Jeremod-Dev/Log_magazineSender")
        lbinfo.pack()

    def previsualiser(self):
        try:
            if self.path=="":
                self.ErreurTemplate.config(text="Veuillez renseigner un template")
                self.ErreurTemplate.place(x=const.ECRAN_X/2-50, y=450)
            elif self.lienPDF.get()=="URL PDF":
                self.ErreurTemplate.config(text="Veuillez renseigner un URL")
                self.ErreurTemplate.place(x=const.ECRAN_X/2-50, y=450)
            else:
                self.ErreurTemplate.config(text="")
                lien = self.lienPDF.get()
                text = self.corpsMail.get("1.0", END)
                enginer.generatorTemplate(self.path, lien, text)
                os.system("4050af11e3cede12a7c250b5f50fcd1c.html google")
        except Exception  as e:
            self.ErreurTemplate.config(text="Previsualisation impossible")
            self.ErreurTemplate.place(x=const.ECRAN_X/2-50, y=450)

    def createurPage(self):
        self.createurPageZone.place(x=0,y=0)
        self.lbUtilisateur.config(text="Connexion: "+enginer.getNameById(self.idUser)+" - "+str(time.strftime("%H:%M:%S")),foreground=const.MAJENTA, font=self.fontClassique, background=const.FOND)
        self.lbUtilisateur.place(x=10, y=const.ECRAN_Y-25)
        self.lbLogMagazineCreateur.place(x=const.ECRAN_X/2-140, y=90)

        btnTemplate = Button(self.createurPageZone, text="Template", background="white",foreground=const.MAJENTA, width=25, command=self.getTemplate, font=self.fontClassique)
        btnTemplate.place(x=const.ECRAN_X/2-80 ,y=165)
        self.lbPathTemplate.place(x=const.ECRAN_X/2-120, y=195)

        self.lienPDF = Entry(self.createurPageZone, width=75, font=self.fontClassique)
        self.lienPDF.insert(0, "URL PDF")
        self.lienPDF.place(x=const.ECRAN_X/4+50, y=225)

        self.corpsMail = ScrolledText(self.createurPageZone, width=75, height=10, bg="white", font=self.fontClassique)
        self.corpsMail.insert(END, "Corps du template")
        self.corpsMail.place(x=const.ECRAN_X/4+50, y=255)

        btnPrevisualiser = Button(self.createurPageZone, text="Valider & Prévisualiser", background="white",foreground=const.MAJENTA, command=self.previsualiser, font=self.fontClassique)
        btnPrevisualiser.place(x=const.ECRAN_X/4, y=450)
        btnSuivant = Button(self.createurPageZone, background="white", text="Copier le code source dans le presse papier",foreground=const.MAJENTA, font=self.fontClassique, command=self.copieSource)
        btnSuivant.place(x=const.ECRAN_X/3*2, y=450)

    def copieSource(self):
        try:
            pyperclip.copy(enginer.getTemplate())
        except:
            self.ErreurTemplate.config(text="Erreur lors de la copie du code source")
            self.ErreurTemplate.place(x=const.ECRAN_X/2-50, y=450)

if __name__ == '__main__':
    app = Application()
    app.homePage()