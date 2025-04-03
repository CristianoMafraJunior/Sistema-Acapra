from django.shortcuts import render


def FormulariosAdmin(request):
    return render(request, "acapra/admin_formularios.html")
