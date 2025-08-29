<<<<<<< HEAD
from django.shortcuts import render, redirect, get_object_or_404
from acapra.models.animal import Animal

=======
from django.shortcuts import redirect, get_object_or_404
from acapra.models.animal import Animal


>>>>>>> b452eddd0296e785cd0aa68cdc83b66e4268d177
def AdotarAnimal(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    if request.method == "POST":
        animal.status_adocao = "A"
        animal.save()
        return redirect("AdocoesAdmin")
    return redirect("DashboardAdmin")
