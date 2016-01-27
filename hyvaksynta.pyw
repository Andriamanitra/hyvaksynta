# coding=UTF-8
# Hyvaksyntaohjelma
#
# Tällä ohjelmalla voit joko hyväksyä tai hylätä
# tiedostosta luettuja rivejä

from tkinter import *
from tkinter.messagebox import showerror
import simpledialog
import random


class HyvaksyntaUI:
    def __init__(self):
        self.__ikkuna = Tk()
        self.__ikkuna.title("Hyvaksyntaohjelma")
        self.__sanat = []
        self.__sananro = 0
        self.alusta_widgetit()
        self.kysy_tiedostonimi()
        self.bindaa()
        self.__ikkuna.mainloop()

    def alusta_widgetit(self):
        self.__sanalabel = Label(self.__ikkuna)
        self.__sanalabel.config(text="", font=("Arial", 24))
        self.__sanalabel.grid(row=0, columnspan=3)

        self.__hyvaksy_nappi = Button(self.__ikkuna, text="Hyväksy",
                               command=self.hyvaksy)
        self.__hyvaksy_nappi.config(width=12)
        self.__hyvaksy_nappi.grid(row=1, column=0)

        self.__sananro_text = Text()
        self.__sananro_text.config(height=1, width=6)
        self.__sananro_text.grid(row=1, column=1)
        
        self.__hylkaa_nappi = Button(self.__ikkuna, text="Hylkää",
                              command=self.hylkaa)
        self.__hylkaa_nappi.config(width=12)
        self.__hylkaa_nappi.grid(row=1, column=2)

        textframe = Frame(self.__ikkuna)
        textframe.grid(row=2, columnspan=3, padx=10, pady=10)
        self.__scroll = Scrollbar(textframe)
        self.__sanalista = Text(textframe, yscrollcommand=self.__scroll.set)
        self.__sanalista.config(height=15, width=35)
        self.__sanalista.pack(side=LEFT)
        self.__scroll.pack(side=LEFT, fill=Y)
        self.__scroll.config(command=self.__sanalista.yview)

    def kysy_tiedostonimi(self):
        self.__ikkuna.wm_state("withdrawn")
        tiedostonimi = simpledialog.askstring("Anna tiedostonimi", "Tiedostonimi", parent=self.__ikkuna)
        self.__ikkuna.wm_state("normal")
        try:
            self.lue_sanalista(tiedostonimi)
        except FileNotFoundError:
            showerror("Open file", "Tiedostoa ei voitu avata")
            self.__sanalabel.config(text="Ei oo sanoja..")
            self.__hyvaksy_nappi.config(state=DISABLED)
            self.__hylkaa_nappi.config(state=DISABLED)
            return
                

    def hylkaa(self, event=""):
        if(self.__hylkaa_nappi.cget( "state" ) != DISABLED):
            self.hae_sana()

    def hyvaksy(self, event=""):
        if(self.__hyvaksy_nappi.cget( "state" ) != DISABLED):
            self.__sanalista.insert(END, self.__sana+"\n")
            self.__sanalista.see(END)
            self.hae_sana()

    def hae_sana(self):
        if(self.__sanat): 
            self.__sananro += 1
            self.__sana = self.__sanat.pop(random.randrange(len(self.__sanat)))
            self.__sanalabel.config(text=self.__sana)
            self.__sananro_text.delete(1.0, END)
            self.__sananro_text.insert(END, self.__sananro)
        else:
            self.__sanalabel.config(text="Sanat loppu!")
            self.__hyvaksy_nappi.config(state=DISABLED)
            self.__hylkaa_nappi.config(state=DISABLED)
            self.__sananro_text.delete(1.0, END)
            self.__sananro_text.insert(END, self.__sananro)
            self.__sananro_text.config(state=DISABLED)

    def lue_sanalista(self, tiedostonimi):
        sanafilu = open(tiedostonimi, "r", encoding="utf8")
        for line in sanafilu:
            self.__sanat.append(line.rstrip())
        self.hylkaa()

    def bindaa(self):
        self.__ikkuna.bind("<Left>", self.hyvaksy)
        self.__ikkuna.bind("<Right>", self.hylkaa)
        self.__ikkuna.bind("1", self.hyvaksy)
        self.__ikkuna.bind("2", self.hylkaa)

HyvaksyntaUI()
