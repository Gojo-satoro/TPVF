from django.urls import path
from .views import liste_produits, ajouter_produit, supprimer_produit,  magasin_login, modifier_produit

urlpatterns = [
    path('', magasin_login, name='magasin_login'),
    path('produits/', liste_produits, name='liste_produits'),
    path('produits/ajouter/', ajouter_produit, name='ajouter_produit'),
    path('produits/modifier/<int:id>/', modifier_produit, name='modifier_produit'),
    path('produits/supprimer/<int:id>/', supprimer_produit, name='supprimer_produit'),
]
