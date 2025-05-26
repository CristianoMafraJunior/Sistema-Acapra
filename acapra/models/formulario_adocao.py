from django.db import models
from .user import User
from .animal import Animal


class FormularioAdocao(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="animais_formulario_adocao"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_formulario"
    )
    data_envio = models.DateField()
    todos_concordam = models.BooleanField()
    outros_animais = models.TextField()
    tipo_residencia = models.CharField(max_length=30)
    residencia_telas = models.BooleanField()
    animal_acesso_rua = models.BooleanField()
    endereco_completo = models.CharField(max_length=200)
    renda = models.DecimalField(max_digits=10, decimal_places=2)
    manter_animal = models.BooleanField()
    castracao_vacinacao = models.BooleanField()
    taxa_adocao = models.BooleanField()

    def __str__(self):
        return f"{self.animal} - {self.user} - {self.data_envio}"
