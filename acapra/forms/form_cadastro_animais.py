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

GATOS = [
    ("Siames", "Siames"),
    ("Persa", "Persa"),
    ("Maine Coon", "Maine Coon"),
]

CACHORROS = [
    ("Labrador", "Labrador"),
    ("Bulldog", "Bulldog"),
    ("Poodle", "Poodle"),
]

VACINAS_OPCOES = [
    ("V4", "V4"),
    ("V8", "V8"),
    ("V10", "V10"),
    ("Raiva", "Raiva"),
    ("Giárdia", "Giárdia"),
    ("Gripe", "Gripe"),
]

DOENCA_OPCOES = [
    ("", "O animal possui doença(s)?"),
    ("Sim", "Sim"),
    ("Não", "Não"),
]


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ["nome", "especie", "idade", "porte", "descricao", "raca", "vacina","doenca","observacao",]

    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Nome",
            }
        )
    )
    especie = forms.ChoiceField(
    choices=[("", "Selecione a espécie")] + list(Animal._meta.get_field("especie").choices),
    widget=forms.Select(
        attrs={
            "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
            }
        ),
        required=True,  # garante que o usuário escolha
    )
    idade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Idade",
            }
        )
    )
    porte = forms.ChoiceField(
    choices=[("", "Selecione o porte")] + [
        ("Pequeno", "Pequeno"),
        ("Médio", "Médio"),
        ("Grande", "Grande")
    ],
    widget=forms.Select(
        attrs={
            "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
         }
        ),
    required=True,
    )
    
    vacina = forms.MultipleChoiceField(
        choices=VACINAS_OPCOES,
        widget=forms.SelectMultiple(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
            }
        ),
        required=False,
    )
    
    doenca = forms.ChoiceField(
        choices=DOENCA_OPCOES,
        widget=forms.Select(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
            }
        ),
        required=True,
    )

    descricao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Descrição da doença",
                "rows": 3,
            }
        ),
        required=False,
    )
    
    observacao = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white",
                "placeholder": "Observação",
                "rows": 3,
            }
        )
    )
    raca = forms.ChoiceField(
    choices=[("", "Selecione a raça")] + GATOS + CACHORROS,
    widget=forms.Select(attrs={"class": "w-full px-4 py-2 rounded-lg bg-gray-800 text-white"}),
    required=True,
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.vacina:
            self.initial["vacina"] = self.instance.vacina.split(",")

    def clean_vacina(self):
        vacinas = self.cleaned_data.get("vacina", [])
        return ",".join(vacinas)
    
    def save(self, commit=True):
        animal = super().save(commit=False)
        if commit:
            animal.save()
            
        vacinas = self.cleaned_data.get("vacina", "")
        animal.vacina = vacinas
        if commit:
            animal.save()

        fotos = self.files.getlist("fotos")
        for foto in fotos:
            Foto.objects.create(animal=animal, imagem=foto)

        return animal
    
    def clean_doenca(self):
        doenca = self.cleaned_data.get("doenca")
        if doenca not in ["Sim", "Não"]:
            raise forms.ValidationError("Por favor, selecione 'Sim' ou 'Não'.")
        return doenca
    
    def clean(self):
        cleaned_data = super().clean()
        doenca = cleaned_data.get("doenca")
        descricao = cleaned_data.get("descricao")

        if doenca == "Sim" and not descricao:
            self.add_error("descricao", "Por favor, descreva a doença.")
        
        return cleaned_data


