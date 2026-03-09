class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage

    def afficher_info(self):
        pass

class Parc:
    def __init__(self, capacite):
        self.capacite = capacite
        self.voitures = []
