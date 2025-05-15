from django.shortcuts import render, redirect
from ..models import User
from ..forms import FormLoginUser
from django.contrib.auth.hashers import check_password


def LoginUser(request):
    if request.method == "POST":
        form = FormLoginUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            senha = form.cleaned_data["password"]

            user = User.objects.get(email=email)
            if check_password(senha, user.senha):
                request.session["user_id"] = user.id
                return redirect("Home")
    else:
        form = FormLoginUser()

    return render(request, "acapra/login_user.html", {"form": form})
