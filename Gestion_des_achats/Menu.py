#les biblio necessaire
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox

def Achats():
    root.destroy()
    call(["python", "Achtas.py"])

def Ventes():
    root.destroy()
    call(["python", "Ventes.py"])


#ma fenetre
root = Tk()
root.title("Gestion des achats")
root.geometry("600x200+400+200")
root.resizable(False, False)
root.configure(background="#808080")


#ajouter le titre
lbtitre = Label(root,borderwidth=3, relief=SUNKEN, text="GESTION DES ACHTAS", font=("sans serif", 25), background="#483D88", foreground="white")
lbtitre.place(x=0, y=0, width=600)

#bouttons achts

btnenregistrer = Button(root, text="ACHATS", font=("Arial", 24),bg="#483D8B",fg="white", command= Achats)
btnenregistrer.place(x=100, y=100, width=200)

btnenregistrer = Button(root, text="VENTES", font=("Arial", 24),bg="#483D8B",fg="white", command= Ventes)
btnenregistrer.place(x=300, y=100, width=200)



#exution
root.mainloop()