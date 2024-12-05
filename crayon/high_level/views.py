# Create your views here.

from typing import Dict, Any
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import DetailView
from .models import (
    Ville,
    Local,
    Usine,
    Machine,
    Objet,
    SiegeSocial,
    Ressource,
    QuantiteRessource,
    Etape,
    Produit,
    Stock,
)
from django.http import JsonResponse

#Modifier tel que : chaque classe a une classe ApiView (json_extended) et detailView (json)

class VilleDetailView(DetailView):
    model = Ville

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended()) #Mettre Json a la place de extended

#class VilleApiView(DetailView):
#    model = Ville
#
#   def render_to_response(
#        self, context: Dict[str, Any], **response_kwargs: Any
#  ) -> HttpResponse:
#        return JsonResponse(self.object.json_extended())
    
class LocalDetailView(DetailView):
    model = Local

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class MachineDetailView(DetailView):
    model = Machine

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class ObjetDetailView(DetailView):
    model = Objet

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class UsineDetailView(DetailView):
    model = Usine

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class SiegeSocialDetailView(DetailView):
    model = SiegeSocial

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class RessourceDetailView(DetailView):
    model = Ressource

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class QuantiteRessourceDetailView(DetailView):
    model = QuantiteRessource

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class EtapeDetailView(DetailView):
    model = Etape

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class ProduitDetailView(DetailView):
    model = Produit

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())


class StockDetailView(DetailView):
    model = Stock

    def render_to_response(
        self, context: Dict[str, Any], **response_kwargs: Any
    ) -> HttpResponse:
        return JsonResponse(self.object.json_extended())