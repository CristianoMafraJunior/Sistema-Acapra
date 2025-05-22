from django.shortcuts import get_object_or_404, redirect
from acapra.models import Foto


def ExcluirFoto(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)
    animal_id = foto.animal.id
    if request.method == "POST":
        foto.delete()
    return redirect("EditarAnimal", animal_id=animal_id)
