from django.contrib.auth import logout
from django.shortcuts import redirect


def Logout(request):
    logout(request)
    return redirect("Home")
