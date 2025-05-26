from django.shortcuts import render
from acapra.models import Animal


def DashboardAdmin(request):
    filtro_status = request.GET.get("status")
    filtro_especie = request.GET.get("especie")
    filtro_idade = request.GET.get("idade")
    animais = Animal.objects.all()
    if filtro_status:
        animais = animais.filter(status_adocao=filtro_status)
    if filtro_especie:
        animais = animais.filter(especie=filtro_especie)
    if filtro_idade:
        animais = animais.filter(idade=filtro_idade)
    return render(
        request,
        "acapra/admin_dashboard.html",
        {
            "animais": animais,
            "filtro_status": filtro_status,
            "filtro_especie": filtro_especie,
            "filtro_idade": filtro_idade,
        },
    )
