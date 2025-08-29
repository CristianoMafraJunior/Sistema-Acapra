from django.shortcuts import redirect, get_object_or_404
from acapra.models.animal import Animal

def CancelarAdocao(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    animal.status_adocao = "D"
    animal.save()
    return redirect("AdocoesAdmin")
