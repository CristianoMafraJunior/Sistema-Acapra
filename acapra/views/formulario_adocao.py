from django.shortcuts import render
from acapra.forms import FormularioAdocaoForm


def FormularioAdocao(request):
    if request.method == "POST":
        form = FormularioAdocaoForm(request.POST)
        if form.is_valid():
            # aqui iremos fazer a lógica do form mais pra frente
            pass
    else:
        form = FormularioAdocaoForm()

    return render(request, "acapra/formulario_adocao.html", {"form": form})
