from django.shortcuts import render, redirect
from acapra.forms import FormCadastrar
from acapra.models import User
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)


def validar_cpf(cpf: str) -> bool:
    cpf = "".join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = (soma * 10) % 11
    digito1 = 0 if digito1 == 10 else digito1

    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = (soma * 10) % 11
    digito2 = 0 if digito2 == 10 else digito2

    return cpf[-2:] == f"{digito1}{digito2}"


def formatar_cpf(cpf: str) -> str:
    cpf = "".join(filter(str.isdigit, cpf))
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf


def Cadastrar(request):
    if request.method == "POST":
        form = FormCadastrar(request.POST)

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        cpf = request.POST.get("cpf")
        data_nascimento = request.POST.get("data_nascimento")
        telefone = request.POST.get("telefone")

        if not validar_cpf(cpf):
            logger.error(f"CPF inválido informado: {cpf}")
            return redirect("Cadastrar")

        cpf = formatar_cpf(cpf)

        if User.objects.filter(cpf=cpf).exists():
            logger.error(f"CPF já cadastrado: {cpf}")
            return redirect("Cadastrar")

        if User.objects.filter(email=email).exists():
            logger.error(f"Email já cadastrado: {email}")
            return redirect("Cadastrar")

        user = User(
            nome=nome,
            email=email,
            senha=make_password(senha),
            cpf=cpf,
            data_nascimento=data_nascimento,
            telefone=telefone,
        )
        user.save()

        return redirect("LoginUser")

    else:
        form = FormCadastrar()

    return render(request, "acapra/cadastrar.html", {"form": form})
