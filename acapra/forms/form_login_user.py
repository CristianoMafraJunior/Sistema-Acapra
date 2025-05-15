from django import forms


class FormLoginUser(forms.Form):
    email = forms.CharField(
        label="E-mail",
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "E-mail",
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
