from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Catégorie,Magasin
from .forms import ProduitForm
from django.contrib.auth.decorators import login_required

def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)  # Incluez request.FILES pour gérer les fichiers
        if form.is_valid():
            form.save()
            return redirect('liste_produits')  # Redirige vers la vue de liste des produits après l'ajout
    else:
        form = ProduitForm()  # Instancie un nouveau formulaire vide

    # Récupération des magasins et catégories depuis la base de données
    magasins = Magasin.objects.all()
    catégories = Catégorie.objects.all()

    context = {
        'form': form,
        'magasins': magasins,
        'catégories': catégories,
    }
    return render(request, 'ajouter_produit.html', context)


def modifier_produit(request, id=None):
    if id:
        produit = get_object_or_404(Produit, pk=id)
    else:
        produit = None

    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm(instance=produit)

    return render(request, 'modifier_produit.html', {'form': form})

def supprimer_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    produit.delete()
    return redirect('liste_produits')



from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import MagasinLoginForm
from .models import Magasin

def magasin_login(request):
    if request.method == 'POST':
        form = MagasinLoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                try:
                    magasin = Magasin.objects.get(propriétaire=user)
                    login(request, user)
                    return redirect('liste_produits')
                except Magasin.DoesNotExist:
                    messages.error(request, "Vous n'êtes pas associé à un magasin.")
            else:
                messages.error(request, 'Adresse email ou mot de passe incorrect.')
        else:
            messages.error(request, 'Erreur de validation du formulaire.')
    else:
        form = MagasinLoginForm()
    return render(request, 'magasin_login.html', {'form': form})





@login_required
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'index.html', {'produits': produits})




# from django.shortcuts import render

# # Create your views here.


# from django.contrib.auth.decorators import login_required
# from .models import Produit
# from .forms import ProduitForm

# @login_required
# def créer_produit(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             produit = form.save(commit=False)
#             produit.magasin = request.user.magasin
#             produit.save()
#             return redirect('store:liste_produits')
#     else:
#         form = ProduitForm()
#     return render(request, 'store/créer_produit.html', {'form': form})

# def index(request, *args, **kwargs):

#     return render(request, 'index.html')


# def modifier_produit(request, produit_id):
#     produit = get_object_or_404(Produit, id=produit_id)
#     if request.method == 'POST':
#         form = ProduitForm(request.POST, instance=produit)
#         if form.is_valid():
#             form.save()
#             return redirect('produit_liste')  # Redirect to a list view after saving
#     else:
#         form = ProduitForm(instance=produit)

#     return render(request, 'modifier_produit.html', {'form': form, 'produit': produit})









