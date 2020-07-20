import os
import tkinter as tk
from pytube import YouTube

fenetre = tk.Tk()
fenetre.geometry("600x300")
fenetre.config(bg="Cyan")
fenetre.title("Music Downloader by Berachem")
fenetre.iconbitmap("C:/Users/berac/Desktop/projet music player/logo.ico")
couleur_fond = "Cyan"
couleur = "Black"

def cacher_label(widget):
	resultat["text"] = ""
  
#Fonction qui va rechercher sur youtube le nm de la musique
def telechargememnt():

    video = YouTube(str(entry.get()))
    video = video.streams.filter(only_audio=True).all()
    video[0].download("C:/Users/berac/Desktop")
    resultat["foreground"] = "Green"
    resultat["text"] = "Téléchargement réussi :)"
    fenetre.after(5000, cacher_label, resultat)
    #LA FONCTION N'EST PAS TERMINEE

txt = tk.Label(fenetre,background=couleur_fond, text = "Veuillez entrer le lien de la musique ", foreground=couleur, font = "Nexabold")
txt.pack(pady = 35)

entry = tk.Entry(fenetre,background=couleur_fond, foreground=couleur)
entry.pack(pady = 5, ipadx = 130)

resultat = tk.Label(fenetre,background=couleur_fond, text = "", foreground=couleur, font = "Nexabold")
resultat.pack()

button = tk.Button(fenetre,background=couleur_fond, text = "Télécharger", foreground=couleur, font = "Nexabold", activebackground=couleur_fond, command = lambda : telechargememnt())
button.pack(pady = 5)

fenetre.mainloop()
