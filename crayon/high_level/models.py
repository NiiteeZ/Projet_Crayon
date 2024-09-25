# Create your models here.
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix = models.IntegerField(defaut=0)

    def __init__(self, nom, code_postal, prix):
        self.nom = nom
        self.code_postal = code_postal
        self.prix = prix


class Local(models.Model):
    nom = models.CharField(max_length=100)
    surface = models.IntegerField(default=0)
    ville = models.ForeignKey(Ville)

    def __init__(self, nom, surface):
        self.nom = nom
        self.ville = Ville()  # composition
        self.surface = surface


class SiegeSocial(Local):  # heritage siege herite de local
    def __init__(self):
        pass


class Usine(Local):  # heritage Usine herite de local
    def __init__(self, machines):
        self.machines = machines


class Machine:
    def __init__(self, nom, prix, n_serie):
        self.nom = nom
        self.prix = prix
        self.n_serie = n_serie


class Objet:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Ressource(Objet):
    def __init__(self):
        pass


class Produit(Objet):
    def __init__(self, premiere_etape):
        self.premiere_etape = premiere_etape


class Stock:
    def __init__(self, nombre):
        self.objet = Objet()
        self.nombre = nombre


class Etape:
    def __init__(self, nom, machine, quantite_ressource, duree):
        self.nom = nom
        self.machine = machine
        self.noquantite_ressourcem = quantite_ressource
        self.duree = duree
        self.etape_suivante = None
