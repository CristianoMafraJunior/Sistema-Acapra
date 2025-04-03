from django.shortcuts import render

from django.shortcuts import redirect
from acapra.forms import AnimalForm


def CadastroAnimaisAdmin(request):
    if request.method == "POST":
        form = AnimalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("DashboardAdmin")
        else:
            print(form.errors)
    else:
        form = AnimalForm()

    return render(request, "acapra/admin_cadastro_animais.html", {"form": form})
