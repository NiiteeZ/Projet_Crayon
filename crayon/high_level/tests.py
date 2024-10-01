# Create your tests here.
from django.test import TestCase
from .models import Ville, Machine, QuantiteRessource, Ressource, Usine


class TestUnitaire(TestCase):
    def test_usine_creation(self):
        ville = Ville.objects.create(nom="Labege", code_postal=31000, prix_metre2=2000)

        machine1 = Machine.objects.create(nom="M1", prix=1000, n_serie=16832)
        machine2 = Machine.objects.create(nom="M2", prix=2000, n_serie=16833)

        usine = Usine.objects.create(nom="EtsIndustries", ville=ville, surface=50)

        usine.machines.set([machine1, machine2])

        objet1 = Ressource.objects.create(nom="bois", prix=10)
        objet2 = Ressource.objects.create(nom="mine", prix=15)

        quantite_bois = QuantiteRessource.objects.create(
            ressource=objet1, quantite=1000
        )
        quantite_mine = QuantiteRessource.objects.create(ressource=objet2, quantite=50)

        total_cout = usine.costs() + quantite_bois.costs() + quantite_mine.costs()
        self.assertEqual(total_cout, 110750)
