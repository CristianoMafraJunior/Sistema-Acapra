from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=50,
        choices=[("Gato", "Gato"), ("Cachorro", "Cachorro")],
    )
    idade = models.IntegerField()
    porte = models.CharField(max_length=50)
    descricao = models.TextField()
    status_adocao = models.CharField(
        choices=[("A", "Adotado"), ("D", "Disponível")],
        default="D",
        blank=True,
    )
    raca = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - Idade: {self.idade} - {self.especie}"
