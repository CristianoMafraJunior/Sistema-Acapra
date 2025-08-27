from django.shortcuts import render
from acapra.models.animal import Animal


def AdocoesAdmin(request):
    animais = Animal.objects.filter(status_adocao="A")  # só adotados
    return render(request, "acapra/admin_adocoes.html", {"animais": animais})
