from django.contrib.auth.forms import AuthenticationForm
from django import forms


class FormLoginAdmin(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Usuário",
            }
        ),
    )
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Senha",
            }
        ),
    )
