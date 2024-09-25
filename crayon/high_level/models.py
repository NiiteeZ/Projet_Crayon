# Create your models here.
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix = models.IntegerField(defaut=0)

    def __str__(self):
        pass


class Local(models.Model):
    nom = models.CharField(max_length=100)
    surface = models.IntegerField(default=0)
    ville = models.ForeignKey(Ville, on_delete=models.PROTECT)

    def __str__(self):
        pass


class SiegeSocial(Local):  # heritage siege herite de local
    def __str__(self):
        pass


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    n_serie = models.IntegerField(default=0)

    def __str__(self):
        pass


class Usine(Local):  # heritage Usine herite de local
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        pass


class Objet(models.Model):
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Ressource(Objet):
    def __str__(self):
        pass


class QuantiteRessource(models.Model):
    quantite_ressource = models.ForeignKey(Ressource, on_delete=models.PROTECT)
    quantite = models.IntegerField(default=0)

    def __str__(self):
        pass


class Produit(Objet):
    premiere_etape = models.CharField(max_length=100)

    def __str__(self):
        pass


class Stock:
    objet = models.ForeignKey(Objet, on_delete=models.PROTECT)
    nombre = models.IntegerField(default=0)

    def __str__(self):
        pass


class Etape:
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    quantite_ressource = models.ForeignKey(QuantiteRessource)
    duree = models.IntegerField(default=0)
    etape_suivant = models.ForeignKey("self", on_delete=models.PROTECT)

    def __str__(self):
        pass
