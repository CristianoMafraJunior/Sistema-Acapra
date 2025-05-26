from django import forms
from acapra.models import DocumentoFormulario, FormularioAdocao
from django.utils import timezone


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


class FormularioAdocaoForm(forms.ModelForm):
    class Meta:
        model = FormularioAdocao
        exclude = ["animal", "user", "data_envio"]

    todos_concordam = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="Todos os membros da casa concordam com a adoção?",
        required=False,
    )
    outros_animais = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Você possui outros animais?",
            }
        )
    )
    tipo_residencia = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Tipo de residência",
                "rows": 2,
            }
        )
    )
    residencia_telas = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="Sua residência possui telas de proteção?",
        required=False,
    )
    animal_acesso_rua = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="O animal terá acesso à rua?",
        required=False,
    )
    endereco_completo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Endereço completo",
                "rows": 2,
            }
        )
    )
    renda = forms.DecimalField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Renda mensal",
            }
        ),
        max_digits=10,
        decimal_places=2,
    )
    manter_animal = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="Você se compromete a manter o animal?",
        required=False,
    )
    castracao_vacinacao = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="Concorda em castrar e vacinar o animal?",
        required=False,
    )
    taxa_adocao = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"class": "w-5 h-5 text-purple-500 focus:ring-purple-600"}
        ),
        label="Concorda com o pagamento da taxa de adoção?",
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

    def save(self, commit=True, animal=None, user=None, arquivos=None):
        if hasattr(user, "_wrapped"):
            user = user._wrapped

        instance = super().save(commit=False)
        if not instance.data_envio:
            instance.data_envio = timezone.now()
        if animal:
            instance.animal = animal
        if user:
            instance.user = user

        if commit:
            instance.save()
        if arquivos:
            for arquivo in arquivos:
                DocumentoFormulario.objects.create(
                    formulario_adocao=instance, arquivo=arquivo
                )

        return instance
