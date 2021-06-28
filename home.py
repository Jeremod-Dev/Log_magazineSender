from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import constante as const
import enginer

class Application:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title(const.TITRE)
        self.fenetre.geometry(str(const.ECRAN_X) +"x"+ str(const.ECRAN_Y) +"+150+100")
        self.fenetre.resizable(False, False)
        self.fenetre.config(background=const.FOND)
        self.fenetre.iconbitmap("logo.ico")

        # Page de connexion
        self.fontTitre = ("Arial",30,"bold")
        self.homePageZone = Frame(self.fenetre, background=const.FOND,width=const.ECRAN_X, height=const.ECRAN_Y)
        self.lbSend = ttk.Label(self.homePageZone, text="LOG_MAGAZINE",foreground=const.MAJENTA,background=const.FOND, font=self.fontTitre)
        self.eMdp = Entry(self.homePageZone, show="*")
        self.ErreurMdp = ttk.Label(self.homePageZone, text="Mot de passe incorrect", foreground="red", background=const.FOND)
    
        # Page de template
        self.fontTitre = ("Arial",30,"bold")
        self.homePageZone = Frame(self.fenetre, background=const.FOND,width=const.ECRAN_X, height=const.ECRAN_Y)
        self.lbSend = ttk.Label(self.homePageZone, text="LOG_MAGAZINE",foreground=const.MAJENTA,background=const.FOND, font=self.fontTitre)
        self.eMdp = Entry(self.homePageZone, show="*")
        self.ErreurMdp = ttk.Label(self.homePageZone, text="Mot de passe incorrect", foreground="red", background=const.FOND)

    def verificationMdp(self):
        if (enginer.verificationMdp(self.eMdp.get())>=0):
            self.createurPage()
        else:
            self.ErreurMdp.place(x=const.ECRAN_X/2-50, y=220)

    def homePage(self):
        self.lbSend.place(x=const.ECRAN_X/2-150, y=150)
        self.homePageZone.place(x=0,y=0)
        self.eMdp.place(x=const.ECRAN_X/2, y=250)
        lbMdp = ttk.Label(self.homePageZone, text="Mot de Passe",foreground="black",background=const.FOND)
        lbMdp.place(x=const.ECRAN_X/2-120, y=250)
        btnValider = Button(self.homePageZone, text="Connexion", background="white", width=25, command=self.verificationMdp)
        btnValider.place(x=542 ,y=372)
        self.fenetre.mainloop()
        

    def createurPage(self):
        print("Createur en cours...")

    def mailPage(self):
        pass

if __name__ == '__main__':
    app = Application()
    app.homePage()