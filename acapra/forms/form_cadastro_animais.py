from django import forms
from acapra.models import Foto, Animal


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


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["nome", "especie", "idade", "porte", "descricao", "raca"]

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Nome",
            }
        )
    )
    especie = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Especie",
            }
        )
    )
    idade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Idade",
            }
        )
    )
    porte = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Porte",
            }
        )
    )
    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Descrição",
                "rows": 3,
            }
        )
    )
    raca = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Raça",
            }
        )
    )
    fotos = MultipleFileField(
        label="Fotos",
        required=False,
        widget=MultipleFileInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-purple-500 hover:bg-purple-600 text-white font-bold cursor-pointer",
            }
        ),
    )

    def save(self, commit=True):
        animal = super().save(commit=False)
        if commit:
            animal.save()

        fotos = self.files.getlist("fotos")
        for foto in fotos:
            Foto.objects.create(animal=animal, imagem=foto)

        return animal
