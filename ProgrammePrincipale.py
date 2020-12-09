# -*- coding: utf-8 -*-
"""
Created on Tue Dec 8 12:12:47 2020

@author: Diego
"""
from canvasFinale import LabelCoup,LabelMotRech,BoutonEntry,BoutonProposer,BoutonRejouer,BoutonQuitter,LabelLettresFausses,console,Canevas,LabelScoreMax
from  tkinter import Tk,Label,Button,Entry,StringVar,Canvas,PhotoImage




LabelCoup.grid(row=1)
LabelMotRech.grid(row=2)
BoutonEntry.grid(row=3)
BoutonProposer.grid(row=4)
BoutonRejouer.grid(row=2,column=3)
BoutonQuitter.grid(row=3,column=3)
LabelLettresFausses.grid(row=5)
LabelScoreMax.grid(row=8,column=3)
Canevas.grid(row=1,column=2,rowspan=4)
console.grid(row=7, column=2)

Rejouer()

Mot=Rejouer()[0]
LettresTrouver=Rejouer()[1]
LettresFausses=Rejouer()[2]
vie=Rejouer()[3]

Mafenetre.mainloop()
