from django.shortcuts import render, redirect
from acapra.forms import FormCadastrar
from acapra.models import User
from django.contrib.auth.hashers import make_password


def Cadastrar(request):
    if request.method == "POST":
        form = FormCadastrar(request.POST)

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        telefone = request.POST.get("telefone")

        user = User(
            nome=nome,
            email=email,
            senha=make_password(senha),
            cpf=cpf,
            data_nascimento=data_nascimento,
            telefone=telefone,
        )
        user.save()

        return redirect("Home")

    else:
        form = FormCadastrar()

    return render(request, "acapra/cadastrar.html", {"form": form})
