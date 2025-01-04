"""
URL configuration for crayon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from high_level import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "Ville/<int:pk>",
        views.VilleDetailView.as_view(),
        name="Ville",
    ),
    path(
        "Ville/api/<int:pk>",
        views.VilleApiView.as_view(),
        name="Ville",
    ),
    path(
        "Local/<int:pk>",
        views.LocalDetailView.as_view(),
        name="Local",
    ),
    path(
        "Local/api/<int:pk>",
        views.LocalApiView.as_view(),
        name="Local",
    ),
    path(
        "Machine/<int:pk>",
        views.MachineDetailView.as_view(),
        name="Machine",
    ),
    path(
        "Machine/api/<int:pk>",
        views.MachineApiView.as_view(),
        name="Machine",
    ),
    path(
        "Objet/<int:pk>",
        views.ObjetDetailView.as_view(),
        name="Objet",
    ),
    path(
        "Objet/api/<int:pk>",
        views.ObjetApiView.as_view(),
        name="Objet",
    ),
    path(
        "Usine/<int:pk>",
        views.UsineDetailView.as_view(),
        name="Usine",
    ),
    path(
        "Usine/api/<int:pk>",
        views.UsineApiView.as_view(),
        name="Usine",
    ),
    path(
        "SiegeSocial/<int:pk>",
        views.SiegeSocialDetailView.as_view(),
        name="SiegeSocial",
    ),
    path(
        "SiegeSocial/api/<int:pk>",
        views.SiegeSocialApiView.as_view(),
        name="SiegeSocial",
    ),
    path(
        "Ressource/<int:pk>",
        views.RessourceDetailView.as_view(),
        name="Ressource",
    ),
    path(
        "Ressource/api/<int:pk>",
        views.RessourceApiView.as_view(),
        name="Ressource",
    ),
    path(
        "QuantiteRessource/<int:pk>",
        views.QuantiteRessourceDetailView.as_view(),
        name="QuantiteRessource",
    ),
    path(
        "QuantiteRessource/api/<int:pk>",
        views.QuantiteRessourceApiView.as_view(),
        name="QuantiteRessource",
    ),
    path(
        "Etape/<int:pk>",
        views.EtapeDetailView.as_view(),
        name="Etape",
    ),
    path(
        "Etape/api/<int:pk>",
        views.EtapeApiView.as_view(),
        name="Etape",
    ),
    path(
        "Produit/<int:pk>",
        views.ProduitDetailView.as_view(),
        name="Produit",
    ),
    path(
        "Produit/api/<int:pk>",
        views.ProduitApiView.as_view(),
        name="Produit",
    ),
    path(
        "Stock/<int:pk>",
        views.StockDetailView.as_view(),
        name="Stock",
    ),
    path(
        "Stock/api/<int:pk>",
        views.StockApiView.as_view(),
        name="Stock",
    ),
]