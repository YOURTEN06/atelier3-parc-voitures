# -*- coding: utf-8 -*-
class Voiture:     def __init__(self, marque, modele, annee, kilometrage):         self.marque = marque         self.modele = modele         self.annee = annee         self.kilometrage = kilometrage      def afficher_info(self):         print(self.marque, self.modele, self.annee, self.kilometrage)   class Parc:     def __init__(self, capacite):         self.capacite = capacite         self.voitures = []      def entrerVoiture(self, voiture):         if len(self.voitures) < self.capacite:             self.voitures.append(voiture)             print("Voiture ajoutée")         else:             print("Parc plein")      def sortirVoiture(self, voiture):         if voiture in self.voitures:             self.voitures.remove(voiture)             print("Voiture retirée")         else:             print("Voiture non trouvée")      def calculerNbrPlacesLibres(self):         return self.capacite - len(self.voitures)  parc = Parc(3)

v1 = Voiture('Toyota','Corolla',2020,50000)
v2 = Voiture('Honda','Civic',2019,60000)
v3 = Voiture('Ford','Focus',2018,70000)
parc = Parc(3)
parc.entrerVoiture(v1)
parc.entrerVoiture(v2)
parc.entrerVoiture(v3)
print(parc.calculerNbrPlacesLibres())
