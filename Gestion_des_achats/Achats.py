import tkinter
from subprocess import call
from tkinter import ttk, Tk
from tkinter import *
from tkinter import messagebox
from cProfile import label
import mysql.connector


#ma fenetre
root = Tk()
root.title("Menu achats")
root.geometry("1350x700+0+0")
root.resizable(False, False)
root.configure(background="#808080")

def Retour():
    root.destroy()
    call(["python", "Menu.py"])

def Ajouter():
    matricule = txtmatricule.get()
    fournisseur = txtfournisseur.get()
    telephone = txtTelephone.get()
    produit = comboproduit.get()
    prix_achat = txtPrice.get()
    quantite_achete = txtQuantite.get()
    somme = txtSomme.get()

    maBase = mysql.connector.connect(
        host="127.0.0.1",  # Adresse IP ou nom d'hôte du serveur MySQL
        port=3306,  # Numéro de port
        user="root",
        password="",
        database="achat"
    )

    print("conneeected")
    meConnect= maBase.cursor()

    try:
        sql = "INSERT INTO tb_achats (matricule, fournisseur, telephone, produit, prix_achat, quantite_achat) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (matricule, fournisseur,telephone, produit, prix_achat, quantite_achete)
        meConnect.execute(sql, val)
        maBase.commit()
        dernierematricule = meConnect.lastrowid
        messagebox.showinfo("information", "achats ajouter")
        root.destroy()
        call("python", "Achats.py")

    except Exception as e:

        print(e)
        # retour
        maBase.rollback()
        maBase.close()

def Supprimer():
    matricule = txtmatricule.get()

    maBase = mysql.connector.connect(
        host="127.0.0.1",  # Adresse IP ou nom d'hôte du serveur MySQL
        port=3306,  # Numéro de port
        user="root",
        password="",
        database="achat"
    )

    print("conneeected")
    meConnect = maBase.cursor()
    try:
        sql = "delete from tb_achats where matricule=%s "
        val = (matricule,)
        meConnect.execute(sql, val)
        maBase.commit()
        dernierematricule = meConnect.lastrowid
        messagebox.showinfo("information", "achats supprimer")
        root.destroy()
        call("python", "Achats.py")
    except Exception as e:

        print(e)
        # retour
        maBase.rollback()
        maBase.close()

def Modifier():
        matricule = txtmatricule.get()
        fournisseur = txtfournisseur.get()
        telephone = txtTelephone.get()
        produit = comboproduit.get()
        prix_achat = txtPrice.get()
        quantite_achete = txtQuantite.get()

        maBase = mysql.connector.connect(
                host="127.0.0.1",  # Adresse IP ou nom d'hôte du serveur MySQL
                port=3306,  # Numéro de port
                user="root",
                password="",
                database="achat")
        meConnect = maBase.cursor()

        try:
                sql = "update tb_achats set fournisseur=%s,telephone=%s, produit=%s, prix_achat=%s, quantite_achat=%s where matricule=%s"


                val = (fournisseur,telephone, produit, prix_achat, quantite_achete,matricule)
                meConnect.execute(sql, val)
                maBase.commit()

        except Exception as e:

                print(e)
                # retour
                maBase.rollback()
                maBase.close()


#ajoputer titre
lbtitre = Label(root,borderwidth=3, relief=SUNKEN, text="GESTION DES ACHTAS", font=("sans serif", 25), background="#483D88", foreground="#FFFAFA")
lbtitre.place(x=0, y=0, width=1350, height=100)

#details des achats
lblmatricule=Label(root,text="MATRICULE", font = ("Arial",18),background="#808080",fg="white")
lblmatricule.place(x=70 ,y=150 ,width=150)
txtmatricule = Entry(root,bd=4 , font=("Arial",14))
txtmatricule.place(x=250,y=150,width=150)
#fournisseur
lblfournisseur=Label(root,text="FOURNISSEUR", font = ("Arial",18),background="#808080",fg="white")
lblfournisseur.place(x=50 ,y=200 ,width=200)
txtfournisseur = Entry(root,bd=4 , font=("Arial",14))
txtfournisseur.place(x=250,y=200,width=300)
#Numero
lblTelephone=Label(root,text="TELEPHONE", font = ("Arial",18),background="#808080",fg="white")
lblTelephone.place(x=70 ,y=250 ,width=150)
txtTelephone = Entry(root,bd=4 , font=("Arial",14))
txtTelephone.place(x=250,y=250,width=300)
#achats
lblProduit=Label(root,text="PRODUIT", font = ("Arial",18),background="#808080",fg="white")
lblProduit.place(x=570 ,y=150 ,width=150)

comboproduit = ttk.Combobox(root, font=("Arial",14))
comboproduit["values"] = ['iphone12','iphone11','Galaxy s22']
comboproduit.place(x=750 ,y=150 ,width=150)

#prix
lblPrix = Label(root, text="Prix", font = ("Arial",18),background="#808080",fg="white")
lblPrix.place(x=550, y=200, width=150, )
txtPrice = Entry(root,bd=4 , font=("Arial",14))
txtPrice.place(x=700,y=200,width=150)


#Quantité
lblQuantite=Label(root,text="QUANTITE", font = ("Arial",18),background="#808080",fg="white")
lblQuantite.place(x=550 ,y=250 ,width=150)
txtQuantite= Entry(root,bd=4 , font=("Arial",14))
txtQuantite.place(x=700,y=250,width=100)





btnenregister = Button(root,text="ENREGISTRER",font = ("Arial",16),bg="#483DBB",fg="white",command=Ajouter)
btnenregister.place(x=1000,y=140,width=200)

#butoon suppression
btnenregister = Button(root,text="SUPPRIMER",font = ("Arial",16) , bg="#483DBB",fg="white",command=Supprimer)
btnenregister.place(x=1000,y=240,width=200)
#button modifier
btnenregister = Button(root,text="MODIFIER",font = ("Arial",16),bg="#483DBB",fg="white",command=Modifier)
btnenregister.place(x=1000,y=190,width=200)



#Retour
btnenregister = Button(root,text="RETOUR",font = ("Arial" , 16) , bg="#FF0000",fg="white",command=Retour)
btnenregister.place(x=1240,y=240,width=100)

#somme
lblSomme=Label(root,text="SOMME", font = ("Arial",18),background="#808080",fg="white")
lblSomme.place(x=1240 ,y=150 ,width=100)
txtSomme= Entry(root,bd=4 , font=("Arial",14))
txtSomme.place(x=1240,y=200,width=150)


#table
table= ttk.Treeview(root,columns=(1,2,3,4,5,6,7),height=10,show="headings")
table.place(x=0,y=290,width=1350,height=700)

#entete
table.heading(1,text ='CODE _ACHAT')
table.heading(2,text ='FOURNISSEUR')
table.heading(3,text ='TEEPHONE')
table.heading(4,text ='PRODUIT')
table.heading(5,text ='PRIX')
table.heading(6,text ='QUANTITE')
table.heading(7,text ='SOMME')
#definir les dimension des colones
table.column(1,width=50)
table.column(2,width=150)
table.column(3,width=150)
table.column(4,width=100)
table.column(5,width=50)
table.column(6,width=50)
table.column(7,width=50)



#affichier les informations de la table

maBase = mysql.connector.connect(
                host="127.0.0.1",  # Adresse IP ou nom d'hôte du serveur MySQL
                port=3306,  # Numéro de port
                user="root",
                password="",
                database="achat")
meConnect = maBase.cursor()
meConnect.execute("select * from tb_achats")
for row in meConnect:
    table.insert('',END, value = row)
maBase.close()


#excution
root.mainloop()





#def somme prix acat
