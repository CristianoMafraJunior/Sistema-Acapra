from django.db import models
from .formulario_adocao import FormularioAdocao


class DocumentoFormulario(models.Model):
    formulario_adocao = models.ForeignKey(
        FormularioAdocao, on_delete=models.CASCADE, related_name="documentos"
    )
    arquivo = models.ImageField(upload_to="documentos/", null=True, blank=True)

    def __str__(self):
        return self.formulario_adocao
