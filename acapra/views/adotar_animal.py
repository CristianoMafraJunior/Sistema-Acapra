from django.shortcuts import render, redirect, get_object_or_404
from acapra.models.animal import Animal

def AdotarAnimal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == "POST":
        animal.status_adocao = "A"  # Marca como adotado
        animal.save()
        return redirect("AdocoesAdmin")  # vai para lista de adotados
    return redirect("DashboardAdmin")  # fallback se não for POST
