from django.shortcuts import render
from acapra.models import Animal, Foto


def DashboardAdmin(request):
    animais = Animal.objects.all()
    fotos = Foto.objects.all()
    return render(
        request, "acapra/admin_dashboard.html", {"animais": animais, "fotos": fotos}
    )
