from django.db import models
from .formulario_adocao import FormularioAdocao


class DocumentoFormulario(models.Model):
    formulario_adocao = models.ForeignKey(
        FormularioAdocao, on_delete=models.CASCADE, related_name="formularios"
    )
    tipo_documento = models.CharField(max_length=30)
    arquivo = models.ImageField(upload_to="documentos/", null=True, blank=True)

    def __str__(self):
        return f"{self.formulario_adocao} - {self.tipo_documento}"
