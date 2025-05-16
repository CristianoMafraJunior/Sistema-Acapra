from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class FormularioAdocaoForm(forms.Form):
    outros_animais = forms.CharField(
        label="Outros Animais",
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Possui outros animais?",
                "rows": 3,
            }
        ),
    )

    tipo_residencia = forms.CharField(
        label="Tipo de Residência",
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Casa, apartamento, etc.",
            }
        ),
    )

    renda = forms.DecimalField(
        label="Renda mensal",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Renda familiar",
            }
        ),
    )

    todos_concordam = forms.BooleanField(
        label="Todos na casa concordam com a adoção?",
        required=False,
    )

    residencia_telas = forms.BooleanField(
        label="A residência possui telas de proteção?",
        required=False,
    )

    animal_acesso_rua = forms.BooleanField(
        label="O animal terá acesso à rua?",
        required=False,
    )

    endereco_completo = forms.BooleanField(
        label="Você fornecerá o endereço completo?",
        required=False,
    )

    manter_animal = forms.BooleanField(
        label="Você tem condições de manter o animal?",
        required=False,
    )

    castracao_vacinacao = forms.BooleanField(
        label="Está de acordo com castração e vacinação?",
        required=False,
    )

    taxa_adocao = forms.BooleanField(
        label="Concorda com a taxa de adoção?",
        required=False,
    )

    documentos = MultipleFileField(
        label="Documentos",
        required=False,
        widget=MultipleFileInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-purple-500 hover:bg-purple-600 text-white font-bold cursor-pointer",
            }
        ),
    )
