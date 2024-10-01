# Create your models here.

from django.db import models


class Ville(models.Model):
    nom = models.CharField(max_length=100)
    code_postal = models.IntegerField(default=0)
    prix_metre2 = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Local(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.ForeignKey(
        Ville, on_delete=models.CASCADE
    )  # Composition ie une seule ville
    surface = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class SiegeSocial(Local):  # heritage siege herite de local
    def __str__(self):
        return f"Siège social à {self.ville.nom}"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)
    n_serie = models.IntegerField(default=0)

    def __str__(self):
        return self.nom

    def costs(self):
        return self.prix


class Usine(Local):  # heritage Usine herite de local
    machines = models.ManyToManyField(Machine)  # agrégation

    def __str__(self):
        return self.nom

    def costs(self):
        machine_cost = 0
        for mach in Machine.objects.all():
            machine_cost = machine_cost + mach.prix

        local_cost = self.surface * self.ville.prix_metre2
        return machine_cost + local_cost


class Objet(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Ressource(Objet):
    def __str__(self):
        return self.nom


class QuantiteRessource(models.Model):
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)  # composition
    quantite = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.ressource.nom} : {self.quantite}"

    def costs(self):
        return self.quantite * self.ressource.prix


class Etape(models.Model):
    nom = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    quantite_ressource = models.ForeignKey(QuantiteRessource, on_delete=models.CASCADE)
    duree = models.IntegerField(default=0)
    etape_suivant = models.ForeignKey(
        "self", on_delete=models.PROTECT
    )  # etape suivant infini demander au prof

    def __str__(self):
        return self.nom


class Produit(Objet):
    premiere_etape = models.ForeignKey(Etape, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Stock(models.Model):
    objet = models.ForeignKey(Objet, on_delete=models.CASCADE)
    nombre = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nombre}"
