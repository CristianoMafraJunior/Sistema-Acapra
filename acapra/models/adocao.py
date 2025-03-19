from django.db import models
from .user import User
from .animal import Animal


class Adocao(models.Model):
    animal = models.ForeignKey(
        Animal, on_delete=models.CASCADE, related_name="animais_adocao"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users_adocao"
    )
    data_adocao = models.DateField()
    status_adocao = models.CharField(
        choices=[("A", "Aprovada"), ("P", "Pendente"), ("R", "Reprovada")],
        default="P",
        blank=True,
        max_length=20,
    )

    def __str__(self):
        return f"{self.animal} - {self.status_adocao}"
