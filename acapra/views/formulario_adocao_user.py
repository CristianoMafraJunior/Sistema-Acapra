from django.shortcuts import render, redirect, get_object_or_404
from acapra.models import Animal, User
from acapra.forms import FormularioAdocaoForm
from django.core.mail import send_mail
from django.utils.html import format_html


def FormularioAdocaoUser(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)

    user = None
    user_id = request.session.get("user_id")
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None

    if request.method == "POST":
        form = FormularioAdocaoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivos = request.FILES.getlist("documentos")
            form.save(animal=animal, user=user, arquivos=arquivos)
            send_mail(
                subject="🐾 Formulário de Adoção Recebido!",
                message=(
                    f"Usuário {user.nome if user else 'Anônimo'} "
                    f"solicitou a adoção do animal: {animal.nome}.\n"
                    f"Email do usuário: {user.email if user else 'Não informado'}."
                ),  # Texto simples (fallback)
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
                html_message=format_html(
                    """
    <div style="font-family: 'Segoe UI', Arial, sans-serif;
                background-color: #0f0f10;
                color: #f5f5f5;
                border: 1px solid #27272a;
                border-radius: 12px;
                padding: 24px;
                max-width: 600px;
                margin: auto;
                line-height: 1.6;">
        <h2 style="color: #a855f7; margin-top: 0; font-size: 22px;">
            🐾 Nova Solicitação de Adoção Recebida!
        </h2>

        <p style="font-size: 15px; color: #d4d4d8;">
            Olá <strong style="color: #f1f1f1;">{nome}</strong>,<br>
            Recebemos sua solicitação de adoção para o animal
            <strong style="color: #a78bfa;">{animal}</strong>.
        </p>

        <p style="font-size: 15px; color: #d4d4d8;">
            Nossa equipe irá analisar as informações e em breve entraremos em contato
            para seguir com o processo de adoção 💜
        </p>

        <div style="background-color: #18181b;
                    padding: 12px 18px;
                    border-radius: 8px;
                    margin: 24px 0;">
            <p style="margin: 0; font-size: 14px; color: #e4e4e7;">
                <strong>Animal:</strong> {animal}<br>
                <strong>Espécie:</strong> {especie}<br>
                <strong>Idade:</strong> {idade} anos
            </p>
        </div>

        <p style="font-size: 14px; color: #a1a1aa;">
            Obrigado por escolher adotar — você está transformando uma vida 🐶💜
        </p>

        <hr style="border: none; border-top: 1px solid #27272a; margin: 24px 0;"/>

        <p style="font-size: 12px; color: #71717a;">
            Este e-mail foi enviado automaticamente pelo sistema Acapra.<br>
            Por favor, não responda diretamente a esta mensagem.
        </p>
    </div>
    """,
                    nome=user.nome if user else "Anônimo",
                    animal=animal.nome,
                    especie=animal.especie,
                    idade=animal.idade,
                ),
            )
            return redirect("AnimaisDisponiveisUser")
    else:
        form = FormularioAdocaoForm()

    return render(
        request, "acapra/formulario_adocao.html", {"form": form, "animal": animal}
    )
