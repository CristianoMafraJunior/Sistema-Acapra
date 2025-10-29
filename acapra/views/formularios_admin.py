from django.shortcuts import render
from acapra.models import FormularioAdocao


def FormulariosAdmin(request):
    formularios = FormularioAdocao.objects.select_related("animal", "user").order_by(
        "-data_envio"
    )

    return render(
        request,
        "acapra/admin_formularios.html",
        {
            "formularios": formularios,
        },
    )
