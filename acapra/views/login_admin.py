from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages

from acapra.forms import FormLoginAdmin


def LoginAdmin(request):
    if request.method == "POST":
        form = FormLoginAdmin(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user and user.is_superuser:
                login(request, user)
                return redirect("CatalogoAdmin")
            else:
                messages.error(
                    request, "Apenas administradores podem acessar esta área."
                )
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = FormLoginAdmin()

    return render(request, "acapra/login_admin.html", {"form": form})
