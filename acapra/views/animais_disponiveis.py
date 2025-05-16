from django.shortcuts import render
from acapra.models import Animal, Foto


def AnimaisDisponiveis(request):
    animais = Animal.objects.all()
    fotos = Foto.objects.all()
    return render(
        request, "acapra/animais_disponiveis.html", {"animais": animais, "fotos": fotos}
    )
