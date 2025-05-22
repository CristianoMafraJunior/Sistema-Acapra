from django.db import models
from .animal import Animal


class Foto(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="fotos")
    imagem = models.ImageField(upload_to="fotos_animais/", null=True, blank=True)

    def __str__(self):
        return self.animal.nome
