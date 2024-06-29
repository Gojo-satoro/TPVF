from django.contrib import admin
from .models import Client,Magasin,Catégorie,Produit,Commande,ArticleDeCommande

admin.site.register(Client)
admin.site.register(Magasin)
admin.site.register(Catégorie)
admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(ArticleDeCommande)

