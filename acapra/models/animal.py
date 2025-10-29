from django.db import models


class Animal(models.Model):
    nome = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=50,
        choices=[("Gato", "Gato"), ("Cachorro", "Cachorro")],
    )
    idade = models.IntegerField(blank=True)
    porte = models.CharField(
        max_length=50,
        choices=[("Pequeno", "Pequeno"), ("Médio", "Médio"), ("Grande", "Grande")],
    )
    descricao = models.TextField(blank=True)
    status_adocao = models.CharField(
        choices=[("A", "Adotado"), ("D", "Disponível")],
        default="D",
        blank=True,
    )
    raca = models.CharField(max_length=50, blank=True)
    vacina = models.CharField(
        max_length=100, help_text="Separar vacina por ;", default="Nenhuma", blank=True
    )
    doenca = models.CharField(default="Nenhuma", blank=True)
    observacao = models.TextField(default="Nenhuma", blank=True)

    def __str__(self):
        return f"{self.nome} - Idade: {self.idade} - {self.especie}"
