from django.shortcuts import render
from acapra.models import Animal


def AnimaisDisponiveisUser(request):
    filtro_especie = request.GET.get("especie")
    filtro_idade = request.GET.get("idade")
    animais = Animal.objects.filter(status_adocao="D")
    if filtro_especie:
        animais = animais.filter(especie=filtro_especie)
    if filtro_idade:
        animais = animais.filter(idade=filtro_idade)
    return render(
        request,
        "acapra/animais_disponiveis_user.html",
        {
            "animais": animais,
            "filtro_especie": filtro_especie,
            "filtro_idade": filtro_idade,
        },
    )
