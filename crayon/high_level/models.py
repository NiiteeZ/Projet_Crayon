# Create your models here.
from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    surface = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class SiegeSocial(Local):  # heritage siege herite de local
    def __str__(self):
        return f"Siège social à {self.ville.nom}"
