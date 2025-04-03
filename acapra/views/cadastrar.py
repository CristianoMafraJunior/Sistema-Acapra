from django.shortcuts import render


from acapra.forms import FormCadastrar


def Cadastrar(request):
    if request.method == "POST":
        form = FormCadastrar(request, data=request.POST)
    else:
        form = FormCadastrar()

    return render(request, "acapra/cadastrar.html", {"form": form})
