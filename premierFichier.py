# -*- coding: utf8 -*-

import random
import json

listePersonnages = []
listeCitations = []
monPersonnage = ""
maCitation = ""

# On veut faire dire à un personnage, une citation au hasard

# Choix du personnage
def choixPersonnage(liste):
	nombreAleatoire = random.randint(0,len(liste)-1)
	#nombreAleatoire = 1
	return liste[nombreAleatoire]

# Récupération de la citation au hasard
def citationHasard(liste):
	nombreAleatoire = random.randint(0,len(liste)-1)
	#nombreAleatoire = 1
	return liste[nombreAleatoire]

# Récupération d'une liste
def recupListeJSON(fichier, motclef):
	valeurs=[]
	with open(fichier) as f:
		data = json.load(f)
		for entry in data:
			valeurs.append(entry[motclef])
	return valeurs
	
# Ecrire du message
def messageAffiche(personage,message):
	return "{} a dit {}".format(personage,message)
	

reponseUtilisateur = input("Pour continuer pressez entrée, pour quitter pressez B")
listePersonnages = recupListeJSON("characters.json","character")
listeCitations = recupListeJSON("quotes.json","quote")
#print(listeCitations)
#print(listePersonnages)
#Proposition personage
while reponseUtilisateur != 'B':
	monPersonnage = choixPersonnage(listePersonnages)
#	print("Mon perso" + monPersonnage)
	maCitation = citationHasard(listeCitations)
#	print("ma citation" + maCitation)
	print(messageAffiche(monPersonnage,maCitation))
	reponseUtilisateur = input("Pour continuer pressez entrée, pour quitter pressez B")