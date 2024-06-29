from django import forms
from .models import Produit
from django.contrib.auth.forms import AuthenticationForm

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['magasin', 'nom', 'description', 'prix', 'stock', 'catégorie', 'image']





from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.forms import AuthenticationForm

class MagasinLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'name@example.com',
        'id': 'floatingInput'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Mot de passe',
        'id': 'floatingPassword'
    }))
