from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    téléphone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Magasin(models.Model):
    nom = models.CharField(max_length=255)
    propriétaire = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Catégorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    magasin = models.ForeignKey(Magasin, on_delete=models.CASCADE)
    catégorie = models.ForeignKey(Catégorie, on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='produit_images/', null=True, blank=True)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_de_création = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, default='En attente')

    def __str__(self):
        return f'Commande {self.id} par {self.client.user.username}'


class ArticleDeCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantité = models.IntegerField()

    def __str__(self):
        return f'{self.quantité} x {self.produit.nom}'


def magasin_login(request):
    if request.method == 'POST':
        magasin_id = request.POST.get('magasin_id')
        password = request.POST.get('password')

        # Authentification du magasin
        magasin = authenticate(request, magasin_id=magasin_id, password=password)

        if magasin is not None:
            login(request, magasin)
            # Rediriger vers la page des fonctionnalités CRUD ou une autre page appropriée
            return redirect('liste_produits')  # Remplacez 'dashboard' par le nom de votre vue de tableau de bord
        else:
            messages.error(request, 'Identifiant du magasin ou mot de passe incorrect.')

    return render(request, 'magasin_login.html')
